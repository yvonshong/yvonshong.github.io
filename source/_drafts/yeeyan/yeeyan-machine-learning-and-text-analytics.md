---
title: yeeyan:Machine Learning and Text Analytics
date: 2015-02-05 22:50:22
toc: false
---

本文为[微软亚洲研究院“机器学习”系列文章译文](http://www.msra.cn/zh-cn/research/machine-learning-group/default.aspx)

[yvonshong译言主页](http://user.yeeyan.com/articles/yvonshong/translation)

译者因此受邀参加2015年微软学生夏令营(西安)

<!-- more -->

# 【机器学习】机器学习和文本分析

本文由微软研究院杰出科学家[Ashok Chandra博士](http://social.technet.microsoft.com/profile/ashok%20chandra/?WT.mc_id=Blog_MachLearn_General_DI)和微软研究院项目经理[Dhyanesh Narayanan](http://social.technet.microsoft.com/profile/Dhyanesh_Narayanan?WT.mc_id=Blog_MachLearn_General_DI)联合撰写。

1970年代时，我（Ashok）正是斯坦福人工智能实验室的一名学生，四处都洋溢着对达到人脑级别的人工智能的乐观的气氛，如今这样的气氛仍一直延续着，而与此同时，采用机器学习（ML）技术，计算机逐渐变得便携。如此种种，使致微软出品的各色新产品都一定程度上使用了机器学习技术，强化对语音、数据或文本等的分析，在这篇文章中我们着力于文本分析。

随着计算机日渐了解自然语言，新的前沿科技正在遍地开花，如改善应用的用户交互界面；优化搜索引擎；如微软小娜(Cortana)和Siri一样的个人虚拟助手；以及对给定文件涵盖内容探测的工具。例如，一个新的网页若被设计得用算法将提及到的人物链接至如维基百科等合适的数据库，这将改善用户的浏览体验，使得读者能够轻易的获取人物的相关信息。此外，通过来自文本的额外信息，还可以像图1一样定义文中提及的对应实体（如运动员，球队）。

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/6443.Text%20Analytics%20Scenario.jpg)

> *图1:促发文本分析的可能情景*

文本分析是当下科学研究的热门领域，并将持续活跃下去。但是创造一种具备人类所有知识（以文字作描述）的语义学模型并不是件轻松的任务。早期的工作可追溯到上个世纪90年代时，包括Brill的标记器[1]，其能对语句进行断句并给后续工作以提示。微软研究院一直致力于这片研究领域中的创新，但我们得将新科技与实用因素适配，创造能量产的工艺，以走得更远。

在这篇博文中，我们仅是对当下机器学习技术如何应用于文本分析的管窥蠡测，在此我们会引用命名识别技术(NER)。作为一个提供机器学习功能的平台，[微软Asure机器学习](http://azure.microsoft.com/en-us/trial/get-started-machine-learning/?WT.mc_id=Blog_MachLearn_General_DI)也涵盖了文本分析等通用功能，并对NER功能的支持进行了优化，以便我们能从通用概念转化到具体设计决策。

NER的任务是明确文本中提及的人物，地点，组织，运动员球队等等，让我们通过图2浏览一下如何通过"监督学习"方法解决上述问题。

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/NER%20workflows.jpg)

> *图2:命名识别技术工作流*

在**设计阶段**或者说"学习阶段"，系统通过训练数据来创造要进行机器学习的使用模型。其主旨是系统对片段样本进行泛化以处理新增的任意文本。

这些训练数据由人工标记的学习目标实体组成，这样看起来就像：“ 当&lt;运动员&gt;Chris bosh &lt; /运动员&gt; 上场，&lt;球队&gt;迈阿密热火 &lt; /球队&gt;便使人狂热起来。”实验的预期结果是从这自然语言样本中习得的模型，能够训练到识别新输入语句中的运动员实体和球队实体。

设计阶段工作流的效率往往由特征提取模块决定，越是煞费苦心的工程特征将产生更为有力的模型。例如，一段文本中的一个单词对上下文产生关联[比如，前一个k开头的字母便与下一个k开头的字母产生关联]是一个强有力的文字关联实体特征。举个例子，“在昨日激烈的比赛中，旧金山击败了红雀队。”这句话中，文本中提及的“旧金山”很明显的指代一个运动球队（即旧金山巨人队）而非旧金山这个城市。在本文中大写字母通常也是十分利于辨别以人或地点命名的实体的特征。

模型的训练_正是机器学习的要义，即产生一个优秀的模型。这通常对选择的特征进行复杂的组合。当下有几种可得的机器学习技术，包括[感知器](http://en.wikipedia.org/wiki/Perceptron?WT.mc_id=Blog_MachLearn_General_DI)，[条件随机域](http://en.wikipedia.org/wiki/Conditional_random_field?WT.mc_id=Blog_MachLearn_General_DI)等等。这些技术的选择取决于这些模型在有限训练数据下所能达到的精度，处理的速度和同时学到不同实体的数目。例如，Azure机器学习命名识别模型默认支持三种实体，即人物，地点和组织。

**运行阶段**工作流是将输入的未标记文本根据对应设计阶段产生的模型，生产标记实体的文本。正如我们所见，运行阶段工作流复用了设计阶段工作流的特征提取模块。相应的，如果对于应用来说实体识别的高吞吐量是必须的，那么渠道中也得准备相应的轻量高质的特征。举个例子，Azure机器学习命名识别技术模块，利用基于相应上下文中易于计算的模块来实现高效率。对于过程中的歧义，可使用如[维特比译码法](http://en.wikipedia.org/wiki/Viterbi_decoder?WT.mc_id=Blog_MachLearn_General_DI)将实体标记分配到输入词序列中。

你会意识到NER的实现才刚起步是十分重要的，但这仍是从原始文本中不过知识的重要的第一步。近期的[博文](http://blogs.technet.com/b/inside_microsoft_research/archive/2014/07/10/sports-fans-enjoy-power-of-leibniz-entity-recognition.aspx?WT.mc_id=Blog_MachLearn_General_DI)将会描述NER配合一系列相关技术来实现必应运动这款应用中的大幅提升。可在Azure机器学习中使用的[相关NER代码](http://azure.microsoft.com/en-us/trial/get-started-machine-learning/?WT.mc_id=Blog_MachLearn_General_DI)也可获得。除了NER，常用的自然语言语法解析，连接和特征，情绪分析，实体提取等等，意味着对以内容为核心的应用来说，其另辟蹊径以改善用户体验，这些技术使得你文本的内容跃然纸上。

我们愿你享受阅读本篇博文，期待你的评论。

Ashok Chandra.&nbsp;
[在这里](http://research.microsoft.com/en-us/people/achandra?WT.mc_id=Blog_MachLearn_General_DI)&nbsp;关注我的研究。

Dhyanesh Narayanan.&nbsp;
[在这里](http://research.microsoft.com/en-us/people/dhyann?WT.mc_id=Blog_MachLearn_General_DI).关注我的研究。

**参考文献**

[1] Eric Brill, 1992,_ A
simple rule-based part of speech tagger_, Applied natural language processing
(ANLC '92)

[2] Li Deng, Dong Yu,
2014, [Deep Learning: Methods and Applications](http://research.microsoft.com/pubs/209355/DeepLearning-NowPublishing-Vol7-SIG-039.pdf)
