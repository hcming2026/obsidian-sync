---
citekey: "aartsCapacityConstrainedUrban2023b"
title: "Capacity of a constrained urban airspace: Influencing factors, analytical modelling and simulations"
authors: "Aarts, Michiel J.M.; Ellerbroek, Joost; Knoop, Victor L."
date: "2023-07-01"
journal: "Transportation Research Part C: Emerging Technologies"
item_type: "journalArticle"
doi: "10.1016/j.trc.2023.104173"
url: "https://linkinghub.elsevier.com/retrieve/pii/S0968090X23001626"
tags: [zotero, "ai-processed", "/unread"]
status: 📥 待阅读
---

# Capacity of a constrained urban airspace: Influencing factors, analytical modelling and simulations


> [!abstract]+ 📄 摘要（原文）
> The traffic density of small aerial vehicles operating within urban environments is expected to increase significantly in the near future. This urban environment is highly constrained due to being limited to the low-altitude airspace directly above the existing road network. Multiple studies have addressed factors influencing the capacity of urban airspace. These have used simulations of aircraft, yet the empirical nature of these simulations limits their use beyond the specific conditions that have been tested. Analytical models would not have this limitation, but they are only developed for general airspace, while the emergent patterns in constrained urban airspace are different than in general, unconstrained conditions. For instance, queuing and local congestion are patterns that are unique to the heavily-constrained environment. Therefore, in this paper, we derive an analytical model for air traffic in a confined airspace to find the influencing factors for its capacity. By means of a simulation of aerial vehicles, we verify the analytical model and show a relationship between the mean flow rate and mean density in a two-dimensional orthogonal grid network airspace. Results show that the entire airspace can become unstable when the maximum capacity of just one intersection is reached. Furthermore, the maximum airspace density is found to be unaffected by cruise speed. The results demonstrate how the derived analytical model provides an effective tool to predict the effect of several design parameters on the capacity of constrained urban airspace. Moreover, this model can form the basis for further extensions, including the altitude dimension and non-orthogonal or non-four-way intersections.


> [!info]+ 📇 文献元数据
> - **作者**: Michiel J.M. Aarts; Joost Ellerbroek; Victor L. Knoop

> - **发表**: Transportation Research Part C: Emerging Technologies · 2023-07-01

