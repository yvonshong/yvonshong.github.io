---
title: yeeyan:Azure ML is Helping CMU Become More Energy Efficient
date: 2015-03-02 18:16:21
toc: false
---

本文为[微软亚洲研究院“机器学习”系列文章译文](http://www.msra.cn/zh-cn/research/machine-learning-group/default.aspx)

[yvonshong译言主页](http://user.yeeyan.com/articles/yvonshong/translation)

译者因此受邀参加2015年微软学生夏令营(西安)

<!-- more -->

*本文由微软信息管理与机器学习中心(IMML)商业战略主管[Vinod Anantharaman](https://social.technet.microsoft.com/Profile/Vinod_Anantharaman)撰写。*

建筑都是由如供热，制冷，照明，通风，安保等多重复合系统共同维持运转，任何一个系统都能影响居住者的舒适度和能源消耗量。传统上每个系统都有它独立的传感器，驱动器或相关元件，这些聚合起来仅为某一特定系统进行数据分析。<span style="line-height: 1.45em; background-color: initial;">正是因为这些建筑物管理的窖式方法，通常缺失对建筑物运作效率整体上的把握，或者全局观。这给精确预测能源使用或浪费带来了挑战。</span>

位于宾夕法尼亚州匹兹堡的卡内基梅隆大学(Carnegie Mellon University, CMU)正引领着超12,000名学生和5,000名职工教员的一项研究，它也是这项研究自1900创建之后催化改革的温床。CMU的[建筑性能和诊断研究中心](http://www.cmu.edu/architecture/research/cbpd/absic-cbpd.html?WT.mc_id=Blog_MachLearn_General_DI)负责研发软硬件，以改善校区建筑在达到高居住舒适度情况下的性能。

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/CMU%20-%201.jpg)

> *卡内基梅隆大学建筑性能和诊断研究中心，版权所有。©Carnegie Mellon University*

建筑性能和诊断研究中心有幸创建了一个综合兼自动化的系统，它能提高建筑能源性能，计算节省的开支，监测故障和实时采取措施。这样的系统也将满足供热和降温需求，并且相应的调整。它会在全局瘫痪之前警告建筑管理员进行修复或替换失效部件。

在这预测分析聚合系统中，CMU有两项基本要求：

1. 易于实施

2. 对非技术人员也易于使用

**解决方案**

在与[OSIsoft](http://www.osisoft.com/Default.aspx?WT.mc_id=Blog_MachLearn_General_DI)的合作关系中，研发中心曾开发了一款利用预测分析的能力管理所有新旧传感器的综合系统。[Azure机器学习](http://azure.microsoft.com/en-us/services/machine-learning/)是CMU解决方案的中坚力量，从本地部署的PI服务器收集整个校区传感器的数据开始，通过基于[微软Azure平台](https://azure.microsoft.com/en-us/)的PI云服务，传输到Azure中运行的一台PI服务器中，然后服务器内利用OSIsoft研究工具进行过滤，统计和定型，然后实时传输到一个Azure储存库中，以便Azure机器学习能访问进行预测分析。所得预测数据存储在PI服务器中可被Power BI访问以备建筑物管理系统调用。

解决方案是如此的简单迅速，易于启动和持续使用。研究中心的研发员Bertrand Lasternas说“我们无需准备客户端软件便能利用Azure机器学习展开工作，云上的一切早已准备就绪。它比我们历来尝试过的工具都更易上手”。

以下是使用了CMU解决方案的一些示范用例：

- 某一建筑的温度需要从早上9点开始工作时需提升至72华氏度，供热系统常常6点就得开始运转，或者天气热点时得从6:30开始，这样很浪费能源。CMU想利用预测分析来确定对建筑物开始供热的具体时间。研究员致力于利用含建筑物近期内外部温度，预期太阳辐射水平和其他因素的模型，来预测9点时建筑物内部温度。因预期太阳辐射水平数据不可得，研究员首先得预测这个变量。他们利用Azure机器学习中的提升决策树算法训练了一项太阳辐射模型，并测试这项模型以验证精确度后，将其运用在内部温度模型上以解决对建筑物开始供热的问题，以节省能源。

- CMU想要解决隐藏在可视检测后的部件故障检测和诊断的难题，因为他们常在墙体之后或者地板之下。通过使用Azure机器学习处理PI系统收集的历史数据，他们预测能节省潜在开支的故障。

Azure机器学习解决方案通过允许研究人员项目组或研究生能互相分享工作空间，以促进之间的合作。

**益处**

据实验结果所得，CMU研究员估计他们的解决方案能节省达20%的能源开支。关于它在校区内实施的事项正在讨论中，一年下来它能在哪节省成百上千的资金。Lasternas说：“节省的能源主要来自于能源使用量的削减和调低每时所需和所流失的能源”。CMU研究员预想PI系统和微软Azure云不仅面向研究员，也面向与建筑物进行交互影响的工程师和技术员。比如现场服务技术员能在远程设备故障之前用手中的平板电脑访问预测分析所得洞察，来检查和升级这些设备。手机通知也可以警醒工程师能量需求高峰的到来。因为这些解决方案具有可扩展性并价廉物美，同样适用于不能由传统解决方案驱动的群体建筑和公共设施系统。

各行各业的客户正利用微软Azure机器学习部署企业级预测分析解决方案——你也可以[现在开始](http://azure.microsoft.com/en-us/trial/get-started-machine-learning/?WT.mc_id=Blog_MachLearn_General_DI)。

在卡内基梅隆大学，他们为创建的解决方案预估其广阔的舞台。“我们见证Azure机器学习和PI系统引领着面向大众的自助式预测分析时代，未来无限可能。”Lasternas如是说。