<!--
┌────────────────────────────────────────────────────────────┐
│  科研型文献阅读模板（Zotero Integration）                    │
│                                                            │
│  颜色编码建议（可在 Zotero 中自定义）：                      │
│    🟡 黄 = 核心论点 / 重要结论                               │
│    🟢 绿 = 方法 / 模型 / 数据来源                            │
│    🔵 蓝 = 结果 / 发现 / 实证数据                            │
│    🔴 红 = 局限 / 问题 / 批判                                │
│    🟣 紫 = 概念 / 定义 / 术语                                │
│    🟥 品红 = 疑问 / 待查证                                   │
│    ⚪ 灰 = 一般背景信息                                      │
│                                                            │
│  使用流程：先读原文 → 填「文献速览」→ 每处高亮下方写「我的   │
│  批注」→ 最后填「我的思考」与「关联与行动」。                │
└────────────────────────────────────────────────────────────┘
-->
---
citekey: "{{citekey}}"
title: "{{title}}"
authors: "{% if creators and creators.length > 0 %}{% for creator in creators %}{% if creator.name %}{{creator.name}}{% else %}{{creator.lastName}}, {{creator.firstName}}{% endif %}{% if not loop.last %}; {% endif %}{% endfor %}{% endif %}"
date: "{{date}}"
journal: "{{publicationTitle}}"
item_type: "{{itemType}}"
doi: "{{DOI}}"
url: "{{url}}"
tags: [zotero{% for tag in tags %}, "{{tag.tag}}"{% endfor %}]
status: 📥 待阅读
---

# {{title}}

> [!abstract]+ 📄 摘要（原文）
> {{abstractNote}}

> [!info]+ 📇 文献元数据
> - **作者**: {% if creators and creators.length > 0 %}{% for creator in creators %}{% if creator.name %}{{creator.name}}{% else %}{{creator.firstName}} {{creator.lastName}}{% endif %}{% if not loop.last %}; {% endif %}{% endfor %}{% endif %}
> - **发表**: {{publicationTitle}} · {{date}}
> - **引用键**: `{{citationKey}}`
{% if DOI %}
> - **DOI**: [{{DOI}}](https://doi.org/{{DOI}})
{% endif %}{% if url %}
> - **来源**: [原文链接]({{url}})
{% endif %}
> - **Zotero 条目**: [在 Zotero 中打开]({{desktopURI}})
{% if attachments and attachments.length > 0 %}{% set file = attachments | filterby("path", "endswith", ".pdf") | first %}{% if file and file.pdfURI %}
> - **PDF**: [打开 PDF]({{file.pdfURI}})
{% endif %}{% endif %}

---

## 🎯 一句话总结

> （读完后用一句话概括：**这篇论文解决了什么问题、核心贡献是什么、和我研究的关联**）

## 📋 文献速览（读后填写）

| 维度 | 记录 |
| --- | --- |
| **研究问题** | 作者试图回答什么？ |
| **方法 / 数据** | 用了什么模型、数据、实验设计？ |
| **核心发现** | 最重要的 1–2 个结论是什么？ |
| **主要贡献** | 相比已有研究新增了什么？ |
| **局限 / 不足** | 审稿人视角的批评点、可改进处？ |
| **与我研究的关系** | 支撑我哪部分工作？或与我的结论有何冲突？ |

---

## 📚 AI 摘要（Zotero 笔记）

{% if notes and notes.length > 0 %}{% for note in notes %}{% if note.note %}
{{note.note}}
{% endif %}{% endfor %}{% else %}
_（暂无 Zotero 笔记）_
{% endif %}

---

## 🖍️ 高亮与批注

{% if annotations and annotations.length > 0 %}

{% for color in ["Yellow", "Green", "Blue", "Red", "Purple", "Magenta", "Orange", "Gray", "Cyan"] %}{% set group = annotations | filterby("colorCategory", "startswith", color) %}{% if group and group.length > 0 %}
### {{ color }}
{% for annotation in group %}{% if annotation.annotatedText %}
> [!quote] **p.{{annotation.pageLabel}}** · {{annotation.type | capitalize}}
> {{annotation.annotatedText}}
{% if annotation.comment %}
>
> **💬 Zotero 批注**: {{annotation.comment}}
{% else %}
>
> **💬 我的批注**: （在此补充我的想法 / 与已有研究的联系）
{% endif %}
>
> [📍 跳转到 PDF 具体位置]({{annotation.desktopURI}})
{% endif %}{% if annotation.imageRelativePath %}
> [!image] 🖼️ 图片批注 · p.{{annotation.pageLabel}}
> ![[{{annotation.imageRelativePath}}]]
>
> [📍 跳转到 PDF 具体位置]({{annotation.desktopURI}})
{% endif %}
{% endfor %}
{% endif %}{% endfor %}

{% else %}
_（该文献暂无高亮批注）_
{% endif %}

---

## 💭 我的思考

- **核心论点**：
- **方法启示**：
- **可复用的点**：
- **存疑 / 想验证**：

## 🔗 关联与行动

- **关联文献**：[[ ]]
- **关联主题**：[[ ]]
- **待办**：
  - [ ] 精读某章节
  - [ ] 引用到论文某处
  - [ ] 复现 / 验证某数据
