---- MODULE FillTable ----
\* One source paper of one RelaxDB protein moving from "text not in hand" to "table delivered", as the work runs on 2026-11-12.
\* Plain meanings of the steps live in FillTable.map.mjs. Steps nobody has run yet (Gina reads, send) are still actions here.

VARIABLES sealed, text, basis, rows, merged, label, spot, blind, owner, sent, gina, claim
vars == <<sealed, text, basis, rows, merged, label, spot, blind, owner, sent, gina, claim>>

TypeOK ==
    /\ sealed \in BOOLEAN
    /\ text \in {"None", "Abstract", "FullRaw", "FullOK", "Rejected"}
    /\ basis \in {"None", "Abstract", "Full"}
    /\ rows \in {"None", "Written", "AbstractRows", "Checked", "Failed"}
    /\ merged \in BOOLEAN
    /\ label \in {"None", "Unreviewed", "Reviewed"}
    /\ spot \in BOOLEAN
    /\ blind \in {"NotRun", "Passed", "Failed"}
    /\ owner \in {"No", "Yes"}
    /\ sent \in BOOLEAN
    /\ gina \in BOOLEAN
    /\ claim \in {"None", "Draft", "Complete"}

Init ==
    /\ sealed \in BOOLEAN
    /\ text = "None" /\ basis = "None" /\ rows = "None" /\ merged = FALSE /\ label = "None" /\ spot = FALSE
    /\ blind = "NotRun" /\ owner = "No" /\ sent = FALSE /\ gina = FALSE /\ claim = "None"

Keep(x) == UNCHANGED <<x>>

\* program: looks for a free legal copy (Europe PMC, PMC, preprint); no logins
FindFree ==
    /\ ~sealed /\ text = "None"  \* scripts/relaxdb_evidence_table/source_fulltext.py:44
    /\ \E t \in {"FullRaw", "Abstract"} : text' = t
    /\ UNCHANGED <<sealed, basis, rows, merged, label, spot, blind, owner, sent, gina, claim>>

\* person: downloads the PDF through the university library into the drop folder
OwnerDrop ==
    /\ ~sealed /\ text \in {"None", "Rejected"}  \* scripts/relaxdb_evidence_table/source_fulltext.py:96
    /\ text' = "FullRaw"
    /\ UNCHANGED <<sealed, basis, rows, merged, label, spot, blind, owner, sent, gina, claim>>

\* program: DOI or title found inside the file, at least 5,000 characters of body
IdentityCheck ==
    /\ text = "FullRaw"
    /\ \E t \in {"FullOK", "Rejected"} : text' = t
    /\ UNCHANGED <<sealed, basis, rows, merged, label, spot, blind, owner, sent, gina, claim>>

\* agent (Sonnet) reads the full text plus supplement and writes rows with verbatim quotes
ReadFull ==
    /\ ~sealed  \* scripts/relaxdb_evidence_table/check_rows.py:34
    /\ text = "FullOK"  \* scripts/relaxdb_evidence_table/build_manifest.py:23
    /\ rows = "None"
    /\ rows' = "Written" /\ basis' = "Full"
    /\ UNCHANGED <<sealed, text, merged, label, spot, blind, owner, sent, gina, claim>>

ReadAbstract ==
    /\ ~sealed  \* scripts/relaxdb_evidence_table/check_rows.py:34
    /\ text = "Abstract"  \* review/20261112_relaxdb_table/briefs/race_b_paper_v2.md:32
    /\ rows = "None"
    /\ rows' = "AbstractRows" /\ basis' = "Abstract"
    /\ UNCHANGED <<sealed, text, merged, label, spot, blind, owner, sent, gina, claim>>

\* program: quotes and numbers verbatim in the text, every empty cell has a reason
RowCheck ==
    /\ rows \in {"Written", "AbstractRows"}
    /\ \E r \in {"Checked", "Failed"} : rows' = r
    /\ UNCHANGED <<sealed, text, basis, merged, label, spot, blind, owner, sent, gina, claim>>

