---
title: 聚焦激光雷达（四）——光学系统
date: 2023-04-19 08:21:00
categories: tech
tags: 
- lidar
- sensor
toc: true
---

激光雷达从器件来看，最主要的构成要素是扫描器、发射器，接收器，处理器，以及一些内部的光学元件了，激光从发射器中产生，除了要通过扫描器来调整激光方向以外，还需要通过各式各样的光学元件，来调整光斑形状大小，光场的能量分布等等。

<!-- more -->

查阅了很多光学供应链公司的产品和研报，这可能是全网唯一比较全面的介绍激光雷达内部涉及的光学元件的科普文章了，欢迎点赞关注本专栏。
  

从激光雷达 BOM 成本拆分来看，透镜等光学组件仍是激光雷达的重要组成部分。以法雷奥 Scala 转镜激光雷达为例，目前年产量十万级规模， BOM 成本约 400 美元，其中主控板占 45%，激光发射接收组件占 33%，光学单元占 13%，外罩 8%，马达 1%。而 Livox 的双楔形棱镜式激光雷达的透镜模组占了成本的 54%。可以看到，光学元件是激光雷达成本里重要组成部分。

由于各种激光器发射的激光束并不是绝对平行的，具有光斑形状不规则，发散角度大的问题，因此还需要一套光学系统，对激光器的输出光束进行准直整形，通过改变光束的发散度、波束宽度和截面积，改善输出光束质量。

发射光学系统主要由透镜、反射器件、衍射器件等光学元器件组成，包含准直镜、分束器、扩散片等。接收光学系统主要由透镜、滤光片等组成，尽可能收集经目标反射后的光能量，将其汇集到探测器的光敏面上。

接下来我们从发射器出发，沿着光路一同探究沿途的光学元件。

---

# 准直镜 Collimator

准直模块通常由 FAC 透镜（Fast-Axis Collimation Lens）和 SAC 透镜（Slow-Axis Collimation Lens）构成，他们本质上是我们熟悉的凸透镜在横纵轴上需求不同而产生的分解，先对快轴方向进行聚焦，然后在慢轴方向进行另一种程度的聚焦。

