---
title: The effect of source amplitude and phase in matched field source localization
date: 2017-02-24 14:12:00
toc: true
---
匹配场源定位中源振幅和相位的影响
<!---more--->
传统的匹配场处理通常应用于定位未知振幅和相位的声源，信号源的频谱信息能够用最大似然估计和 Bartlett处理器来估计。本文提出了信号源频谱的最大后验概率，定位声源和噪声的方差估计，吉布斯采样后计算所有参数的联合后验概率分布。


匹配场：源信号和接收信号进行匹配
Bartlett 和线性处理器经常用MFP，计算源信号和接收信号的内积。

本文采用Bartlett 处理器，和简单的高斯白噪声环境。


[The effect of source amplitude and phase in matched field source localization](http://asa.scitation.org/doi/full/10.1121/1.2166927)

# 最大似然估计

$X=\alpha G(r,z_s)+W$

$G(r,z_s)$ :通过求解亥姆霍兹方程得到格林函数

振幅为1，相位为0，频率f，

传播环境完全已知，除了确定G的范围range-r和深度depth-z_s

$\alpha$：包含信号在传输是的振幅和相位的复数

W：符合均值为0，对角空间协方差矩阵为$\Sigma = 2\sigma ^2 I_{L\times L } ​$的高斯分布的加性噪声

接收到的信号能够用高斯分布来处理，所以选了高斯噪声环境

$p(X|r,z_s,\alpha) = \frac{1}{\sigma^{2L}(2\pi)^L} exp(-\frac{1}{2\sigma^2}(X-\alpha G(r,z_s))^*(X-\alpha G(r,z_s)))$

以上提供了参数$\alpha,r,z_s$的最大似然函数

$l(r,z_s,\alpha,\sigma^2|X)\propto  exp(-\frac{1}{2\sigma^2}(X-\alpha G(r,z_s))^*(X-\alpha G(r,z_s)))$

后两个为多余参数，在MFP中已知

$\hat{\alpha}=\frac{G^*(r,z_s)X}{||G(r,z_s)||^2}$

$l(r,z_s|X)\propto  (||X||^2-\frac{G^*XX^*G}{||G||^2})^{-L}$

$l_{r,z_s}$ 的最大化等价于对等式

$P(r,z_s)=\frac{G^*XX^*G}{||G||^2}$

最大化



P即是模糊表面



# MFP中吉布斯采样

通过这些参数的最大后验分布来进行估计

假设q向量包含了所有未知参数，最大后验分布为

$p(q|X)=\frac{l(q|X)p(q)}{p(X)}$

$p(q)$ 包含了所有先验知识

$l(q|X)$ 为参数的似然估计

$q=[r, z_s,\alpha, \sigma^2]^T$ 

$\alpha$ 已知，其先验分布$p(\alpha) = C , -\infty < Re(\alpha), Im(\alpha)<\infty $

这个等式不包含瑞利参数，比瑞利Rayleigh 更普通



对于未知的源的range和depth，我们使用在区间$[r_1,r_2], [z_{s1},z_{s2}]$ 的先验概率

$p(r)=\frac{1}{r_2-r_1}$

$p(z_s)=\frac{1}{z_{s1}-z_{s2} }$



$\sigma$ 使用无信息的先验分布

$p(\sigma^2)=\frac{1}{\sigma}, 0<\sigma<\infty$



综上

$p(r,z_s,\alpha,\sigma^2|X)=M \frac{1}{\sigma^{2L+2} } exp((-\frac{1}{2\sigma^2})(X-\alpha G)^*(X-\alpha G)) $

M为常数

边缘分布

$p(r,z_s,|X)   =  \int _{\alpha } \int _{\sigma^2}p(r,z_s,\alpha,\sigma^2|X)d\sigma^2 d \alpha $

# 源定位和源谱估计的吉布斯采样

通过吉布斯采样估计$p(r,z_s|X)$ ，无需计算$p(r,z_s,\alpha,\sigma^2|X)$ 和积分

固定其他参数，$p(\alpha |r,z_s,\sigma^2 ,X)=M_\alpha exp((-\frac{||G||^2}{2\sigma^2})(\alpha -G^*X / ||G||^2)^* (\alpha - G^*X / ||G||^2))$

$M_\alpha$：常数

$\alpha$：均值为 $G^*X / ||G||^2$，方差为$2\sigma^2 / ||G||^2$的正态分布

方差的条件后验估计为反$\chi^2$分布

$p(σ^2∣r,z_s,α,X))=\frac{1}{σ^{2L+2} }exp(−\frac{1}{2σ^2}∥X−αG(r,z_s)∥^2)$

推导出

$p(r,z_s∣α,σ^2,X))=K\ exp(−\frac{1}{2σ^2}∥X−αG(r,z_s)∥^2),$

K是常数



吉布斯采样起始于对未知参数的一系列随机初始化，然后根据一份样本确定range和depth的条件分布，然后求$\alpha$的高斯边缘后验分布，然后确定根据反$\chi^2$分布确定方差，然后进行迭代。

# 性能评估

使用合成数据进行模拟，24个水听器，600Hz的频率，信噪比为7-14dB，Bartlett处理器和本文提出的处理器进行对比，range为2km，depth为34m，实验接受的正确结果范围为range 1.8-2.2km，depth 28-40m，range搜索范围为0-5km，间隔0.02km；depth搜索范围为0-72m，间隔2m。

![](http://asa.scitation.org/na101/home/literatum/publisher/aip/journals/content/jas/2006/jas.2006.119.issue-3/1.2166927/production/images/large/1.2166927.figures.f1.jpeg)



计算后验概率和最大似然估计

![](http://asa.scitation.org/na101/home/literatum/publisher/aip/journals/content/jas/2006/jas.2006.119.issue-3/1.2166927/production/images/large/1.2166927.figures.f2.jpeg)