Repair ==
    /\ rows = "Failed"
    /\ rows' = "Written"
    /\ UNCHANGED <<sealed, text, basis, merged, label, spot, blind, owner, sent, gina, claim>>

\* program: builds the workbook from checked rows; the cover sheet says whether rows had a blind review
Merge ==
    /\ rows = "Checked" /\ ~merged  \* scripts/relaxdb_evidence_table/build_all.py:225
    /\ merged' = TRUE
    /\ label' = IF blind = "Passed" THEN "Reviewed" ELSE "Unreviewed"
    /\ claim' = "Draft"
    /\ UNCHANGED <<sealed, text, basis, rows, spot, blind, owner, sent, gina>>

\* main session: opens the paper and compares a sample of rows value by value
SpotCheck ==
    /\ merged /\ ~spot  \* review/20261112_relaxdb_table/steps/09_spot_check.md:5
    /\ spot' = TRUE
    /\ UNCHANGED <<sealed, text, basis, rows, merged, label, blind, owner, sent, gina, claim>>

\* second model: reads the paper blind, then a judge compares rows with that reading (a seeded sample of papers)
BlindReview ==
    /\ rows = "Checked" /\ blind = "NotRun"  \* review/20261112_relaxdb_table/steps/10_blind_review.md:5
    /\ \E b \in {"Passed", "Failed"} : blind' = b /\ label' = IF merged THEN (IF b = "Passed" THEN "Reviewed" ELSE "Unreviewed") ELSE label
    /\ UNCHANGED <<sealed, text, basis, rows, merged, spot, owner, sent, gina, claim>>

\* owner: decides to send to Gina and Soojung
OwnerApprove ==
    /\ merged /\ owner = "No"  \* review/20261112_relaxdb_table/steps/12_owner_decision.md:5
    /\ owner' = "Yes"
    /\ UNCHANGED <<sealed, text, basis, rows, merged, label, spot, blind, sent, gina, claim>>

Send ==
    /\ owner = "Yes" /\ merged /\ ~sent  \* review/20261112_relaxdb_table/steps/12_owner_decision.md:5
    /\ sent' = TRUE
    /\ UNCHANGED <<sealed, text, basis, rows, merged, label, spot, blind, owner, gina, claim>>

\* Gina: reads the entries she picks and says what is missing
GinaReads ==
    /\ sent /\ ~gina  \* review/20261112_relaxdb_table/steps/13_gina_reads.md:5
    /\ gina' = TRUE
    /\ UNCHANGED <<sealed, text, basis, rows, merged, label, spot, blind, owner, sent, claim>>

\* a person writing "complete" on the table or in a report
MarkComplete ==
    /\ merged /\ spot /\ claim = "Draft"  \* review/20261112_relaxdb_table/steps/13_gina_reads.md:5
    /\ claim' = "Complete"
    /\ UNCHANGED <<sealed, text, basis, rows, merged, label, spot, blind, owner, sent, gina>>

Next == FindFree \/ OwnerDrop \/ IdentityCheck \/ ReadFull \/ ReadAbstract \/ RowCheck \/ Repair
        \/ Merge \/ SpotCheck \/ BlindReview \/ OwnerApprove \/ Send \/ GinaReads \/ MarkComplete

Spec == Init /\ [][Next]_vars

\* A sealed protein is never read: it stays the final test.
NoSealedRead == sealed => (text = "None" /\ basis = "None" /\ rows = "None" /\ ~merged)

\* Only rows that passed the program check reach the workbook.
OnlyCheckedRowsInTable == merged => rows = "Checked"

\* A paper counts as full text only after its identity was checked.
FullTextNeedsIdentity == basis = "Full" => text = "FullOK"

\* The cover sheet never hides that rows were not reviewed.
LabelMatchesReview == merged => (label = "Reviewed" <=> blind = "Passed")

\* Gina 10-22: a few accurate examples do not show that extraction is complete. Only a scientist reading can say so.
NoCompleteWithoutGina == claim = "Complete" => gina

\* Rows leave the team only after a blind reader checked a sample (decision 2026-11-11).
NoSendUnreviewed == sent => blind = "Passed"
====
