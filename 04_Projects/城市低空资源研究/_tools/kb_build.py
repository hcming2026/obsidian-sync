# -*- coding: utf-8 -*-
"""
城市低空资源研究 - 参考文献知识库构建脚本 v3（论文独立笔记版 + 阅读状态 + Zotero 关联）
v3 新增：
  - frontmatter 增加 status（未读/精读中/已精读/待复核）与 abstractStatus（完整/片段/待补）
  - 论文笔记新增"## 摘录"区块（供粘贴 Zotero 高亮链接 + 自己的话），重跑脚本时该区块内容保留
  - 已关联 Zotero 的论文自动生成"## Zotero 关联"区块（zotero:// 跳转链接 + 引用键）
  - 用户手动改过的 status（非默认值）在重跑时保留

用法：python kb_build.py
输出：
  参考文献/论文/<文件名>.md     每篇论文一个笔记
  作者资料/<作者名>.md          作者笔记（链接论文）
  期刊/<期刊名>.md              期刊笔记（链接论文）
"""
import os, json, re

BASE = r"D:\claude\hcmingGo\hcmingGo\04_Projects\城市低空资源研究"
AUTH_DIR = os.path.join(BASE, "作者资料")
JOUR_DIR = os.path.join(BASE, "期刊")
PAPER_DIR = os.path.join(BASE, "参考文献", "论文")

# 摘要缓存（Semantic Scholar 批量查询结果，14 篇）
S2 = {}
_s2path = os.path.join(BASE, "_tools", "s2_abstracts.json")
if os.path.exists(_s2path):
    S2 = json.load(open(_s2path, encoding="utf-8"))

# 阅读状态：未填写的论文默认"未读"
STATUS = {
    "taye2024": "精读中",   # 示例论文，正在 Zotero 中精读
}

# 已确认的 Zotero 条目：pid -> (条目key, citation key)
# 其余论文尚未可靠匹配 Zotero 条目，先不写入，避免错误关联
ZOTERO = {
    "taye2024": {"key": "HDXSQBPQ", "citekey": "tayeEnergyDemandAnalysis2024"},
}

# 摘要来源 -> 状态标签
ABSTRACT_STATUS = {"s2": "完整", "search": "片段", "none": "待补"}