> - **引用键**: `aartsCapacityConstrainedUrban2023b`
> - **DOI**: [10.1016/j.trc.2023.104173](https://doi.org/10.1016/j.trc.2023.104173)
> - **来源**: [原文链接](https://linkinghub.elsevier.com/retrieve/pii/S0968090X23001626)
> - **Zotero 条目**: [在 Zotero 中打开](zotero://select/library/items/HB2HLS6Y)
> - **PDF**: [打开 PDF](zotero://open-pdf/library/items/7VVLK457)

---

## 🎯 一句话总结

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 读完后用一句话概括：**解决了什么问题、核心贡献、与我研究的关联**。直接写在下方两个标记之间即可（Obsidian 阅读模式下标记会自动隐藏）。
>
%% begin tldr %%
%% end tldr %%

## 📋 文献速览

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 依次填写以下六项，自由组织文字即可：
> - 研究问题 / 方法·数据 / 核心发现 / 主要贡献 / 局限·不足 / 与我研究的关系
>
%% begin review %%
%% end review %%

---

## 📚 AI 摘要（自动刷新）


# AI 摘要: Capacity of a constrained urban airspace: Influencing factors, analytical modelling and simulations

这篇论文旨在研究高度受限的城市低空空域容量及其影响因素。随着城市中无人机和个人飞行器数量的预期增长，低空空域受限于现有道路网络，形成了高度约束的环境。现有研究多采用仿真方法，但其经验性质限制了结果的泛化能力，而针对一般空域的解析模型无法捕捉受限空域特有的排队和局部拥堵等现象。因此，本文的研究目标是建立一个适用于受限空域的解析模型，以识别影响空域容量的关键参数。

方法上，作者首先基于二维正交网格网络空域（模拟城市街道上方的飞行走廊）推导了空中交通的解析模型，重点分析了交叉口的流量-密度关系以及冲突解决机制（采用基于速度的分散式方法）。随后，利用BlueSky模拟器进行飞行器仿真，验证了解析模型的准确性，并校准了模型参数。通过对比解析预测与仿真结果，证实了模型的有效性。

研究的主要发现包括：（1）空域的整体稳定性高度依赖于单个交叉口的容量——当任一交叉口达到最大通行能力时，整个空域可能迅速变得不稳定；（2）最大空域密度与飞行器的巡航速度无关，说明容量瓶颈主要由交叉口结构而非速度决定。该解析模型为预测不同设计参数（如网格间距、冲突解决规则）对容量的影响提供了有效工具，并可扩展至三维空域、非正交交叉口等更复杂场景。这一工作为城市空中交通管理（UTM）的规划与规则制定奠定了理论基础。

# AI 摘要: Capacity of a constrained urban airspace: Influencing factors, analytical modelling and simulations

这篇论文旨在解决城市低空空域因受限于道路网络上方而高度约束的情况下，其容量如何被影响因素所塑造的问题。与以往依赖仿真的经验性研究不同，作者提出了一个解析模型来预测受限城市空域（具体为二维正交网格网络）的容量，以避免仿真结果受特定条件限制的弊端。研究目标是找出影响该空域容量的关键因素，并验证解析模型的有效性。

研究方法上，作者首先基于空中交通在受限网格空域中的行为（包括排队和局部拥堵等特有现象），推导了一个分析流量的解析模型。随后，利用对飞行器的计算机仿真，在模拟的二维正交网格空域中测量平均流量与平均密度之间的关系，以此对解析模型进行验证。仿真中还采用了基于速度的冲突解决机制以模拟实际运行。

研究的关键发现表明，整个空域可能因单个交叉路口达到其最大容量而变得不稳定，即局部拥堵会迅速扩散至全局。此外，最大空域密度不受飞行器巡航速度的影响。解析模型与仿真结果吻合，验证了其预测能力。该模型的贡献在于提供了一个有效工具，能够评估诸如交叉路口设计、空域结构等设计参数对容量的影响，并为未来扩展至三维空域（加入高度层）及非正交交叉路口等更复杂场景奠定了基础。

# AI 摘要: Capacity of a constrained urban airspace: Influencing factors, analytical modelling and simulations

该研究旨在推导一个针对受约束城市空域的解析模型，以量化影响其容量的关键因素。研究背景是小型飞行器在低空城市空域中的密度预计将大幅增长，而该空域高度受限，通常局限于现有道路网络上方。现有研究多依赖仿真模拟，但模拟的实证性质使其结果难以推广至未测试的条件；而现有解析模型则针对一般空域，无法捕捉受约束环境中特有的排队和局部拥堵等模式。因此，本文提出一个专门适用于二维正交网格网络空域的解析模型，用于描述平均流入率与平均密度之间的关系。

研究方法包括理论推导和仿真验证。首先，作者基于交通流理论和冲突概率分析，建立了空域容量与交叉口容量、飞行器速度、间距要求等参数的数学关系。随后，利用BlueSky ATM仿真工具构建了模拟环境，对解析模型的预测进行验证。仿真采用分散式速度调节冲突解决机制，在正交网格网络上测试不同流入率和巡航速度下的空域流量与密度特性。

研究的关键发现是：当网络中单个交叉口达到其最大容量时，整个空域可能变得不稳定，即局部拥堵会迅速蔓延。此外，最大空域密度与巡航速度无关，表明速度并非容量的主要限制因素。该解析模型能够有效预测设计参数（如网格间距、冲突解决策略）对容量的影响，为城市空域规划提供了理论工具。模型的贡献在于其可扩展性，未来可纳入高度维度以及非正交或非四向交叉口等更复杂结构。


---

## 🖍️ 高亮与批注（自动刷新）




### Yellow

> [!quote] **p.1** · Highlight
> 在本文中 ,我们推导了受限空域中空中交通的分析模型,以找出影响其容量的 因素。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=1&annotation=DDSJXZLD)


> [!quote] **p.3** · Highlight
> 虽然受限城市空域与非受限空域具有不同的特征,但它与道路交通环境有许多相似之处。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=6A24BDY2)


> [!quote] **p.3** · Highlight
> 道路 交通研究也很少考虑冲突。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=PM5SNQL4)


> [!quote] **p.13** · Highlight
> 分析模型可依据假设3和公式(25),预测给定参数(如巡航速度、尺寸、间隔距离)的空域的理论最大 密度和流量。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=13&annotation=4UX89SJP)


