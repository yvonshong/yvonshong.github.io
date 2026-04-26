---
title: yeeyan:Machine Learning, meet Computer Vision - Part 2
date: 2015-02-08 23:42:17
toc: false
---

本文为[微软亚洲研究院“机器学习”系列文章译文](http://www.msra.cn/zh-cn/research/machine-learning-group/default.aspx)

[yvonshong译言主页](http://user.yeeyan.com/articles/yvonshong/translation)

译者因此受邀参加2015年微软学生夏令营(西安)

<!-- more -->

*本文由微软剑桥研究院的[Jamie Shotton](http://social.technet.microsoft.com/Profile/Jamie%20Shotton?WT.mc_id=Blog_MachLearn_General_DI),&nbsp;[Antonio Criminisi](http://social.technet.microsoft.com/Profile/Antonio%20Criminisi%20-%20MSR?WT.mc_id=Blog_MachLearn_General_DI)和[Sebastian Nowozin](http://social.technet.microsoft.com/Profile/Sebastian%20Nowozin?WT.mc_id=Blog_MachLearn_General_DI)联合撰写。*

在[上一篇博文](http://blogs.technet.com/b/machinelearning/archive/2014/08/06/machine-learning-meet-computer-vision.aspx?WT.mc_id=Blog_MachLearn_General_DI)中，我们引领大家进入了计算机视觉这片领域，并提及到一种强有力的解决方案，利用决策森林实现逐像素分类，该技术已在[医学显像](http://research.microsoft.com/apps/pubs/default.aspx?id=135567&amp;WT.mc_id=Blog_MachLearn_General_DI)和[Kinect](http://research.microsoft.com/apps/pubs/default.aspx?id=145347&amp;WT.mc_id=Blog_MachLearn_General_DI)中得到广泛应用。接下来我们将聚焦于近来火热的深度神经网络和其在计算机视觉领域中的应用，其次展望计算机视觉和机器学习之后的下一个发展方向。

**深度神经网络**

近几年来我们在训练数据集的保质保量上和视觉搜索器上取得了同样巨大的进展。这主要源于从[众包法](http://en.wikipedia.org/wiki/Crowdsourcing?WT.mc_id=Blog_MachLearn_General_DI)中乍现的灵感，才将数据集扩展至涵盖千上万张标记图像。其中难度十足的[ImageNet](http://www.image-net.org/?WT.mc_id=Blog_MachLearn_General_DI)数据集包含了按图片划分的数百万种标记图像。

经历了ImageNet数据集社区几年缓慢的发展后，[Krizhevsky等人](http://www.cs.toronto.edu/~hinton/absps/imagenet.pdf?WT.mc_id=Blog_MachLearn_General_DI)终于在2012年扣响了通往成功的大门，在某种深层次训练[卷积神经网络](http://en.wikipedia.org/wiki/Convolutional_neural_network?WT.mc_id=Blog_MachLearn_General_DI)的精妙算法辅助下，他们向大家展示了[通用GPU计算](http://en.wikipedia.org/wiki/GPGPU?WT.mc_id=Blog_MachLearn_General_DI)。在1000种ImageNet图片数据集测试下，其显著地提高了图像分类的精确度。这引发了主流媒体的密集报道甚至导致些许初创公司被大公司收购。自此“深度学习”在计算机视觉的话题中如日中天，一些新近的论文还将其沿用到[目标定位](http://arxiv.org/abs/1311.2524?WT.mc_id=Blog_MachLearn_General_DI)，[人脸识别](http://www.cs.toronto.edu/~ranzato/publications/taigman_cvpr14.pdf?WT.mc_id=Blog_MachLearn_General_DI)和[人体姿态估计](http://arxiv.org/abs/1312.4659?WT.mc_id=Blog_MachLearn_General_DI)的研究中。

**未来展望**

卷积神经网络是如此简明有效，那这就是计算机视觉研究的终结么？目前我们能确认的是在接下来几年，它将持续流行并不断推动行业的技术水平，然而我们仍然坚信我们还会有其他方面的技术飞跃，在此以强调我们可实现的技术契机作结。

表达：这些网络学着去揣测图片内容的一系列简单表达法，不再关注图片中独立对象的细节，而是全局之间的联系，或者我们日常中的某一特定对象（比如我们不再仅凭一人光滑的头发和拿着吹风机这个事实，而自以为是地认为他的头发是湿的）。应对“非具象化”的图片，即图中存在很多并不突出的对象，像[微软CoCo](http://mscoco.org/?WT.mc_id=Blog_MachLearn_General_DI)一样的新数据集将提供更细化标记的独立对象划分。

效率：利用并行化，深度网络对测试图片的估算可以发挥得淋漓尽致，但是神经系统网络并没有[前文](http://blogs.technet.com/b/machinelearning/archive/2014/08/06/machine-learning-meet-computer-vision.aspx?WT.mc_id=Blog_MachLearn_General_DI)中提到的条件计算法的概念：每张测试图片得遍历网中每个节点并得到输出。此外，即使有着强劲的图形处理器(GPUs)，训练一个网络也得花费数天乃至数周的时间，这成为了实验高效性的瓶颈。

结构化学习：当下的卷积深度网络经过多年研究，已演变成一个设计精良的刚性结构，换句话说，特定层次的大小或层次的数目将对预测结构的质量产生不良影响。除了穷举参数来优化网络结构，我们希望有个契机以习得一种直接基于数据的弹性网络结构。

近来，我们正逐步解决上述两个问题，尤其是最后两个。我们感到热血的是近期就[决策丛林](http://research.microsoft.com/pubs/205439/DecisionJunglesNIPS2013.pdf?WT.mc_id=Blog_MachLearn_General_DI)的工作：集成根决策的[有向无环图](http://en.wikipedia.org/wiki/Directed_acyclic_graph?WT.mc_id=Blog_MachLearn_General_DI)(DAGs)。你可以认为一个决策有向无环图就是一颗[决策树](http://blogs.technet.com/b/machinelearning/archive/2014/08/06/machine-learning-meet-computer-vision.aspx?WT.mc_id=Blog_MachLearn_General_DI)，其孩子节点因归并而可有多重父母。相较于决策树，我们[发现](http://research.microsoft.com/pubs/205439/DecisionJunglesNIPS2013.pdf?WT.mc_id=Blog_MachLearn_General_DI)这些能有效的减少内存消耗而利于泛化。一个有向无环图虽与神经网络的结构相类似，但有着以下两点关键性区别：首先，结构和模型参数可后期习得；其次，有向无环图保留了决策树的优点，具有高效的条件计算法：每一个独立测试样例遵循有向无环图中的单一路径，而神经网络会遍历所有节点。我们正积极研究，将决策丛林和其他形式的深度学习结合，包括[堆叠](http://pages.ucsd.edu/~ztu/publication/pami_autocontext.pdf?WT.mc_id=Blog_MachLearn_General_DI)和[纠缠](http://research.microsoft.com/pubs/146430/Criminisi_IPMI_2011c.pdf?WT.mc_id=Blog_MachLearn_General_DI)，可给深度神经网络提供一个高效的解决方案。

若你意图使用决策丛林解决你的疑难杂症，Azure机器学习中的Gemini模块可助你一臂之力。

总的来说，计算机视觉前程似锦，而机器学习功不可没。在这一片领域的进展令人瞩目，但我们仍相信关于计算机视觉的研究仍任重而道远。

Jamie, Antonio 和 Sebastian
