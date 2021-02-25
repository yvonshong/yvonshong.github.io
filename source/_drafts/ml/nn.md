---
title: Neural Network
date: 2017-08-28 19:05:39
toc: true
---
神经网络
<!-- more -->
# 神经网络算法类型

1、有监督学习(Supervised learning):通过生成一个函数将输入映射为一个合适的输出（通常也称为标记，多数情况下训练集都是有人工专家标注生成的）。例如分类问题，分类器更加输入向量和输出的分类标记模拟了一个函数，对于新的输入向量，得到它的分类结果。

有监督学习主要会提供一些标注样本，分为两大问题：回归regression和分类classification

2、无监督学习(Unsupervised learning):与有监督学习相比，训练集没有人为标注的结果。常见的无监督学习算法有聚类。

无先验信息

3、半监督学习: 介于监督学习与无监督学习之间。

4、强化学习(Reinforcement learning): 通过观察来学习如何做出动作，每个动作都会对环境有所影响，而环境的反馈又可以引导该学习算法。

其他的类型包括推荐系统，Transduction，Learning to learn等




# 神经网络

## 结构

输入	$X=(x_1,x_2,\cdots, x_n)^T$

连接权	$w=(w_1,w_2,\cdots, w_n)$

网络输入	$net$=\Sigma x_i w_i

向量形式	$net=XW$

网络输出	$output=f(net)$



### 神经元

网络中的节点，多个输入，一个输出

$y=f(WX)+bias$

### 权重

多个输入对结果的影响有着不同的权重，本质就是节点内部的函数中对不同的输入x有着不同的权值。

### 偏差

除了与输入有关的量，也存在着bias常量对结果有影响。

### 输入输出隐藏层

输入层：被记作第0层。该层负责接收来自网络外部的信息

第j层：第j-1层的直接后继层（j>0），它直接接受第j-1层的输出。

输出层：它是网络的最后一层，具有该网络的最大层号，负责输出网络的计算结果。

隐藏层：除输入层和输出层以外的其它各层均叫隐藏层。隐藏层不直接接受外界的信号，也不直接向外界发送信号

输出层的层号为该网络的层数：n层网络或n级网络。

## 成本函数

衡量网络预测值和真实值之间的差距。可以理解为误差，整个网络的训练朝着降低误差的方向进行。

逻辑回归的0-1 cost function 把  0 1 合并

$J(\Theta) = - \frac{1}{m} [ \Sigma ^m_{i=1} \Sigma^K_{k=1} y^{(i)}_k log(h_{\Theta}(x^{(i)}))_k + (1- y^{(i)}_k)log(1-h_\Theta (x^{(i)})_k) ] + \frac{\lambda }{2m} \Sigma ^{L-1} _{l=1} \Sigma _{i=1}^{s_l} \Sigma _{j=1} ^{s_{l+1}} (\Theta _{ji} ^{(l)})^2$

$h_\Theta (x) \in R^K ;(h_\Theta(x))_i = i^{th}  output$ 第 $i$ 层的输出 hypothesis 假设值  y 真实值

$L$ ： 神经网络的层数

$s_l$ ：第$l$层的单元个数（不包括偏置单元bias）



**目标函数** 是 最小化cost function 

