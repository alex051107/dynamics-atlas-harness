#!/usr/bin/env python3
"""Render the three Dynamics Atlas flowcharts as PNG and SVG.

Content comes from figures/flowcharts.json (shared with scripts/build_flowcharts.cjs,
which writes the editable PowerPoint version). Layout geometry is expressed in inches on a
10 x 5.625 in (16:9) canvas with the y axis pointing down, the same coordinate frame that
the PowerPoint renderer uses.

Usage (from the worktree root):
    MPLCONFIGDIR=$TMPDIR/mpl python3 scripts/build_flowcharts.py
"""
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch  # noqa: E402
from matplotlib.textpath import TextPath  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_PATH = os.path.join(ROOT, "figures", "flowcharts.json")
OUT_DIR = os.path.join(ROOT, "figures")

with open(SPEC_PATH, encoding="utf-8") as fh:
    SPEC = json.load(fh)

S = SPEC["style"]
FONT = S["font"]
CANVAS_W = SPEC["canvas"]["w"]
CANVAS_H = SPEC["canvas"]["h"]
LINE_SPACING = 1.2  # multiple of the font size
OVERFLOW = []  # (figure, text, reason)


def col(hexstr):
    return "#" + hexstr


# ---------------------------------------------------------------- text helpers
def text_width_pt(text, size, bold=False):
    fp = FontProperties(family=FONT, weight="bold" if bold else "normal")
    if not text:
        return 0.0
    return TextPath((0, 0), text, size=size, prop=fp).get_extents().width


def wrap(text, width_pt, size, bold=False):
    """Greedy word wrap measured with the real font metrics."""
    lines = []
    for para in text.split("\n"):
        words = para.split(" ")
        cur = ""
        for w in words:
            cand = w if not cur else cur + " " + w
            if text_width_pt(cand, size, bold) <= width_pt or not cur:
                cur = cand
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


class Canvas:
    def __init__(self, name):
        self.name = name
        self.fig = plt.figure(figsize=(CANVAS_W, CANVAS_H))
        self.fig.patch.set_facecolor("white")
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, CANVAS_W)
        self.ax.set_ylim(CANVAS_H, 0)
        self.ax.set_aspect("equal")
        self.ax.axis("off")

    # -- primitives (inches, y down) ------------------------------------------
    def box(self, x, y, w, h, fill, line, radius=0.05):
        self.ax.add_patch(
            FancyBboxPatch(
                (x, y), w, h,
                boxstyle=f"round,pad=0,rounding_size={radius}",
                facecolor=col(fill), edgecolor=col(line), linewidth=0.8, zorder=1,
            )
        )

    def text(self, x, y, w, h, runs, size=11, color=None, align="center",
             valign="middle", pad=0.08, bold=False):
        """runs: str or list of (text, bold, color) tuples rendered as separate lines."""
        if isinstance(runs, str):
            runs = [(runs, bold, color)]
        avail_pt = (w - 2 * pad) * 72
        lines = []
        for t, b, c in runs:
            for ln in wrap(t, avail_pt, size, b):
                lines.append((ln, b, c or color or S["body"]))
        line_h = size * LINE_SPACING / 72  # inches
        block_h = line_h * len(lines)
        if block_h > h - 2 * pad * 0.5 + 1e-6:
            OVERFLOW.append((self.name, runs[0][0][:50], f"{len(lines)} lines need {block_h:.2f} in, box has {h:.2f} in"))
        for ln, b, c in lines:
            if text_width_pt(ln, size, b) > avail_pt + 0.5:
                OVERFLOW.append((self.name, ln[:50], "single word wider than box"))
        if valign == "top":
            y0 = y + pad
        elif valign == "bottom":
            y0 = y + h - pad - block_h
        else:
            y0 = y + (h - block_h) / 2
        if align == "left":
            tx, ha = x + pad, "left"
        elif align == "right":
            tx, ha = x + w - pad, "right"
        else:
            tx, ha = x + w / 2, "center"
        for i, (ln, b, c) in enumerate(lines):
            cy = y0 + line_h * (i + 0.5)
            self.ax.text(
                tx, cy, ln, fontsize=size, fontfamily=FONT,
                fontweight="bold" if b else "normal", color=col(c),
                ha=ha, va="center", zorder=3,
            )

    def arrow(self, x0, y0, x1, y1, color=None, lw=1.4, head=True):
        c = col(color or S["arrow"])
        style = "-|>" if head else "-"
        self.ax.annotate(
            "", xy=(x1, y1), xytext=(x0, y0),
            arrowprops=dict(arrowstyle=style, color=c, lw=lw, mutation_scale=14,
                            shrinkA=0, shrinkB=0),
            zorder=2,
        )

    def circle(self, cx, cy, r, fill, line):
        self.ax.add_patch(Circle((cx, cy), r, facecolor=col(fill), edgecolor=col(line),
                                 linewidth=1.2, zorder=4))

    def title(self, text):
        self.text(0.4, 0.22, 9.2, 0.45, text, size=18, color=S["heading"], align="left",
                  valign="middle", pad=0.0, bold=True)

    def footer(self):
        self.text(0.4, 5.28, 6.0, 0.22, SPEC["footer"], size=9, color=S["muted"],
                  align="left", valign="middle", pad=0.0)

    def save(self):
        png = os.path.join(OUT_DIR, self.name + ".png")
        svg = os.path.join(OUT_DIR, self.name + ".svg")
        self.fig.savefig(png, dpi=200, facecolor="white")
        self.fig.savefig(svg, facecolor="white")
        plt.close(self.fig)
        return png, svg