> [!quote] **p.13** · Highlight
> 因此,模拟中遇到的最大容量被假定为与实际最大值 非常接近。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=13&annotation=JETRPV4F)


> [!quote] **p.14** · Highlight
> 8.2. 空域设计参数的影响

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=14&annotation=X4S7RTSX)


> [!quote] **p.14** · Highlight
> 观察到三个设计 参数会影响本文中使用的容量指标:巡航速度 、水平间隔要求 以及交叉路口的流量交替次数。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=14&annotation=7DA2C33Q)


> [!quote] **p.15** · Highlight
> 预计在不久的将来,高度受限的低空城市空域内小型飞行器的交通密度将显著增加

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=15&annotation=3MN5C3MZ)


> [!quote] **p.1** · Highlight
> 不同。例 在本文中 其容量的 如，排队和局部拥堵是高度受限环境所特有的模式。因此，在本文中 ，我们推导了受限空域中空中交通的分析模型，以找出影响其容量的 因素。通过飞行器模拟，我们验证了分析模型，并展示了二维正交网 ，我们 因素。 格网络

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=1)


> [!quote] **p.3** · Highlight
> 要一个量身定制的分析模型。 虽然受限城市空域与非受限空域具有不同的特征，但它与道路交通环境有许多相似之处。 研究成为受限城市空域容量建模的一个明显灵感来源。与我们上面关于街道连锁冲突的观察

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 道路交 道路 中在 通研究成为受限城市空域容 交通研究也很少考虑冲突。 网络中的平均流入率和平均

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.13** · Highlight
> 法得出最大容量的确切上限。然而，所有三个实验在其 因此，模拟中遇到的最大容量被假定为与实际最大值 大密度时都 非常接近。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=13)


> [!quote] **p.13** · Highlight
> 了1.35倍，比 实验高估

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=13)


> [!quote] **p.14** · Highlight
> 8.2. 空域设计参数的影响

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=14)


> [!quote] **p.14** · Highlight
> 观察到三个设计 流量交替次数。 分析模型的准确程度允许量化几个相关空域设计参数的影响。基于方程中使用的参数，观察到三个设计 参数会影响本文中使用的容量指标：巡航速度 、水平间隔要求 以及交叉路口的流量交替次数。 前瞻时间足够长时，不会影响平均流入率与平均密度之间的关系。此外，还讨论了空域结构的影响，例如

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=14)


> [!quote] **p.15** · Highlight
> 预计在不久的将来，高度受限的低空城市空域内小型飞行器的交通密度将显著增加 增进对影响受限城市空域容量的因素的理解。受限城市空域中飞机的涌现行为，如排

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=15)



### Green

> [!quote] **p.1** · Highlight
> 通过飞行器模拟,我们验证了分析模型,并展示了二维正交网 格网络空域中平均流量与平均密度之间的关系。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=1&annotation=Q4B5Z5FK)


> [!quote] **p.2** · Highlight
> 限的城市空域能否以及如何维持这样的密度。  在先前的研究中,已经表明对空域施加某种结构可以对容量和安全产生有益影响。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=2&annotation=XYVNZE37)


> [!quote] **p.3** · Highlight
> 提出了一种分析方法,用于估计平均流入率与平均 密度之间的关系,为此我们使用二维正交网格网络空域。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=LQ2RT7PN)


