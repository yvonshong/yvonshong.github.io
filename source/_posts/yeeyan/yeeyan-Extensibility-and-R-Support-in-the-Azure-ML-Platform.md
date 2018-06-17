---
title: yeeyan:Extensibility and R Support in the Azure ML Platform
date: 2015-03-03 14:04:58
categories: code
tags: ML
toc: true
---

本文为[微软亚洲研究院“机器学习”系列文章译文](http://www.msra.cn/zh-cn/research/machine-learning-group/default.aspx)

[yvonshong译言主页](http://user.yeeyan.com/articles/yvonshong/translation)

译者因此受邀参加2015年微软学生夏令营(西安)

<!-- more -->

*本文作者微软信息管理和机器学习团队合作工程经理[Debi Mishra](http://social.technet.microsoft.com/Profile/Debi%20Mishra%20-%20ML?WT.mc_id=Blog_MachLearn_General_DI)。*

近年来开源社区使用R语言和Python开发工具和程序包对机器学习(ML)的驯化突飞猛进，尤其是在机器学习从业者得到广泛应用。许多基于以上语言开发的强有力的机器学习库，使更多的人采纳这些语言进行开发，形成良性循环。R语言的普及与[CRAN](http://cran.r-project.org/?WT.mc_id=Blog_MachLearn_General_DI)有很大关系，而Python的流行得益于[SciPy](http://scipy.org/index.html?WT.mc_id=Blog_MachLearn_General_DI)堆。但是，通常以上语言和相关工具和程序包像一个个孤立的岛屿，常无法实现互用性协作，而协作的瓶颈不仅仅在编程语言或脚本层面。这些环境中有面向“数据集”的特定对象，“柱式模式”的特定解释和其他关键数据的科学建构。要实现“云环境下的智能”，机器学习平台得允许开发人员和数据科学家混合搭配不同的编程语言和程序框架，形成自己的解决方案。数据科学解决方案通常包括许多阶计算，数据流和机器学习算法，数据流包括数据摄取，转换和优化。不同的编程语言，开发工具和程序包在满足特定阶段需求的条件下，可能会适用于不同的步骤。

[Azure机器学习服务](http://azure.microsoft.com/en-us/services/machine-learning/?WT.mc_id=Blog_MachLearn_General_DI)是可扩展，基于云端的多用户服务，可编辑和执行数据科学工作流，并将工作流产品化。Azure机器学习的独门秘籍在于Azure机器学习工作室的工具集赋予了人们利用数据和计算，进行功能复合和执行任意工作流的能力。这样的工作流可作为Azure的表述性状态传递(REST)终端进行运转。这使开发者和数据科学家能仅用“拖拽连接”模式编辑数据和计算工作流，仅用轻轻点击便能测试工作流和作为网络服务产品启动。

Azure机器学习服务未来愿景中的关键部分是强调机器学习平台的可扩展性和对诸如R语言，Python和其他类似环境下开源软件的支持。如此现有机器学习从业者所积累的技巧，代码和脚本都能直接引入Azure机器学习平台并毫无阻力地对Azure机器学习的内容进行操作。在创建Azure机器学习平台根基时就牢记这一原则。

我们首先支持的是R语言编程环境，尤其在以下方面：
- 数据科学家能导入R语言编写的一切，与Azure机器学习工作流无缝衔接。
- Azure机器学工作室能几分钟内将R语言脚本变成可扩展和低延迟的网络服务。
- 数据科学家能使用预装的超400种热门CRAN程序包，另外他们还可使用英特尔数学核心函数库的优化线性代数核心函数。
- 数据科学家可用如ggplot2的R语言绘图库，将数据可视化。
- 通过高保真双向数据框架和模式桥，该平台和运行环境能自动识别和提供扩展，以达到协作互用性。
- 开发者能访问R语言公共机器学习算法并和Azure机器学习平台提供的其他算法组合。

下图展示了如何在Azure机器学习中使用“执行R模块”，将“乳腺癌数据”数据集可视化。

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/6237.R-image%201.JPG)

我们欣喜地看见R语言在我们第一批用户中是如此的受欢迎。有趣的是，用户最常见的错误是在他们自己的脚本中的语法错误。使用数据表明，R语言应用于Azure机器学习模型化实验近四分之一的实现。R语言预测程序包正被微软的重要客户和我们的内部团队使用。

你也可[立即开启Azure机器学习的R语言编程之旅](http://azure.microsoft.com/en-us/pricing/free-trial/?WT.mc_id=Blog_MachLearn_General_DI)。与此同时，我们的工程师团队正致力于扩展Azure机器学习对Python的类似支持——想了解更多，请继续关注此博客。

Debi

关注我的[Twitter](https://twitter.com/debipmishra?WT.mc_id=Blog_MachLearn_General_DI)