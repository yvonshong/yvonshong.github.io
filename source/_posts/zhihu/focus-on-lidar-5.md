---
title: 聚焦激光雷达（五）——处理器
date: 2023-05-11 19:55:00
categories: tech
tags: 
- lidar
- sensor
toc: true
---

我们在系列文章中，讲解了发射器，扫描器，接收器，光学系统，接下来便是激光雷达中的核心电子元件——处理器。由于篇幅原因，本文暂不涉及激光雷达的控制流程，或者是激光雷达的时间同步、脉冲的编解码、点云的解算等问题，仅依次介绍处理器硬件中涉及到的电子元件。文后附有几种激光雷达的拆解案例，罗列了激光雷达处理器中涉及到的电子元件，如有兴趣可点赞收藏该文章。

<!-- more -->

# 激光脉冲驱动控制器

通常发射端每个激光器需要链接一个激光器脉冲驱动控制器 LD Driver，它负责在接收到主控芯片的发光指令后，给激光器发送一个控制信号。实现激光的脉冲式发射和编码，通过配置脉冲强度和脉冲宽度，增加编码功能，增强抗干扰能力。

驱动控制器要求控制信号能越快越好，有足够陡峭的上升沿。通常在低速信号电路中，信号从 0(低电平) 变成 1(高电平) 可以看成是瞬间完成的，但在高速电路中， 从 0 跳到 1 的时间消耗就无法忽略了，上升沿指的就是这个从 0 到 1 的过程，反之下降沿就是从 1 到 0 的过程。 之所以对上升沿有较高要求，是因为激光对人眼有加热效应，受到人眼安全约束，但可以通过提高瞬时功率，提高探测距离，缩短发光时间，降低发热效应（**关于人眼安全，后期将会单独撰写一篇文章**）。同时，缩短发光脉冲时间对于提高激光器点频也有所帮助。因此， 尽可能缩短上升沿和下降沿时间也成了必要。

同时激光器要达到高功率短脉冲，不仅需要快速的激光脉冲驱动，还需要一个能够快速响应 LD 驱动的大功率电流源，常见的是 TI 的 GaN FET。