# 每篇论文：id, 文件名, 原文标题, 短标题, 年份, [作者], 期刊, DOI, 卷期, 摘要来源, 摘要, 用途
# 摘要来源: s2=Semantic Scholar全文 / search=检索片段 / none=未获取
PAPERS = [
    # ---------- 第 1 节 模型精细度与模型复杂度 ----------
    ("priesmann2019", "Priesmann 2019 - 模型复杂度与精度",
     "Are complex energy system models more accurate? An intra-model comparison of power system optimization models",
     "Are complex energy system models more accurate?", 2019,
     ["Priesmann J", "Nolting L", "Praktiknjo A"], "Applied Energy",
     "10.1016/j.apenergy.2019.113783", "255: 113783", "s2", None,
     "复杂度—精度边际收益递减的直接证据，适合作为方法论主引用。"),

    ("wirtz2021", "Wirtz 2021 - 多能源系统MILP模型细节",
     "Design optimization of multi-energy systems using mixed-integer linear programming: Which model complexity and level of detail is sufficient?",
     "Design optimization of multi-energy systems using MILP", 2021,
     ["Wirtz M", "Hahn M", "Schreiber T", "Müller D"], "Energy Conversion and Management",
     "10.1016/j.enconman.2021.114249", "2021", "s2", None,
     "研究问题几乎与本论文相同，是\"最低够用复杂度\"框架的最近对标。"),

    ("gils2022", "Gils 2022 - 电力部门模型对比",
     "Modeling flexibility in energy systems — comparison of power sector models based on simplified test cases",
     "Modeling flexibility in energy systems", 2022,
     ["Gils H C", "Gardian H", "Kittel M"], "Renewable and Sustainable Energy Reviews",
     "10.1016/j.rser.2021.111995", "158: 111995", "s2", None,
     "高影响力综述型模型对比，证明\"同问题、不同细节层级\"的研究范式成立。"),

    ("nigischer2023", "Nigischer 2023 - FlexSim保真度层级",
     "Finding the proper level of detail to achieve sufficient model fidelity using FlexSim: An industrial use case",
     "Finding the proper level of detail to achieve sufficient model fidelity using FlexSim", 2023,
     ["Nigischer C", "Reiterer F", "Bougain S", "Grafinger M"], "Procedia CIRP",
     "10.1016/j.procir.2023.02.192", "119: 1240–1245", "search",
     "Because high-fidelity modelling is always a time-consuming and therefore expensive task, the necessary level of detail of a simulation model is an important question to answer. The goal of this work is to examine the different levels of detail of a series of models created for a complex industrial production system utilizing the FlexSim simulation environment, with an iterative modelling approach.",
     "近期\"足够保真即可\"的实证案例，用于说明研究空白仍未完全闭合。"),

    ("madan2005", "Madan 2005 - FMS仿真保真度",
     "Determination of efficient simulation model fidelity for flexible manufacturing systems",
     "Determination of efficient simulation model fidelity", 2005,
     ["Madan M S", "Son Y J", "Cho H", "Kulvatunyou B"], "International Journal of Computer Integrated Manufacturing",
     "10.1080/0951192052000288143", "18(2-3): 236–250", "search",
     "This paper presents a framework for the determination of an efficient level of simulation model fidelity for flexible manufacturing systems, which will achieve acceptable output accuracy with minimum resources and thereby reduce model building effort and computation time. To this end, we first formally define different levels of model fidelity (five levels) using object-oriented (O-O) modelling.",
     "早期经典文献，用于交代模型精细度选择问题的历史沿革。"),

    ("daganzo2012", "Daganzo 2012 - 简约交通模型",
     "The potential of parsimonious models for understanding large scale transportation systems and answering big picture questions",
     "The potential of parsimonious models", 2012,
     ["Daganzo C F", "Gayah V V", "Gonzales E J"], "EURO Journal on Transportation and Logistics",
     "10.1007/s13676-012-0003-z", "1(1–2): 47–65", "s2", None,
     "交通领域\"简约模型\"的方法论宣言，说明\"够用即可\"在交通建模中已有思想传统。"),

    ("peinturier2025", "Peinturier 2025 - 建筑仿真校准复杂度",
     "Building energy simulation calibration accuracy and modelling complexity: Implications for energy performance improvement",
     "Building energy simulation calibration accuracy and modelling complexity", 2025,
     ["Peinturier L", "Wallom D"], "Energy and Buildings",
     "10.1016/j.enbuild.2025.115971", "344: 115971", "search",
     "Building Energy Simulation (BES) offers valuable virtual assessment of decarbonisation strategies but faces implementation challenges due to the complex balance between accuracy, modelling detail, and data availability. This study proposes a novel integrated framework that correlates input data quality, modelling complexity, and ECM (energy conservation measure) reliability across diverse building types and sizes, and introduces a quantitative scoring.",
     "用敏感度分析判断\"哪些模型简化可接受、哪些必须保留\"，可直接迁移到你的判断流程。"),

    ("schricker2001", "Schricker 2001 - 保真度评价框架FEF",
     "Fidelity Evaluation Framework",
     "Fidelity Evaluation Framework", 2001,
     ["Schricker B C", "Franceschini R W"], "Proceedings of the IEEE Annual Simulation Symposium",
     "10.1109/SIMSYM.2001.922122", "2001: 109–116", "search",
     "While the modeling and simulation community commonly uses the word fidelity, there exists no clearly accepted definition or method of measuring fidelity. We present a new approach for measuring fidelity: the Fidelity Evaluation Framework (FEF), that uses a referent (a formal representation of reality intermediate between reality and the simulation). The paper proposes and illustrates three new methods of computing fidelity objectively within the FEF: category-based, model-based and weight-based.",
     "早期\"保真度评价框架\"，适合做方法论谱系起点。"),

    ("muller2021", "Müller 2021 - EV充电模型与配电网规划",
     "Impact of different electric vehicle charging models on distribution grid planning",
     "Impact of different electric vehicle charging models on distribution grid planning", 2021,
     ["Müller T", "Ali S A", "Becker M"], "CIRED",
     "10.1049/icp.2021.1858", "2021", "s2", None,
     "直接比较\"简化充电模型 vs 完整充电模型\"对电网规划的影响，和你的 F0–F4 对比思路一致。"),

    # ---------- 第 2 节 低空交通网络与管理 ----------
    ("fu2026", "Fu 2026 - 空中高速路",
     "Sky highway: An air traffic structure for low-altitude heterogeneous VTOL aircraft",
     "Sky highway: An air traffic structure for low-altitude heterogeneous VTOL aircraft", 2026,
     ["Fu R", "Safadi Y", "Quan Q", "Haddad J"], "Transportation Research Part C",
     "10.1016/j.trc.2026.105531", "185: 105531", "none", None,
     "低空\"空中高速路\"网络结构，TRC 最新低空交通组织方法。"),

    ("weng2025", "Weng 2025 - 低空交通动静态管理",
     "Urban low-altitude air transport management: Bridging dynamic traffic control and static network equilibrium",
     "Urban low-altitude air transport management", 2025,
     ["Weng C", "Pan T", "Chen C", "Zhong R"], "Transportation Research Part C",
     "10.1016/j.trc.2025.105237", "178: 105237", "none", None,
     "城市低空交通管理的动静态模型衔接，最贴近 TRC 框架的低空论文之一。"),

    ("kitthamkesorn2024", "Kitthamkesorn 2024 - UAM网络最大捕获",
     "Maximum capture problem for urban air mobility network design",
     "Maximum capture problem for urban air mobility network design", 2024,
     ["Kitthamkesorn S", "Chen A"], "Transportation Research Part E",
     "10.1016/j.tre.2024.103569", "187: 103569", "none", None,
     "UAM 网络设计的设施捕获模型，作为案例侧供给侧方法参照。"),

    ("he2024", "He 2024 - 无人机分布式航路规划",
     "A distributed route network planning method with congestion pricing for drone delivery services in cities",
     "A distributed route network planning method with congestion pricing", 2024,
     ["He X", "Li L", "Mo Y", "Huang J", "Qin S J"], "Transportation Research Part C",
     "10.1016/j.trc.2024.104536", "160: 104536", "search",
     "Structured route-based UAV operations have been implemented for traffic management of UAVs in support of commercial delivery services in cities. Yet, its essence, multi-path planning with constraints is not well solved. Centralized planning might result in inefficiencies and unfairness in the allocation of precious urban airspace to individual routes. This paper describes a novel distributed route planning method to support UAV operations in a high-density urban environment: each origin–destination (OD) pair competes for an optimized route (e.g. shortest distance), coordinated by a system-level evaluation. The core concept is the introduction of congestion pricing, a soft constraint to coordinate the allocation of airspace.",
     "低空物流航路网络规划，反衬充电负荷精细度问题仍少人研究。"),

    # ---------- 第 3 节 低空 / UAM / 机场充电需求与电网 ----------
    ("wu2025", "Wu 2025 - UAM智能充电与电网",
     "Integrating urban air mobility into the power grid through smart charging solutions",
     "Integrating urban air mobility into the power grid through smart charging solutions", 2025,
     ["Wu J", "Cao S", "Hansen M", "González M C"], "Transportation Research Part C",
     "10.1016/j.trc.2025.105281", "179: 105281", "search",
     "Adapting the existing power grid to support large-scale UAM operations using eVTOL aircraft presents a critical infrastructural challenge. This paper presents a framework for estimating the potential of smart charging to improve power system welfare when integrating large-scale UAM into the power grid. We first estimate passenger travel demand for UAM from location-based service (LBS) data, then evaluate smart charging strategies.",
     "TRC 顶刊直接研究 UAM 充电需求与电网，是最主要对标论文。"),

    ("fan2026a", "Fan 2026 - 低空经济多模态能源",
     "Analysis of multi-modal energy supply and power systems adaptability for eVTOL and UAV applications in the low-altitude economy",
     "Analysis of multi-modal energy supply and power systems adaptability", 2026,
     ["Fan P", "Bu S", "Zhu M", "Wen Y", "Li S", "Zhang G", "Zhang C"], "eTransportation",
     "10.1016/j.etran.2026.100626", "29: 100626", "none", None,
     "明确以\"low-altitude economy\"为对象，做多模态能源供应与电力适配，是案例最直接的对标。"),

    ("fan2026b", "Fan 2026 - 短途航空电气化",
     "Empowering short-haul aviation electrification: Insights into load characterization, grid adaptability, and social welfare",
     "Empowering short-haul aviation electrification", 2026,
     ["Fan P", "Bu S", "Li S", "Wen Y"], "eTransportation",
     "10.1016/j.etran.2026.100585", "28: 100585", "none", None,
     "负荷特征刻画 + 电网适配 + 社会福利，方法可借鉴。"),

    ("qian2026", "Qian 2026 - 城市能源与三维交通集成",
     "Urban energy and three-dimensional mobility integration for eVTOL scale-up",
     "Urban energy and three-dimensional mobility integration for eVTOL scale-up", 2026,
     ["Qian T", "Yue J", "Wang C", "Hu Q", "Hui H"], "Applied Energy",
     "10.1016/j.apenergy.2026.128226", "421: 128226", "none", None,
     "把垂直起降场定义为\"能源—交通耦合节点\"，支撑问题设定。"),

    ("chen2024", "Chen 2024 - UAM交通需求影响",
     "Potential short- to long-term impacts of on-demand urban air mobility on transportation demand in North America",
     "Potential short- to long-term impacts of on-demand UAM", 2024,
     ["Chen S K", "Shamshiripour A", "Seshadri R"], "Transportation Research Part A",
     "10.1016/j.tra.2024.104288", "190: 104288", "search",
     "The study develops a modeling framework including (iii) a demand-driven vertiport placement and capacity generation module. The results show that the UAM market is expected to start narrow (0.187% to 0.197% of all trips) and remain niche in the long term (1.45% to 1.81% of all trips) for both cities. In addition, the service is expected to increase mobility inequality, even in the long term.",
     "批评现有模型忽略充电、场内活动与容量，是研究空白的直接证据。"),

    ("li2025", "Li 2025 - 城际低空航线规划",
     "Electrifying regional mobility: Planning intercity low-altitude air routes for Chinese cities",
     "Electrifying regional mobility: Planning intercity low-altitude air routes", 2025,
     ["Li Y"], "The Innovation Energy",
     "10.59717/j.xinn-energy.2025.100113", "2(4): 100113", "search",
     "With the rise of eVTOL aircraft, intercity low-altitude air routes (LAARs) are emerging as a new paradigm in urban mobility and regional transportation. Through integrating demand-driven planning, straight-line distance, and infrastructure readiness across four key domains, we propose a planning framework for intercity LAARs of China Cities to enhance urban air mobility (UAM).",
     "低空航线电能需求分析，兼顾中国场景与基础设施需求。"),

    ("coenen2024", "Coenen 2024 - 机场电量容量需求",
     "Estimating Electrical Energy and Capacity Demand for Regional Electric Flight Operations at Two Mid-Size Airports in Washington, U.S.",
     "Estimating Electrical Energy and Capacity Demand for Regional Electric Flight Operations", 2024,
     ["Coenen T", "Malarkey A", "MacKenzie D"], "Transportation Research Record",
     "10.1177/03611981231201110", "2678(6): 911–925", "s2", None,
     "机场级电量/容量需求估算，用于和\"精细化到哪一步\"形成对比。"),

    ("dong2026", "Dong 2026 - 航班感知充电与机场电价",
     "Evaluating flight-aware charging for electric aircraft under airport-specific pricing",
     "Evaluating flight-aware charging for electric aircraft under airport-specific pricing", 2026,
     ["Dong H", "Chung C-Y", "Chen Y"], "Transport Policy",
     "10.1016/j.tranpol.2026.104229", "186: 104229", "none", None,
     "电动飞机\"航班感知充电\"与机场定价，补充机场充电策略模型。"),

    ("han2025", "Han 2025 - UAM滚动时域调度",
     "Rolling horizon optimization of urban air mobility (UAM) service with shared riding, vertiport-airspace capacity, and recharge",
     "Rolling horizon optimization of UAM service with shared riding and recharge", 2025,
     ["Han H", "Song B D"], "Transportation Research Part E",
     "10.1016/j.tre.2025.104548", "2025", "search",
     "Urban Air Mobility (UAM) is expected to become a new form of urban transportation, using eVTOL vehicles to help reduce congestion and lower emissions. However, the operational complexity of UAM demands sophisticated planning that accounts for constraints unique to aerial environments. This study develops an integrated routing optimization framework for multi-eVTOL operations, considering battery limitations, vertiport and air corridor capacities, minimum turnaround times, and passenger pooling through stopovers.",
     "同时考虑垂直起降场容量、空域容量与充电约束的 UAM 调度，案例侧建模细节参照。"),

    ("preis2022", "Preis 2022 - 垂直起降场ABM仿真",
     "Vertiport Operations Modeling, Agent-Based Simulation and Parameter Value Specification",
     "Vertiport Operations Modeling, Agent-Based Simulation and Parameter Value Specification", 2022,
     ["Preis L", "Hornung M"], "Electronics",
     "10.3390/electronics11071071", "11(7): 1071", "s2", None,
     "垂直起降场 Agent 仿真与参数取值，直接对应你 F0–F4 里的细节参数。"),

    ("nagrare2026", "Nagrare 2026 - 垂直起降场吞吐能力",
     "Throughput and Capacity Analysis of a Vertiport with Taxiing and Parking Levels",
     "Throughput and Capacity Analysis of a Vertiport with Taxiing and Parking Levels", 2026,
     ["Nagrare S R", "Lieb T J"], "Aerospace",
     "10.3390/aerospace13010109", "13(1): 109", "s2", None,
     "垂直起降场滑行/停放/充电层级对吞吐能力的影响，适合\"细节保留到哪一层\"的对照。"),

    ("doctor2022", "Doctor 2022 - 电动飞机机场运营",
     "Modelling the effect of electric aircraft on airport operations and infrastructure",
     "Modelling the effect of electric aircraft on airport operations and infrastructure", 2022,
     ["Doctor F", "Budd T", "Williams P D", "Prescott M", "Iqbal R"], "Technological Forecasting and Social Change",
     "10.1016/j.techfore.2022.121553", "2022", "s2", None,
     "电动飞机对机场运营与基础设施影响的建模，交代机场侧研究基础。"),

    ("nature2026", "Nature 2026 - 机场GSE电动化需求",
     "Energy, power, and infrastructure demands from electrifying airport ground support equipment at United States airports",
     "Energy, power, and infrastructure demands from electrifying airport ground support equipment", 2026,
     [], "Nature Communications",
     "10.1038/s41467-026-71125-4", "17: 4612", "s2", None,
     "顶刊机场地面保障设备电动化的充电负荷与基础设施需求，方法上可对比\"简化 vs 精细\"建模。"),

    ("taye2024", "Taye 2024 - eVTOL充电站能量需求",
     "Energy Demand Analysis for eVTOL Charging Stations in Urban Air Mobility",
     "Energy Demand Analysis for eVTOL Charging Stations in Urban Air Mobility", 2024,
     ["Taye A G", "Pradeep P", "Wei P", "Jones J C", "Bonin T", "Eberle D"], "AIAA AVIATION Forum and ASCEND",
     "10.2514/6.2024-4627", "AIAA 2024-4627", "s2", None,
     "eVTOL 充电站能量需求分析的早期会议论文，用于展示该问题正在形成研究线（充电脉冲库精读条目）。"),

    # ---------- 第 4 节 综述与中文低空文献 ----------
    ("garrow2021", "Garrow 2021 - UAM综合综述",
     "Urban air mobility: A comprehensive review and comparative analysis",
     "Urban air mobility: A comprehensive review and comparative analysis", 2021,
     ["Garrow L A", "German B J", "Leonard C E"], "Transportation Research Part C",
     "10.1016/j.trc.2021.103377", "2021", "s2", None,
     "TRC 顶刊 UAM 综述，引言首选引用。"),

    ("schweiger2022", "Schweiger 2022 - 垂直起降场综述",
     "Urban Air Mobility: Systematic Review of Vertiport Design and Operations",
     "Urban Air Mobility: Systematic Review of Vertiport Design and Operations", 2022,
     ["Schweiger K", "Preis L"], "Drones",
     "10.3390/drones6070179", "6(7): 179", "s2", None,
     "垂直起降场设计与运营综述，确认充电负荷精细度研究缺口。"),

    ("kotwicz2024", "Kotwicz 2024 - 机队与起降场规模",
     "Fleet and Vertiport Sizing for Urban Air Mobility",
     "Fleet and Vertiport Sizing for Urban Air Mobility", 2024,
     ["Kotwicz Herniczek M T", "German B J", "Preis L"], "Transportation Research Record",
     "10.1177/03611981231216977", "2024", "s2", None,
     "机队与垂直起降场规模匹配，案例侧间接支撑。"),

    ("li2020", "李诚龙 2020 - eVTOL交通管理综述",
     "面向eVTOL航空器的城市空中运输交通管理综述",
     "面向eVTOL航空器的城市空中运输交通管理综述", 2020,
     ["李诚龙", "屈文秋", "李彦冬"], "交通运输工程学报",
     "10.19818/j.cnki.1671-1637.2020.04.003", "20(4): 35–54", "search",
     "UAM将直接面对更为复杂的有人机、无人机融合运行场景，UAM交通规则需要革新并对现有的运输航空交通规则保持兼容，高带宽的通信技术会促使UAM运行控制向空地协同决策和自动驾驶方向发生转变，未来交通管理中如何处理人与系统的关系至关重要。UAM交通管理将可能会和现有无人机交通管理体系产生交集并逐渐融合。",
     "国内低空/UAM 交通管理权威综述，交代中文研究现状。"),

    ("quan2020", "全权 2020 - 低空无人机交通管理",
     "低空无人机交通管理概览与建议",
     "低空无人机交通管理概览与建议", 2020,
     ["Quan Q", "李刚", "柏艺琴"], "航空学报",
     "10.7527/S1000-6893.2019.23238", "41(1): 023238", "search",
     "大量无序飞行的低空无人机运行会对地面设施、公共安全、空中载人飞行器等带来危害。然而，目前民航空中交通管理不能适应未来数以百万架的无人机。为了应对该挑战，世界各国针对低空无人机空中交通管理开发了新框架。本文聚焦于低空无人机交通管理，从4个方面进行概览：低空无人机相关的空中交通基本概念及现状、低空无人机交通管理介绍、低空无人机交通管理的关键技术和低空无人机交通管理相关科学问题。",
     "国内低空无人机交通管理的早期权威框架，引言用。"),
]

