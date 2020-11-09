---
title: yeeyan:Machine Learning for Industry - A Case Study
date: 2015-02-23 15:49:12
toc: true
---

本文为[微软亚洲研究院“机器学习”系列文章译文](http://www.msra.cn/zh-cn/research/machine-learning-group/default.aspx)

[yvonshong译言主页](http://user.yeeyan.com/articles/yvonshong/translation)

译者因此受邀参加2015年微软学生夏令营(西安)

<!-- more -->

*本文作者微软雷德蒙德研究院首席研究经理[Chris Burges](http://social.technet.microsoft.com/Profile/Chris%20Burges?WT.mc_id=Blog_MachLearn_General_DI)*

大家好，我是Chris Burges。回顾我在微软工作的14年，和先前在贝尔实验室的14年，我花费了大量时间涉猎机器学习（ML），也关注如何解决工业能力问题。自从机器学习（尤其是面向工业的机器学习）彰显其魅力以来，它也逐渐普及。这正为全局思考机器学习的实现提供了契机，得从实用角度兼算法角度优化机器学习。

在2004年，微软研究院（MSR）和微软网页搜索组决定一探究竟，我们能否合力改善网页搜索结果的相关性。当时使用的系统叫做The Flying Dutchman(飞翔的荷兰人)。几个月后我们设计出的系统不仅改善了结果的相关性，相比于Flying Dutchman花费好几天，产生一系列网页搜索结果排序模型的聚合体，名为[RankNet](http://research.microsoft.com/en-us/um/people/cburges/papers/ICML_ranking.pdf?WT.mc_id=Blog_MachLearn_General_DI)的简易神经网络排序器仅需在一台机器上跑一个小时，产生的排序模型便表现得十分出色。

在未来几年内，一个关于科学，研究，算法设计和产品设计交织的迷人故事一览无遗，在这第一篇博文中，我想让你身临其境般感受它们之间的相互影响，在下一篇博文中，假设大家对机器学习是零基础的，我将向大家解释现行基本算法是如何运作的。我们已经接触到了开发过程中的一个重要环节：高速实验的能力。如果你有好主意，并且你想得到实验证明，无论如何，请立即行动。所以即使初始模型执行得并没有现行模型那样良好，或是在训练和测试过程中运作得足够快，机器学习也能使得进展更快，这终将在精度和速度方面迅速超过现行模型。

现在，有种叫做[提升决策树](http://en.wikipedia.org/wiki/Gradient_boosted_decision_tree#Gradient_tree_boosting?WT.mc_id=Blog_MachLearn_General_DI)(BDTs)的系列模型正日益流行，BDTs能灵活处理多种预测性任务，比如：

- 排序。如在列表顶端放置最相关的网页搜索结果。

- 分类。如判定某一邮件是否为垃圾邮件。

- 回归。如预测你的房子能卖个什么价钱。


BDTs是如此的灵活多变，又十分有用，不是嘛？微软展示的过去几年间机器学习服务的内部日志显示，有超过670,000的训练流量使用着微软开发的BDTs。因特定的实验者往往只会运行精选后的模型（即训练众多模型，每个配置不同参数设置，并用某一特定数据集筛选出最优模型），这个数据是被夸大了的，但至少也描绘出了概貌。这是否意味着当前火热的BDTs是微软的发展趋势么？或者其他地方的人们也喜欢它？早在2010年，雅虎组织了一场[排序算法学习挑战赛](http://jmlr.org/proceedings/papers/v14/chapelle11a/chapelle11a.pdf?WT.mc_id=Blog_MachLearn_General_DI)，以揭示谁拥有最强网页搜索排序算法。超过1000支队伍注册了此次挑战赛。令人欣慰的是[微软小组赢得了这场比赛](http://research.microsoft.com/en-us/um/people/cburges/papers/YahooChallenge.pdf?WT.mc_id=Blog_MachLearn_General_DI)，排序结果十分仿真。对我而言意料之外的是，前五名的系统都使用了全套决策树，并进行了优化（实际上我们的系统是基于全套BDTs和神经网络）。所以如果你正打算训练固定模型来完成预测性任务，可将BDTs纳入考虑范围。</span>

让我们以网页搜索排序作为范例研讨一个经典的搜索/产品周期。搜索中最难的是提出正确的问题，然后合理验证想法（除了历史悠久的出版物之外，某些验证测试也是充满了干扰因素）。从这些挑战中得到的帮助也将致力于对万千人类至关重要的问题的研究，

当你在[必应](http://www.bing.com/?WT.mc_id=Blog_MachLearn_General_DI)上发出查询请求，我们将高效扫描索引中的所有文件。通过使用一些高速筛选器，可剔除大量候选文件（比如我们不会考虑并无查询词的文件）。削减部分候选文件集达到可控容量。针对每个候选文件我们生成几千个显明此文件与你查询关联程度的特征。比如有个特征可能是“文件标题是否包含了你的查询词？”或者更高级别的“文件是否涉及了查询中提到的实体？”。排序模型的任务是将一系列特征和图示量化成一项文件与查询关联度的编码数值。加之最初的筛选步骤，我们得以按其与查询的关联度，对网页上所有内容进行排序。我们过去常用一项名为[NDCG](http://en.wikipedia.org/wiki/Normalized_discounted_cumulative_gain#Normalized_DCG)的度量来量化搜索结果的质量（现在我们用几种指标测量用户的满意程度）。整个排序结果列表决定了NDCG在0到1之间的值，1表示对特定标记数据集（即D）满足可达最佳排序。

而RankNet对BDTs有何贡献呢？RankNet虽然是现阶段的重大突破，但并未达到终极目的，尤其是它忽视了NDCG度量值，仅试图修正文件关联顺序。RankNet会针对给定的查询，从数据集中寻找已标记最优匹配文件，和稍次的匹配文件，当然也会尽力次中择优（要补充的是，这些并不是我们实际使用的标记！）。创造一个NDCG优化模型的瓶颈在于NDCG精确度上运转不良；若你想让（排序模型所指定的）每个文件都有度量值，使排序结果仅需基于度量值，NDCG会将离散的度量值转换为连续的度量值。为解决这个问题，在训练神经网络时仅需提供函数梯度（量化神经网络输出评分的函数会如何变化）而非优化的真实函数值。排序任务中，你可以视这些数值为小箭头或者力，驱动着每个文件在排序列表中浮沉。我们可将这些文件对之间的力，模型化为NDCG中（对数据集内）两文件的交换，然后在给定查询中累加所有文件的力，视所得为函数梯度来训练神经网络。这便诞生了[Lambda排序法](http://research.microsoft.com/en-us/um/people/cburges/papers/YahooChallenge.pdf?WT.mc_id=Blog_MachLearn_General_DI)，虽派生于神经网络模型，但在关联性性能方面和RankNer比更是青出于蓝。稍后我们将这个想法贯彻到提升决策树模型中名为[LambdaMART](http://research.microsoft.com/en-us/um/people/cburges/papers/lambdaMART.pdf?WT.mc_id=Blog_MachLearn_General_DI)的算法中，而BDTs凌越于神经网络对此产生的影响有以下两点：

- 更自然地处理差异巨大的不同特征的能力。</span>

- 训练更快速，并实验结果返回更迅速。</span>

随后由[Ofer Dekel](http://research.microsoft.com/en-us/um/people/oferd/?WT.mc_id=Blog_MachLearn_General_DI)带领的小组展示了如何构建BDTs，它能以比神经网络快约两个数量级的速度训练数据，也能处理更大的数据集。

简而言之，这便是我们对BDTs一见倾心的原因。整个流程就是，工程周期和产品需求驱动着研究，研究为产品创造新的契机。对于其中三分之二的步骤（RankNet和BDTs），其主要为实验的高速和大容量数据做出了贡献。值得一提的是，与其走进小而精的排序算法，虽然我们正聚焦于它的历史，不如了解必应中所运用到工程和特性。在下篇博文中，我将带你一览BDTs是如何工作的。

Chris Burges

[了解更多](http://research.microsoft.com/en-us/people/cburges/?WT.mc_id=Blog_MachLearn_General_DI)

