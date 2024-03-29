---
title: 聚焦激光雷达（二）——激光器
date: 2023-03-28 21:00:00
categories: tech
tags: 
- lidar
- sensor
toc: true
---

之前我们讲述了激光雷达扫描器件的原理，而作为激光雷达的发射器，我查阅了很多教材、论文、厂家说明文档、行研报告和科普文，发现没有一篇写得比较系统的科普文章，因为并没有找到读到一篇就能讲透的文。教材讲得很深入，但不同教材侧重点又不同，为了深入剖析激光雷达，梳理我自己的知识系统而写本篇。如有问题，请各位不吝指正。欢迎点赞关注后再收藏。

<!-- more -->


# 激光器原理

所有激光器都包含以下三个组件：1、泵浦源；2、受激介质；3、谐振腔。

受激介质位于激光器内部，取决于不同的激光器结构设计，受激介质是一种包含可将激发光的能量转换为激光的原子的物质，可能是气体混合物 、固体晶体棒或玻璃纤维。激光介质在获得泵浦源从外部获得的能量供给时，受激产生能量辐射。

被激发的介质位于谐振腔两端两个镜子的中间位置，其中一个镜子是半透半反镜，受激介质产生的能量辐射在谐振腔内放大，与此同时，只有特定的辐射光能够穿过单向透镜，形成一束辐射光，这一辐射光束即是激光。

