---
title: yeeyan:Recommendations Everywhere
date: 2015-02-23 15:13:29
toc: true
---


本文为[微软亚洲研究院“机器学习”系列文章译文](http://www.msra.cn/zh-cn/research/machine-learning-group/default.aspx)

[yvonshong译言主页](http://user.yeeyan.com/articles/yvonshong/translation)

译者因此受邀参加2015年微软学生夏令营(西安)

<!-- more -->

*本文中作者是微软首席研究员[Thore Graepel](http://social.technet.microsoft.com/Profile/Thore%20Graepel?WT.mc_id=Blog_MachLearn_General_DI)*

优秀的推荐需求渐广，无论你是在寻找一部可能会喜欢的电影或者是书籍，甚至寻找Facebook或者LinkedkIn上与你志同道合的推荐人物，而自动推荐系统便是一种解决方案。

然而这样的系统已优先应用于互联网巨头中，我们将随待发布的[微软Azure机器学习](http://azure.microsoft.com/en-us/campaigns/machine-learning/?WT.mc_id=Blog_MachLearn_General_DI)推出一款受众更广，增加顾客收益，面向个人和企业的推荐系统。

**推荐系统是如何运作的？**

在一个推荐系统（RS）中，通常由两种实体构成，我们称之为用户和项目，用户便是你要进行推荐的对象，项目就是想推荐给他们的东西，诸如电影，书籍，网页，菜谱甚至其他人物。

假如我们要进行推荐，比如向某一特定用户推荐身边某一基于五星制的餐馆，其星级是由其它用户打出的。我们将这项推荐任务分为两步：

1. 预测每家餐馆用户将给出的评分，可使用五星制的评分。


2. 从一系列合适的餐馆中，预测这名用户将会给出最高评分的餐馆。

但我们是如何预测用户对他实际上并未评价过的餐馆的得分呢？这便是机器学习（ML）的用武之地。

**如何预测评分？**

为了建立一个在特定用户/项目的组合中，预测用户评分的机器学习模型，我们需要收集信息表格，涵盖用户账户，项目账户和评分，你可以视之为一个大型矩阵，用户为行，项目为列，评分即是元素。

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/UsersItems.jpg)

这将是一个存在许多缺失元素的稀疏矩阵，因为用户往往仅评价一小部分项目。Azure机器学习中实现的贝叶斯推荐系统采取这些训练数据，优化模型，最终得到一个能对特定用户/项目对进行预测评分的函数，这些评分并不局限于五星制。其他指标诸如购买量，点击量或者浏览时长，在没有更多信息来提供好的推荐时，也将被等效处理。

所以这样会奏效么？推荐系统学着将用户和项目嵌入到我们所谓的潜在特质空间中（见下图），一个用户（蓝点）给了一个项目（红点）好评，则其向量与项目的向量同向；若是差评，则与项目的向量反向。相似的用户和相似的项目将会在特质空间近距离放置，这使得推测训练数据中未评价的用户和项目的组合成为可能。下图所示为一个仅供阐释的二维特质空间，其实在我们部署的系统中使用了20到100维的空间。甚至有时我们在特质空间内找到可解释的坐标轴（即“特征”），比如下图，南-北特征便是“成人”和“儿童”，东-西特征便是“主流”和“小众”。

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/Trait%20Space.jpg)

**如何应对新用户或者新项目？**

推荐系统的一个关键问题便是冷启动。新用户群还未做出足够的评价行为，而新的项目还未受到足够人数的评价而无法做出好的预测。为了缓和这个矛盾，Azure机器学习推荐系统不仅显示用户和项目的账户，而且从元数据中构建特征向量。对于用户，可包含诸如年龄，地理位置等大概信息，对于项目，如电影，可包含如类型，演员，导演，拍摄年代等信息。这使得系统能利用元数据中的公共属性对用户和项目进行泛化。

**了解更多**

如果你对推荐系统的数学基础感兴趣，请查阅这篇论文：[Matchbox: Large Scale Bayesian Recommendations.](http://article.yeeyan.com/edit/))

如果你急于创建属于你自己的推荐系统渠道，一旦Azure机器学习开放使用（很快了），你便可尝试着从它开始。如下图所示，Azure机器学习工作室开辟了一个推荐系统模块，和基于浏览器且仅用拖拽操作，十分强大的图形用户界面，这使得你的任务能相对轻松一点。

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/Azure%20ML%20Studio.jpg)


事实上，Azure机器学习推荐系统包含两个强有力的预测评分范例：基于内容过滤和[协同过滤](http://article.yeeyan.com/edit/))，我们希望它能有更广泛的自动推荐系统用途，能应用到使顾客全方位受益的场景中，而致力于它的大范围推广。

Thore
Graepel

了解我更深入的[研究](http://research.microsoft.com/en-us/people/thoreg/?WT.mc_id=Blog_MachLearn_General_DI). 请关注我的[Twitter](https://twitter.com/ThoreG?WT.mc_id=Blog_MachLearn_General_DI).