# 中文要点（研究问题/方法/数据/结论/局限），以 id 索引
KEYPOINTS = {
    "priesmann2019": ("能源系统模型越复杂，结果就越准确吗？",
        "基于替代模型表述的框架，对电力系统调度与投资问题构造 160 个不同复杂度的优化模型实现并横向对比。",
        "160 个复杂度递增的电力系统优化模型。",
        "一定程度的复杂度确实是获得足够精度所必需的，但复杂度—精度存在边际收益递减。",
        "单一领域（电力系统优化），未给出\"最优复杂度\"的通用判据。"),
    "wirtz2021": ("多能源系统 MILP 优化设计中，需要多少模型细节才能得到可靠设计？",
        "系统性对比 24 个 MILP 模型，组合 5 种常用模型特征（分段线性投资曲线、多组件分辨率、最小部分负荷限制、部分负荷效率等）。",
        "24 个 MILP 多能源系统设计模型。",
        "不同细节组合会显著影响设计结果可靠性；存在\"足够细节\"的最低要求。",
        "多能源系统单一场景，结论迁移需验证。"),
    "gils2022": ("不同电力部门模型对同一未来情景为何会得出偏差结论？",
        "9 个带部门耦合的电力部门模型在统一简化测试用例上的系统对比，分析技术表征方式、优化方法等差异的影响。",
        "9 个电力部门模型 + 简化测试用例。",
        "模型对技术的表征方式（而非仅输入数据）是结果差异的重要来源。",
        "基于简化测试用例，与真实系统规模有差距。"),
    "nigischer2023": ("仿真模型需要多少细节才能达到足够保真度？",
        "用 FlexSim 对复杂工业产线建立一系列不同细节层级的模型，迭代建模并对比。",
        "复杂工业产线（FlexSim 仿真环境）。",
        "高保真建模耗时昂贵，须在细节与成本间权衡，存在\"足够保真即可\"的细节层级。",
        "单案例、单仿真工具。"),
    "madan2005": ("柔性制造系统仿真中如何确定\"高效\"的模型保真度层级？",
        "提出保真度确定框架，用对象导向建模形式化定义 5 个保真度层级。",
        "柔性制造系统案例。",
        "可用最少资源达到可接受的输出精度，显著降低建模工作量与计算时间。",
        "早期框架、制造业场景，依赖具体建模工具。"),
    "daganzo2012": ("简约模型能否理解大规模交通系统、回答宏观问题？",
        "梳理交通领域\"有效简约模型\"的历史，按子领域分类综述。",
        "文献综述。",
        "简约模型提供聚焦细节时容易丢失的洞察，特别适合回答 big-picture 问题。",
        "观点性/综述性文献，非实证。"),
    "peinturier2025": ("建筑能耗仿真的校准精度、建模复杂度与数据可得性如何交互影响节能措施建模可靠性？",
        "集成框架关联输入数据质量、建模复杂度与 ECM 可靠性，跨建筑类型与规模，引入定量评分。",
        "多样建筑类型与规模（DesignBuilder 模型，数据已公开）。",
        "精度、细节与数据三者需平衡，复杂度不足或数据质量差都会损害 ECM 可靠性。",
        "结论依赖建筑仿真场景，迁移需重估。"),
    "schricker2001": ("仿真保真度如何客观定义与度量？",
        "保真度评价框架 FEF：以 referent 隔离主观性，给出 category-based / model-based / weight-based 三种客观计算方法。",
        "实验验证 FEF 可提供有意义且有用的保真度测量。",
        "FEF 可将保真度评价主观性收敛到明确定义的框架组件。",
        "早期框架，未被广泛采纳为标准。"),
    "muller2021": ("EV 充电过程的建模假设差异对配电网规划结果有何影响？",
        "对比简化充电过程建模与完整（精细化）充电过程建模对配电网负荷的影响。",
        "配电网规划案例。",
        "充电过程建模假设会显著影响电网规划结论。",
        "地面 EV 场景。"),
    "fu2026": ("面向低空异构 VTOL 机群的\"空中高速路\"交通结构如何设计？",
        "空中高速路网络结构设计与分析（待精读原文）。",
        "待精读原文补全。",
        "待精读原文补全。",
        "待精读原文补全。"),
    "weng2025": ("城市低空交通管理如何衔接动态交通控制与静态网络均衡？",
        "动、静态交通管理模型的桥接框架（待精读原文）。",
        "待精读原文补全。",
        "待精读原文补全。",
        "待精读原文补全。"),
    "kitthamkesorn2024": ("UAM 网络设计中垂直起降场布点如何最大化需求捕获？",
        "最大捕获问题（MCP）建模，与 weibit 型路径选择模型方法一脉相承（待精读）。",
        "待精读原文补全。",
        "待精读原文补全。",
        "待精读原文补全。"),
    "he2024": ("城市高密度环境下无人机配送的分布式航路网络规划如何解决多路径约束规划？",
        "分布式路由规划：每个 OD 对竞争最优路径，系统级评估协调；拥堵定价作为空域分配软约束。",
        "高密度城市环境。",
        "分布式方法可避免集中式规划的效率与公平问题，实现个体路径与系统网络性能兼优的设计。",
        "案例规模与实证细节待精读。"),
    "wu2025": ("智能充电在多大程度上能改善大规模 UAM 接入电网后的电力系统福利？",
        "先从位置服务（LBS）数据估计 UAM 旅客出行需求，再构建框架评估智能充电对电力系统福利的改善潜力。",
        "LBS 出行数据（美国城市）。",
        "智能充电可显著提升 UAM 并网后的系统福利（具体幅度待精读）。",
        "需求估计依赖 LBS 数据质量。"),
    "fan2026a": ("低空经济中 eVTOL/UAV 的多模态能源供应方案及其电力系统适应性如何？",
        "多模态能源供应建模 + 电力系统适应性分析（待精读原文）。",
        "待精读原文补全。",
        "待精读原文补全。",
        "待精读原文补全。"),
    "fan2026b": ("短途航空电气化的负荷特征、电网适配能力与社会福利如何刻画与评估？",
        "负荷特征刻画 + 电网适配分析 + 社会福利评估（待精读原文）。",
        "待精读原文补全。",
        "待精读原文补全。",
        "待精读原文补全。"),
    "qian2026": ("eVTOL 规模化背景下城市能源系统与三维交通如何集成？",
        "能源—交通耦合建模（待精读原文）。",
        "待精读原文补全。",
        "待精读原文补全。",
        "待精读原文补全。"),
    "chen2024": ("按需 UAM 服务对北美交通需求的短期至长期影响如何？",
        "出行需求建模框架（含需求驱动的垂直起降场布点与容量生成模块）。",
        "北美两座城市。",
        "UAM 初期仅占全部出行 0.187%–0.197%，长期 1.45%–1.81%；且可能加剧出行不平等。",
        "作者指出现有模型普遍忽略充电、场内活动与容量约束。"),
    "li2025": ("中国城际低空航线（LAAR）如何规划以支撑区域交通电气化？",
        "集成需求驱动规划、直线距离与基础设施就绪度四个关键域的城际低空航线规划框架。",
        "中国城市群。",
        "提出面向中国城市群的城际低空航线规划框架以增强 UAM 可达性。",
        "具体算例与量化结论待精读。"),
    "coenen2024": ("区域电动飞机运营在机场层面产生多少电量与容量需求？",
        "估算框架：年电量（MWh）与平均/峰值功率（MW）需求。",
        "美国华盛顿州两个中型机场。",
        "机场电动飞机充电将构成电网显著的新负荷（具体数字待精读）。",
        "两机场案例，外推需谨慎。"),
    "dong2026": ("机场特定电价机制下\"航班感知充电\"策略的效果如何？",
        "航班感知充电建模 + 机场差异化电价评估（待精读原文）。",
        "待精读原文补全。",
        "待精读原文补全。",
        "待精读原文补全。"),
    "han2025": ("同时考虑合乘、垂直起降场/空中走廊容量与充电约束时，多 eVTOL 运营如何集成优化？",
        "多 eVTOL 集成路由优化框架（滚动时域），纳入电池限制、容量约束、最短周转时间与经停合乘；数学模型 + 高效启发式。",
        "待精读原文补全。",
        "集成框架可处理 UAM 运营的复杂约束（具体结果待精读）。",
        "求解规模与算例细节待精读。"),
    "preis2022": ("垂直起降场运营动态（吞吐能力）如何建模？现有静态解析方法有何不足？",
        "首次将 agent-based 仿真（ABM）应用于垂直起降场：对 pads/gates/stands 模型精化，100+ 场景敏感度研究 + 参数规范。",
        "垂直起降场运营模型与参数取值。",
        "静态解析方法不足以刻画运营动态；ABM 可显著提升对吞吐过程的理解。",
        "参数取值依赖假设与规范。"),
    "nagrare2026": ("带滑行层与停放层的垂直起降场，其吞吐能力与充电设施集成如何影响运营？",
        "分离滑行层与停放层建模，分析 eVTOL 在场时间与电池充电设施集成的动态。",
        "垂直起降场设计案例。",
        "充电设施集成方式显著影响垂直起降场吞吐（具体结论待精读）。",
        "待精读原文补全。"),
    "doctor2022": ("电动飞机如何融入现有机场运营与基础设施（地面充电时间 vs 运营容量）？",
        "排队论 + 仿真建模，基于机型预测识别潜在的地面电池充电制度。",
        "基于电动飞机预测情景的机场运营分析。",
        "地面充电时间若不管理将影响机场运营容量；机场需部署充电设施。",
        "情景依赖机型预测。"),
    "nature2026": ("美国机场地面保障设备（GSE）电动化产生多少能源、功率与基础设施需求？",
        "灵活的自底向上建模框架，估算各机场设备数量、充电桩需求与成本。",
        "美国 300+ 机场。",
        "量化了 GSE 电动化新增电力负荷的规模（具体数字待精读）。",
        "仅覆盖地面保障设备，不含飞行充电。"),
    "taye2024": ("垂直起降场的充电能量需求如何基于 eVTOL 能耗模型预测？",
        "eVTOL 能耗模型（旋翼动量理论：诱导/废阻/型阻功率）＋能量最优制导（PSOPT）＋充电过程与需求预测耦合；纳入机型、风况（WRF）与航班任务清单。",
        "达拉斯—沃斯堡（DFW）大型 UAM 网络，4 小时运营时域。",
        "充电需求主要受离场航班数量及其时刻安排影响；充电功率沿时间呈脉冲式聚合。",
        "假设起飞前充满电、忽略充电桩容量与排队约束；仅覆盖巡航段能耗。"),
    "garrow2021": ("UAM 研究进展如何？与 EV/AV 研究相比缺口在哪里？",
        "对 2015.1–2020.6 发表的约 800 篇 UAM/EV/AV 文献做元分析，并对需求建模、运营与基础设施集成做深度综述。",
        "约 800 篇文献。",
        "横向对比三条研究主线，识别 UAM 未来研究重点。",
        "综述覆盖至 2020 年中，后续进展需补充。"),
    "schweiger2022": ("垂直起降场设计与运营的文献与法规现状如何？",
        "系统综述，文档-术语矩阵方法对文献分类、筛选与归纳。",
        "垂直起降场文献 + 监管文件。",
        "识别出垂直起降场研究主题簇与协调需求（具体主题待精读）。",
        "领域快速演进，法规部分时效性有限。"),
    "kotwicz2024": ("UAM 通勤服务的机队规模与垂直起降场规模如何随需求与运营参数变化？",
        "双层滚动窗口机队调度（垂直起降场面积为次目标）+ 垂直起降场面积估算（下界）+ 参数敏感度分析。",
        "地理需求分布、日旅客量等参数情景。",
        "量化机队与垂直起降场对需求/运营参数的敏感度（具体结果待精读）。",
        "参数情景设定依赖假设。"),
    "li2020": ("面向 eVTOL 的城市空中运输交通管理现状、挑战与趋势如何？",
        "综述：有人机/无人机融合运行、交通规则革新与兼容、空地协同决策与自动驾驶、人与系统关系。",
        "国内外 UAM 交通管理研究综述。",
        "UAM 将面对有人/无人融合的复杂运行场景，需革新并兼容现有交通规则；未来将与无人机交通管理体系逐渐融合。",
        "综述类，2020 年视角。"),
    "quan2020": ("低空无人机交通管理是什么、为什么需要、如何构建？",
        "四方面概览：基本概念及现状、交通管理框架介绍、关键技术、相关科学问题。",
        "国内外低空无人机交通管理框架综述。",
        "现有民航空管难以适应百万级无人机规模，需开发新管理框架并攻克多项关键技术。",
        "综述类，2020 年早期框架。"),
}