> [!quote] **p.3** · Highlight
> 2. 空域容量模型

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=ISG7DND6)


> [!quote] **p.3** · Highlight
> 对于自由的、无约束的空域,存在几种空域容量的分析模型。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=NZ9X3IIC)


> [!quote] **p.3** · Highlight
> 使用宏观基本图,可以观察道路 网络的行为,从而确定交通状态(自由流或拥堵)、临界密度和效率。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=G7QVM5JS)


> [!quote] **p.3** · Highlight
> 由于在受限城市环境中飞机行为与道路交通行为有许多相似之处,因此将宏观基本图应用于评估受限城 市空域具有潜力,因此本文将对此进行探索。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=HKPZB3N6)


> [!quote] **p.4** · Highlight
> 4. 受限环境中的飞机相互作用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=4&annotation=9JYKG5ZI)


> [!quote] **p.5** · Highlight
> 4.1. 两条流的直飞交通在单个交叉点处的相互作

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=5&annotation=PHFITGPH)


> [!quote] **p.5** · Highlight
> 用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=5&annotation=5ZW6P8XB)


> [!quote] **p.5** · Highlight
> 4.2. 单交叉口处转弯交通与直飞交通的相互作用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=5&annotation=GU7B6TAE)


> [!quote] **p.6** · Highlight
> 4.3. 受限城市空域中冲突解决导致的宏观相互作用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=6&annotation=48R3B6HU)


> [!quote] **p.7** · Highlight
> 5. 受限城市空域的解析计算

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=7&annotation=MKM8BRQD)


> [!quote] **p.8** · Highlight
> 5.1. 分析延误模型

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=8&annotation=NNQZJDSX)


> [!quote] **p.10** · Highlight
> 5.3. 空域容量度量

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=10&annotation=XF82ZR34)


> [!quote] **p.10** · Highlight
> 我们关注理论通行能力(即最大稳定流量)及其影响因素。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=10&annotation=PFFQWLWG)


> [!quote] **p.10** · Highlight
> 我们旨在建立一个模拟,以便能够捕捉我们想要研究的元素的本质。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=10&annotation=AEEZR6Y2)


> [!quote] **p.11** · Highlight
> 通过随机恒定流入量生成场景,使交通密度基本保持稳定。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=11&annotation=576N9TIK)


> [!quote] **p.12** · Highlight
> 引入了 参数

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=12&annotation=69ENSUIL)


> [!quote] **p.13** · Highlight
> 7.2. 理论空域容量与模拟空域容量的比较

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=13&annotation=5YURAVP8)


> [!quote] **p.1** · Highlight
> 推导了受限空域中空中交通的分析模型，以找出影响其容量的 通过飞行器模拟，我们验证了分析模型，并展示了二维正交网 空域中平均流量与平均密度之间的关系。结果表明，当仅一个 因素。通过飞行器模拟，我们验证了分析模型， 格网络空域中平均流量与平均密度之间的关系。 交叉路口达到最大容量时，整个空域可能会变得

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=1)


> [!quote] **p.2** · Highlight
> 市空域。在常规的航路空域中，并未出现如此高的飞机密度和增加的限制水平，这就 限的城市空域能否以及如何维持这样的密度。 在先前的研究中，已经表明对空域施加某种结构可以对容量和安全产生有益影响。 等人（年）得出结论，无约束空域容量受益于有限程度的结构化，即增加

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=2)


