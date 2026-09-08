---
citekey: "{{citekey}}"
title: "{{title}}"
authors: "{% if creators and creators.length > 0 %}{% for creator in creators %}{% if creator.name %}{{creator.name}}{% else %}{{creator.lastName}}, {{creator.firstName}}{% endif %}{% if not loop.last %}; {% endif %}{% endfor %}{% endif %}"
date: "{{ date | format("YYYY-MM-DD") }}"
journal: "{{publicationTitle}}"
item_type: "{{itemType}}"
doi: "{{DOI}}"
url: "{{url}}"
tags: [zotero{% for tag in tags %}, "{{tag.tag}}"{% endfor %}]
status: 📥 待阅读
---

# {{title}}

{% if abstractNote %}
> [!abstract]+ 📄 摘要（原文）
> {{abstractNote}}

{% endif %}
> [!info]+ 📇 文献元数据
> - **作者**: {% if creators and creators.length > 0 %}{% for creator in creators %}{% if creator.name %}{{creator.name}}{% else %}{{creator.firstName}} {{creator.lastName}}{% endif %}{% if not loop.last %}; {% endif %}{% endfor %}{% endif %}
{% if publicationTitle %}
> - **发表**: {{publicationTitle}} · {{ date | format("YYYY-MM-DD") }}
{% else %}
> - **发表**: {{ date | format("YYYY-MM-DD") }}
{% endif %}
> - **引用键**: `{{citationKey}}`
{%- if DOI %}
> - **DOI**: [{{DOI}}](https://doi.org/{{DOI}})
{%- endif %}
{%- if url %}
> - **来源**: [原文链接]({{url}})
{%- endif %}
> - **Zotero 条目**: [在 Zotero 中打开]({{desktopURI}})
{%- if attachments and attachments.length > 0 %}
{%- set file = attachments | filterby("path", "endswith", ".pdf") | first %}
{%- if file and file.pdfURI %}
> - **PDF**: [打开 PDF]({{file.pdfURI}})
{%- endif %}
{%- endif %}

---

## 🎯 一句话总结

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 读完后用一句话概括：**解决了什么问题、核心贡献、与我研究的关联**。直接写在下方两个标记之间即可（Obsidian 阅读模式下标记会自动隐藏）。
>
{% persist "tldr" %}
{% endpersist %}

## 📋 文献速览

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 依次填写以下六项，自由组织文字即可：
> - 研究问题 / 方法·数据 / 核心发现 / 主要贡献 / 局限·不足 / 与我研究的关系
>
{% persist "review" %}
{% endpersist %}

---

## 📚 AI 摘要（自动刷新）

{% if notes and notes.length > 0 %}{% for note in notes %}{% if note.note %}
{{note.note}}
{% endif %}{% endfor %}{% else %}
_（暂无 Zotero 笔记）_
{% endif %}

---

## 🖍️ 高亮与批注（自动刷新）

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
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）
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

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 核心论点 / 方法启示 / 可复用的点 / 存疑待验证
>
{% persist "thoughts" %}
{% endpersist %}

## 🔗 关联与行动

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 关联文献 [[citekey]] · 关联主题 [[标签]] · 待办清单
>
{% persist "actions" %}
{% endpersist %}

<!--
颜色编码建议（可在 Zotero 中自定义）：
🟡 黄 = 核心论点/重要结论  🟢 绿 = 方法/模型/数据来源  🔵 蓝 = 结果/发现/实证数据
🔴 红 = 局限/问题/批判     🟣 紫 = 概念/定义/术语       🟥 品红 = 疑问/待查证
⚪ 灰 = 一般背景信息
持久化说明：元数据/AI摘要/高亮 = 自动刷新；一句话总结/文献速览/我的思考/关联行动 = 写在 %% begin/end %% 标记间（Obsidian 阅读模式下标记自动隐藏），重导不丢。
-->