# 作者别名
AUTHOR_ALIASES = {
    "Quan Q": ["全权", "Quan Quan"],
    "Taye A G": ["Abenezer Taye", "Abenezer G. Taye"],
    "Li Y": ["Yitang Li"],
    "Hui H": ["Hongxun Hui"],
}

# 期刊信息：名称 -> (出版社, 领域)
JOURNALS = {
    "Applied Energy": ("Elsevier", "能源技术、经济与政策应用"),
    "Energy Conversion and Management": ("Elsevier", "能源系统建模与优化"),
    "Renewable and Sustainable Energy Reviews": ("Elsevier", "可再生能源与可持续能源综述"),
    "Procedia CIRP": ("Elsevier", "制造工程（CIRP 会议论文集）"),
    "International Journal of Computer Integrated Manufacturing": ("Taylor & Francis", "计算机集成制造"),
    "EURO Journal on Transportation and Logistics": ("Springer", "交通与物流研究（EURO）"),
    "Energy and Buildings": ("Elsevier", "建筑能耗与能效"),
    "Proceedings of the IEEE Annual Simulation Symposium": ("IEEE", "仿真与建模方法"),
    "CIRED": ("IET（国际供电会议 CIRED）", "配电网与供电"),
    "Transportation Research Part C": ("Elsevier", "交通研究（方法、新兴技术）"),
    "Transportation Research Part E": ("Elsevier", "交通经济与物流运营"),
    "Transportation Research Part A": ("Elsevier", "交通政策与实践"),
    "eTransportation": ("Elsevier", "电动交通与能源"),
    "The Innovation Energy": ("Cell Press（The Innovation 系列）", "能源交叉创新"),
    "Transportation Research Record": ("SAGE（美国交通研究委员会 TRB）", "交通研究（TRB 会议论文）"),
    "Transport Policy": ("Elsevier", "交通政策"),
    "Electronics": ("MDPI", "电子科学与系统"),
    "Aerospace": ("MDPI", "航空航天工程"),
    "Technological Forecasting and Social Change": ("Elsevier", "技术预测与社会变革"),
    "Nature Communications": ("Springer Nature", "综合自然科学"),
    "AIAA AVIATION Forum and ASCEND": ("AIAA（美国航空航天学会）", "航空航天年会会议"),
    "Drones": ("MDPI", "无人机系统"),
    "交通运输工程学报": ("长安大学", "交通运输工程综合"),
    "航空学报": ("中国航空学会", "航空航天科学与技术"),
}