![](https://pic4.zhimg.com/80/v2-261b8cf7d1c458a6e510ef36ed50405f_720w.webp)

大电流窄脉冲驱动能力能够实现驱动 GaN 产生脉冲宽度小于 3 ns、峰值电流超过 30 A 的电流脉冲， 控制激光器产生高峰值功率窄脉宽的光脉冲信号，有利于提升激光雷达产品的测远能力和测距精度。

# 扫描器驱动和编码器

我们在前文 [Yvon Shong：聚焦激光雷达（一）——扫描器](https://zhuanlan.zhihu.com/p/611852342) 提到，一些类型的激光雷达，存在机械/微机电扫描结构，比如需要电机转动反射棱镜，或者是电磁驱动振镜。所以在主控芯片发出发光指令时，也会向扫描器驱动发射控制指令，控制电机或振镜的转动。

编码器可分为：电阻类、电感类、电容类和光电类，其功能是将位置和旋转等物理量转换为数字或模拟电信号。最常见的应用是在电动机的运动控制中提供反馈。大多数应用都使用光学编码器，因为光学编码器除了有准确性，还不需要任何单独的电子设备来提供位置或精确位置。

- 光学式编码器
  
光学式编码器轴带动光栅盘旋转时，经发光元件发出的光被光栅盘狭缝切割成断续光线，并被接收元件接收产生初始信号。该信号经后继电路处理后,输出脉冲信号。光栅实际上是一个刻有规则透光和不透光线条的圆盘，光敏元件接收的光通量随透光线条同步变化，光敏元件输出波形经整形后，变为脉冲信号，每转一圈，输出一个脉冲。根据脉冲的变化，可以精确测量和控制设备位移量。

![](https://pic3.zhimg.com/80/v2-6f3a046c3a455c04a9e2460f53c5e66e_720w.webp)

> 透射型旋转编码器

反射型将来自光源的光束，反射到由柱面透镜和棱镜组成的转盘上，并将其作为受光元件进行检测，从而易于实现产品的小型化。 这些光学元件的特点是精度高、分辨率高，不易受磁场影响。

![](https://pic1.zhimg.com/80/v2-3bd8b3a1bbe10d03ef22838757e50d38_720w.webp)

> 反射型旋转编码器

- 磁性编码器

磁性编码器通过磁阻元件检测，在外圆周上交替排列的磁化 N 极和 S 极的旋转圆盘的磁极变化，将其转换为电信号，并以方波形式输出。 其特点是体积小、重量轻，而且由于没有发光元件，因此功耗比光学式低。但磁性容易受到外界影响。

![](https://pic1.zhimg.com/80/v2-c4e988b1cef94579b617fc47a54b4804_720w.webp)

> 磁性编码器

# 接收器驱动和读出电路

我们在 [Yvon Shong：聚焦激光雷达（三）——接收器](https://zhuanlan.zhihu.com/p/618634684) 中有详细介绍，接收器需要电路控制来放大光生电信号， 并且 SPAD 需要配合猝灭电路来进行重置，所以接收器链接着处理器中驱动和读出电路。

# 跨阻放大器

在接收端，APD 或 SiPM 接收到光子后产生电流，理论上通过这个电流即可获知光强， 然而实际上尽管反射光信号已经经过了 SiPM 或 APD 的放大，却仍然较小，信号过于微弱，满足不了系统载噪比要求，通常需要在前端要采用低噪声放大器进行放大，以提高信噪比。

![](https://pic1.zhimg.com/80/v2-2e4c434ed7f895aa440166b35c5e603c_720w.webp)

> 速腾 M1 接收端的 TIA

而且光电传感器输出的是电流信号，不利于与数字电路相融合，会将其转化为电压信号，一方面方便数字电路处理，另一方面也能够减小功耗。完成放大和电流转成较大电压任务的就是跨阻放大器 TIA（Trans-Impedance Amplifier，TIA），属于高速运算放大器的一种。

# 数字转换

由于探测器的光电反应信号，通过跨阻放大器输出电压信号，往往需要将其转化成采样后的数字信号才便于核心处理器进行处理及运行后续的算法。

## 时间数字转换器 TDC

TDC，Time-to-Digital Converter 时间数字转换器，精确测量电信号时间间隔，主要发挥计时器功能，通常用于低功耗、低成本、环境简单的系统，此时只 TDC 需要连接到主控芯片和光接收器之间，当主控芯片发出发光信号时，也同步给 TDC 一个开始计时的信号，随后反射回来的光经过 TIA 转换成放大的电压，再经过比较器与参考电压比较，判断是否有光入射，TDC 则将比较器的输出当做结束信号，完成计时，并将时间信息送回主控芯片。

![](https://pic2.zhimg.com/80/v2-3ef6a975dc5f6539e6f7848cf77a3da5_720w.webp)

> TDC 的波形处理：通过时钟来读出前沿和脉宽，无峰值

TDC 功耗低、成本低、集成度高，但是采集到的信息量较少，难以做波形处理，适合低成本场景。

![](https://pic4.zhimg.com/80/v2-f531075fe487faf38bbe233ce4aca8fb_720w.webp)

> TI 基于 TDC 的 ToF 方案

## 模拟数字转换器 ADC

ADC，Analog-to-Digital Converter，模数转换器，将连续变化的电信号，转换为离散的数字量。

![](https://pic1.zhimg.com/80/v2-be14341103ebddc6a4b566d9f9c478d8_720w.webp)

> ADC 的波形处理：边沿检测得到上升沿时间、脉宽、峰值

ADC 通常用于更复杂的系统，ADC 对反射光信号进行持续采样，转换成数字信号，并由控制芯片进行波形处理、计时等工作。

ADC 能够采集到完整的波形，信息丰富，易应用波形处理算法（处理拖点、雨雾等）。但功耗高、成本高、集成度低。它适合更精密测量需求。

![](https://pic2.zhimg.com/80/v2-969538423a128cb565b4e157dcebedfd_720w.webp)

> TI 基于 ADC 的 ToF 方案

# 主控芯片

主控芯片需要控制发射系统发射激光脉冲，并处理电路返回的观测数据，计算开始信号和停止信号的时间间隔。FPGA 芯片通常被用作激光雷达的主控芯片，完成光电的处理进而输出点云信号，国外主流的供应商有 AMD 收购的 Xilinx（赛灵思），Intel 收购的 Altera，还有 Lattice 等规模稍小的厂商，国内主要的供应商有紫光国芯、西安智多晶等公司。

不过 FPGA 不是激光雷达主控芯片的唯一选择，也可以选用高性能单片机 （Microcontroller Unit，MCU）、数字信号处理单元（Digital Signal Processor，DSP） 代替。MCU 的国际主流供应商有 Renesas（瑞萨）、Infineon（英飞凌）等，DSP 的主流供应商有 TI（德州仪器）、ADI（亚德诺半导体）等。

为什么不采用 CPU 作为主控？因为激光雷达需要进行大量的信号处理、电机时序控制等，CPU 虽然也能做，但如果采用专用的算法以及为算法专门优化设计的电路，其效率会高得多。而激光雷达作为汽车领域的新生事物，从 2007 年 Velodyne 激光雷达首次被用于 DARPA 挑战赛至今，其上车的历史也不过十五年，还有许多硬件/算法设计尚处在探索阶段，因此采用 FPGA 有利于反复迭代修改，同时还满足了专用电路的高效性。

比如，仅仅反射波的波形处理就需要消耗大量算力，而且每一个激光器的反射光都需要进行处理，使用 CPU 既难以满足算力需求，又浪费 CPU 的通用能力，因此往往需要专门的电路进行处理。并且实际中波形的处理比理论中复杂许多，虽然发射端发射的是一个短促的脉冲，但由于光束的扩散，飞行过程中会遇到多个障碍物，产生多个反射波，判断反射光的返回时间，以及反射率将变得十分复杂，更不遑说对激光脉冲进行编码解码的处理。

关于 FPGA 的科普可以查看 [FPGA 技术江湖：简谈 CPU、MCU、FPGA、SoC 芯片异同之处](https://zhuanlan.zhihu.com/p/347799990)

而以下是 TI 的 机械旋转式 LiDAR 的电路模块图 [Mechanically scanning LIDAR](https://link.zhihu.com/?target=https%3A//www.ti.com/solution/automotive-mechanically-scanning-lidar%3Fvariantid%3D34407%26subsystemid%3D20812%23block-diagram)，可以看到通常还会有一些温度传感器和相应的温度控制，来避免激光雷达电路板处在极端温度环境。还包含整个系统的电源相关驱动模块。

![](https://pic4.zhimg.com/80/v2-630c1fb5bee03fbcda7e0d20f3205377_720w.webp)

> LiDAR 各模块控制信号链路，以及电源，接口，时钟，监测和诊断模块

# System on Chip

模拟前端电路（Analog Front End，AFE）处理的对象是信号源给出的模拟信号，接收器的感生信号具有动态范围大，脉宽窄，幅度弱的特点，为了解决这些问题，处理数据，模拟前端通常包含传感器接口、模拟信号调理（Conditioning，包括阻抗变换、程控增益放大、滤波和极性转换等）电路、模拟多路开关、采样保持器、ADC、数据缓存以及控制逻辑等部件的存以及控制逻辑等部件的集成组件。

但由于激光雷达模拟芯片技术难度相对有限，且厂商之间尚无统一的设计标准，因此考虑到适用性和降本需求，众多激光雷达厂商开始自研 ASIC 或 SOC 芯片将以上功能集成到单个芯片中。

![](https://pic4.zhimg.com/80/v2-11c58befc88a644e1d394dce3d3b5537_720w.webp)

> 激光雷达专用芯片及功能模块示意图

处理器目前逐步向企业自研专用片上集成芯片（System on Chip， SoC）迁移发展，TIA、ADC 等也可能集成到 SoC 中，随着 VCSEL 发射器和 SPAD 接收器的芯片化，实现更强的运算能力、更低的功耗和更高的集成度。进一步的集成有多方面好处，第一是继续降低成本；第二是缩短距离，避免电路板层面以及外界的其他干扰；第三是减少元器件数量，提高可制造性，适合大规模量产；第四是缩小体积，更高的可制造性和更低的干扰有利于通过车规，而更小的体积和更低的成本对于汽车应用十分重要。

# 拆解案例

## Scale Gen 2
可以查看 [朱玉龙：技术讨论｜Valeo Lidar Scala Gen 2 拆解](https://zhuanlan.zhihu.com/p/582053195)

## Velodyne VLP 16

Velodyne 16 线激光雷达的主板是该设备的核心，具有许多控制器，RF 组件和开关。包括 Intel，Microchip，ADI 和 TI 的组件。

![](https://pic1.zhimg.com/80/v2-3e69fde8179be553884c7382a8bef0b4_720w.webp)

> VLP 16 主板

- TI：微控制器，逆变器，调节器和接收器，温度传感器；
- ADI：放大器，ADC 驱动器和开关多路复用器；
- Microchip：稳压器；
- 英特尔： Cyclone III FPGA，8 MB 闪存（主板背面）
- 英飞凌：双 MOSFET 驱动器（主板背面）

![](https://pic1.zhimg.com/80/v2-a64d40dc552c87566fe16ee8cc4e11d0_720w.webp)

> VLP 16 电源板

- 英特尔：第二个 Cyclone III FPGA ，并行的 128 MB NOR 闪存；
- ISSI： 32 MB SDRAM 内存；
- 意法半导体：调节器；
- Microchip： ADC 和 MOSFET 驱动器；
- Broadcom：双通道光耦，光学编码器（电源板背面）；
- Allegro Microsystems：霍尔效应传感器；
- 凌力尔特：降压转换器（电源板背面）；
- TI：以太网收发器（电源板背面），温度传感器（电源板背面）；

## Ouster OS1

Ouster OS1 激光雷达传感器的主板上的组件包括：

![](https://pic4.zhimg.com/80/v2-56fa05fd0c999208031bf031a35290c3_720w.webp)

> Ouster OS1 主板

- Maxim：12 位模数转换器和限幅放大器
- Marvell Semiconductor：千兆以太网收发器
- 美光多：芯片内存 8GB MLC NAND 闪存、内存控制器和 DDR3L SDRAM 内存
- TI：DDR 终端稳压器和可调节的 slap-down 转换器
- Analog Devices：射频功率检测器
- Macronix：串行 NOR 闪存 16MB

![](https://pic4.zhimg.com/80/v2-e0b633bc93580c885f95e4191b55b6b7_720w.webp)

> Ouster 内部转子板

内部的转动子板用作 Ouster OS1 内部的控制单元，其中包含：

- Microchip： 125 MHz MEMS 振荡器
- Xilinx：Artiz-7 FPGA
- Nexperia：双电源转换收发器
- Maxim： 12 位 ADC
- TI：电流分流监视器芯片


![](https://pic1.zhimg.com/80/v2-b981d90046a26f7f71cca97598023aec_720w.webp)

> Ouster 电机板

电机板包含内存和其他芯片，用于车辆和 LiDAR 的通信：

- 包括与车辆通信的芯片
- Microchip ：串行 EEPROM 存储器 2KB
- TI ：补偿器、电流分流芯片和功率 MOSFET
- ON Semi： MOSFET 驱动器

## Livox HAP

![](https://pic4.zhimg.com/80/v2-5ef8b9fdda2ac0a3c2daf3cbf488599f_720w.webp)

> 大疆 Livox HAP 主控板以及两大控制芯片

- 英飞凌：ARM Cortex M4 FPGA
- Xilinx：Xilinx：Zynq Ultra Scale+ MPSoC

## RoboSense Helios
![](https://pic3.zhimg.com/80/v2-498ea5eddde66583994a71c76d79ff26_720w.webp)

> RS Helios 主控板

- 赛灵思：ZYNQ ARM 双核 Cortex-A0 FPGA；
- 美光：512MB SDRAM 内存；
- TI：DDR 终端稳压器、LDO 稳压器、半桥栅极驱动器、降压电源块和功率 MOSFET；
- Broadcom：汽车以太网收发器；
- Winbond：串行闪存；
- Diodes Incorporated：ESD 保护；
- Maxim：Step-down DC-DC 转换器

在激光雷达里面还有一个数字适配器板，主要包含包含

![](https://pic4.zhimg.com/80/v2-52eee3cf900c8270e6dc3476941ebb93_720w.webp)

> RS Helios 数字转接板

- ST Microelectronics：ARM 32 位 Cortex-M3 微控制器 MCU（用作激光雷达的连接和电源管理）
- On Semiconductor：稳压器
- Diodes Incorporated：功率 MOSFET
- Broadcom：以太网收发器；

另一块辅助板：

![](https://pic1.zhimg.com/80/v2-1f3ba1d685d0107a1b45f5bb1e893f40_720w.webp)

> RS Helios 激光雷达辅助板

- Xilinx： Spartan-7 FPGA（用于控制激光雷达传感器内部的传感器、连接和电源管理）
- Analog Devices：VCO
- TI：LDO、差分放大器、step-down 转换器和温度传感器
- Maxim：DC-DC 转换器
- Diodes Incorporated：ESD 保护
- IDT：时钟缓冲器
- NXP Semiconductors：双 USB 2.0 开关
- Vishay：功率 MOSFET

# Reference

- 马鹏阁. 多脉冲激光雷达[M]. 国防工业出版社, 2017.
- 王颖麟, 廖进昆, 晏思平,等. 基于FPGA和MCU的激光成像雷达信号处理系统[J]. 兵器装备工程学报, 2009, 030(011):60-62.
- [上海证券交易所：禾赛科技 2021 年科创板招股书](https://link.zhihu.com/?target=http%3A//static.sse.com.cn/stock/information/c/202101/e999c0661a644c928d259e4fb47e358b.pdf)
- [TI：飞行时间和激光雷达 - 光学前端设计](https://link.zhihu.com/?target=https%3A//www.ti.com.cn/cn/lit/pdf/zhcaa62)
- [与非网：模拟前端（AFE）原理及选型指南](https://link.zhihu.com/?target=https%3A//www.eefocus.com/article/317489.html)
- [可易亚半导体 KIA：集成电路-专用集成电路（ASIC）简介、优缺点等知识](https://link.zhihu.com/?target=http%3A//www.kiaic.com/article/detail/2146.html)
- [面包板社区：FPGA与ASIC对比，优缺点一目了然！](https://link.zhihu.com/?target=https%3A//www.eet-china.com/mp/a39484.html)
- [FPGA技术江湖：简谈CPU、MCU、FPGA、SoC 芯片异同之处](https://zhuanlan.zhihu.com/p/347799990)
- [车东西：看懂这颗激光雷达芯片，就看懂了索尼汽车](https://zhuanlan.zhihu.com/p/454125523)
- [中信证券：拆解5款车载激光雷达带你了解里面的元器件](https://link.zhihu.com/?target=https%3A//www.ctfiot.com/77494.html)
- [汽车电子设计：技术讨论｜Valeo Lidar Scala Gen 2 拆解](https://zhuanlan.zhihu.com/p/582053195)
- [芝能汽车：激光雷达 Ouster 公司情况和 Ouster OS1-64 拆解](https://link.zhihu.com/?target=https%3A//new.qq.com/rain/a/20220322A05F2C00)
- [智能汽车俱乐部：拆解分析｜速腾RS Helios激光雷达的拆解](https://link.zhihu.com/?target=https%3A//www.smartautoclub.com/p/34362/)
- [燃云汽车：Velodyne 激光雷达 Puck VLP-16 拆解](https://link.zhihu.com/?target=https%3A//www.vision-systems-china.com/deinews.asp%3Fid%3D4820)
- [Teardown: Velodyne Lidar Puck VLP-16 sensor](https://link.zhihu.com/?target=https%3A//electronics360.globalspec.com/article/16089/teardown-velodyne-lidar-puck-vlp-16-sensor)
- [科普中国：激光干涉光栅编码器——走进精密运动控制的世界](https://link.zhihu.com/?target=https%3A//cloud.kepuchina.cn/newSearch/imgText%3Ffrom%3D1%26id%3D6775895315027607552)
- [尼得科科智博电子：编码器特集](https://link.zhihu.com/?target=https%3A//www.nidec-components.com/cn/featuring/encoder/)

---

欢迎在我的专栏「[自律走行](https://www.zhihu.com/column/jiritsu-soko)」中查看更多「聚焦激光雷达」系列文章

- [聚焦激光雷达（一）——扫描器](https://zhuanlan.zhihu.com/p/611852342)
- [聚焦激光雷达（二）——激光器](https://zhuanlan.zhihu.com/p/616243016/)
- [聚焦激光雷达（三）——接收器](https://zhuanlan.zhihu.com/p/618634684)
- [聚焦激光雷达（四）——光学元件](https://zhuanlan.zhihu.com/p/622652543)
- [聚焦激光雷达（五）——处理器](https://zhuanlan.zhihu.com/p/628148718)