> [!quote] **p.3** · Highlight
> 年）以及此后的其他各个城市中 。使用宏观基本图，可以观察道路 得到了实验验证。有关个城市的比较，请参见等人（年）。 网络的行为，从而确定交通状态（自由流或拥堵）、临界密度和效率。 由于在受限城市环境中飞机行为与道路交通行为有许多相似之处，因

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 由于在受限城市环境中飞机行为与道路交通行为有许多相似之处，因此将宏观基本图应用于评估受限城 空域具有潜力，因此本文将对此进行探索。此前已经基于特定的冲突避免使用模拟进行了一些初步探索 由于在受限城市环境中飞机行为与道路交通 市空域具有潜力，因此本文将对此进行探索。 （例如，等人，年；和

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 提出了一种分析方法，用于估计平均流入率与平均 。结果，可以量化几个空域设计参数对受限城市空 因此，本研究将调查影响受限城市空域容量的因素。提 密度之间的关系，为此我们使用二维正交网格网络空域。 域容量的影响。这些见解可用于城市空域设计应用。它们

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 2. 空域容量模型

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 对于自由的、无约束的空域，存在几种空域容量的分析模型。这 与空域稳定性和冲突概率联系起来。它们通常被称为“气体模型

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.4** · Highlight
> 4. 受限环境中的飞机相互作用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=4)


> [!quote] **p.5** · Highlight
> 4.2. 单交叉口处转弯交通与直飞交通的相互作用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=5)


> [!quote] **p.5** · Highlight
> 4.1. 两条流的直飞交通在单个交叉点处的相互作用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=5)


> [!quote] **p.5** · Highlight
> 用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=5)


> [!quote] **p.6** · Highlight
> 4.3. 受限城市空域中冲突解决导致的宏观相互作用

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=6)


> [!quote] **p.7** · Highlight
> 5. 受限城市空域的解析计算

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=7)


> [!quote] **p.8** · Highlight
> 5.1. 分析延误模型

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=8)


> [!quote] **p.10** · Highlight
> 5.3. 空域容量度量

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=10)


> [!quote] **p.10** · Highlight
> 我们旨在建立一个模拟，以便能够捕捉我们想要研究的元素的本质。因 ，并且由于我们考虑的是受限空域（例如，建筑物之间），所以我们考

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=10)


> [!quote] **p.10** · Highlight
> 我们关注理论通行能力（即最大稳定流量）及其影响因素。 之间过渡点的度量，我们根据假设，基于平均队列长度（以

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=10)


> [!quote] **p.11** · Highlight
> 通过随机恒定流入量生成场景，使交通密度基本保持稳定。 变量间隔引入，即按平均流入率 呈指数分布。表总结了模

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=11)


> [!quote] **p.12** · Highlight
> 模型预测与模拟 引入了 参数

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=12)


> [!quote] **p.13** · Highlight
> 7.2. 理论空域容量与模拟空域容量的比较

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=13)



### Blue

> [!quote] **p.3** · Highlight
> 这些模型使用基于二项式组合的方程将容 量与空域稳定性和冲突概率联系起来。它们通常被称为“气体模型”方程,自20世纪60年代末以来已在航空 研究中提出

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=6R3U76JA)


> [!quote] **p.3** · Highlight
> 在受限环境中,基于速度的冲突解决机动产生的一个突发行为是,飞机在繁忙交叉路口上游排队。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=R8PWPT9R)


> [!quote] **p.3** · Highlight
> 沿着街道行驶的交通本质上 的一维性质将导致连锁冲突更加普遍,这降低了冲突计数模型和多米诺效应模型作为空域容量预测指标的 价值。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=WJGHN6G2)


> [!quote] **p.3** · Highlight
> 总之,现有的分析模型对受限城市空域无效,这表明  需要一个量身定制的分析模型。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=KVEFHYF2)


> [!quote] **p.15** · Highlight
> 本文采用分析方法 来增进对影响受限城市空域容量的因素的理解。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=15&annotation=2QWQD8PD)


> [!quote] **p.15** · Highlight
> 因此,本文推导了一个新的数学模型,用于估计二维正交网格网络中平 均流入率与平均密度之间的关系,类似于宏观基本图的自由流部分。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=15&annotation=8X2D6BEU)