SRC_LABEL = {"s2": "摘要来源：Semantic Scholar（已核验）", "search": "摘要来源：公开检索（片段）", "none": "未获取到公开摘要"}

DEFAULT_EXCERPT = """> 用法：在 Zotero 打开 PDF 划高亮 → Annotation Links 复制链接 → 粘贴到下方，并写一句自己的话（为什么重要 / 可复用点 / 与哪篇矛盾）。
>
> 格式：`[高亮原文](zotero://open-pdf/library/items/<附件key>?page=<页码>&annotation=<标注key>)` — 你的理解
"""


def extract_kept(path, default_status):
    """从现有笔记提取需保留的手动内容：摘录区块正文、非默认的 status。"""
    kept = {"excerpt": None, "status": None}
    if not os.path.exists(path):
        return kept
    try:
        txt = open(path, encoding="utf-8").read()
    except Exception:
        return kept
    m = re.search(r"^status:\s*(.+)$", txt, re.M)
    if m:
        s = m.group(1).strip()
        if s and s != default_status:
            kept["status"] = s
    m = re.search(r"^## 摘录\s*\n(.*?)(?=^## |\Z)", txt, re.S | re.M)
    if m:
        body = m.group(1).strip()
        # 若仅剩默认提示，视为空
        if body and body != DEFAULT_EXCERPT.strip():
            kept["excerpt"] = body
    return kept


