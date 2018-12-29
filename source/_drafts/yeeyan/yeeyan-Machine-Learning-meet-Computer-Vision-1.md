---
title: yeeyan:Machine Learning, meet Computer Vision - Part 1
date: 2015-02-07 00:33:01
categories: code
tags: ML
toc: true
---

本文为[微软亚洲研究院“机器学习”系列文章译文](http://www.msra.cn/zh-cn/research/machine-learning-group/default.aspx)

[yvonshong译言主页](http://user.yeeyan.com/articles/yvonshong/translation)

译者因此受邀参加2015年微软学生夏令营(西安)

<!-- more -->




*本系列文章分为上下两篇，由微软剑桥研究院的[Jamie Shotton](http://social.technet.microsoft.com/Profile/Jamie%20Shotton?WT.mc_id=Blog_MachLearn_General_DI), [Antonio Criminisi](http://social.technet.microsoft.com/Profile/Antonio%20Criminisi%20-%20MSR?WT.mc_id=Blog_MachLearn_General_DI)和[Sebastian Nowozin](http://social.technet.microsoft.com/Profile/Sebastian%20Nowozin?WT.mc_id=Blog_MachLearn_General_DI)联合撰写。其下篇将稍后发布。*

计算机视觉是一门涉及图像自动识别算法领域的研究，起源于20世纪60年代的人工智能和认知神经科学。“解决“机器视觉问题是1996年麻省理工学院的一项著名暑期项目，但人们迅速认识到这点时间显得十分仓促。之后的50年间通用图像识别技术仍显得高深莫测，但这片领域却在蓬勃发展。在视觉算法取得突破之后终于迎来了它广阔的天地，包括[交互式图像划分](http://research.microsoft.com/pubs/67890/siggraph04-grabcut.pdf?WT.mc_id=Blog_MachLearn_General_DI)（在[微软Office办公套件](http://office.microsoft.com/?WT.mc_id=Blog_MachLearn_General_DI)中可实现“[移除背景](http://blogs.technet.com/b/office2010/archive/2009/10/19/the-magic-of-background-removal.aspx?WT.mc_id=Blog_MachLearn_General_DI)”功能，搜索图片，人脸识别与校准和Kinect中人体运动捕获等功能，这些在商业上日益受欢迎。这便是过去15至20年间从机器学习（ML）中快速汲取所获得的主要进展。

本系列的第一篇文章将探索计算机视觉所面临的挑战和利用决策森林这种机器学习技术处理逐像素分类的初体验。

**图像分类**

试着来回答这个图像分类问题：“图片中是否有着一辆车？”对于计算机来说，一张图片仅意味红绿蓝三原色像素网格，每个颜色渠道由0到255的像素值描述。这些数值不仅随实体是否存在而快速改变，还受相机视角，光线条件，背景和对象姿态影响。此外还得处理花样繁多的汽车类型，例如旅行车，卡车或者跑车，每款都会产生不同的像素网格。

幸运的是监督式机器学习提供了取代手动编码穷举的方案，即采集图片训练数据集并为每张图手动贴上合适的标签，利用我们最爱的机器学习算法提取出与我们识别任务相关的像素模型和干扰因素。我们尝试着领悟干扰因素的不变形，以将模型推广应用到新的、过去无法识别的对象中。我们已在视觉学习新算法的开发以及数据的采集和标记中取得了长足的进步。

**逐像素分类的决策森林**

图像包含着许多层次上的细节，正如先前所言，我们提出图片中是否有着某一特定对象的问题。但我们却解决了“语义图像划分”这一难题：描述场景中的所有对象。下面便是一个街道场景划分的样例：

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/MLB%20post%2011%20-%20Image%201.JPG)

如图你可以想象这些技术如何帮你有选择性的编辑图片，甚至[人工合成一张全新的图片](http://mi.eng.cam.ac.uk/research/projects/Query/?WT.mc_id=Blog_MachLearn_General_DI)；接下来我们会领略它的更多应用。

解决语义划分有着许多途径，但其中最强有力的构造方法还属逐像素分类：训练分类器去预测一种事物的像素级分布。这项任务对机器学习来说存在些许计算难题，特别是一张图包含了海量的像素（比如[诺基亚Lumia 1020手机](http://www.nokia.com/global/products/phone/lumia1020/?WT.mc_id=Blog_MachLearn_General_DI)每张图可采集4100万像素）。这意味着我们在做训练和测试样本实验时得花全图域分类项目的上百万倍时间。

如此险峻的麻烦致使我们研发某一特效的分类模型，即[决策森林](http://research.microsoft.com/en-us/projects/decisionforests/?WT.mc_id=Blog_MachLearn_General_DI)(也称作随机森林或随机决策森林)。决策森林其实的一系列分别受训练的决策树集合：

![](https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/02/52/MLB%20post%2011%20-%20Image%202.JPG)

每棵树都有一个根节点，很多内部“分裂”节点，和很多终端“叶”节点。测试阶段分类从跟节点开始，对某些数据进行二元"分裂函数"计算，这简单得就像“这枚像素是否比其邻像素格更红？”这样的问题。它会被划分到左子树还是右子树，完全取决于它的二元决策法，然后遍历到下一分裂函数，如此循环。当到达叶节点，预测结果便会储存起来，通常分类标记也会随着一起输出。（也请参见Chris Burges近期有关优化搜索排序的进阶决策树优质[博文](http://blogs.technet.com/b/machinelearning/archive/2014/07/11/machine-learning-for-industry-a-case-study.aspx?WT.mc_id=Blog_MachLearn_General_DI)。）

决策树之美来源于其测试阶段的高效：当从根节点到叶节点的路径数呈指数爆炸，每一个测试像素点却有且仅有一条路径通过。此外，分裂函数的计算法也是基于其之前遍历的数据，即分类器更希望依照先前判断提出合适的问题。这跟我们通常玩的“二十问”是一个道理：当你只能问一定数目的问题时，你会基于前一问题的答案反复琢磨下一个问题。

有了这种技术，我们便能在应对[图像语义划分](http://research.microsoft.com/apps/pubs/default.aspx?id=117887&amp;WT.mc_id=Blog_MachLearn_General_DI)，[街景划分](http://research.microsoft.com/apps/pubs/default.aspx?id=117889&amp;WT.mc_id=Blog_MachLearn_General_DI)，[基于医学三维扫描的人体解剖](http://research.microsoft.com/apps/pubs/default.aspx?id=135567&amp;WT.mc_id=Blog_MachLearn_General_DI)，[镜头重定位](http://research.microsoft.com/apps/pubs/default.aspx?id=184826&amp;WT.mc_id=Blog_MachLearn_General_DI)和Kinect的深度图像中[人体部位划分](http://research.microsoft.com/apps/pubs/default.aspx?id=145347&amp;WT.mc_id=Blog_MachLearn_General_DI)等难题时得心应手。拿Kinect来说，决策树在测试阶段的效率是至关重要的：我们那极其紧张的计算预算，我们可利于与Xbox上图形处理器(GPU)逐像素并行计算的能力适配的条件计算法来调整[1]。

在本系列第二篇文章当中，我们将讨论最近火热的“深度学习”技术在图像分类中的使用，并展望它今后的未来。与此同时，如果你想学习基于云端的机器学习技术，欢迎参观[微软机器学习中心](http://azure.microsoft.com/en-us/documentation/services/machine-learning/?WT.mc_id=Blog_MachLearn_General_DI)。

感谢浏览。

Jamie, Antonio 和 Sebastian

> [1]人体部位划分仅是天才工程师[团队](http://www.microsoft.com/about/technicalrecognition/Kinect-Skeletal-Tracking.aspx?WT.mc_id=Blog_MachLearn_General_DI)在Xbox全身骨骼追踪法的冰山一角。