通常是取 平方误差函数 $min_\Theta (J(\Theta)$ ;$\frac{1}{2}$ 系数为方便求导

$\frac{1}{2m}\Sigma ^m _{i=1}(h_\theta(x^{(i)}) -y^{(i)})^2$  预测值-真实值



成本函数得是凸函数才能求到最小值



| 函数       | 公式                                       |
| -------- | ---------------------------------------- |
| 0-1 损失函数 | $L(Y,f(X))=\begin{cases} 1,  & Y\neq f(X)\\0,&  Y=f(X)\end{cases}$ |
| 平方损失函数   | $L(Y,f(X))=(Y-f(X))^2$                   |
| 绝对损失函数   | $L(Y,f(X))=\|Y-f(X)\|$                   |
| 对数损失函数   | $L(Y,P(Y\|X))=-logP(Y\|X)$               |



## 逻辑回归

分类是监督学习的一个核心问题，在监督学习中，当输出变量Y取有限个离散值时，预测问题便成为分类问题。这时，输入变量X可以是离散的，也可以是连续的。监督学习从数据中学习一个分类模型或分类决策函数，称为分类器(classifier)。分类器对新的输入进行输出的预测(prediction)，称为分类(classification).



二分类问题 {1,0} 将函数拉拢到 0,1 之间，靠阈值划分

$0\le h_\theta (x) \le 1$

线性回归无法将预测值全都拉到0，1之间

$h_\theta(x) = g(\theta^T x)$

$g(z)=\frac{1}{1+e^{-z}}$

阈值决定决策边界


# 参数调优

http://blog.csdn.net/han_xiaoyang/article/details/52654879

## 激活函数

激活函数是用来加入非线性因素的，因为线性模型的表达能力不够。

我们可以设计一种神经网络，通过激活函数来使得这组数据线性可分。
激活函数我们选择阀值函数（threshold function），也就是大于某个值输出1（被激活了），小于等于则输出0（没有激活）。这个函数是非线性函数。



| 函数                     | 公式                                       | 备注                                       | 优点                                       | 缺点                                       |
| ---------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| 线性函数 purelin           | $f(net)=k(net)+c$                        |                                          |                                          |                                          |
| 斜面函数 ramp function     | $f(x)=\begin{cases} T,  & x  \gt c \\ k*c& \|x\| \le c\\ -T, & x \lt c \end{cases}$ |                                          |                                          |                                          |
| 阈值函数 threhold function | $f(x)=\begin{cases} 1,  & x  \ge c\\ 0, & x \lt c \end{cases}$ |                                          |                                          |                                          |
| Sigmoid 型函数            | $f(net)=\frac{a+b}{1+exp(-d*net)}$       | $a<f(net)<a+b$；导数：$f'(net)=\frac{-d(a+b) e^{-d net}}{1+exp(-d*net)}$ | Sigmoid函数的输出映射在(0,1)之间，单调连续，输出范围有限，优化稳定，可以用作输出层；求导容易。 | 由于其软饱和性，容易产生梯度消失，导致训练出现问题；其输出并不是以0为中心的。  |
|                        | $f(x)=\frac{1}{1+e^{-\alpha x}} (0<f(x)<1)$ | 导数：$f'(x)=\frac{\alpha e^{-\alpha x}}{(1+e^{-\alpha x})^2} = f(x)[1-f(x)]$ |                                          |                                          |
| tanh函数                 | $tanh(x)=\frac{1-e^{-2x}}{1+e^{-2x}}$    |                                          | 比Sigmoid函数收敛速度更快；相比Sigmoid函数，其输出以0为中心。   | 相比Sigmoid函数，其输出以0为中心。                    |
| 双极S形函数                 | $f(x)=\frac{1}{1+e^{-\alpha x}}$         |                                          |                                          |                                          |
|                        | $f(x)=\frac{2\alpha e ^{- \alpha x}}{(1+e^{-\alpha x})^2} = \frac{\alpha [1-f(x)^2]}{2}$ | 双极S和Sigmoid函数主要区别在于值域；都是连续可导             |                                          |                                          |
| ReLU 整流线性单元            | $f(x)=max(x,0)$                          |                                          | 对于大于0的所有输入来说，它都有一个不变的导数值。常数导数值有助于网络训练进行得更快；相比起Sigmoid和tanh，ReLU(e.g. a factor of 6 in Krizhevsky et al.)在SGD中能够快速收敛。例如在下图的实验中，在一个四层的卷积神经网络中，实线代表了ReLU，虚线代表了tanh，ReLU比起tanh更快地到达了错误率0.25处。据称，这是因为它线性、非饱和的形式；Sigmoid和tanh涉及了很多很expensive的操作（比如指数），ReLU可以更加简单的实现；有效缓解了梯度消失的问题；在没有无监督预训练的时候也能有较好的表现；提供了神经网络的稀疏表达能力。 | 随着训练的进行，可能会出现神经元死亡，权重无法更新的情况。如果发生这种情况，那么流经神经元的梯度从这一点开始将永远是0。也就是说，ReLU神经元在训练中不可逆地死亡了。 |
| LReLU                  |                                          |                                          |                                          |                                          |
| PReLU                  |                                          |                                          |                                          |                                          |
| RReLU                  |                                          |                                          |                                          |                                          |
| ELU                    | $f(x)=\begin{cases} a(e^x-1),  & x  < 0\\ x, & 0 \le x \end{cases}$ |                                          | ELU减少了正常梯度与单位自然梯度之间的差距，从而加快了学习;在负的限制条件下能够更有鲁棒性。 |                                          |
| softplus               | $f(x)=log(e^x+1)$                        |                                          |                                          |                                          |
| softsign               | $f(x)=\frac{x}{\|x\|+1}$                 |                                          |                                          |                                          |
| Softmax函数              |                                          |                                          |                                          |                                          |




## 诊断（Diagnostics）

## 权重初始化（Weight Initialization）

## 网络拓扑（Network Topology）


## 优化和损失

## 早停法

## 学习率 

学习率影响着网络收敛的速度，以及网络能否收敛。学习率设置偏小可以保证网络收敛，但是收敛较慢。相反，学习率设置偏大则有可能使网络训练不收敛，影响识别效果。



## 梯度下降

调整 $\Theta$ 的时候，保持$J(\Theta)$ 递减，达到一个满意的最小值（极小值）

梯度下降描述的是更新$\Theta$ 的一种方法

$\theta_j := \theta_j -\alpha \frac{\partial }{\partial \theta_j} J(\theta)$  



$\alpha$ 学习速率 步长

如果过小 梯度下降速率很慢  过长则可能迈过最小点并发散

当函数接近局部最小值的时候，梯度下降法将自动的采取“小步子”， 所以没有必要随着时间的推移减小learning rate.

- 需要选择合适的learning rate ;

- 需要很多轮迭代；

- 但是即使n很大的时候效果也很好；


## 正规方程

Normal equation-区别于迭代方法的直接解法)

