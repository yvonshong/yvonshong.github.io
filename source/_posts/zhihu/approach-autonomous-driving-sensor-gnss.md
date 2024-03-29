---
title: 走进自动驾驶传感器（三）——卫星导航系统
date: 2021-09-21 15:36:00
categories: tech
tags: 
- sensor
- gps
- gnss
toc: true
---

之前写了自动驾驶用到的相机传感器、激光雷达、毫米波雷达，现在终于写，大学需要专门开一门课写一本书难度的传感器——GNSS 。在此期间阅读了几本 GPS 教科书，理清了 GPS 的整个数据流，以及涉及到的相关技术，如有错漏恳请不吝指正。（也求个点赞不要只收藏(╯‵□′)╯︵┻━┻）

<!-- more -->


无人驾驶想要获得全局定位，一定是相对于某一固定坐标系的，而地球上范围最广的坐标系便是地球坐标系，想要获得这么宏达层面上的观测，便必须依靠 GPS 卫星的数据。

如果我们事先知道卫星每一时刻相对于地球的位置（地面监测站监测后告诉卫星，卫星一直广播自身星历），然后观测自身距离多颗卫星的位置（用户接收机接收到多颗卫星的信号，得知相对距离），便能知道自身在地球坐标系的位置。

打个简单的比方，在一条单向高速公路上，前车一直在广播它距离起点的位置（这个是路边监控告诉它的），而我们能够测得距离它的位置，所以我们也就知道了自身距离起点的位置。GPS 中是需要观测到至少四颗卫星，来解算三维坐标和用户设备时间和卫星时间的差异。



这之中涉及到了坐标系和时间标准的统一，所以我们可以用 GNSS 来进行给自身定位，给时间高敏感度的设备进行授时（比如服务器时间）；而如果用户装有双天线，便可同时知道自身的朝向；而同时由于卫星或用户在移动，接收到的电磁波发生了多普勒效应，可以用来测速；而我国的北斗还提供了低成本的短报文服务。

GPS 可以观测得到空间坐标系的三维坐标值，加上陀螺仪和加速度计，便可以得到在空间中的完整姿态，在此对惯性导航先不赘述，待笔者写完 IMU 传感器后再来详细剖析惯性导航。

# 时空参考坐标系

全球定位系统的基本任务是确定用户在空间的位置，首先需要设立适当的坐标系。

## 空间系统

### 天球坐标系

为了确定卫星，宇宙飞船等在宇宙空间的位置和飞行状态，首先需要确定一个在宇宙空间可视为不变的参考系。空间卫星不被地球自转影响，但是观测站和用户都会跟随地球自转。

假设以地球的质心为球心，半径为无穷大的球（天球）存在于宇宙空间，选天球中心为天球坐标系的原点，而地球绕其极轴自转就像是个大陀螺，由于陀螺的定轴性，地球的极轴在宇宙空间的指向（赤道平面法向量）是稳定不变的，可以选作固定不变的轴来作为天球坐标系的坐标轴。

而地球绕太阳公转的轨道平面（黄道平面）也是稳定的平面，黄赤交角即为春秋分点，两点和质心的连线可以定义坐标系的另一条轴，然后构成右手坐标系，地心天球坐标系，简称天球坐标系，其不随地球的自转而变化。