# ---------------------------------------------------------------- figures
def fill_for(kind):
    if kind == "current":
        return S["current"], S["current_line"]
    if kind == "grey":
        return S["grey"], S["grey_line"]
    if kind == "none":
        return "FFFFFF", S["empty_line"]
    return S["box"], S["box_line"]


def draw_project_map(name, f):
    c = Canvas(name)
    c.title(f["title"])
    steps = f["steps"]
    n = len(steps)
    x0, span, gap = 0.4, 9.2, 0.22
    cw = (span - gap * (n - 1)) / n
    y_step, h_step = 0.85, 0.5
    y_by, h_by = 1.38, 0.44
    y_lab2, y_row2, h_row2 = 1.92, 2.18, 0.9
    y_lab3, y_row3, h_row3 = 3.22, 3.48, 1.4
    for i, st in enumerate(steps):
        x = x0 + i * (cw + gap)
        fill, line = fill_for("box")
        c.box(x, y_step, cw, h_step, fill, line)
        c.text(x, y_step, cw, h_step, st["name"], size=11.5, color=S["heading"], bold=True)
        if i < n - 1:
            c.arrow(x + cw + 0.03, y_step + h_step / 2, x + cw + gap - 0.03, y_step + h_step / 2)
        c.text(x, y_by, cw, h_by, st["by"], size=11, color=S["muted"], valign="top", pad=0.02)
        # row 2: where a rule can enter
        fill, line = fill_for(st["rule_kind"])
        c.box(x, y_row2, cw, h_row2, fill, line)
        c.text(x, y_row2, cw, h_row2, st["rule"], size=11,
               color=S["muted"] if st["rule_kind"] == "none" else S["body"])
        # row 3: what happened
        fill, line = fill_for("grey")
        c.box(x, y_row3, cw, h_row3, fill, line)
        c.text(x, y_row3, cw, h_row3, st["happened"], size=11)
    c.text(x0, y_lab2, span, 0.24, f["row_labels"]["rule"], size=11, color=S["heading"],
           align="left", valign="middle", pad=0.0, bold=True)
    c.text(x0, y_lab3, span, 0.24, f["row_labels"]["happened"], size=11, color=S["heading"],
           align="left", valign="middle", pad=0.0, bold=True)
    c.footer()
    return c.save()


def draw_timeline(name, f):
    c = Canvas(name)
    c.title(f["title"])
    nodes = f["nodes"]
    n = len(nodes)
    x0, span, bw = 0.4, 9.2, 1.7
    gap = (span - n * bw) / (n - 1)
    y_line = 1.65
    y_date, h_date = 1.15, 0.36
    y_box, h_box = 2.05, 1.75
    r = 0.11
    c.arrow(x0, y_line, x0 + span, y_line, lw=2.0)
    for i, nd in enumerate(nodes):
        x = x0 + i * (bw + gap)
        cx = x + bw / 2
        kind = "current" if nd["current"] else "box"
        fill, line = fill_for(kind)
        c.circle(cx, y_line, r, S["current"] if nd["current"] else S["heading"],
                 S["current_line"] if nd["current"] else S["heading"])
        c.text(x, y_date, bw, h_date, nd["date"], size=12, color=S["heading"], bold=True,
               valign="bottom", pad=0.02)
        c.arrow(cx, y_line + r, cx, y_box, head=False, lw=1.2)
        c.box(x, y_box, bw, h_box, fill, line)
        c.text(x, y_box, bw, h_box, nd["text"], size=11)
    c.text(x0, 4.15, span, 0.36, f["caption"], size=12, color=S["heading"], bold=True, pad=0.0)
    c.footer()
    return c.save()


def draw_vertical_flow(name, f):
    c = Canvas(name)
    c.title(f["title"])
    boxes = f["boxes"]
    x, w, h, gap = 0.4, 5.6, 0.7, 0.18
    y0 = 0.85
    sx, sw = 6.5, 3.1
    ys = []
    for i, b in enumerate(boxes):
        y = y0 + i * (h + gap)
        ys.append(y)
        fill, line = fill_for("box")
        c.box(x, y, w, h, fill, line)
        runs = []
        if b.get("lead"):
            runs.append((b["lead"], True, S["heading"]))
        runs.append((b["text"], False, S["body"]))
        c.text(x, y, w, h, runs, size=11, align="left")
        if i < len(boxes) - 1:
            c.arrow(x + w / 2, y + h + 0.02, x + w / 2, y + h + gap - 0.02)
    for sn in f["side_notes"]:
        y = ys[sn["box"]]
        fill, line = fill_for("grey")
        c.arrow(x + w, y + h / 2, sx, y + h / 2, head=False, lw=1.2)
        c.box(sx, y, sw, h, fill, line)
        c.text(sx, y, sw, h, sn["text"], size=11, align="left")
    c.footer()
    return c.save()


RENDERERS = {
    "project_map": draw_project_map,
    "timeline": draw_timeline,
    "vertical_flow": draw_vertical_flow,
}


def main():
    plt.rcParams["svg.fonttype"] = "none"  # keep text as text in the SVG
    plt.rcParams["font.family"] = FONT
    written = []
    for name, f in SPEC["figures"].items():
        written.extend(RENDERERS[f["kind"]](name, f))
    for p in written:
        print(f"wrote {os.path.relpath(p, ROOT)} ({os.path.getsize(p)} bytes)")
    if OVERFLOW:
        print("TEXT OVERFLOW WARNINGS:", file=sys.stderr)
        for fig, txt, why in OVERFLOW:
            print(f"  [{fig}] {txt!r}: {why}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