直接求解导数为0的极值点

$\frac{d}{d\theta}J(\theta = \cdots =0)$

在多变量中求对于所有变量 偏导数为0的点。

$\frac{\partial}{\partial\theta_j}J(\theta = \cdots =0)$

$\theta = (X ^T X)^{-1} X^{T} y$ 由最小二乘法推导出来 The partial derivatives of $|| Ax-b||^2 $ are zero when $A^TAx=A^Tb$

不需要选择 $\alpha$

不需要迭代，一次搞定；

但是需要计算 $(X^TX)^{-1}$，其时间复杂度为 $O(n^3)$

对于Normal Equation，如果 $X^TX$ 不可逆

- 去掉冗余的特征（线性相关）：
- 过多的特征，例如m <= n:  删掉一些特征，或者使用regularization



## 正则化(丢弃dropout)  

减少某参数的影响 加大惩罚

underfit  high-bias / overfit high-variance 

针对过拟合问题

a) 减少特征的数量：

- 人工的选择保留哪些特征；
- 模型选择算法

b) 正则化

- 保留所有的特征，但是降低参数$\theta_j$ 的量/值；
- 正则化的好处是当特征很多时，每一个特征都会对预测y贡献一份合适的力量；

正则化：

参数 $\theta_0,\theta_1,\theta_2,\cdots ,\theta_n$ 取小一点的值，这样的优点：

- “简化”的hypothesis；
- 不容易过拟合；

对除 某参数以外的参数进行惩罚，也就是正则化

本来代价函数是

$J(\theta)=\frac{1}{2m} \Sigma ^m_{i=1} (h_\theta(x^{(i)}) -y^{(i)})^2$

正则化后的

$J(\theta)=\frac{1}{2m} [\Sigma ^m_{i=1} (h_\theta(x^{(i)}) -y^{(i)})^2  +\lambda \Sigma ^n _{j=1} \theta _j^2]$

其中 $\lambda$ 成为正则化参数

