---
title: Active wideband higher-order raypath separation in multipath environment
date: 2017-02-21 21:00:00
categories: math
tags: algorithm
toc: true
---


 多路径环境下的有源宽带高阶信号分离

在线发布时间: January 2017

收稿时间: November 2016

<!-- more -->
 [Active wideband higher-order raypath separation in multipath environment](http://asa.scitation.org/doi/10.1121/1.4972570)

[Longyu Jiang](http://asa.scitation.org/author/Jiang%252C+Longyu) 和  [Yaping Hong](http://asa.scitation.org/author/Hong%252C+Yaping) 

- The Laboratory of Image Science and Technology, [Southeast University](http://asa.scitation.org/action/doSearch?field1=Affiliation&text1=Southeast%20University&field2=AllField&text2=&Ppub=&Ppub=&AfterYear=&BeforeYear=&access=), Nanjing 210096, China    jly#seu.edu.cn, hongyaping#126.com

[Philippe Roux](http://asa.scitation.org/author/Roux%252C+Philippe)

- [Institut des Sciences de la Terre, Université Joseph Fourier](http://asa.scitation.org/action/doSearch?field1=Affiliation&text1=Institut%20des%20Sciences%20de%20la%20Terre,%20Universit%C3%A9%20Joseph%20Fourier&field2=AllField&text2=&Ppub=&Ppub=&AfterYear=&BeforeYear=&access=), Centre National de la Recherche Scientifique, 1381 Rue de la Piscine, Saint-Martin d'Hères, France  philippe.roux#ujf-grenoble.fr

[Jiasong Wu](http://asa.scitation.org/author/Wu%252C+Jiasong) 和 [Huazhong Shu](http://asa.scitation.org/author/Shu%252C+Huazhong)b)

- The Laboratory of Image Science and Technology, [Southeast University](http://asa.scitation.org/action/doSearch?field1=Affiliation&text1=Southeast%20University&field2=AllField&text2=&Ppub=&Ppub=&AfterYear=&BeforeYear=&access=), Nanjing 210096, China jswu#seu.edu.cn , shu.list#seu.edu.cn

《美国声学学会杂志》**141**, EL38 (2017); doi: [http://dx.doi.org/10.1121/1.4972570](http://dx.doi.org/10.1121/1.4972570)

# 摘要

多路径的信号传播是由水柱表面和底部的反射和折射引起的。

在这项研究中，提出了有源宽带高阶分离算法，是一种在海洋传统环境中能够在角度到时间域中分离有色噪声和信号。和传统算法进行对比，它更精确，实验的数值结果显示噪声抑制性能更佳，甚至不需要假设接收阵传感器数量不必大于发射阵信号源个数。

声场传播环境，声波的速度，水面和海底的反射和折射，导致了多路径的信号，这就像是一种特殊的透镜。在许多有源声纳或者海洋声层析的应用中，多路径分离或者定位是必要的。前人已经提出了许多分离多路径的方法。

根据时间反演原理，Roux等人发明了双波束形成算法（DBF），并且此算法用两个垂直发射/接收阵列来进行实验，能通过模拟两阵列之间的波束形成来识别单个信号的发射角/接收角/到达时间。

为了进一步提高波束形成算法的低分辨率性能，Jiang等人在浅海海洋声层析成像的背景下，推导出了一种高精度的平滑多信号分类主动大带算法（**Smoothing-MUSICAL**）方法。

**平滑MUSICAL**是以信号的频谱长度为先验信息，将MUSIC算法扩展到MUSICAL中的宽带情形。此外smoothing-MUSICAL算法还结合了有源多信号分类大带（MUSICAL）算法和空间频率平滑技术，来分离在到达方向（DOA）-时空域上相干或完全相关的路径。实验结果显示这种算法能显著的改善分离性能，产生的杂质更少。

但是Roux和Jiang的算法都是基于以下假设：

- 接收信号受到高斯白噪声影响，而不是存在于海洋环境中的有色噪声。
- 高斯信号的信息在一阶和二阶，非高斯过程包含的信息在大于二阶的高阶累积量中。

所以有必要考虑如何分离在彩色噪声环境下的信号。

理论上高斯信号的所有信息都包含在一阶和二阶，非高斯过程的信号的信息在高阶累积量中。应用了高阶累积量而不是二阶的技术主要是得将彩色噪声纳入阵列处理技术的考虑范围。在过去的二十年间，越来越多的人着力于将高阶累计量应用到定位问题上。

Chen 和 Lin 开发了一种四阶算法，其性能在高斯噪声和非高斯噪声环境中比MUSICAL 算法都更佳。

Dogan 和 Mendel ， 率先阐释累积量是如何增加传感器阵列的有效孔径的，并在加性彩色噪声的不敏感性研究下有显著突破。

Gonen 等人利用 四阶累计量进行方向定位，来研究比接收器列传感器数量还多的信号的分解。

近来提出了使用2q阶(q>2)的一系列阵列处理算法，能分辨率，模型误差的鲁棒性，和传感器阵列接收到的信号的数量。理论上随着q增加，分辨率增加，传感器阵列处理能力增加。

但其局限是其使用了窄带数据假设。因为在多径环境下，接收到的信号可能是宽带。

Bourennane 和 Bendjama 提出了宽带下使用高阶累积量的定位算法，但他只是用了高斯白噪声下的到达方向来进行定位声源，并且在近距离的阵列间信号定位失败。

在这课题中我们提出了一种海洋声层析环境下高阶有源宽带MUSIC算法，有源意味着发射的信号是已知的，频谱在我们提出的高分辨率算法中是先验信息。它能利用信号的到达时间作为附加参数，在到达方向-时间域上分离有噪声干扰的相近信号。

这篇论文的结构如下，第二段中我们研究高阶高分辨率有源算法，第三段中提出我们的仿真结果，第四段是结论和未来展望。

# 高阶高分辨率有源算法

如第一段中我们提到的，Jiang等人提出了一种海洋声层析环境下新型高分辨率阵列处理的smoothing-MUSICAL算法，能够分离完全相干的路径，算法建立两个假设下

- 加性噪声是高斯白噪声
- 传感器数量N大于信号路径数P

为了克服以上假设，我们在这段里将介绍一种四阶  smoothing-MUSICAL 算法

## 信号模型

P个信号路径到达M个传感器组成的垂直接收阵列，第m个传感器接收到的信号在时间域上表示为

（1）： $x_m(t)=\Sigma_{p=1}^P a_p e(t−\tau_{m,p})+n_m(t)$

其中

​	$e(t)$ ：信号源发射的信号

​	$a_p$：第m个水听器接受到的第p个路径的信号振幅

​	$n_m(t)$　：第m个传感器接收到的加性噪声

​	$\tau_{m,p} $:第p个信号在基准传感器和第m个传感器之间的传播延迟delay ，传播延迟满足此式：（2）：$\tau_{m,p} = T_p +t_m(\theta_p)　$

​	$T_p$ ：第p个信号路径在基准传感器上的到达时间

​	$t_m(\theta_p)$ ：基准传感器和第m个传感器之间的延迟delay ，是信号路径到达方向（角度）的函数

在频域上，（1）式可写为：

（3）： $x_m(ν)=\Sigma_{p=1}^P a_p e(ν) exp(−jν(Ψ_p+(m−1)Φ_p))+n_m(ν)$

其中 

​	$Ψ_p=2πT_p  $

​	$Φ_p=2πt_m(θ_p)=2π\frac{d sin θ_p}{c}$

​	d ： 邻近传感器之间的距离

​	c ：  声传播速度

​	$e(ν)$ ： 在频率为ν 时信号的振幅 （每个信号的振幅$a_p$ 是随机和不相关的）

## 算法的原理

### 宽带频谱矩阵估计

我们假设信号使用的频率区间是F，（3）式在频率域可写作宽带频谱矩阵表达式

（4）： $x_g=H · A +n_g$

​	$x_g=[x^+(ν_1),x^+(ν_2),…,x^+(ν_F)]^+$  中各项 $x(ν_i)=[x_1(ν_i),x_2(ν_i),…,x_M(ν_i)]^+ $

​	x_g ：M × F  维大小的矩阵，包含所有传感器接收到的频率信息

​	 $n_g=[n^+(ν_1),n^+(ν_2),…,n^+(ν_F)]^+$ 中各项$ n(ν_i)=[n_1(ν_i),n_2(ν_i),…,n_M(ν_i)]^+$ ：

​	$n_g$ ：$M × F$ 维大小的矩阵，包含每个频域的噪声信息

​	 $A=[a_1,a_2,…,a_P]^+$ ：是P个信号的方向组成的向量

​	$H=[h_1,h_2,…,h_P]^+$  中各项 $h_p=[e(ν_i)e^{−2iπν_1τ_1p},…,e(ν_F)e^{−2iπν_Fτ_Mp}]^+ $

​	H： (*M* × *F*, *P*)维的矩阵，其项 $e^{−2iπν_1τ_1p}$ 描述了源信号和接收信号的传递函数

​	+：转置

接收信号的频谱矩阵可表示为：

（5）： $C=E{(x_g⊗x^∗_g)(x_g⊗x^∗_g)^H}−E{(x_g⊗x^∗_g)}E{(x_g⊗x*∗_g)^H}−E{(x_g x^H_g)}⊗E{(x_g x^H_g)^∗}$

其中

​	⊗​ ： 克罗内克积（Kronecker product）作用于矩阵（可视为二阶张量），是张量积的特殊形式。而张量积作用于张量。

但是不同路径的信号是完全相干的，因为不同路径的信号是一系列的信号的延迟和副本。所以矩阵 ​ 缺秩。这将降低分离算法的性能，因为特征结构的高分辨率是基于和信号的导向矢量正交的最小特征值的特征向量。所以在 Jiang 的基础上，提出了一种空间-频率平滑处理来分离相干信号。

这种空间平滑算法首先将由M个传感器组成的 阵列[1,2,3,......,M]​

划分成$[1,...,k_s-1],[k_s,k_s+1,......,k_s+M-2k_s],[M-k_s+1,......,M]$；

​索引为k_s 的子天线区域包括了 $[k_s;k_s+1;k_s+M-2K_s]$ 范围内的传感器。 

频率平滑也将带宽在频域上划分成 $[1,...,k_F-1],[k_F,k_F+1,......,k_F+M-2k_F],[M-k_F+1,......,M]$ ； 

​索引为k_f 的子带区域包括了 $[k_f;k_f+1;k_f+F-2K_f]$ 范围内的频率。 

​所以单个可观测矩阵x 可知，产生的一系列的按$\underline{x}_{ks,kfx}$递归的矩阵 $K=(2K_f+1)(2K_s+1)$ 可用下图描述

![img](http://asa.scitation.org/na101/home/literatum/publisher/aip/journals/content/jas/2017/jas.2017.141.issue-1/1.4972570/20170111/images/medium/1.4972570.figures.online.f1.jpg)

（Fig.1）子天线区域的结构示例

​	(a) 空间平滑因子K_s = 1​时，M=7个传感器阵列被划分成3组；

​	(b) K_f=2​ 时频率F=10被划分成5组

使用平滑技术，我们能用下式估计宽带的频谱矩阵

（6）：$ \hat{C} =E{(\underline{x}_{g,k_s},k_f⊗\underline{x}^∗_{g,k_s,k_f})(\underline{x}_{g,k_s,k_f}⊗\underline{x}^∗_{g,k_s,k_f})^H}−E{(\underline{x}_{g,k_s,k_f}⊗\underline{x}^∗_{g,k_s,k_f})}E{(\underline{x}_{g,k_s,k_f}⊗\underline{x}^∗_{g,k_s,k_f})^H}−E{(\underline{x}_{g,k_s,k_f} \underline{x}^H_{g,k_s,k_f})}⊗E{(\underline{x}_{g,k_s,k_f} \underline{x}^H_{g,k_s,k_f})^∗}$

频谱矩阵估计的秩等于K，为了达到有效的分离噪声和信号，必须使K大于P

## 信号子空间估计

假设信号和噪声不相干（加性噪声），我们得到下列关系式

（7）： \hat{C}=\hat{C}_s+\hat{C}_n

频谱矩阵具有 埃尔米特对称（Hermitian symmetry）  

（8）： \hat{C}=\hat{C}_*​

埃尔米特对称：n阶复方阵A的对称单元互为共轭，即A的共轭转置矩阵等于它本身，则A是埃尔米特矩阵(Hermitian Matrix)。显然埃尔米特矩阵是实对称阵的推广。

能够被特征向量分解(EVD)为

（9）： ​

其中

​	Λ=diag(λ_1,…,λ_{ {(MF)}^2})​ 是特征值组成的对角矩阵

​	**U**： (MF)^2×(2K_s+1)(2K_f+1)​大小的矩阵，其列向量 μ_1,…,μ_{ {(MF)}^2}​ 是\hat{C}​的正交特征向量。

特征向量μ_i​对应特征值\lambda_i​，特征值从大到小排序

（10）： λ_1≥λ_2⋯≥λ_{ {(MF)}^2}​

## 噪声子空间上的投影

在上面特征值分解的基础上，信号子空间是由 \hat{C}​ 的前 p^2​ 个特征向量张成的特征子空间。而它的补集，噪声子空间，由倒数的(MF)^2-p^2​ 的正交的特征向量张成的特征子空间。这些正交向量在噪声子空间上投影可估计为

（11）： \hat{C}_n=\Sigma _{k=p^2+1}^{(MF)^2}μ_k μ^∗_k​

最后，算法包含了下列函数的最值

（12）： P(θ,T)=\frac{1}{a(θ,T)^∗\hat{C}_n a(θ,T)}​

其中 

​	a(θ,T)​ ：基于宽带的四阶累积量的导向矢量，是b(θ,T)​ 和b(θ,T) ^ ∗​ 的克罗内克积 a(θ,T)=b(θ,T)⊗b(θ,T) ^ ∗​

​	b(θ,T)= \begin{pmatrix}{e(ν_1)e^{−2iπν_1T}d^+(ν_1,θ)} \\...\\\ {e(νF_)e^{−2iπν_FT}d^+(ν_F,θ)}\end{pmatrix}​

​	d(ν_i,θ)=[1,e^{−2iπν_iτ_{1,2}(θ)},…,e^{−2iπν_iτ_{1,M−1}(θ)}]^+​

​	d(ν_i,θ)​ 在窄带分析中是经典的导向矢量，包含了传感器和信号给定频率\theta​之间的相位延迟信息

# 仿真

在这一段中国，我们提供了仿真来演示我们算法在非高斯有色噪声环境下，相干信号源的方向定位性能。仿真中使用到了等距的垂直阵列，传感器各向同性，传感器间相距半波长，发射信号的频率带包含了红色噪声（红色噪声指功率密度随着频率增加而递减的随机噪声）。仿真实验使用了一个单次观测。我们的仿真结果将和二阶、四阶统计量在同环境下进行对比。

## 性能分析

使用了由六个传感器组成的垂直阵列的例子

在这一段我们将考虑想近的信号情况进行分离，我们假设五束信号到达了由六个水听器组成的等距接收阵列。选取第一个水听器作基准传感器

如图2(a) 2(b)显示，是smoothing-MUSICAL和四阶-smoothing-MUSICAL算法的分离结果，频率从3000-500Hz中取了25个值，信号是等功率的。每个点都对应着一个信号，黑色的十字点意为信号的理论值。对应这个点最大振幅的估计值在图2(b)中显示。

从左到右从上到下为第1，2，3，4，5个信号。而第2个和第4个信号到达后，图2(a)将比图2(b)更容易的侦测第5个信号的到达。而且五个信号在图2(b)中更分明，2(a)中有少许杂质污染波束形成结果。杂质仅由仿真时的有限采样，信号和噪声子空间的不完全分离造成。这种由于使用高阶累积量，对有色噪声和白噪声共有的抑制能力，已经在参考文献[Ref. 5](http://asa.scitation.org/doi/10.1121/1.4972570#)中得到了证明。到达方向角DOA由此式计算 ​

![img](http://asa.scitation.org/na101/home/literatum/publisher/aip/journals/content/jas/2017/jas.2017.141.issue-1/1.4972570/20170111/images/medium/1.4972570.figures.online.f2.jpg)

(Fig 2.)性能分析（黑色十字点意为信号理论值）

​	(a)smoothing-MUSICAL算法的分离结果

​	(b)四阶-smoothing0MUSICAL算法的分离结果

​	(c)信噪比为20dB时，到达时间的均方根误差，a线代表四阶smoothing-MUSICAL算法，b线代表smoothing-MUSICAL算法

​	(d)信噪比为20dB时，延迟的均方根误差，a线代表四阶smoothing-MUSICAL算法，b线代表smoothing-MUSICAL算法

​	(e)信噪比为20dB时，smoothing-MUSICAL算法的延迟的均方根误差和带宽的关系，由10次独立实验测得

​	(f)信噪比为20dB时，四阶-smoothing-MUSICAL算法的延迟的均方根误差和带宽的关系，由10次独立实验测得

## 性能定量分析

在这一段，我们将用定量分析来佐证提出的算法的性能。对于已知方法，经常使用均方根误差来量化相关参数估计的特性。我们定义了到达时间​ ， p信号的延迟​ 的量化均方根误差

​	​ ：独立实验的次数

​	​ ： ​的估计

​	​ ：​  的估计

假设一束信号 ​ , ​ ，被一个由四个各向同性的传感器组成的阵列接收到，传感器相距半波长。

图2(c)和2(d)显示了结果的均方根误差。相比于smoothing-MUSICAL算法，四阶smoothing-MUSICAL有更好的性能，尤其是到达时间的均方根误差更小。

在上面两段的讨论基础上，我们能得出结果，提出的算法不仅能得到更精确的探测结果，相比于smoothing-MUSICAL算法有着更好的噪声抑制能力。

### 带宽对性能的影响

为了研究宽带对提出算法的性能的影响，我们假设一个高斯窗口正弦脉冲（中心频率为100Hz）被一个由四个各向同性传感器组成均匀线性分布阵列接收到，传感器相距半周长。到达时间和延迟是0.075 和 0.015 s。在此假设下，图2(e) 和 2(f) 用十个独立实验得到了带宽和均方根误差的关系。带宽大于0.2时，到达时间和延迟的均方根误差都在可接受范围内。

## 比信号更多的传感器

在这一段，我们将对提出算法用比到达信号少的接收器来进行测试。我们假设有五束信号被四个传感器组成的垂直阵列接收到，信号是等功率的。信号的频率从3000-5000Hz中取了25个值，并且按信噪比等于20dB掺杂了红色噪声。

图3(a) 和 3(b) 为smoothing-MUSICAL算法和四阶-smoothing-MUSICAL算法的探测结果。黑色十字点位信号在角度到时间域的理论预期值。图3(a)中有两束信号丢失，而3(b)中5束信号泾渭分明。此外，这两种算法在峰值处存在偏差，而用我们的算法的偏差更小。到达方向角用此式计算 ​

这一段的模拟结果说明了当接收器阵列传感器个数小于信号数时，四阶-smoothing-MUSICAL算法仍能分离信号，而smoothing-MUSICAL算法不能探测到所有信号。传感器阵列的有效孔径能够因四阶累积量扩展到​ 

![img](http://asa.scitation.org/na101/home/literatum/publisher/aip/journals/content/jas/2017/jas.2017.141.issue-1/1.4972570/20170111/images/medium/1.4972570.figures.online.f3.jpg)

图3 结果对比

​	五束信号到达四个传感器组成的垂直阵列，信噪比为20dB，黑色十字为信号理论值。

​	(a)使用smoothing-MUSICAL算法的分离结果

​	(b)使用四阶-smoothing-MUSICAL算法的分离结果

# 结论

在这项研究中，我们开发了一种基于高阶统计量的有源的宽带MUSIC算法。模拟结果显示，在有色噪声存在的情况下，相比二阶算法，能更精确的分离信号和噪声。另一个优势是使用比接收到信号数少的传感器阵列，性能也更好。未来，将研究发射器阵列到接收器阵列间此算法的扩展，而非仅对接收到的信号和接收器阵列的研究。

# 鸣谢

感谢

​	中国国家自然科学基金会(Nos. 61401085 和 31400842)

​	中国科学院国家重点声学实验室(No. SKLA201604)

​	归侨学者科研基金会

对此项目的支持

# 参考文献

1. P. Roux , B. D. Cornuelle , W. Kuperman , and W. Hodgkiss , “ The structure of raylike arrivals in a shallow-water waveguide,” J. Acoust. Soc. Am. **124**(6), 3430–3439 (2008). [https://doi.org/10.1121/1.2996330](https://doi.org/10.1121/1.2996330) **Google Scholar**, **Scitation**
2. L. Jiang , F. Aulanier , G. Le Touze , B. Nicolas , and J. Mars , “Raypath separation with high resolution processing,” in *IEEE OCEANS 2011*, Spain (2011), pp. 1–5. **Google Scholar**, **CrossRef**
3. Y. H. Chen and Y. S. Lin , “ Doa estimation by fourth-order cumulants in unknown noise environments,” in *IEEE International Conference on Acoustics, Speech, and Signal Processing, 1993. ICASSP-93* (1993), Vol. **4**, pp. 296–299. **Google Scholar**, **CrossRef**
4. M. C. Dogan and J. M. Mendel , “ Applications of cumulants to array processing. I. Aperture extension and array calibration,” IEEE Trans. Signal Processing **43**(5), 1200–1216 (1995). [https://doi.org/10.1109/78.382404](https://doi.org/10.1109/78.382404) **Google Scholar**, **CrossRef**
5. M. C. Dougan and J. M. Mendel , “ Applications of cumulants to array processing. II. Non-Gaussian noise suppression,” IEEE Trans. Signal Processing **43**(7), 1663–1676 (1995). [https://doi.org/10.1109/78.398727](https://doi.org/10.1109/78.398727) **Google Scholar**, **CrossRef**
6. E. Gonen , J. M. Mendel , and M. C. Dogan , “ Applications of cumulants to array processing. iv. direction finding in coherent signals case,” IEEE Trans. Signal Processing **45**(9), 2265–2276 (1997). [https://doi.org/10.1109/78.622949](https://doi.org/10.1109/78.622949) **Google Scholar**, **CrossRef**
7. P. Chevalier , A. Ferreol , and L. Albera , “ High-resolution direction finding from higher order statistics: The 2q-music algorithm,” IEEE Trans. Signal Processing **54**(8), 2986–2997 (2006). [https://doi.org/10.1109/TSP.2006.877661](https://doi.org/10.1109/TSP.2006.877661) **Google Scholar**, **CrossRef**
8. G. Birot , L. Albera , and P. Chevalier , “ Sequential high-resolution direction finding from higher order statistics,” IEEE Trans. Signal Processing **58**(8), 4144–4155 (2010). [https://doi.org/10.1109/TSP.2010.2049569](https://doi.org/10.1109/TSP.2010.2049569) **Google Scholar**, **CrossRef**
9. P. Pal and P. Vaidyanathan , “ Multiple level nested array: An efficient geometry for 2*q*th order cumulant based array processing,” IEEE Trans. Signal Processing **60**(3), 1253–1269 (2012). [https://doi.org/10.1109/TSP.2011.2178410](https://doi.org/10.1109/TSP.2011.2178410) **Google Scholar**, **CrossRef**
10. S. Bourennane and A. Bendjama , “ Locating wide band acoustic sources using higher order statistics,” Appl. Acoust. **63**(3), 235–251 (2002). [https://doi.org/10.1016/S0003-682X(01)00039-1](https://doi.org/10.1016/S0003-682X(01)00039-1)**Google Scholar**, ****CrossRef****