def build_paper_notes():
    os.makedirs(PAPER_DIR, exist_ok=True)
    for pid, fname, title, short, year, authors, journal, doi, vol, src, abstract, use in PAPERS:
        # 从 Semantic Scholar 缓存补全 s2 摘要
        if abstract is None and S2.get(doi):
            abstract = S2[doi].get("abstract") or abstract
        kp = KEYPOINTS.get(pid)

        default_status = STATUS.get(pid, "未读")
        path = os.path.join(PAPER_DIR, fname + ".md")
        kept = extract_kept(path, default_status)
        status = kept["status"] or default_status
        excerpt = kept["excerpt"] or DEFAULT_EXCERPT.strip()

        zt = ZOTERO.get(pid)
        lines = ["---", "type: paper", "fileClass: paper", f"year: {year}", f"journal: {journal}",
                 f"doi: {doi}", f"status: {status}", f"abstractStatus: {ABSTRACT_STATUS[src]}"]
        if zt:
            lines += [f"citationKey: {zt['citekey']}", f"zoteroKey: {zt['key']}"]
        lines += ["---",
                  f"# {title}", "",
                  "**作者**：" + (", ".join(f"[[{a}]]" for a in authors) if authors else "（待补全）") + "  ",
                  f"**期刊**：[[{journal}]], {vol}  ",
                  f"**DOI**：[{doi}](https://doi.org/{doi})  ",
                  f"**阅读状态**：{status}（修改 frontmatter 的 `status` 字段，看板自动更新）",
                  "", "## 摘要", f"> {SRC_LABEL[src]}", ">", "> " + (abstract or "（暂未获取到公开摘要，待精读原文补全。）"),
                  "", "## 中文要点"]
        if kp:
            labels = ["研究问题", "方法", "数据/案例", "主要结论", "局限/空白"]
            for lab, val in zip(labels, kp):
                lines.append(f"- **{lab}**：{val}")
        lines += ["", "## 用途", use, "", "## 摘录", excerpt, "", "> 此区块内容在重跑脚本时会保留，可放心粘贴高亮与批注。"]
        if zt:
            lines += ["", "## Zotero 关联",
                      f"- **Zotero 条目**：[打开 Zotero 条目](zotero://select/library/items/{zt['key']})（点击跳转）",
                      f"- **引用键**：`@{zt['citekey']}`",
                      f"- **导入备份**：`_tools/zotero/Taye2024.bib`（该文件仅示例论文有）"]
        lines.append("")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    return len(PAPERS)