正则化后的梯度下降算法为

- 未收到正则化的参数不变
- $\theta_j:=\theta_j -\alpha [\frac{1}{m} \Sigma^m_{i=1} (h_\theta(x^{(i)})-y^{(i)})x^{(i)}_j - \frac{\lambda}{m} \theta_j]$

如果 $\lambda$ 设为一个很大的值

- 算法依然会正常的工作, 将 $\lambda$ 设置的很大不会影响算法本身；
- 算法在去除过拟合问题上会失败；
- 算法的结构将是欠拟合（underfitting),即使训练数据非常好也会失败；
- 梯度下降算法不一定会收敛；



模型选择的典型方法是正则化。正则化是结构风险最小化策略的实现，是在经验风险上加一个正则化项(regularizer)或罚项(penalty term)。正则化项一般是模型复杂度的单调递增函数，模型越复杂，正则化值就越大。比如，正则化项可以是模型参数向量的范数。

正则化符合奥卡姆剃刀(Occam's razor)原理。奥卡姆剃刀原理应用于模型选择时变为以下想法：在所有可能选择的模型中，能够很好地解释已知数据并且十分简单才是最好的模型，也就是应该选择的模型。从贝叶斯估计的角度来看，正则化项对应于模型的先验概率。可以假设复杂的模型有较大的先验概率，简单的模型有较小的先验概率。



## 批次Batches
https://www.zhihu.com/question/32673260

批训练的引入最大好处是针对非凸损失函数来做的， 毕竟非凸的情况下， 全样本就算工程上算的动， 也会卡在局部优上， 批表示了全样本的部分抽样实现， 相当于人为引入修正梯度上的采样噪声，使“一路不通找别路”更有可能搜索最优值。

Batch 的选择，**首先决定的是下降的方向。**如果数据集比较小，完全可以采用**全数据集** （ **Full Batch Learning** ）的形式，这样做至少有 2 个好处：其一，由全数据集确定的方向能够更好地代表样本总体，从而[更准确地朝向极值所在的方向](http://www.zhihu.com/question/37129350/answer/70964527#)。其二，由于不同权重的梯度值差别巨大，因此选取一个全局的学习率很困难。 Full Batch Learning 可以使用**Rprop** 只基于梯度符号并且针对性单独更新各权值。

对于更大的数据集，以上 2 个好处又变成了 2 个坏处：其一，随着数据集的海量增长和内存限制，一次性载入所有的数据进来变得越来越不可行。其二，以 Rprop 的方式迭代，会由于各个 Batch 之间的采样差异性，各次梯度修正值相互抵消，无法修正。这才有了后来 **RMSProp** 的妥协方案。

可不可以选择一个适中的 Batch_Size 值呢？

当然可以，这就是批梯度下降法（Mini-batches Learning）。因为如果数据集足够充分，那么用一半（甚至少得多）的数据训练算出来的梯度与用全部数据训练出来的梯度是几乎一样的。

在合理范围内，增大 Batch_Size 有何好处？

- 内存利用率提高了，大矩阵乘法的并行化效率提高。
- 跑完一次 epoch（全数据集）所需的迭代次数减少，对于相同数据量的处理速度进一步加快。
- 在一定范围内，一般来说 Batch_Size 越大，其确定的下降方向越准，引起训练震荡越小。

盲目增大 Batch_Size 有何坏处？

- 内存利用率提高了，但是内存容量可能撑不住了。
- 跑完一次 epoch（全数据集）所需的迭代次数减少，要想达到相同的精度，其所花费的时间大大增加了，从而对参数的修正也就显得更加缓慢。
- Batch_Size 增大到一定程度，其确定的下降方向已经基本不再变化。




## 周期 Epochs

http://blog.csdn.net/han_xiaoyang/article/details/52654879 （好文）

batch size大小会决定最后的梯度，以及更新权重的频度。一个周期(epoch)指的是神经网络看一遍全部训练数据的过程。

你是否已经试验了不同的批次batch size和周期数？ 
之前，我们已经讨论了学习率，网络大小和周期之间的关系。

在很深的网络结构里你会经常看到：小的batch size配以大的训练周期。

下面这些或许能有助于你的问题，也或许不能。你要在自己的数据上尝试和观察。

- **尝试选取与训练数据同大小的batch size，但注意一下内存（批次学习（batch learning））**
- **尝试选取1作为batch size（在线学习（online learning））**
- **尝试用格点搜索不同的小的batch size（8，16，32，…）**
- **分别尝试训练少量周期和大量周期。**

考虑一个接近无穷的周期值(持续训练)，去记录到目前为止能得到的最佳的模型。

## 批量归一化

在深度神经网络的训练过程中，先前层参数的调整会导致之后每一层输入值的分布发生变化，这种现象使模型的训练变得很复杂。所以在深度神经网络模型的训练中，通常需要仔细选取初始参数并采取较小的学习率，这不但导致模型训练的效率低下，而且使得饱和非线性模型的训练极为困难。我们把这种现象称为内部协变量转移(covariate shift)，并通过归一化(normalizing)每层的输入来解决这个问题。我们方法的强大之处在于把归一化的步骤作为模型训练架构的一部分来实现, 并且对每个训练小批量都执行归一化操作。批量归一化允许我们使用很高的学习率并且对初始化不太在意。它在一定情况下也可以起到正则化的作用，并减轻了对Dropout的需求。

https://ask.julyedu.com/question/7706 




# 类型

前馈是从网络结构上来说的，是前一层神经元单向馈入后一层神经元，而后面的神经元没有反馈到之前的神经元；而BP网络是从网络的训练方法上来说 的，是指该网络的训练算法是反向传播算法，即神经元的链接权重的训练是从最后一层（输出层）开始，然后反向依次更新前一层的链接权重。

## 前馈神经网络(Feedforward Neural Networks)

$O_1=F_1(XW_1)$

$O_2=F_2(O_1W_2)$

$O_3=F_3(O_2W_3)$



## 反馈神经网络(Feedback Neural Networks)

基本的BP算法就是沿着负梯度方向通过调整权值来减小均方误差

Elman网络

Hopfield网络

## 自组织网络(Self-Organizing Neural Networks)

 自组织神经网络是一种无导师学习网络。它通过自动寻找样本中的内在规律和本质属性，自组织、自适应地改变网络参数与结构。

## 多层感知机

**多层感知器**（Multilayer Perceptron,缩写MLP）是一种前向结构的[人工神经网络](https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)，映射一组输入向量到一组输出向量。MLP可以被看作是一个有向图，由多个的节点层所组成，每一层都全连接到下一层。除了输入节点，每个节点都是一个带有非线性激活函数的神经元（或称处理单元）。一种被称为[反向传播算法](https://zh.wikipedia.org/wiki/%E5%8F%8D%E5%90%91%E4%BC%A0%E6%92%AD%E7%AE%97%E6%B3%95)的[监督学习](https://zh.wikipedia.org/wiki/%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0)方法常被用来训练MLP。[[1\]](https://zh.wikipedia.org/wiki/%E5%A4%9A%E5%B1%82%E6%84%9F%E7%9F%A5%E5%99%A8#cite_note-1)[[2\]](https://zh.wikipedia.org/wiki/%E5%A4%9A%E5%B1%82%E6%84%9F%E7%9F%A5%E5%99%A8#cite_note-2) MLP是[感知器](https://zh.wikipedia.org/wiki/%E6%84%9F%E7%9F%A5%E5%99%A8)的推广，克服了感知器不能对[线性不可分](https://zh.wikipedia.org/w/index.php?title=%E7%BA%BF%E6%80%A7%E4%B8%8D%E5%8F%AF%E5%88%86&action=edit&redlink=1)数据进行识别的弱点。

### MLP的缺陷

**1.**网络的隐含节点个数选取问题至今仍是一个 世界难题（Google, Elsevier, CNKI）；

**2.**停止阈值、学习率、动量常数需要采用”trial-and-error”法，极其耗时（动手实验）；

**3.**学习速度慢；

**4.**容易陷入局部极值，学习不够充分


