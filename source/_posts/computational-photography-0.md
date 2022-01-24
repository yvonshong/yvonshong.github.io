---
title: 计算摄影——“看得见”的未来
date: 2020-10-19 01:52:00
categories: tech
tags: 
- camera
toc: true
---

之前的专栏「自律走行」键盘摄影系列文章中，介绍了作为一名新手，使用相机拍一张照片时需要了解的一些摄影基础知识，当然还要更多关于构图，相机预设的模式等等实际操作时遇到的问题，和拍摄时的经验等等完全没有提及，所以我称之为「键盘摄影」（笑

但作为一名搞自动驾驶的算法工程师，怎能止步于在使用相机传感器时知道摄影的基本概念就可以了呢！我当然会疑惑相机是如何对焦的？它又是如何自动曝光的？它的自动白平衡又是怎么做的？当这些关于相机算法的一系列问题从我的脑海中冒出时，我发现，我已经站在了计算摄影的大门口。

<!-- more -->

戳>>「[键盘摄影](https://www.zhihu.com/column/jiritsu-soko」系列文章，后续想到了什么会再更新！

- [键盘摄影（一）——相机成像基本元件](https://zhuanlan.zhihu.com/p/93481287)
- [键盘摄影（二）——曝光三要素](https://zhuanlan.zhihu.com/p/138585113)
- [键盘摄影（三）——等效焦距和等效光圈](https://zhuanlan.zhihu.com/p/138585371)
- [键盘摄影（四）——相机成像元件：胶片与彩色暗房](https://zhuanlan.zhihu.com/p/139384545)
- [键盘摄影（五）——相机成像元件：CMOS/CCD](https://zhuanlan.zhihu.com/p/139394687)
- [键盘摄影（六）——相机成像模型](https://zhuanlan.zhihu.com/p/138585667)
- [键盘摄影（七）——深入理解图像信号处理器 ISP](https://zhuanlan.zhihu.com/p/139432684)
- [键盘摄影（八）——相机结构和卡口](https://zhuanlan.zhihu.com/p/263018344)
- [键盘摄影（九）——光学像差](https://zhuanlan.zhihu.com/p/263867036)
- [键盘摄影（十）——滤镜的种类和作用](https://zhuanlan.zhihu.com/p/412506198)


苹果 iPhone 11 发布会上，苹果高级副总裁 Phil Schiller 将新 iPhone 的相机称呼为

「It is computational photography mad-science. 」

**这是一场计算摄影的疯狂科学实践**。

![](https://pic1.zhimg.com/80/v2-c255b5ec1206450551713ee7c63c33d8_720w.jpg)

而在撰写以上系列文章，尤其是 [键盘摄影（七）——深入理解图像信号处理器 ISP](https://zhuanlan.zhihu.com/p/139432684) 时，我更切身地意识到：「计算摄影」正在改变传统摄影器材，奠基新的摄影技术，进而影响摄影艺术——它是我们看得见的未来。（当然计算摄影首推 Google ！Pixel 才是这个行业的老大哥！）

所以在接下来的文章中主要会去探讨计算摄影的相关话题，不仅仅是相机内部的算法，也会探(现)讨(学)如何利用算法来处理图像，比如相机的去噪，模糊图像的恢复等等（开始挖坑）。主要关注点会是如何利用算法去解决摄影中切实的问题，而不只是传统的图像处理，以及我对计算摄影框架性的理解，不会追最新 paper，会努力在看一类问题时查一查前沿技术是怎么解决这类问题的，可能会有一些公式推导和代码。

而关于计算机视觉中的多视图几何，三维重建， SLAM，我的专业方面的东西，会在我重啃 MVG 时另开新坑来写（滑稽），只希望大家轻喷。

目前关于计算摄影的中文资料也比较少，这里也先贴一些与之有关的链接：

- [Wang Hawk：计算摄影学 专栏](https://www.zhihu.com/column/hawkcp)
- 浙大章国锋老师的课程： [计算摄影学](http://www.cad.zju.edu.cn/home/gfzhang/course/computational-photography/)
- 佐治亚理工学院的优达学城课程： [计算摄影技术](https://cn.udacity.com/course/computational-photography--ud955)
- 韩国科学技术研究院的书：Computational Photography: Principles and Practice
[Tiancheng Zhi](http://www.cs.cmu.edu/~tzhi/), CMU：[Computational Photography](http://graphics.cs.cmu.edu/courses/15-463/2017_fall/)
- Gordon Wetzstein, Stanford：[Computational Imaging and Display](http://stanford.edu/class/ee367/)
- Derek Hoiem, UIUC：[Computational Photography](https://courses.engr.illinois.edu/cs445/fa2015/)
- James Hays, Brown：[Computational Photography)](http://cs.brown.edu/courses/csci1290/)
- Fredo Durand, MIT：[Digital and Computational Photography](http://stellar.mit.edu/S/course/6/sp12/6.815/index.html)
- Oliver Cossairt, Northwestern：[Introduction to Computational Photography](http://users.eecs.northwestern.edu/~ollie/eecs395/eecs395.htm)
- Kyros Kutulakos, University of Toronto：[Introduction to Visual Computing](http://www.cs.toronto.edu/~kyros/courses/320/)
- Kayvon Fatahalian, CMU：[Visual Computing Systems](http://graphics.cs.cmu.edu/courses/15769/fall2016/)
- Ramesh Raskar and Jack Tumblin, SIGGRAPH course：[Computational Photography](http://web.media.mit.edu/~raskar/photo/)

期待您的点赞和关注！