![](https://pic3.zhimg.com/80/v2-e62b34f7f654b4701f977d349e8db316_720w.webp)

> 激光雷达用快轴准直镜 / 慢轴准直镜

为什么需要对激光器发出的光进行校准？因为激光器发射的激光并不是笔直的光束，而是存在着发散角的，尤其是半导体激光器，发散角非常大。由于半导体激光器体积小，谐振腔小，对光束的筛选作用比较弱，而且发光面积小，发出的光线会发生衍射。

另外，半导体激光器由于谐振腔的筛选能力不够强，还存在光束质量问题（光斑的强弱分布不均），且在主要光斑周围还有少量剩余能量（拖尾效应），所以需要进行调整。针对拖尾问题，经常采用光阑将主光斑之外的少量光束舍弃。

![](https://pic2.zhimg.com/80/v2-9632322c3a540470450060a02ac24d69_720w.webp)

> EEL 和 VCSEL 激光器光斑强度示意图

对于 EEL 来说通常射出的都是椭圆锥形光束，椭圆形光斑的长轴通常称为**快轴**，快轴方向发散角可能达到 25-50 度，短轴通常称为**慢轴**，慢轴方向发散角为 10-20 度。通常需要在发光界面后立刻使用柱面透镜进行快轴准直，便可先抑制住发散最严重的方向，减少后续使用的透镜面积。

![](https://pic1.zhimg.com/80/v2-c9aae90dfc7ea77aae33100106ff87a0_720w.webp)

> EEL 激光器的发散角

例如速腾 M1 是五个激光器，在每个激光器后紧跟一个快轴准直。在进行快轴准直后，再进行一次慢轴准直，激光将具有较好的直线性。

![](https://pic4.zhimg.com/80/v2-a8389f423f2cf543d3d07b41b70c43b7_720w.webp)

> 速腾 M1 激光雷达拆解图

镭神智能的一款激光雷达发射模组中采用 8 个 EEL 激光器，在每个激光器的出光口直接安装一个快轴准直镜，体积更小，仅有亚毫米尺度，肉眼基本无法直接分辨。

![](https://pic3.zhimg.com/80/v2-bf62aa3c3697b272f4596afb43787d3e_720w.webp)

> 镭申智能激光雷达拆解

VCSEL 激光器的光束也会呈现圆锥形发散，发散角可以达到 20 度左右。如果采取这样的光束直接照射，则能量会很快分散殆尽，无法进行有效探测。

![](https://pic4.zhimg.com/80/v2-e4a80ec9ea569fcd353f1b4599b47a7f_720w.webp)

> 光纤激光雷达输出的圆形高斯光束

而针对光学校准，1550nm 路线再次展现了其优势。由于 1550nm 激光雷达使用光纤激光器，而单模光纤本身就具有极强的光学校准能力，因此 1550nm 激光器的光束质量较高，输出的几乎是完美的圆形高斯光斑。同时其发散角也较小，圆光纤的发散角只有 6 度多，通常只需要在光纤后加一个普通的球面凸透镜即可。

![](https://pic1.zhimg.com/80/v2-953c9190595325a93ee00d224a607ebc_720w.webp)

> 图达通 Falcon 激光雷达拆解图

---

# 分束器 Beam Splitter

衍射激光分束器简称分束器（Beam Splitter）又叫做激光分束镜，激光分光镜，分光片，光束分束器。

激光分束器可以把一束准直的入射激光均匀地分配成 N 束出射光，输出光束会以特定的分离角度射出，出射光的光束直径、发散角和波前相位完全和入射激光相同，只是传播方向发生改变。并且分离角度极其精准，误差小于 0.03mRad。分束器的衍射效率介于 70~95% 之间，均匀性一般<5%，很多情况下光束直径的能量差别<1%。

![](https://pic2.zhimg.com/80/v2-6798a0503f93f000eadb5708a4003e99_720w.webp)

> EFL：有效焦距；θs：两个焦点之间的分离角度；θf：全角；D：光点阵列的长度

根据输出光斑的分布，分束器可以分为一维分束、二维分束、点阵分束，一维分束在激光加工中最为常用，例如激光一分二、一分三和一分四，都可以成倍地提高加工效率。

---

# 扩散片 Diffuser

扩散片又称作扩散器、匀光片、匀化镜、光场匀化器 、Beam Homogenizer、Optical Diffuser、Beam Transformation System。其作用是将入射激光转化成任意形状尺寸的强度均匀的光斑。将激光束扩散成一个圆锥形，可以使激光雷达接收到更多的反射光，从而提高激光雷达的探测距离和精度。

![](https://pic2.zhimg.com/80/v2-b26d67ba6d878c9b7ec61149010bb901_720w.webp)

> d：成形光斑尺寸；D：光束直径；EFL=有效焦距；

匀光片在半随机方向上分裂入射光束，以便在远场或焦平面上获得所需要的强度分布形状。这种方法可以设计出能够产生精确发散角度和任意的输出光斑尺寸和形状以及强度分布的元件。匀光片产生的光斑的性能在很大程度上取决于入射光束参数。入射激光可以为单模或多模，衍射效率 70%~90% 不等。通过使用高 $M^2$ 输入光束可以实现更高的均匀性。匀光片对光束尺寸，位移和元件倾斜不敏感。它具有高激光损伤阈值（元件被激光损坏的阈值），而均匀性和效率随设计而变化。

光束质量系数 $M^2$ 是一个单位的参数，用于描述实际激光束的不完美程度。$M^2$ 值越接近于 1.0，光束就能被聚焦到其衍射限制的光斑大小。在激光加工工艺中往往要求以尽可能小的光斑聚集光束的大部分激光能量，因此激光光束质量 $M^2$ 因子便是一个量化激光聚焦能力的参数。

---

# 扫描器 Scanner

扫描结构中最常见的就是反射镜（如 MEMS 中的振镜，或者是因为结构设计而需要改变光路）、棱镜（为了实现扫描，通常使用电机转动棱镜）和单向透光发射镜（为了实现收发同轴，发射的激光从里到外通过半透半反镜，接收的激光从外到里经过反射，进入接收器光路），具体可以查看我之前的系列文章 [Yvon Shong：聚焦激光雷达（一）——扫描器](https://zhuanlan.zhihu.com/p/611852342)。

振静方案：振镜通过摆动来扩散激光，但受制于机械振动的损耗控制要求，MEMS 振镜的振幅一般在 25 度左右，需要搭配光路扩散系统对出射激光进行放大，来满足对物体的覆盖要求。

转镜方案：复杂形状让面型精度成为关键。转镜方案通过多面体转镜的旋转来扩散出射激光，涉及多个镜片表面的相互胶合，其相邻界面处的平整程度会对光束反射效率造成影响。因此，转镜对于元件的制备精度要求更高。

---

# 视窗 Windows

![](https://pic3.zhimg.com/80/v2-1e7c3a6b06616d3a8a6f3e90f750d7e2_720w.webp)

> 车规环境要求视窗等元件具备疏水等抗干扰功能

视窗作为激光雷达最外部的光学元件，需具备一定的主动抗干扰能力，其次恶劣的环境需要这些滤波片能够经受很宽泛的温度范围（零下 40℃ 到零上 80 ℃），特别是车窗所面临的环境，还可能暴露在雨水、冰层、道路除冰盐以及其他所有路上驾驶时所能遇到的元素环境中。这就需要视窗同时镀有疏水膜、 增透膜、除雾膜等多种膜系以保障恶劣天气的性能稳定性。 此外，在车辆使用寿命内，这些滤波片需要在没有维护和校准的情况下，在上述环境状况中正常运行。

---

## 滤波片 Filter

如果探测器是 LiDAR 系统的“眼睛”，那么光学滤波片就是“太阳镜”——减少眩光，让眼睛可以无背景干扰观察所寻求的目标。相信大家也在使用 iPhone 的过程中遇到很多鬼影现象，这其实就是镀膜设计问题在搞鬼。在实际使用中，LiDAR 的镀膜作为光学滤波片主要有两种功能：

- 激光透过率的要求

光学元件通过镀防反射增透膜来满足高透过特性，减少散射光、重影和背向反射，否则激光传输将产生很大光损，直接影响最终的探测效果。防反射增透膜是光学元件中最基础、最通用的镀膜技术。增透膜利用了光的干涉原理， 通过控制薄膜的厚度和折射率来实现光线的增透。这些镀膜专为提供更低反射率 (< 0.5%) 而设计，因为低透光率的缺陷会在光路中被一层层放大，成倍影响最终打到物体上的激光效能。

增透膜的技术难度主要是对膜材的特定折射率要求和现实中膜材固有物理特性并不完全匹配。增透膜对薄膜厚度和折射率的要求被特定的物理公式限定，但现实的薄膜材料折射率由自身属性固定，二者只能近似，无法完全匹配。

理论上，最理想的透过率要求膜材的折射率等于空气折射率和元件折射率乘积的算数平方根。比如一般空气折射率在 1.0 左右，玻璃折射率在 1.5-1.7 左右，对应折算出理想膜材的折射率在 1.224/1.304 左右，但实际中并没有精准贴合理论要求的镀膜材料，这就要求光学企业通过合理的材料选择（同时还需考虑材料成本、机械稳定性等因素）、多层膜制备等技术手段来无限接近 100%透过率的理想目标。

![](https://pic1.zhimg.com/80/v2-13df2fc89284bc8a5b437a54d600ae88_720w.webp)

> 905nm 带通滤波片的光谱性能曲线

- 特定波长透过的要求

光学元件需要依据干涉原理来满足分光特性，其高透射率波段要尽可能窄，过滤其他波段的干扰杂散光并保障特定波长激光顺利透过。 激光在膜材上表面和下表面的反射光相位差为 180 度。依据光学原理推导后要求薄膜厚度为特定透射光波长的四分之一奇数倍。这对于薄膜制备精度有着极高要求。

具体光学元器件可能造成的影响，其实在相机中更为常见，可以参考我之前的文章：[Yvon Shong：键盘摄影（九）——光学像差](https://zhuanlan.zhihu.com/p/263867036)。

---

# Reference
  
-   [炬光科技：Fast Axis Collimators (FAC) for LiDAR](https://link.zhihu.com/?target=https%3A//www.focuslight.com/product/solutions/automotive-application-solution/beam-shaping-solution/fac-for-lidar/)
-   [炬光科技：准直模块](https://link.zhihu.com/?target=https%3A//www.focuslight.com/product/component/micro-optical-component/optical-module-assembly/collimation-module/)
-   [炬光科技：Beam Transformation Systems (BTS)](https://link.zhihu.com/?target=https%3A//www.focuslight.com/product/component/micro-optical-component/optical-module-assembly/beam-transformation-system/)
-   [海纳光学：匀化器操作原理，匀光片应用手册](https://link.zhihu.com/?target=https%3A//www.highlightoptics.com/Technology/217.html)
-   [海纳光学：分束器原理及应用手册](https://link.zhihu.com/?target=https%3A//www.highlightoptics.com/Technology/213.html)
-   [海纳光学：分束器](https://link.zhihu.com/?target=https%3A//www.highlightoptics.com/Product/26.html)
-   [海纳光学：衍射光学元件示意图](https://link.zhihu.com/?target=https%3A//www.highlightoptics.com/Technology/154.html)
-   [海纳光学：衍射光学元件](https://link.zhihu.com/?target=https%3A//www.highlightoptics.com/Product/223.html)
-   [Optics for Hire：LIDAR Lens Design](https://link.zhihu.com/?target=https%3A//www.opticsforhire.com/blog/lidar-lens-design-optical-layout/)
-   [奥林巴斯生命科学：Laser Systems for Optical Microscopy](https://link.zhihu.com/?target=https%3A//www.olympus-lifescience.com/en/microscope-resource/primer/techniques/microscopylasers/)
-   [益瑞电 Iridian：用于自动驾驶汽车的 LiDAR 和光学滤波片](https://link.zhihu.com/?target=https%3A//www.iridian.ca/zh-hans/%25e6%258a%2580%25e6%259c%25af%25e8%25b5%2584%25e6%25ba%2590/articles-whitepapers/%25e7%2594%25a8%25e4%25ba%258e%25e8%2587%25aa%25e5%258a%25a8%25e9%25a9%25be%25e9%25a9%25b6%25e6%25b1%25bd%25e8%25bd%25a6%25e7%259a%2584-lidar-%25e5%2592%258c%25e5%2585%2589%25e5%25ad%25a6%25e6%25bb%25a4%25e6%25b3%25a2%25e7%2589%2587/)
-   [面包板社区：激光雷达中的激光发射与接收光学原理](https://link.zhihu.com/?target=https%3A//www.eet-china.com/mp/a126297.html)
-   范娜娜, 王懋, 温少聪,等. 基于二维MEMS振镜的激光雷达系统的光学设计[J]. 光学技术, 2020, 46(3):5.
-   刘壮, 王超, 江伦,等. 低空高分辨率激光雷达光学系统设计[J]. 红外与激光工程, 2021.
-   Choi H , Kim W C . Optical system design for light detection and ranging sensor with an ultra-wide field-of-view using a micro actuator[J]. Microsystem Technologies, 2020.
-   Cheng Y, Cao J, Zhang F, et al. Design and modeling of pulsed-laser three-dimensional imaging system inspired by compound and human hybrid eye[J]. Scientific reports, 2018, 8(1): 17164.
-   [中信证券：激光雷达产业深度研究 从拆解五款激光雷达看智能驾驶投资机遇](https://link.zhihu.com/?target=http%3A//k.sina.com.cn/article_7426890874_1baad5c7a001014gh0.html)
-   [华西证券：激光雷达 汽车智能化中的黄金赛道](https://link.zhihu.com/?target=https%3A//pdf.dfcfw.com/pdf/H3_AP202208161577261488_1.pdf)
-   [浙商证券：华为哈勃生态成员，全球激光雷达光源模组先行者——炬光科技深度报告](https://link.zhihu.com/?target=http%3A//pg.jrj.com.cn/acc/Res/CN_RES/STOCK/2022/8/22/0ebcefde-2a09-4a6f-b1a8-734979392a07.pdf)
-   [浙商证券：2022年永新光学研究报告 激光雷达重新定义光学元件技术壁垒](https://link.zhihu.com/?target=https%3A//www.vzkoo.com/read/202211157f584a85f42bc46479c113cd.html)
-   [国海证券：2022年激光雷达行业研究 激光雷达BOM成本以主板和激光单元为主](https://link.zhihu.com/?target=https%3A//www.vzkoo.com/read/202207227acae24569c568c745185482.html)
-   [bilibili 绿芯频道：全网首拆！自制光路图！小鹏G9激光雷达—速腾聚创M1，究竟怎么样？](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1yY4y1N7Hy)
-   [bilibili 绿芯频道：两千美刀，直接拆掉！蔚来ET7激光雷达全网首拆｜Lidar拆解系列 2](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1fG411c7of)

---

欢迎在我的专栏「[自律走行](https://www.zhihu.com/column/jiritsu-soko)」中查看更多「聚焦激光雷达」系列文章

- [聚焦激光雷达（一）——扫描器](https://zhuanlan.zhihu.com/p/611852342)
- [聚焦激光雷达（二）——激光器](https://zhuanlan.zhihu.com/p/616243016/)
- [聚焦激光雷达（三）——接收器](https://zhuanlan.zhihu.com/p/618634684)
- [聚焦激光雷达（四）——光学元件](https://zhuanlan.zhihu.com/p/622652543)
- [聚焦激光雷达（五）——处理器](https://zhuanlan.zhihu.com/p/628148718)