def build_author_notes():
    author_papers = {}
    for pid, fname, title, short, year, authors, journal, doi, vol, src, abstract, use in PAPERS:
        for a in authors:
            author_papers.setdefault(a, []).append((fname, short, year))
    for a in sorted(author_papers):
        papers = sorted(author_papers[a], key=lambda x: x[2])
        aliases = AUTHOR_ALIASES.get(a, [])
        lines = ["---", "type: author"]
        if aliases:
            lines.append("aliases:")
            for al in aliases:
                lines.append(f"  - {al}")
        lines += ["---", f"# {a}", "", "> 待补充：全名、机构、研究方向、主页", "", "## 论文"]
        for fname, short, year in papers:
            lines.append(f"- [[{fname}|{short} ({year})]]")
        lines.append("")
        with open(os.path.join(AUTH_DIR, f"{a}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    return len(author_papers)


def build_journal_notes():
    journal_papers = {}
    for pid, fname, title, short, year, authors, journal, doi, vol, src, abstract, use in PAPERS:
        journal_papers.setdefault(journal, []).append((fname, short, year))
    for j in sorted(journal_papers):
        papers = sorted(journal_papers[j], key=lambda x: x[2])
        pub, field = JOURNALS[j]
        lines = ["---", "type: journal", "---", f"# {j}", "",
                 f"- 出版社：{pub}", f"- 领域：{field}", "", "## 论文"]
        for fname, short, year in papers:
            lines.append(f"- [[{fname}|{short} ({year})]]")
        lines.append("")
        with open(os.path.join(JOUR_DIR, f"{j}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    return len(journal_papers)


if __name__ == "__main__":
    os.makedirs(AUTH_DIR, exist_ok=True)
    os.makedirs(JOUR_DIR, exist_ok=True)
    os.makedirs(PAPER_DIR, exist_ok=True)
    n_p = build_paper_notes()
    n_a = build_author_notes()
    n_j = build_journal_notes()
    print(f"生成论文笔记: {n_p} 个")
    print(f"生成作者笔记: {n_a} 个")
    print(f"生成期刊笔记: {n_j} 个")
