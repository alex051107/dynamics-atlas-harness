## 1. 只有摘要；行已过原文核对；已并进总表（标注：未盲评）；主会话抽查过；表被写成“完整”

Rule broken: Gina 10-22: a few accurate examples do not show that extraction is complete. Only a scientist reading can say so.
Why: 没有科学家看过就能写“完整”：只要程序核对和抽查过了就放行，没有要求 Gina 看过.
In the model, one step leads into this bug: "把表写成“完整”〔人；今天没有任何程序拦这一步〕". The steps below are the shortest path that TLC found.

0. Start: 全文还没拿到
1. 找免费合法全文〔程序：Europe PMC、PMC、预印本，不登录；封存条目拒绝〕. Now: 只有摘要
2. 只按摘要写行〔agent Sonnet；摘要里没有的条件不写〕. Now: 只有摘要；摘要行已写，未核对
3. 核对证据行〔程序：引文逐字在原文，数字在原文，空格子有原因；标准固定〕. Now: 只有摘要；行已过原文核对
4. 并进总表〔程序：只收过核对的行；总表首页注明是否盲评〕. Now: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）
5. 回原文抽查〔主会话 Fable：打开论文逐值对照；看判断，不是固定标准〕. Now: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）；主会话抽查过
6. 把表写成“完整”〔人；今天没有任何程序拦这一步〕. Now: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）；主会话抽查过；表被写成“完整”

With the fix, step 6 (把表写成“完整”〔人；今天没有任何程序拦这一步〕) cannot happen, so you stay at: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）；主会话抽查过.

## 2. 只有摘要；行已过原文核对；已并进总表（标注：未盲评）；已发出

Rule broken: Rows leave the team only after a blind reader checked a sample (decision 2026-11-11).
Why: 没做盲评就能发出：发出前只要求项目负责人同意，没有要求盲评通过.
In the model, one step leads into this bug: "发给 Gina、Soojung〔人：项目负责人〕". The steps below are the shortest path that TLC found.

0. Start: 全文还没拿到
1. 找免费合法全文〔程序：Europe PMC、PMC、预印本，不登录；封存条目拒绝〕. Now: 只有摘要
2. 只按摘要写行〔agent Sonnet；摘要里没有的条件不写〕. Now: 只有摘要；摘要行已写，未核对
3. 核对证据行〔程序：引文逐字在原文，数字在原文，空格子有原因；标准固定〕. Now: 只有摘要；行已过原文核对
4. 并进总表〔程序：只收过核对的行；总表首页注明是否盲评〕. Now: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）
5. 决定发不发〔人：项目负责人〕. Now: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）
6. 发给 Gina、Soojung〔人：项目负责人〕. Now: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）；已发出

With the fix, step 6 (发给 Gina、Soojung〔人：项目负责人〕) cannot happen, so you stay at: 只有摘要；行已过原文核对；已并进总表（标注：未盲评）.
