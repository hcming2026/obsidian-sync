# AGENTS.md — hcmingGo Obsidian 知识库

## 文献知识库（城市低空资源研究）

知识库根：`04_Projects/城市低空资源研究/`
- 论文笔记：`参考文献/论文/`　作者笔记：`作者资料/`　期刊笔记：`期刊/`
- 阅读看板：`参考文献/阅读看板.md`　FileClass 定义：`参考文献/_fileclasses/paper.md`
- 构建脚本：`_tools/kb_build.py`　摘要缓存：`_tools/s2_abstracts.json`
- 新文献导入模板：`05_Templates/文献导入模板.md`

### 权威数据源与重建

- 论文/作者/期刊笔记的**唯一权威数据源是 `_tools/kb_build.py` 内的 PAPERS dict**（含 title / year / journal / doi / abstract / 中文要点 / 用途等）。
- 在 `_tools/` 下运行 `python kb_build.py` 会全量重建三类笔记。生成计数以脚本输出为准（论文/作者/期刊）。
- **新增文献流程**：
  1. 先在 Zotero 添加条目，记录条目 key 与 Better BibTeX 引用键（citationKey）；
  2. 将该文献信息加入 kb_build.py 的 PAPERS dict（`zoteroKey` 仅在确认真实条目 key 时写入，未核验不得填）；
  3. 运行 `python kb_build.py` 重建，核对计数增加；作者/期刊笔记与反向引用自动生成。

### 关联与保留规则

- 论文笔记通过 `[[作者]]`、`[[期刊]]` 双链引用作者/期刊；作者/期刊笔记反向列出该论文。
- 重跑脚本**保留**每篇论文笔记 `## 摘录` 区块的手动内容与手动修改的 `status`（extract_kept 逻辑），其余字段按 PAPERS dict 重写。用户手写内容若需保留必须放在摘录区块内。
- `abstractStatus` 不随脚本保留用户手动值——未取到可靠摘要的一律标 `待补`，禁止编造摘要（参考已知摘要缓存 `s2_abstracts.json`）。

### 字段规范（frontmatter 硬约束）

- 论文笔记必须含：`type: paper`、`fileClass: paper`、`year`、`journal`、`doi`、`status`、`abstractStatus`、`citationKey`；有 Zotero 条目的加 `zoteroKey`。
- `status` 四态枚举：未读 / 精读中 / 已精读 / 待复核（默认未读）。
- `abstractStatus` 三态枚举：完整 / 片段 / 待补（默认待补）。
- 两个枚举字段由 **Metadata Menu 下拉**维护（定义在 `_fileclasses/paper.md`），不手工写入枚举外的值；阅读看板的 Dataview 查询依赖这两个字段。
- 作者/期刊笔记结构由脚本生成，不要手工改动其反向引用列表。

### Zotero 联动（硬约束）

- Zotero 本地 API：`http://127.0.0.1:23119`。**所有 API 调用必须用 curl.exe**（PowerShell 的 Invoke-WebRequest / RestMethod 在此环境不兼容）。
- 单条高亮跳转链接：`zotero://open-pdf/library/items/<附件key>?page=<页码>&annotation=<标注key>`（由插件 zotero-annotation-links 右键复制，快捷键 Ctrl+Shift+C）。
- Zotero 条目跳转：`zotero://select/library/items/<条目key>`。
- Obsidian 侧插件：Zotero Integration（data.json 含批量"摘录导入（高亮+跳转）"格式）、Dataview、Metadata Menu、obsidian-git。

## 常规约定

- 工作目录为用户 Windows 机器（PowerShell 5：不支持 `&&`，命令用 `;` 连接）。
- 用户偏好中文回复；未核验的文献信息（摘要、条目 key）标"待补/未核验"，不编造。