![](https://pic4.zhimg.com/80/v2-dc8e54bd530dbea91bd302ccb0935877_720w.jpg)

> *天球赤道和黄道*

### 岁差和章动

然而黄赤交角不变是一种理想假设，陀螺仪的自转轴在干扰力矩的作用下存在进动和章动，地球也是一样，存在日月岁差和章动。

日月岁差是日月行星引力共同作用的结果，使地球自转轴在空间的方向发生周期性变化。在天体上，以这种规律运动的北天极通常称为瞬时平北天极或简称为平北天极，与之相应的天球，赤道和春分点称为瞬时天球，平赤道和瞬时平春分点，简称平天球，平赤道，平春分点。

北天极除了这种有规律的长周围的运动外，在天体力各种天体力的影响下，还存在有短周期的变化，他叠加在岁差运动上，使得瞬时北天极（真北天极）绕瞬时平北天极（真北天极）旋转，大致行程椭圆轨迹（叠加起来便类似正弦轨迹），称之为章动。

**只考虑岁差为平，考虑章动为真**。

![](https://pic1.zhimg.com/80/v2-6d0118c59d214d7cadbdda37fbafcefc_720w.jpg)

> 春分点的漂移方向和章动影响

以上两种天球坐标系都是动坐标系，它们相差一个章动角，并非静止的惯性坐标系。为此需要建立一个指向保持稳定不变的天球坐标系，用它来代表惯性坐标系，这就是人为定义的协议天球坐标系，以 2001 年 1 月 15 日时的指向为标准历元。

### 地球坐标系
然而实际上，由于地球内部存在着复杂的物质运动，地球并非刚体，北地极在地球表面随着时间的变化而不断变化，这种现象称为地球极移（极移）。

为此在一系列瞬时地球坐标系中人为定义了一个特殊地球坐标系（协议地球坐标系），使其 Z 轴朝向某一固定的基准点，它随地球自转，在地球球体中的指向不再随时间而变化。

有了地心和极轴，再靠零度经线和赤道的交点定义出另一条轴，则可以建立地心地固坐标系（ECEF），然后根据测定的地球海拔高度的测量，建立世界大地测量系统（WGS-84，或者 更适合各地的 datum，如 IGS，推荐 epsg 网站可以了解更多 datum），球坐标式的表达则是我们熟悉的经纬高（高度的定义也取决于使用的 datum），然后变换到地面某一点为原心则是站心坐标系（ENU / NED）。

用不同的方式将地球投影到一张平面图上，可得到不同投影展开的平面地图（比如等角正切方位投影，等积斜切方位投影，等距正割圆锥投影，等积正割圆锥投影，等角正割圆锥投影，等角正切圆柱投影 Mercator Projection，等角横切椭圆柱投影， UTM 投影等）。

![](https://pic4.zhimg.com/80/v2-580373d3f6fa3cd66b016706613ea4e7_720w.jpg)

> *各种常见地图投影方式*

地心地固坐标系、站心坐标系和墨卡托投影、UTM 地图投影详情可以参考之前写的高精度地图（一）——地理坐标系。

## 时间系统

前述各种天球坐标系和地球坐标系的给定，无不和时间瞬时相关，卫星的位置在过程中是变化的。并且 GPS 定位是通过接收机接收的信号，测定卫星到接收机的信号传播时间，来确定接收机到卫星的距离，进而确定接收机的位置。因此在给定卫星的位置坐标时，必须给出相应的瞬时时刻。

一般来说时间参考系统的物理实现，必须具有可观测的周期运动，这种周期运动应具备连续性稳定性和复现性，三者缺一不可。在实践中所选择的周期运动现象不同，便产生了不同的时间系统。

### 恒星时、平太阳时、世界时

**恒星时**的原点定义为春分点通过本地子午圈的瞬时。而春分点有真春分点，和平春分点之别，相应的也就有了真恒星时和平恒星时之分。

**平太阳时**的原点定义为平太阳通过观察者所在子午圈的瞬时。

由于平太阳时的地方性，地球上不同经纬圈上的平太阳时各不相同，地球上零经度子午圈（格林尼治子午圈）所对应的平太阳时，且以平子夜为零时起算的时间系统成为**世界时**。

### 原子时、协调世界时、GPS 时

现代物理学发现物质内部原子的跃迁所辐射或吸收的电磁波频率具有极高的稳定性和复现性。所以根据这一物理现象所建立的原子时，便成为了当代所理想的时间系统。

原子时的秒长比世界时的秒长略短，这就是原子时比世界时每年约快一秒多。两者之差逐年积累，为了避免原子时与世界时之间产生过大的偏差，同时又要使两种时间系统同时并存，就有必要建立一种兼有两种时间系统各自优点的新的时间，这就是从 1972 年起所采用的协调世界时。

全球定位系统为了满足精密定位与导航的需要，在系统设计与试验之初就建立了自己专用的时间系统 GPS 时，它由 GPS 主控站的高精度原子钟守时与授时。 GPST 属于原子时系统，它的秒长即为原子时秒长，GPS 的原点与国际原子时相差固定秒数。

实际上 GPS 时由于设备内存问题，会周期性进行重置，时间计数器最多只能向前计数 1024 周，即大约 19.7 年。 经过 1024 周后，此计数器会进行重置，GPS 时间将重新开始向前计数。第一次重置发生在 1999 年 8 月。 第二次重置发生在 2019 年 4 月 6 日。

### Unix 时间戳

而用户的计算机设备通常也会包含 Unix 时间戳，Unix 时间戳是从 1970 年 1 月 1 日（UTC/GMT 的午夜）开始所经过的秒数，不考虑闰秒。在大多数的 Unix 系统中 Unix 时间戳存储为 32 位，这样会引发 2038 年问题。

---

# GNSS 介绍

## 发展

### GPS
GPS 是军民合用的系统，但它针对军用和民用提供了不同的定位精度。军用为 3 米，民用信号增加了干扰机制，使精度下降到 100 米。鉴于 GPS 在民用中发挥越来越重要的作用，美国政府 2000 年初取消了 GPS 的干扰机制，使民用信号的精度提高了 10 倍以上，大大方便了民用用户的使用，也为 GPS 的普及奠定了基础。

为了更好地进行国际间的兼容和 交互操作，实现全球民用卫星导航系统的无缝隙连接，美国第三阶段发射的卫星，附加 GPS 第四个民用信号 L1C，该信号能够与伽利略公开服务信号互操作，并与日本准天顶系统（Qzss）共用。

### Beidou

第一代北斗系统由三颗卫星提供区域定位服务。从 2000 年开始，该系统主要在中国境内提供导航服务。2012 年 12 月，北斗一号的最后一颗卫星寿命到期，试验系统停止运作。

北斗二号系统是一个包含 16 颗卫星的全球卫星导航系统，分别为 6 颗静止轨道卫星、6 颗倾斜地球同步轨道卫星、4 颗中地球轨道卫星。

2012 年 11 月，第二代北斗系统开始在亚太地区为用户提供区域定位服务。由三种不同轨道的卫星组成，包括 24 颗地球中圆轨道卫星（覆盖全球），3 颗倾斜地球同步轨道卫星（覆盖亚太大部分地区）和 3 颗地球静止轨道卫星（覆盖中国）。北斗三号系统于 2020 年 7 月 31 日开通。

我国的北斗系统采用三频信号向用户广播导航数据。三频信号可以更好地消除高阶电离层延迟影响，提高定位可靠性，增强数据预处理能力，大大提高模糊度的固定效率。而且如果一个频率信号出现问题，可使用传统方法利用另外两个频率进行定位，提高了定位的可靠性和抗干扰能力。

北斗卫星导航的短报文通信服务 也是一项实用性很强的原创功能。这一特色功能也是有容量限制的，所以并不适合日常通信功能，而是作为紧急情况通信比较合适，作为求救使用。

### Glonass

俄罗斯的格洛纳斯卫星采用频分多址技术，这是与其他主要导航系统明显的一个区别。所有的格洛纳斯卫星都发射同样的伪随机码，但采用不同的频率发射。具有某些抗干扰和抗互相关的特性，以及更简单的选码判据，可以防止整个卫星导航系统同时被敌方干扰，因而具有更强的抗干扰能力。频分多址技术的缺陷就是用户接收机的体积大而且造价昂贵，应用普及度还远不及 GPS，主要是因为俄罗斯长期以来不够重视开发民用市场。

格洛纳斯有两种导航电文，S 码电文和 P 码保密电文，两种电文的速率都是 50 位每秒。主要用途是提供卫星星历和频道分配方面的信息。

格洛纳斯所用的坐标系是 1990 年苏联所制定的 PZ-90 参考坐标系，与 GPS 所用的 WGS-84 也不相同。GPS 系统时与世界标准时间 UTC 相关联，而 GLONASS 则与莫斯科标准时间 UTC+3 相关联，除了存在跳秒外，与 GPS 时间之间还有数十纳秒的差异。

### Galileo

欧盟的伽利略系统采用了与 GPS 类似的码分多址技术来区别不同的卫星。为了提供更多的服务，伽利略信号结构比 GPS 的民用码信号复杂，其信号传输速率从 50 位每秒到 1000 位每秒不等。伽利略系统提供含有测距码和数据信息的导航信号，测距码由每颗卫星上的高稳定度星钟产生，数据信息则由地面上行注入站向卫星发送。导航电文的内容包括星钟、星历、识别码和状态标识等，以及能使用户预测星钟和星历精度的“空间精度信息”。

## 组成

### 一、地面监控部分

GPS 地面监控部分主要由分布在全球的 1 个主控站，4 个注入站和 6 个监测站组成。

![](https://pic4.zhimg.com/80/v2-97e839070657b228c9942f8e67128e63_720w.jpg)

> GPS 地面监控部分的分布


地面监控部分部分数据流动为：卫星运行-> 监测站观测 -> 主控站计算 -> 注入站注入 -> 卫星得知星历（广播给地面接收机）

#### 地面监测站

监测站是在主控站控制下的一个数据自动采集中心，其主要装置包括 GPS 双频接收机、高精度原子钟、计算机、环境数据传感器等。

监测站的主要任务是通过接收机对 GPS 卫星进行连续观测和数据采集，收集积分多普勒观测值、卫星时钟、工作状态数据等数据。同时通过环境传感器采集有关当地的气象数据，传送给主控站。

#### 主控站
负责协调和控制地面监控部分的工作，通过接收、处理所有监测站传来的数据，计算卫星星历、时钟修正、状态数据、信号电离层延迟修正等，编算导航电文并传送到注入站，诊断卫星状态，调度卫星。

坐落于美国科罗拉多州 Falcon 空军基地的主控站是地面监控部分，甚至整个 GPS 的核心。具体实现以下功能：

1. 采集数据、推算编制导航电文。采集监测站所测的伪距和积分多普勒观测值、气象参数、卫星时钟、卫星工作状态、各监测站工作状态参数、根据搜集的全部数据，推算各个卫星的星历、卫星钟差改正数、状态数据以及大气改正数、传送到注入站注入。
2. 给定全球定位系统时间基准。计算各个卫星的钟差，以确保各颗卫星的原子钟与主控站的原子钟同步，维护 GPS 的时间基准；
3. 协调管理所有地面监测站和注入站系统，诊断所有地面支撑系统和天空卫星的健康状况，并加以编码向用户指示。
4. 调整卫星运动状态，启动备用卫星。根据观测到的卫星轨道参数以及卫星姿态参数，发生偏离时发出调整卫星轨道的控制命令，确保卫星沿预定的轨道和正确姿态运行；监视卫星是否工作正常，并在卫星出现故障、失效的情况下启动备用卫星。

#### 地面注入站

导航卫星注入站是指向在轨运行导航卫星注入导航电文和控制指令的地面无线电发射站，是导航卫星系统地面运行控制的组成部分。注入站的主要设备报考一套直径 3.6m 的天线，一台 C 波段发射机和计算机。

注入站接收主控站送来的导航电文和卫星控制指令，经射频链路上行发送给各导航卫星。

导航电文通常包括预报的卫星轨道参数（即卫星星历表）、卫星时钟偏差参数以及轨道和钟差的改正参数等。

卫星控制指令通常包括有效载荷控制指令和卫星平台控制指令。

### 二、空间星座部分

GPS 空间卫星星座，比如保证在地球各处能同时观测到高度角为 15° 以上的至少 4 颗卫星。GPS 全球定位系统的空间星座由 24 颗工作卫星构成，其中 3 颗为备用卫星，部署在 6 个轨道平面，平均高度约为 202002km，运行周期为 11h58min。

卫星主体呈柱形，星体两侧装有两块双叶向日定向太阳能帆板，全场 5.33m，接收日光面积为 7.2m²，以保证卫星正常工作用电。

星体底部装有多波束定向天线，其波束方向图能覆盖约半个地球。星体两端面上装有全遥测遥控天线，用于与地面监控网通信，还装有姿态控制系统和轨道控制系统。

核心设备是高精度铯原子钟（稳定度 10^-14~10^-14），为 GPS 提供高精度的时间标准。

GPS 卫星采用多种编号识别系统，在导航定位种通常采用 PRN 编号（伪随机噪声码 pseudo random noise code）

![](https://pic4.zhimg.com/80/v2-9d0c972fd6d730006df7f0e8097af347_720w.jpg)

> 卫星星座轨道分布

### 三、用户设备部分

GPS 接收机部分主要由接收机硬件（主机、天线、电源）、数据处理软件、微处理机和终端设备组成。

空间星座部分和地面监控部分为卫星确定了准确位置，然后需要多颗卫星广播给用户自身信息，用户通过 GPS 接收机接收到多颗的卫星轨道信息（相当于用多个卫星建立了一个坐标系）和时间（计算出到各个卫星的距离），于是用户就知道了用户相对于卫星星座的位置，而卫星星座相对于地球的位置是已知的，所以就能知道用户在地球的具体位置。

信号接收处理单元是 GPS 接收机的核心单元，接收来自天线的信号，经过中频放大，滤波和信号处理，实现对信号的跟踪、锁定、测量，由跟踪环路重建载波解码得广播电文并获得伪距定位信息。根据需要，GPS 接收机可以设计成 1~12 个通道供选择，每一个通道在某一时刻跟踪一颗卫星，当次卫星被锁定时，便占据这一通道。现已广泛采用并行多通道技术或同时相关型通道技术。

## 性能

衡量用户使用 GPS 时的性能，主要参考以下指标。

准确性：准确性用来衡量定位结果与目标的真实相接近的程度，是定位结果与真实位置值的差异，而精度可以理解为重复性。列入对于静态定位而言，若接收机的多次定位结果基本集中于一点，则说定位精度很高，尽管可能偏离真实值一定距离。

正直性（可靠性、完整性）：定位系统在出现故障时能及时警告用户，以免用户被非正常工作的定位系统所误导。

连续性：系统在一段时间内能连续地同时满足所规定的准确性和正直性要去的概率。

有效性：定位系统能同时满足准确性、正直性和连续性要求的时间百分比。

首次定位所需时间：接收机启动后到获得第一个定位结果所需要经历的时间；

灵敏度：衡量接收机能接收到多弱的 GPS 信号。

城市峡谷中的性能：在城市峡谷中时，接收机在一定时段能实现定位的个数与该时段内总的定位历元数之比成为定位有效率。

---

# 原理

## 星历数据

描述任意时刻卫星在空间的位置的一组参数称为卫星星历。 GPS 卫星在空间的瞬时位置作为已知参数，以星历的方式，在卫星绕地球运行的过程中，连续不断的向地球地面用户播发，用户通过测量对卫星的相对距离，进而确定自己在地球上的位置实现高精度的定位和导航。

为了理解和运用 GPS 卫星的轨道信息，需要了解有关卫星的运动规律，轨道的描述，以及卫星位置的计算。而卫星的运动规律和轨道描述为天体物理学开普勒三大定律相关的知识，具体可以参考 [GPS 定位笔记 4 (轨道理论和星历和历书)](https://zhuanlan.zhihu.com/p/111325516)， 在此不做展开。

利用 GPS 进行导航和定位就是根据 GPS 卫星发布的卫星轨迹信息，结合用户的观测资料，通过数据处理来确定用户的位置，速度乃至姿态等参数，所以星历（精确描述轨道的一组参数）是实现精确定位与导航的基础，GPS 卫星星历的提供方式一般有两种，一种是预报星历（广播星历），另一种为后处理星历（精密星历）。

预报星历是一组这样的数据，它包含相对于某一参考历元的开普勒轨道参数和必要的轨道摄动改正项参数。 GPS 卫星的广播星历更新频率很快，每小时就发布一组最新的星历。

广播星历一共有 16 个星历参数，其中包含一个参考历元，6 个相应于参考历元的开普勒椭圆轨道参数，和 9 个反应摄动力影响的改正项参数。

![](https://pic4.zhimg.com/80/v2-0169db5c8c04c4658acfab8fe7b332c3_720w.jpg)

> GPS 卫星轨道参数示意图

- 参考时刻的平近点角 $M_{so}$
- 平均运行速度差 $\Delta n$
- 轨道偏心率 $e$
- 轨道长半轴的方根 $\sqrt{a_s}$
- 参考时刻的升交点赤经度 $\Omega_0$
- 参考时刻的轨道倾角 $i_0$
- 近地点角距 $\omega$
- 升交点赤经变率 $\dot{\Omega}$
- 轨道倾角变率 $\dot{i}$
- 升交距角的调和改正项振幅 $C_{uc}, C_{us}$
- 卫星地心距的调和改正项振幅 $C_{rc}, C_{rs}$
- 轨道倾角的调和改正项振幅 $C_{ic}, C_{is}$
- 星历参数的参考历元 $t_{oe}$
- 星历数据的龄限 $AODE$

为了满足大地测量学和地球动力学，对高精密度定位的要求，需要精确地刻画某时刻的卫星轨道参数，即后处理星历。后处理星历是一些国家的有关部门根据各自建立的 GPS 卫星跟踪站所获得的 GPS 卫星精密观测资料，采用确定预报星历相似的方法，计算出以前任意观测时刻的卫星星历。它是一种根据观测资料事后计算的时间和星历对应的精密轨道信息库。

## 卫星信号

用户 GPS 接收机接收到的 GPS 卫星广播的信号，测定由卫星到接收机的信号传播时间延迟，或测定卫星载波信号相位在传播路径上变化的周数解算出由接收机到卫星之间的距离（应含误差，而被称为伪距），从而确定 GPS 接收机的位置和时间改正数。

GPS 卫星播发的信号包含三种成分，即数据码、测距码和载波信号。数据码中包含多种与导航有关的信息，这些信息是卫星的星历，卫星钟差改正数，测距时间标志及大气折射改正参数，以及由 C/A 码捕获 P 码得到的其他导航信息，这些信息为 GPS 导航定位提供数据基础，故又称为导航电文。

![](https://pic1.zhimg.com/80/v2-1c3ff84e007910417c2ac299a85c636c_720w.jpg)

> *GPS 卫星信号示意图*

GPS 卫星信号采用了组合码调制技术，即将编码脉冲（即导航电文或者基带信号）先调制到伪随机码，即经过伪随机码扩频成为组合码，再对 L 波段进行双向调制，然后由 GPS 卫星天线发射出去，使用两个载波频率发射，是为了对大气层效应产生的附加延时进行双频矫正。


![](https://pic2.zhimg.com/80/v2-950d78ea639debdb139c18edd8510439_720w.jpg)

> *GPS 发射信号构成原理图*

## 导航电文

导航电文是二进制编码文件，按规定格式组成数据帧，按帧向外播放，每帧电文含有 1500bit，播送速度是每秒 50bit，所以一帧电文的播放时间是 30 秒。

每帧电文还有 5 个子帧，每个子帧含有 10 个字，每个字为 30bit，所以每一子帧共含有 300bit，按上述比特率 50bit/s 速度播发，每幅子帧需播放 6 秒。

![](https://pic3.zhimg.com/80/v2-43e0c9e36341f565bdcb90dd3a8b36c2_720w.jpg)

> *导航电文格式*

第 1、2、3 子帧中含有该卫星的广播星历和卫星星钟修正参数，每小时更新一次，第 4、5 子帧中存放所有空中 GPS 卫星的历书，信息量比较庞大，故子帧 4、5 各含 25 页。4、5 子帧是空中全部 GPS 卫星的历书，它的内容仅在地面注入站注入新的导航数据后才更新，现也有技术根据设备接入互联网网络获取附近基站拿到过的所有卫星历书。

![](https://pic2.zhimg.com/80/v2-774a1f048cf51d94c79c9e3d618e2869_720w.jpg)

> *导航电文的内容*

- 遥测字 TeLemetry Word：包含捕获信息的前导，遥测电文（地面监控系统注入数据的状态信息、诊断信息和其他），指示用户是否选用该卫星。
- 转换字 How-hand Over Word：提供用于捕获 P 码的 Z 计数（从每周六-周日子夜零时起算的时间计数），可以实时了解观测瞬时在 P 码周期中所处的准确位置，预先确定码的移动量，使本机产生的伪随机码的码元与即将到来的卫星信号 P 码码元相匹配。
- 数据块 1：卫星时间计数器 WN，调制码标识（C/A 或 P），卫星测距精度 URA，数据是否正常，电离层延迟改正参数，时钟数据龄期，卫星时钟参数对应的参考时刻，卫星钟改正参数。
- 数据块 2：开普勒六参数，轨道摄动九参数，卫星星历参考时刻，广播星历外推时间间隙。
- 数据块 3：全部 GPS 卫星星历概略模式，健康状况和 GPS 星期编号，方便用户利用码分址较快的捕获其他合适的卫星信号。

## 坐标计算方式

用户的 GPS 接收机收到轨道信息轨道参数后，计算出卫星在地球坐标系中的位置，然后地球 GPS 接收机通过测码伪码或测相伪距的处理方式，实时测量卫星到用户的距离。由于存在卫星和接收机时间不完全同步，且载波信号受到电离层和对流层的折射影响，所以测得的距离称为伪距。

于是利用 GPS 进行定位，在几何意义上的解释就显得非常简单清晰，GPS 卫星在地球坐标系中的位置坐标已知。

比如 $(x_i,y_i, z_i)$ 为卫星 i 在协议地球坐标系中的位置，而我们测得的到卫星 i 的距离为 $\rho_i(\Delta t)= \sqrt{(x-x_i)^2 + (y-y_i)^2 + (z-z_i)^2 }$

而接收机又收到了四颗卫星便能联立解方程组，解得关于三维坐标和用户钟差的方程。

- 测码伪距观测量：测量 GPS 卫星发射的测距码信号到达用户接收机天线的电波传播时间。因此这种观测方法也称为时间延迟测量。
- 测相伪距观测量：卫星载波信号由发射到被接收，其间载波信号传播的相位称为载波相位观测量（测相伪距观测量）。由于载波频率高波长短，所以载波相位测量精度高。
- 开普勒积分计数伪距差： 卫星相对于地面的 GPS 接收机存在着相对运动，因此接收到的信号中存在着多普勒平移。利用多普勒平移测得相对距离。
- 干涉法测量时间延迟：目前广泛采用前两种（码相位观测量和载波相位观测量）进行定位测量，第 3 种多普勒积分计数法静态定位需要数小时的观测时间，一般应用于大地测量之中，在动态应用中多普勒测量，可用来计算测站的运动速度。而用最后一种干涉法测量时所需的设备相当昂贵，数据处理也十分复杂，它的广泛应用上待进一步的研究开发。

## 误差影响与消除

### 卫星星历误差

由于卫星在空中运行受到多种摄动力影响，地面监测站难以充分可靠的测定这些摄动力的影响，使得测定的卫星轨道会有误差。

同时监测系统的质量，如跟踪站的数量及空间分布轨道参数等的数量和精度轨道计算时，所用的轨道模型及定轨软件的完善程度，应会导致星历误差。

此外用户得到的卫星星历并非是实时的，而是由 GPS 用户接收的导航电文中对应于某一时刻的星历参数而推算出来的，由此也会导致计算卫星位置产生误差。

为了尽可能削弱星历误差，对定位的影响一般常采用同步观测求差法（卫星星历误差对相距不太远的两个测站的定位影响大致相同，因此采用两个或者多个近距离的观测站对同一个卫星进行同步观测，然后求差）或轨道改进法（在数据处理中引入表示表述卫星轨道偏差的改正数，并假设在短时间内这些改正参数为常量，并将其作为待求解量与其他位置参数一并求解，从而较正星历误差）。

### 卫星时钟误差

卫星上使用高精度的原子钟，但由于这些钟与 GPS 标准时之间会存在着随时间变化的频偏频飘，导致星钟和 GPS 标准时之间的不同步偏差。主要通过接收机对星钟误差，进行二项式拟合求解来进行消除。

### 电离层误差

电离层的折射率与大气电子密度成正比，和穿过的电磁波频率平方成反比，对于频率确定的电磁波而言，电离层折射率仅取决于电子密度。 电离层的电子密度随太阳及其他天体的辐射强度，季节，时间，以及地理位置等因素的变化而变化。

为了减弱电离层的影响，在 GPS 定位中通常采用以下措施，
1. 利用双频观测加以修正。
2. 利用电离层模型加以修正。
3. 利用同步观测值求差。

### 对流层误差

对流层与地面接触，并从地面得到辐射热能，其温度一般随将，除了与高度变化有关外对流层的折射率与大气压力，湿度和温度密切相关。减少对流程折射，对电磁波延迟影响的措施主要为：
1. 当基线较短时气象条件稳定，两个测站的气象条件相似，利用基线两端同步观测量求差，可以有效的减弱甚至消除大气层折射影响。
2. 利用在观测站附近实测的地区气象资料，完善对流层大气改正模型，可以减少对流层对电磁波延迟的影响的 90%。

### 多路径

多路径效应通常也叫做多路径误差，接收机存在接收到卫星发射的信号外，尚可能收到天线周边建筑物或者水面的一次或多次反射的卫星信号，这些信号叠加起来会引起测量参考点位置的变化，从而使观测量发生误差。

反射波除了存在相位延迟外，信号强度一般也会减小，其原因是一部分能量被反射面所吸收，同时由于反射面会改变波的极化特性，而**接收天线为右旋圆极化天线**对于改变了极化特性的反射波，存在着抑制作用。

多路径误差取决于反射物距测站的距离和反射系数，以及卫星信号的方向等条件因素，无法建立起准确的误差改正模型，只能改善环境或者选择造型适宜屏蔽良好的天线，或者延长观测时间，改善接收机电路设计。

### 接收机噪声

天线观测误差、接收机钟差、天线相位中心的的位置偏差、载波相位观测整周期未知数、地球自转、相对论效应。

### 精度码

GPS 的精度级别分为两种：

- SPS（Standard Position System 标准定位系统）：最常见的定位系统，水平方向精度为 30 米，使用 C/A 码。
- PPS（Precis Position System 精密定位系统）：过去只提供给军事或国家使用，使用 P 码，精度达水平 15 米，垂直 27.7 米。

民用通常只是 SPS，使用粗码 （C/A 码），指定单位设备可使用 PPS，更甚至可以接入 RTK 差分服务。

![](https://pic4.zhimg.com/80/v2-01d70b1cb758da0130d80f0b66c86baf_720w.jpg)

> 测码伪距测量误差 (URE)


### 差分定位 Differential GPS

是首先利用已知精确三维坐标的差分 GPS 基准站，求得伪距修正量或位置修正量，再将这个修正量实时或事后发送给用户，对用户的测量数据进行修正，以提高 GPS 定位准确度。

![](https://pic3.zhimg.com/80/v2-ee6705780a39b6e5b6fa398c07df945e_720w.jpg)

> *差分定位示意图：卫星，基准站，移动站*


根据差分 GPS 基准站发送的信息方式可将差分 GPS 定位分为三类，即：**位置差分、伪距差分和相位差分**。 这三类差分方式的工作原理是相同的，即都是由基准站发送改正数，不同的是，发送改正数的具体内容不一样，其差分定位精度也不同。

1. 位置差分：

最简单的差分方法，由于存在着轨道误差、时钟误差、SA 影响、大气影响以及其他误差，接收机解算出的坐标与基准站的已知坐标是不一样的， 存在误差。基准站利用网络将此改正数发送出去，由用户站接收，并且对其解算的用户站坐标进行改正。

最后用户坐标已消去了基准站和用户站的共同误差，例如卫星轨道误差、 SA 影响、大气影响等，提高定位精度。适用于基准站和用户站观测同一组卫星的情况，用户与基准站间距离在 100km 以内的情况。

2. 伪距差分：

伪距差分是用途最广的一种技术。几乎所有的商用差分 GPS 接收机均采用这种技术。基准站的接收机知道自身的精确位置，便可知到卫星的距离，并将此计算出的距离与含有误差的测量值加以比较。然后将所有卫星的测距误差传输给用户，用户用来改正测量的伪距。

与位置差分相似，伪距差分能将两站公共误差抵消，但随着用户到基准站距离的增加又出现了系统误差，这种误差用任何差分法都是不能消除的。用户和基准站之间的距离对精度有决定性影响。

3. 相位差分：

载波相位差分技术又称为 RTK 技术（Real Time Kinematic），是建立在实时处理两个测站的载波相位基础上的。它能实时提供观测点的三维坐标，并达到厘米级的高精度。

基准站通过网络实时将其载波观测量及站坐标信息一同传送给用户站。用户站接收 GPS 卫星的载波相位与来自基准站的载波相位，并组成相位差分观测值进行实时处理，能实时给出厘米级的定位结果。

实现载波相位差分 GPS 的方法分为两类：修正法：与伪距差分相同，基准站将载波相位修正量发送给用户站，以改正其载波相位，然后求解坐标。差分法：将基准站采集的载波相位发送给用户台进行求差解算坐标。前者为准 RTK 技术，后者为真正的 RTK 技术。



# Reference

以上内容参考自

- 《GPS 原理与接收机设计》-谢钢-电子工业出版社
- 《GPS 导航原理与应用》-王惠南-科学出版社
- [GPS 定位技术 - 李理的博客](http://fancyerii.github.io/2020/04/06/gps/)
- [知乎专栏文章：GPS 定位笔记 4 (轨道理论和星历和历书)](https://zhuanlan.zhihu.com/p/111325516)
- [牛老师的集思空间：地图投影介绍](https://my.oschina.net/lzugis15/blog/4799507)


---

欢迎在我的专栏「[自律走行](https://www.zhihu.com/column/jiritsu-soko)」中查看更多「走进自动驾驶传感器」系列文章

- [走进自动驾驶传感器（一）——激光雷达](https://zhuanlan.zhihu.com/p/139350599)
- [走进自动驾驶传感器（二）——毫米波雷达](https://zhuanlan.zhihu.com/p/346374177)
- [走进自动驾驶传感器（三）——卫星导航系统](https://zhuanlan.zhihu.com/p/157925827)