> [!quote] **p.3** · Highlight
> 证。有关㐱 个城 网络的行为，从而确定交通状

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 战术性航路冲突解决将使用基于速度的算法执行。 在受限环境中，基于速度的冲突解决机动产生的一个突发行为是，飞机在繁忙交叉路口上游排队。 说，在一条航路内，一架飞机可能会与直接在其前方的飞机持续发生冲突。沿着街道行驶的交通本质

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> ，㈰ㄷ 年； （例如，䩡湧 等人，㈰ㄷ 年；

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 。受限城市空域就是一个有许多热点的环境的明显例 。总之，现有的分析模型对受限城市空域无效，这表明 子，因为交通可能会集中在繁忙 需要一个量身定制的分析模型。 虽然受限城市空域与非受限空

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.15** · Highlight
> 本文采用分析方法 队和局部热点，使 预计在不久的将来，高度受限的低空城市空域 来增进对影响受限城市空域容量的因素的理解。 得现有的一般空域分析模型无效。因此，本文推

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=15)


> [!quote] **p.15** · Highlight
> 的因素的理解。受限城市空域中飞机的涌现行为，如排队和局部热点，使 。因此，本文推导了一个新的数学模型，用于估计二维正交网格网络中平 ，类似于宏观基本图的自由流部分。通过进行涉及超过次飞行的三 得现有的一般空域分析模型无效。因此，本文推导了一个新的数学模 均流入率与平均密度之间的关系，类似于宏观基本图的自由流部分。 次模拟实验，该数学模型的准确率高于。这一高准确率证实了该

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=15)



### Magenta

> [!quote] **p.3** · Highlight
> 相反,网络效率和不稳定性得到了广泛研究。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=WN9S7BQR)


> [!quote] **p.3** · Highlight
> 这种关系在所谓的宏观基本图(MFD)中得到了体现 ,该图已在日本横滨的实际道路交通研究中(Geroliminis和Daganzo,2008年)以及此后的其他各个城市中 得到了实验验证。

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3&annotation=XRJEFTB4)


> [!quote] **p.3** · Highlight
> 和，年；等人，年； 这种关系在所谓的宏观基本图（MFD）中得到了体现 和，年）以及此后的其他各个城市中 和，年；等人，年）。这种关系在所谓的宏观基本图（）中得到了体现 ，该图已在日本横滨的实际道路交通研究中（Geroliminis和Daganzo，2008年）以及此后的其他各个城市中 得到了实验验证。有关个城市的比较，请参见等人（年）。使用宏观基本图，可以观察道路 ，该图已在日本横 得到了实验验证。 网络的行为，从而

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)


> [!quote] **p.3** · Highlight
> 量建模的一个明显灵感来源。与我们上面关于 相反，网络效率和不稳定性得到了广泛研究。 密度之间的关系上（和，

>
> **💬 批注**: （在 Zotero 中对该高亮添加评论，导入时会自动带出）

>
> [📍 跳转到 PDF 具体位置](zotero://open-pdf/library/items/7VVLK457?page=3)






---

## 💭 我的思考

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 核心论点 / 方法启示 / 可复用的点 / 存疑待验证
>
%% begin thoughts %%
%% end thoughts %%

## 🔗 关联与行动

> [!note] 📝 手写区（重新导入不会覆盖这里的内容）
> 关联文献 [[citekey]] · 关联主题 [[标签]] · 待办清单
>
%% begin actions %%
%% end actions %%

<!--
颜色编码建议（可在 Zotero 中自定义）：
🟡 黄 = 核心论点/重要结论  🟢 绿 = 方法/模型/数据来源  🔵 蓝 = 结果/发现/实证数据
🔴 红 = 局限/问题/批判     🟣 紫 = 概念/定义/术语       🟥 品红 = 疑问/待查证
⚪ 灰 = 一般背景信息
持久化说明：元数据/AI摘要/高亮 = 自动刷新；一句话总结/文献速览/我的思考/关联行动 = 写在 %% begin/end %% 标记间（Obsidian 阅读模式下标记自动隐藏），重导不丢。
-->


%% Import Date: 2026-09-08T15:56:54.457+08:00 %%