![](https://pic3.zhimg.com/80/v2-7f61cfedc95f473941c343bbcf1043de_1440w.webp)

> 激光的原理

---

# 泵浦源

泵浦源的作用是对增益介质进行激励使其辐射发光。具体而言，泵浦源提供能量激励原子跃迁到高能级，以实现粒子数反转（使高能态粒子数多于低能态粒子数），被激发的粒子会自发对外辐射激光从而由高能级向下跃迁，回到稳定形态。

激光的产生应满足两个基本条件：有较好的发光效率；泵浦源的光谱分布与激光增益介质的吸收光谱相匹配。常见的有以下 4 种:光学激励(光泵浦)、气体放电激励、化学激励、核能激励。

- 光学激励：利用外界光源发出的光来辐照激光工作物质以实现粒子数反转的，整个激励装置，通常是由气体放电光源(如氙灯、氨灯)和聚光器组成。如固体激光器等。
- 放电激励：对于气体激光工作物质，通常是将气体密封在细玻璃管内,在其两端加电压,通过气体放电的方法来进行激励，整个激励装置通常由放电电极和放电电源组成。如惰性气体放电灯（灯内充入氙、氪等惰性气体）、金属蒸气灯（灯内充入汞、钠、铒等金属蒸气）、卤化物灯（碘钨灯、镊钨灯、半导体激光器等。
- 化学激励：化学激励是利用在激光工作物质内部发生的化学反应过程来实现粒子数反转的，通常要求有适当的化学反应物和相应的引发措施。
- 核能激励：核能激励是利用小型核裂变反应所产生的裂变碎片、高能粒子或放射线来激励激光工作物质并实现粒子数反转的。


半导体泵浦源单元器件的主要封装形式包括单管（单发射腔）、bar 条。单元器件的综合特性决定了最终泵浦源模块的输出光功率、转换效率以及体积等。单管只有一个发光区，是将激光芯片封装后形成的发光单元，通常在 3~300μm。 bar 条可以看做是多个半导体单管并排在同一衬底上形成的激光器单条，通常 1cm 长，泵浦功率更高。

![](https://pic1.zhimg.com/80/v2-7c79b8c51677b9ee01c9571addbf78c0_1440w.webp)

通过光束整形和传输，耦合成具有各种不同泵浦光功率密度、光束传输模式、光斑形状和光强分布的泵浦源，进一步，bar 条按排列形式，耦合成具有各种不同泵浦光功率密度、光束传输模式、光斑形状和光强分布的泵浦源。

由于半导体激光器叠阵工作时会产生大量的废热，因此必须采用冷却手段降低器件温度，防止温度过高导致激光器失效和使用寿命缩短。目前主要有两种冷却方式：帕尔贴形开放式制冷以及水等高效载冷剂方式。具体采用哪种散热制冷方式应该根据器件的输出功率、工作环境和应用方式确定。

提高半导体激光泵浦源单元器件输出功率和转换效率的方法主要从芯片结构上采用大光腔外延结构、宽条形结构、腔面钝化、增加腔长等措施，同时提高激光器的材料生长质量和优化散热封装技术也是关键。

---

# 媒质

被泵浦源激发，然后发光的物质，其物理特性会影响所产生激光的波长等特性。

## 气体激光

![](https://pic1.zhimg.com/80/v2-a0d3f5030f07da3b7f3d697d165a3778_1440w.webp)

$CO_2$ 激光是以 $CO_2$ 气体为媒质的激光。在填充有 $CO_2$ 气体的管内，配置电极板，以产生放电。电极板连接外部电源，使其可投入高频率电力作为激发源。因电极间放电而在气体中产生等离子体， $CO_2$ 分子会变换为激发态，该数量增加后开始受激辐射。此外，为了让光往返而产生振荡，相对设置一对镜面，则构成了谐振腔。光会在全反射镜和输出镜之间往返，放大后输出为激光。振荡波长一般为 10.6μm。气体成分构成为 $CO_2$ 在 10% 以下、氮 $N_2$ 在 30% 左右、氙 $Xe$ 在百分之几、其余为氦 $He$ 。各气体有其各自的功能，根据构造和激光的特性不同而改变成分。

## 固体激光

固体激光器基本上都是由工作物质、泵浦系统、谐振腔和冷却、滤光系统构成的。

![](https://pic3.zhimg.com/80/v2-9e2ac31a03174fc370772f575c138d56_1440w.webp)

固体激光工作物质是绝缘晶体，一般都采用光泵浦激励。目前的泵浦光源多为工作于弧光放电状态的惰性气体放电灯，泵浦灯在空间的辐射都是全方位的，因而固体工作物质一般都加工成圆柱棒形状，所以为了将泵浦灯发出的光能完全聚到工作物质上，必须采用聚光腔。固体激光器的泵浦系统还要冷却和滤光，也有使用激光二极管作为光泵浦的。

![](https://pic2.zhimg.com/80/v2-71076b30e992a561c19e979b080ea101_1440w.webp)

> YAG 激光器和 YVO4 激光器

## 半导体激光

![](https://pic4.zhimg.com/80/v2-d065ce0c890c7b79b5cc827e48661e8b_1440w.webp)

> 半导体激光器的典型 EEL 结构

可以看到，它是一个半导体 PN 结二极管。因此半导体激光器也被称为激光二极管 （Laser Diode, LD）。有源区 Active Region 是一层薄的光波导芯层 ，厚度通常小于 1μm。上下两侧为折射率较低的波导包层 Cladding，分别为 P 型和 N 型半导体。激活区左右两侧为掩埋层 Burying，其作用是限制激活区的条宽 ，以降低工作电流。通常基横模 LD 的条宽仅为 2~5ｍｍ。经典的 FP 型激光器反射镜面由半导体晶体的解理面构成，典型腔长仅为 0.5mm ，芯片典型宽度仅为 0.3~0.5mm。芯片两面制备了减小接触电阻的金属层，即欧姆接触层 Ω Contact 。当电流从 P 面注入二极管时，就可以从它的解理腔面中发出激光 。可见，半导体激光器具有体积小、重量轻的突出优点。


半导体激光器增益谱很宽，FP 腔没有纵模选择的功能，因而普通的 FP-LD 难以实现单纵模工作。众所周知，光栅的衍射具有优越的选频特性 。人们利用半导体工艺将光栅与半导体激光器的有源区结合在一起 ，研制成功以分布反馈 （Distributed Feedback，DFB）激光器、分布布拉格反射 （Distributed Bragg Reflector, DBR）激光器为代表的单片集成单频激光器 。DFB 激光器具有极好的单纵模工作特性；DBR 激光器在保持单模工作的同时 ，具有大范围的可调谐特性 。 这两种器件在技术上和产品化方面都取得了成功 。根据多层介质膜滤波器的原理和半导体异质结生长技术，人们又研制成功垂直腔面发射激光器 （Vertical Cavity Surface Emitting Laser, VCSEL ）。它不仅具有优越的单频运转特性 ，而且大大改善了输出光束的方向性和调制响应 。



# 光纤激光

光纤激光 Fiber Laser 使用掺杂稀土元素的光纤为媒质，通常以半导体激光器作为能量泵浦源，是长距离通信的中断放大技术发展为高功率输出激光的产物。光纤由中心传输光的核心和以同心圆状包覆核心的金属包层构成。光纤激光以该核心为激光媒质放大光。发射的光不能被硅吸收，因此需要使用铟镓砷 InGaAs 为衬底的接收器。摻杂不同稀土元素的光纤接受泵浦的波长和发射的波长存在差异。

由于光纤激光器的增益介质形状特殊且具有典型的技术和产业优势，行业中一般将其与其他激光器分开进行研究。使用光纤激光器的激光雷达具备优异的探测性能，但由于产业链尚未成熟且制造原材料价格昂贵，在大规模上车前仍需实现大幅降本。

![](https://pic4.zhimg.com/80/v2-9db9c07de84b6915b90c4152a51ce63b_1440w.webp)

> 光纤激光结构示意图

光纤激光通过激光二级管（Seed LD）产生的脉冲光作为种子光源（Seed Light），然后通过多个光纤放大器进行放大。各 LD 为低功率输出，因此具有热负荷较小的优点，实现了长寿命。此外，该 LD 数量越多，越可实现高功率输出的激光。

采用光纤光栅作为谐振腔反射镜，消除了腔镜与光纤介质之间耦合的消耗，实现了激光器核心部件的全光纤集成，提高了激光器的效率及稳定性。同时，光纤光栅可以改变反射性质选择特定频率进行输出，适用性更广泛。

光纤合束器主要作用是进行光束合成增大输出功率。光纤合束器可以分为功率合束器和泵浦合束器。功率合束器将多路单模激光合束到一根光线中输出，以提高激光的输出功率；泵浦合束器主要是将多路泵浦光合束到一根光线中输出，主要用来提高泵浦功率。

光纤激光器种类很多，从光纤结构上可分为单包层光纤激光器、双包层光纤激光器、光子晶体光纤激光器和特种光纤激光器。 从增益介质上可分为塑料光纤激光器、稀土类掺杂光纤激光器、非线性光学型光纤激光器、光纤受激拉曼散射激光器和晶体光纤激光器。 从输出激光特性上可分为连续光纤激光器和脉冲光纤激光器。



具体来看，光纤激光器的优点包括

1. **轻量化及高灵活柔绕性**：光纤体积小且可以弯曲，因此集成时可以通过光纤运输光束以实现灵活安装；
2. **可实现大功率**：光纤的几何形状具有很大的“表面积/体积”比，散热快，可以在更高功率的情况下工作，有效探测距离及精度均会提高；
3. **光束质量高**：光纤的波导结构决定了光纤激光器易于获得单横模输出，且受外界因素影响很小。激光介质本身就是导波介质所以耦合效率高；利于光纤通信系统的应用，同时可借助光纤方向耦合器构成各种柔性谐振腔，使激光器的结构更加紧凑、稳定；光纤还具有相当多的可调谐参数和选择性，能获得相当宽的调谐范围和相当好的色散性和稳定性。

缺点方面，相较于半导体激光器仅需要电激励即可实现直接的电光转换，光纤不能够直接实现电光转换，需要使用半导体激光器作为光泵浦，因此光纤激光器的电光转换效率天然低于半导体激光器。此外，光纤激光器还需要配套使用铟镓砷探测器，这将提升激光雷达的制造成本。

---

# 谐振腔

![](https://pic3.zhimg.com/80/v2-ee44ef09ffc82edef1d626626261bdfa_1440w.webp)

> 谐振腔原理示意图

谐振腔的作用是筛选一定方向光子并进行放大。介质被泵浦源激活后会产生不同方向的光子，传播方向与谐振腔横轴线不同的光子将逃逸出腔体，沿横轴线运动的光子将在腔内往返产生振荡，为把激光引出腔外，其中一面反射光栅为部分反射，透射部分成为发出的激光。反射部分留在腔体内继续振荡，与受激发粒子相遇后发生辐射，不断增殖最终形成传播方向一致、频率和相位相同的发射激光。

## 内腔光反馈法

具有紧凑结构的高功率窄线宽半导体激光器是目前各国研究人员的关注热点，其中 DFB 半导体激光器和 DBR 半导体激光器是实现窄线宽半导体激光器的重要手段。

### 法布里-珀罗型 Fabry-Perot 激光器

![](https://pic3.zhimg.com/80/v2-0df04e472856cfeeef64da9d77f75ede_1440w.webp)

> FP 激光器示意图

法布里-珀罗激光器（FP-LD）是最常见、最普通的半导体激光器，它的谐振腔由半导体材料的两个解理面构成。其反射镜只是激光芯片末端的平面裂开表面，发出多纵模相干光的半导体发光器件，目前光纤通信上采用的 FP-LD 的制作技术已经相当成熟。

![](https://pic1.zhimg.com/80/v2-f529d7a2a3626c31ec850053e97e58b4_1440w.webp)

> FP 激光器 3D 结构示意图

FP-LD 的结构和制作工艺最简单，成本最低，主要适用于 1310/1550nm 波段下的低速率短距离通信，传输距离一般在 20km 以内，存在损耗大、传输距离短的问题。

### 分布反馈式 DFB 激光器

实现动态单纵模工作的最有效的方法之一就是在 FP 激光器的基础上，在半导体内部建立一个光栅滤光器件（布拉格光栅是一种周期性，作为波长选择镜的微结构，光源被注入到光纤后，只有布拉格波长的光会被光栅反射）。DFB 激光器的特点在于光栅分布在整个谐振腔中，光波在反馈的同时获得增益，因此其单色性优于一般的 FP-LD。

![](https://pic2.zhimg.com/80/v2-e12fbb13435f0fc3c8f82c88525ef66d_1440w.webp)

> DFB 激光器示意图

分布反馈激光器通常将布拉格光栅结构分布于整个谐振腔中，其主要起到光反馈选模及增益的作用。主要用于高速中长距离传输。这种激光器具有优越的光谱特性和可高速调制特性等优点，使其广泛应用于高精度探测、光通信等领域。

![](https://pic1.zhimg.com/80/v2-abda8402d1c3b96d02c21f3b809a3654_1440w.webp)

> DFB 激光器 3D 结构示意图

目前 DFB 半导体激光器主要研究在有源区附件构建光栅的二次外延分布反馈(Re-Grown DFB, RG-DFB)激光器，以及在外延芯片 P 面光波导表面或者侧壁直接刻蚀光栅，形成表面光栅分布反馈(Surface Grating DFB, SG-DFB)激光器这两种结构。这两种结构的共同点都是将布拉格光栅结构分布于整个谐振腔中，其主要起到光反馈选模及增益的作用。

### 二次外延分布反馈半导体激光器 RG-DFB

二次外延分布反馈激光器 RG-DFB 激光器通常采用二次外延技术在 N 型或 P 型波导层生长完成后，采用光刻和刻蚀的手段在其 N 型或 P 型波导层上构建一组低折射率光栅结构，之后将芯片放入外延设备中继续完成生长工艺。这种二次外延光栅分布在有源区附近，有利于光栅与光模式场的高效耦合，可有效降低散射损耗，提高耦合效率，实现频率选择和线宽压缩，但是二次外延技术可能引入芯片结构缺陷，影响芯片的可靠性和成品率。

### 表面光栅分布反馈半导体激光器 SG-DFB

SG-DFB 激光器是在外延芯片 P 面光波导表面 (BA-DFB) 或者侧壁 (LC-DFB) 直接刻蚀光栅，形成表面光栅分布反馈半导体激光器，可保证波导内的光模式场与光栅充分耦合反馈，利用散射效应抑制高阶模式，实现波导中单模振荡，SG-DFB 的研制难点是光栅结构的设计与制备，要充分考虑光栅基本参数对激光器性能的影响。



### 分布布拉格反射 DBR 激光器

![](https://pic4.zhimg.com/80/v2-7195119eb3e2f32db95d398e474b7ec7_1440w.webp)

分布布拉格反射激光器的谐振腔由集成于端面的反射光栅结构和增益区构成，其与法布里-珀罗(F-P)腔类似，在增益区的一端或两端构建布拉格光栅，代替 F-P 激光器的一端或者两端腔面反射镜，光栅只相当于一个反射率随波长变化的反射镜，由于光栅结构对满足布拉格条件的光模式具有极强的反射作用，因此可以通过对光栅区的耦合系数进行优化，获得理想的最大反射率和反射谱宽度，实现 DBR 激光器的单纵模、窄线宽工作。

![](https://pic2.zhimg.com/80/v2-a8dd1b0ba4e5bb5d28fcbb9cc947f815_1440w.webp)

> DBR 激光器 3D 结构示意图

目前窄线宽分布布拉格反射半导体激光器主要采用表面布拉格光栅结构作为反射镜实现频率选择作用，通过合理设计光栅结构参数，获得理想的光栅反射率、反射率半宽和光栅中光波相位变化等光电特性，实现窄线宽输出的 DBR 半导体激光器。这种表面 DBR 激光器相比于传统的多次外延 DBR 激光器的优势就是避免了不同区位波导间耦合效率低下的问题，降低了制备工艺复杂程度，提高了 DBR 激光器的应用价值。



## 外腔半导体激光器

基于外腔光反馈技术的窄线宽半导体激光器 (External Cavity Laser，ECL)，是一种采用外部光学元件对半导体激光芯片的出射光进行反馈和选频，增加谐振腔有效长度，提高激光器谐振腔的品质因子 Q 值，降低激光线宽，又因其采用无源光学元件进行频率选择和光反馈，更容易实现低相位噪声和高温度稳定性，是空间相干通信、相干探测、高精度传感等应用领域的理想光源。

ECL 可有效避免内腔集成光栅的光波衍射与散射损耗，但是其对外部光学选频元件耦合光路与工作环境的稳定性要求较高，其中外部光学选频元件作为 ECL 的核心装置，主要包括: 1、采用激光全息技术在特殊光敏玻璃中制作的体全息光栅、体布拉格光栅等衍射光栅元件；2、低损耗 F-P 波导、镀膜反射镜及采用飞秒激光技术加工的光纤光栅波导等波导型反馈元件。

以下两种外腔反馈激光器都是采用外部光反馈元件实现激光频率的选择和线宽的压缩，线宽水平都能达到 kHz 量级。而外腔光栅反馈半导体激光器的优势就是通过调整光栅位置就能实现波长调谐，有效降低半导体激光器线宽，并获得低噪声光谱特性，同时由于光路耦合效率高，更易于实现高功率输出，应用前景更加广阔。

### 外腔光栅反馈半导体激光器

选用衍射光栅作为反馈元件的外腔激光器通常会采用 Littrow 或 Littman 结构，这两种结构外腔激光器的谐振腔通常由半导体激光芯片、光学透镜或反射镜、闪耀光栅或者全息光栅等光学元件构成。

![](https://pic1.zhimg.com/80/v2-483d9b22d1eadd43a7badd5af3eb1460_1440w.webp)

> Littrow 结构和 Littman 结构 外腔半导体激光器结构示意图

Littrow 结构 ECL 通常由半导体芯片、光学透镜和衍射光栅构成，通过改变光栅角度 θ，使某一特定波长光波反馈回半导体激光芯片，大幅提高其余波长光波的衍射损耗，同时改变谐振腔整体长度，实现波长稳定的窄线宽激光输出。在获得窄线宽输出的同时，可获得相对较高的输出功率。除此结构，还有直接采用体(全息/布拉格)光栅作为光反馈元件的外腔激光器。

Littman 结构 ECL 通常由半导体芯片、光学透镜、衍射光栅和**反射镜**构成，其中反射镜起到调谐器作用，光栅固定不动，通过改变反射镜角度，将入射光沿入射光路返回，光波经过光栅二次衍射后，边模抑制比大幅提高，激光线宽进一步窄化，但其结构比 Littrow 结构 ECL 复杂，导致功率损耗大，不易于实现高功率输出。

![](https://pic1.zhimg.com/80/v2-bdf70b8a808b05f6bba0da44b50e75a4_1440w.webp)

> Littrow 结构和 Littman 结构 外腔半导体激光器 3D 结构示意图


### 外腔波导反馈半导体激光器
基于外腔波导反馈技术的窄线宽激光器，主要通过耦合外部低损耗波导或光纤光栅波导，增加激光器谐振腔的长度，提高激光器谐振腔的品质因子 Q 值，达到降低激光器线宽的目的。

![](https://pic4.zhimg.com/80/v2-6d99e653e43e4ea5ad9dcce645582c5f_1440w.webp)

> 外腔波导反馈半导体激光器 3D 结构示意图

## 垂直腔面发射激光器

图为其典型结构图，其上下分别为分布布拉格反射（DBR）介质反射镜，中间（InGaAsN）为量子阱有源区，氧化层有助于形成良好的电流及光场限制结构，电流由 P、N 电极注入，光由箭头方向发出。其激光垂直于顶面射出，与激光由边缘射出的边射型激光有所不同。

![](https://pic4.zhimg.com/80/v2-3d8aa8d37904915e21b915d7eba4e077_1440w.webp)

> VCSEL 结构示意图

它是在由高、低折射率介质材料交替生长成的分布布拉格反射器（DBR）之间连续生长单个或多个量子阱有源区所构成。 典型的量子阱数目为 3~5 个，它们被置于驻波场的最大处附近，以便获得最大的受激辐射效率而进入振荡场。 在底部还镀有金属层以加强下面 DBR 的光反馈作用，激光束从顶部透明窗口输出。

![](https://pic4.zhimg.com/80/v2-700b6b91c71cd0201fc04c5579368aab_1440w.webp)

> VCSEL 3D 结构示意图

因此相较于边射型激光器，VCSEL 激光器具有低阈值电流、稳定单波长工作、可高频调制、容易二维集成、没有腔面阈值损伤等优点，在半导体激光器中占有很重要的地位。

---

# 波长

激光发射器影响激光雷达产品的核心性能。激光器的原理是增益介质（工作物质）通过吸收激励源（泵浦源）的能量而产生光子，通过光学谐振腔的放大形成激光光束。增益介质和光学谐振腔共同决定了所发出激光的波长。对于激光雷达激光器而言，性能上希望激光器实现较高的发射功率密度、较低的温升、较小的温漂系数、以及较高的光束质量等指标，成本上希望本身激光器的加工以及后续的配套都能实现低成本化。

- **功率密度**：功率密度决定同样尺寸的器件能发出多强的激光。目前供应商均致力于通过多节方案，即将半导体激光器内的多个有源区通过隧道结串联起来，来成倍提升功率，同时大幅提高器件发光效率。
- **温漂系数**：半导体均存在一定的光热效应，不同温度下，激光器发出激光的波长会有微小的漂移，漂移的幅度被称为温漂系数。实际应用中，激光雷达前端的滤波片亦需要将这部分“漂移”的波长范围考虑在内，被迫提升滤波宽度，影响激光雷达的信噪比。因此激光器厂商们致力于通过各种方式降低激光器的温漂系数。
- **光束质量**：即光斑的形状和能量分布，最好是规整圆形以方便测距使用。
- **光谱宽度**：又称为激光线宽，即激光的色彩纯度。激光雷达接收端会用滤波片将其他波长的光过滤掉，探测激光的线宽越窄意味着抗干扰性越强，信噪比越高。


根据激光波长分类，适用于汽车激光雷达系统的激光器主要可以分为 850nm、905nm 以及 1550nm 三种方案，不同波长方案的选择主要需要从涉及到安全性、性能及成本的多个维度考量。

- **功率问题**：通常由其对人眼的安全性决定；外界光的干扰情况；激光器本身的制备难度和成本问题等。
- **人眼安全**： 905nm 及以下波长的激光接近可见光，不能被人眼晶状体和角膜吸收，可穿透人眼的透明部分直达视网膜，这期间人眼屈光介质能将入射光束汇聚成极小的光斑，灼伤风险大。人眼安全峰值功率为 6W。探测距离一般为 150m~200m。而 1550nm 激光在经过人眼角膜等部分就被大量吸收，不会触及视网膜。在同等人眼安全要求下，可以采用比 905nm 激光雷达高 40 倍以上的发射功率，进而大幅提升探测距离，通常在 200 米以上。
- **抗干扰性**：850nm 方案为主流技术路径中水汽穿透性最好的方案，因此最大功率有限，导致产品探测距离较近。受限于安全功率，850nm 方案的有效探测距离较近。但因为波长更短，850nm 激光更难被空气中的水汽吸收，这有助于提高在潮湿场景下的自动驾驶可靠性。1550nm 所在的波段太阳辐射强度相对较弱，面临的光干扰更小，可获得更好的探测效果。
- **硅光芯片适配度**：1550nm 激光可在硅基介质中传播，是光通信中最常见的一种波长，可完美的与硅光产品配合，更容易实现芯片化。
- **成本和生产效率**：相比 905nm 激光器可直接采用半导体激光芯片耦合封装制备，1550nm 须采用光纤激光器来提升光束质量和功率，光纤激光器结构复杂。
- **发射和接收所用半导体材料**：波长在 800-1000nm 范围的接收端可以用半导体材料，发射端用砷化镓；而 1000nm 以上波长的光由于发射端用磷化铟 InP 的 EEL，由于硅基光电探测器在 1000nm 以上波长工作时的光敏感性极低，接收端需要用锗或者铟砷镓 等材料的探测器，且供应链成熟度仍然不高，产品良率也仍需提升，导致其整体成本远高于 905nm 激光器。

---

# 发光方向

通常 905nm 波长激光可选择半导体激光器。能够被硅吸收，可使用以硅为衬底的探测器。半导体激光器相较于前辈如固体、气体、液体激光器等有体积小、重量轻、功耗低、可靠性高、寿命长等特点。根据半导体激光器的发光方向可以分为出光方向平行于衬底平面的边发射激光器 (EEL) 和垂直于衬底平面的垂直腔面发射激光器(VCSEL）。这其中，EEL 激光器凭借其成熟的产品和供应链体系，极高的功率密度，成为目前主流的激光器形式。

![](https://pic4.zhimg.com/80/v2-52b0fa01cccfcf31f4a837ed5e900f0f_1440w.webp)

> 边发射激光器 EEL 和面发射激光器 VCSEL

## EEL

边发射激光器中就包含 FP、DFB、DBR、双异质结，量子阱等激光器。EEL 的光斑是椭圆的，特点是功率高——光电效率高、照度高（峰值功率 125W），但是激光的光谱稍宽。技术成熟且具备高发光功率密度， 950nm 的 EEL 方案是当下激光雷达厂商的主流选择。

成本上，生产成本方面， EEL 激光器由于激光从侧面发射，使用过程中需要进行切割、翻转、镀膜、再切割的工艺步骤，需要单颗一一贴装，人工成本较高。

配套成本方面，由于 EEL 发射的光斑为椭圆形，整形难度较高，并且需要分立的光学器件进行光束整形，依赖产线工人的手工装调，成本高一致性难以保障。

## VCSEL

无论是常规的 FP 腔半导体激光器 ，还是高性能的 DFB、EBR 激光器，激光振荡的方向都与生长的 PN 结有源区平行，激光都从半导体材料的解理面输出 。 这样的结构充分利用了有源区的增益 ，具有效率高、输出功率大的优点 。但是也有缺点，一是发光区为一个小的长方形 ，输出光束发散角大 ，且呈长椭圆形 。在许多应用中，无论是与光纤耦合，还是用透镜准直 、聚焦，都希望圆形光束 ，这就需要在外部做复杂的光束整形。二是在激光器生产中必须采用解理工艺 ，批量生产时难以机械化和自动化，工艺复杂，成本高。因此，从芯片表面发射激光的激光器成为一个重要的研究课题。

VCSEL 全称（Vertical-Cavity Surface-Emitting Laser），是垂直腔面发射激光器。它与边发射激光器最大的不同点是：出射光垂直于器件的外延表面，即平行于外延生长的方向。最初用于光通信领域，比如光模块中，后来开始应用于消费电子领域的 3D 感测方面，比如人脸识别，2017 年苹果将其用在 iPhone 人脸识别模组，VCSEL 也开始受到消费电子领域的大规模关注。目前来看国外在 VCSEL 芯片方面还是较为领先，近些年国内多家厂商发展迅速，并且开始逐渐小批量或者批量生产，多家 VCSEL 芯片也得到了资本的较多关注。



VCSEL 技术的许多优点可以总结如下：

1. 波长稳定性：VCSEL 中的激光波长非常稳定，因为它由很薄的（1~1.5个波长厚的）F-P 腔固定。与边射型激光器不同，VCSEL 仅能以单个纵向模式运行。
1. 波长均匀性和光谱宽度：生长技术的改进使得 VCSEL 3 英寸晶圆的腔波长标准偏差小于 2nm。这使得 VCSEL 2-D 阵列的制造可以使得阵列元素之间的波长差异很小（全宽半峰值光谱宽度 <1nm）。相比之下，边射型激光器的条形阵列由于缺乏内在的稳定波长机制，从一个条到另一个条存在明显的波长变化，导致光谱宽度较宽（全宽半峰值光谱宽度为 3~5nm）。
1. 波长对温度的敏感性：VCSEL 的发射波长比边射型激光器对温度变化的敏感度低约 5 倍。原因是在 VCSEL 中，激光波长由单个纵向模式腔的光学厚度定义，而这个光学厚度的温度依赖性很小（腔的折射率和物理厚度对温度具有较弱的依赖性）。另一方面，边射型激光器中的激光波长由增益峰波长定义，其温度依赖性要强得多。因此，高功率阵列（发热大）的光谱线宽在 VCSEL 阵列中比在边射型激光器阵列中窄得多。此外，相对于 20°C 的温度变化，VCSEL 的发射波长变化小于 1.4nm（边射型激光器为约 7nm）。
1. 高温运行（泵浦系统无需冷却）：VCSEL 器件可以在没有冷却的情况下运行，因为它们可以在 80℃ 的温度下运行，这种方法使得冷却系统变得非常小巧、坚固和便携。
1. 单位面积输出功率更高：边发射激光器的最大功率密度约为 0.5kW/cm2，因为必须保持激光器之间的间隙以便冷却流动，而 VCSEL 现在可以提供约 1.2kW/cm2 的功率密度，未来可能提供 2-4kW/cm2 的功率密度。
1. 光束质量更好：VCSEL 发射圆形光束。通过适当的腔体设计，VCSEL 也可以发射单横模（圆高斯型）光束。与边发射激光器相比，这种简单的光束结构大大降低了耦合/光束成形光学器件的复杂性和成本，并提高了到光纤或泵浦介质的耦合效率，这是 VCSEL 技术在低功率市场上的一个关键卖点。
1. 可靠性更高：由于 VCSEL 不容易受到灾难性光学损伤（COD）的影响，因此它们的可靠性比边发射激光器高得多。
1. 制造可行性和良率：VCSEL 的制造可行性一直是该技术的一个关键卖点。由于边发射激光器具有制造过程复杂和灾难性光学损伤相关的可靠性问题，因此其良率较低（从 2 英寸晶圆中能获得约 500 个边发射 980nm 泵浦芯片）。另一方面，VCSEL 的良率超过 90％（从 2 英寸晶圆中获得约 5000 个 VCSEL 芯片）。事实上，由于其平面属性，VCSEL 制造与芯片加工相同。
1. 可扩展性：对于高功率应用，VCSEL 的一个关键优势是它们可以直接加工成单片 2D 阵列，而边发射激光器则不可能（只有 1D 单片阵列）。此外，需要复杂且热效率低下的安装方案才能将边发射器条堆叠在一起。
1. 封装和散热：将大型高功率 VCSEL 二维阵列以“junction-down”配置安装很简单（类似于微处理器封装），使热移除过程非常高效，因为热量只需穿过几微米的 AlGaAs 材料。
1. 成本：由于简单的加工和散热技术，封装二维 VCSEL 阵列比等效的边缘发射器条形堆栈更容易。现有的硅行业散热技术可以用于高功率阵列的热移除，这将显著降低高功率模块的成本。
1. 而 VCSEL 十分方便量产，且可在制造过程中的各个阶段进行测试，生成良率可控，降低制造成本。VCSEL 易于和面上工艺的硅材料微型透镜整合，成本较低。除功率密度较 EEL 低外，在线宽、温漂系数、光束形状等指标上均优于 EEL，随着自动驾驶技术的快速发展以及激光雷达成本的下探，VCSEL 方案的能量密度及发光效率都将逐年提升，未来 VCSEL 方案将替代 EEL 成为行业主流。目前禾赛科技和 Lumentum 合作已经在 AT128 转镜式激光雷达上搭载了 VCSEL 激光器。

# Reference

- 方祖捷. 单频半导体激光器原理、技术和应用[M]. 上海交通大学出版社, 2015.
- 马鹏阁. 多脉冲激光雷达[M]. 国防工业出版社, 2017.
- 陈良惠, 杨国文, 刘育衔. 半导体激光器研究进展[J]. 中国激光, 2020, 47(5):19.
- 马骁宇, 张娜玲, 仲莉,等. 高功率半导体激光泵浦源研究进展[J]. 强激光与粒子束, 2020(012):032.
- 郎兴凯, 贾鹏, 陈泳屹,等. 窄线宽半导体激光器研究进展[J]. 中国科学F辑, 2019.
- 孙国玉, 杨君婷, 包明冉,等. 高功率光纤激光的发展现状与应用[J]. 现代物理, 2020.
- 杜悦宁, 陈超, 秦莉,等. 硅光子芯片外腔窄线宽半导体激光器[J]. 中国光学, 2019(2):13.
- [wikipedia: laser pumping](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Laser_pumping)
- [Princeton Optronics: Vertical-Cavity Surface-Emitting Laser Technology](https://link.zhihu.com/?target=https%3A//www.newmetals.co.jp/pdf/234.pdf)
- [ProLabs: Laser Sources For Optical Transceivers White Paper](https://link.zhihu.com/?target=https%3A//uk.insight.com/content/dam/insight-web/en_GB/Buy/shops/prolabs/White-Paper-Laser-Sources-For-Optical-Transceivers.pdf)
- [中国科学技术大学课件：半导体发光器件发光器](https://link.zhihu.com/?target=https%3A//www.google.com/url%3Fsa%3Dt%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dweb%26cd%3D%26cad%3Drja%26uact%3D8%26ved%3D2ahUKEwiKqdyM8-_9AhUPJUQIHU0KBAkQFnoECAgQAQ%26url%3Dhttp%253A%252F%252Fhome.ustc.edu.cn%252F~cruishan%252F%2525D7%2525CA%2525C1%2525CF%2525BA%2525CDPPT%252F%2525CA%2525AE%2525D2%2525BB%2525D5%2525C2%2525B0%2525EB%2525B5%2525BC%2525CC%2525E5%2525B7%2525A2%2525B9%2525E2%2525C6%2525F7%2525BC%2525FE.pdf%26usg%3DAOvVaw13yoZT2w2yZPG9kxjiNBV1)
- [中国大百科全书：泵浦源](https://link.zhihu.com/?target=https%3A//www.zgbk.com/ecph/words%3FSiteID%3D1%26ID%3D121509%26Type%3Dbkzyb)
- [知乎专栏：第十一章-半导体激光器](https://zhuanlan.zhihu.com/p/338970148)
- [华泰证券： 解构激光器核心元器件，国产化破冰而立](https://link.zhihu.com/?target=http%3A//pdf.dfcfw.com/pdf/H3_AP201807221168905277_1.pdf)
- [激光雷达行业深度报告：技术路线逐渐清晰、国产激光雷达占得先机](https://link.zhihu.com/?target=https%3A//new.qq.com/rain/a/20220812A01UUU00)
- [光电汇：3分钟了解窄线宽激光技术——“单色性”趋于极致的激光器](https://link.zhihu.com/?target=https%3A//www.oeshow.cn/informationdetail/12783)
- [半导体行业观察：VCSEL激光器技术科普！](https://link.zhihu.com/?target=http%3A//www.semiinsights.com/s/electronic_components/23/37850.shtml)
- [长三角激光联盟：干货，垂直腔面发射激光器最全科普！](https://link.zhihu.com/?target=https%3A//www.sohu.com/a/433315058_100034932)
- [自动驾驶欲“抛弃”激光雷达？窄线宽半导体激光器来救场](https://link.zhihu.com/?target=https%3A//www.sohu.com/a/321740399_744047)

---

欢迎在我的专栏「[自律走行](https://www.zhihu.com/column/jiritsu-soko)」中查看更多「聚焦激光雷达」系列文章

- [聚焦激光雷达（一）——扫描器](https://zhuanlan.zhihu.com/p/611852342)
- [聚焦激光雷达（二）——激光器](https://zhuanlan.zhihu.com/p/616243016/)
- [聚焦激光雷达（三）——接收器](https://zhuanlan.zhihu.com/p/618634684)
- [聚焦激光雷达（四）——光学元件](https://zhuanlan.zhihu.com/p/622652543)
- [聚焦激光雷达（五）——处理器](https://zhuanlan.zhihu.com/p/628148718)