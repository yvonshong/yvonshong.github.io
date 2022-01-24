---
title: 键盘摄影（六）——相机成像模型
date: 2020-05-22 00:19:00
categories: tech
tags: 
- photography
- camera
toc: true
---

本篇文章更多的是计算机视觉的基本知识，讲解真实的 3D 世界投影到相机的 2D 图像的这个过程。

<!-- more -->

# 坐标变换

首先需要介绍的是我们如何用数学工具来表示物体在坐标中位姿（位置+姿态）的变换。

我们线性代数学习的矩阵*向量的乘法，其本质是对向量进行变换，如下述的旋转过程，v 向量变换到 v' 向量，可以用矩阵来表示为

![](https://pic3.zhimg.com/v2-e1ebe291f2772f3833c8c9ab85acceb6_r.jpg)

> *旋转*

$$\begin{bmatrix}  x' \\ y'  \end{bmatrix} =  \begin{bmatrix}  cos\theta && -sin\theta\\ sub\theta && cos \theta  \end{bmatrix}*\begin{bmatrix}  x \\ y  \end{bmatrix}$$

平移可以表示为

![](https://pic3.zhimg.com/v2-899529d1f72fce9d1d8322e0f82b3a9a_r.jpg)

> *平移*

$$\begin{bmatrix}  x' \\ y'  \end{bmatrix}= \begin{bmatrix}  x \\ y  \end{bmatrix} + \begin{bmatrix}  t_x \\ t_y  \end{bmatrix}$$

整理起来

$$\begin{bmatrix}  x' \\ y'  \end{bmatrix} =  \begin{bmatrix}  cos\theta && -sin\theta\\ sub\theta && cos \theta  \end{bmatrix}*\begin{bmatrix}  x \\ y  \end{bmatrix}+\begin{bmatrix}  t_x \\ t_y  \end{bmatrix}$$

$$v' =  \begin{bmatrix}  R && t\\ 0 && 1  \end{bmatrix}*v$$

为了再继续统一成一个整体的变换，我们使用齐次的表达式

$$X_{camera}=\begin{bmatrix}  x_c \\ y_c \\ z_c  \end{bmatrix} , X_{world}=\begin{bmatrix}  x_w \\ y_w\\ z_w  \end{bmatrix}$$

$$\begin{bmatrix}  X_{world} \\ 1  \end{bmatrix} =  \begin{bmatrix}  R^T && -R^T t \\ 0 && 1  \end{bmatrix} \begin{bmatrix}  X_{camera} \\ 1  \end{bmatrix}$$

# 世界坐标系到相机坐标系

理解了坐标系内的变换，我们便可以使用数学工具来描述世界坐标系下的物体，在相机坐标系下的位置，本质就是一个坐标系的变换。

![](https://pic2.zhimg.com/80/v2-b45a02f0b2941e326f9119e790df6b95_720w.jpg)

$$X_{camera}=\begin{bmatrix}  x_c \\ y_c \\ z_c  \end{bmatrix} , X_{world}=\begin{bmatrix}  x_w \\ y_w\\ z_w  \end{bmatrix}  $$

$$X_{camera} = RX_{world}+t$$

$$\begin{bmatrix}  X_{camera} \\ 1  \end{bmatrix} =  \begin{bmatrix}  R && t \\ 0 && 1  \end{bmatrix} \begin{bmatrix}  X_{world} \\ 1  \end{bmatrix}$$

而旋转矩阵是正交矩阵，矩阵的逆等于矩阵的转置，上述逆变换可以表示为

$$X_{world} = R^T X_{camera}- R^T t$$

$$\begin{bmatrix}  X_{world} \\ 1  \end{bmatrix} =  \begin{bmatrix}  R^T && -R^T t \\ 0 && 1  \end{bmatrix} \begin{bmatrix}  X_{camera} \\ 1  \end{bmatrix}$$

根据坐标系的转换关系，也可以直接得到相机中心在世界坐标系中的位置

$$O_{cam}^{world} = R^TO_{cam}^{camera}-R^Tt = -R^Tt$$

# 针孔相机成像模型

初中物理中我们便学过的针孔相机模型可以近似为小孔成像模型，而我们日程生活中接触到的相机大部分是按照针孔相机模型来设计的，镜头组实现针孔的作用，让光照射到了 CMOS 上，汇聚了更多光的同时，也由于工艺的原因带来了畸变。在不考虑畸变或者恢复畸变的前提下，我们可以用下述小孔成像模型来模拟拍摄物体，镜头，CMOS 上的像的关系。

![](https://pic1.zhimg.com/v2-66d7752c7c57cb2ddbe675593922c990_r.jpg)

物体在 A 点，Z 为物距，BP' 为像平面，X 为水平方向上的距离，Y 为竖直方向上的距离，该图为水平方向截面图，并将符号皆表示为正。

$$\frac{Z}{f} =  \frac{X}{X'} =  \frac{Y}{Y'}$$

$$X' =f \frac{X}{Z}, Y' =f \frac{Y}{Z}$$

但其实我们可以直接构造出一个虚拟的归一化像平面，与物理像平面平行（距离相机光心距离为 f ），距离相机光心距离为 1。

因为最后生成的图片（像素平面）受制于成像元件大小不一而不同，物理像平面的比例又和焦距有关。我们使用归一化像平面，这只与物体的相机坐标有关，然后根据焦距可以恢复为物理像平面，再根据成像元件的像素恢复成图像。

$$\frac{Z}{1} =  \frac{X}{x} =  \frac{Y}{y}$$

$$\begin{bmatrix}  x \\ y \\1 \end{bmatrix}  =\frac{1}{z_c} \begin{bmatrix}  x_c \\ y_c \\ z_c \end{bmatrix} $$

X',Y'可表示物理像平面上点(X',Y')，X,Y 为相机坐标系下物体的点 $(x_c, y_c)$ ，那么我们可以表示为

$$\begin{bmatrix}  X' \\ Y' \end{bmatrix}  = \begin{bmatrix}  f\frac{x_c}{z_c} \\ f \frac{y_c}{z_c} \end{bmatrix} = \begin{bmatrix}  f x \\ f y \end{bmatrix} $$

而像素平面上的点其像素坐标 (u,v)，它的坐标原点在图像的左上角，而上述的物理像平面是中心为原点，所以我们需要移动坐标原点：

![](https://pic2.zhimg.com/v2-1e4d538b1aaa415c38bffeef29ff6241_r.jpg)

$$\begin{bmatrix}  u \\ v  \end{bmatrix} =  \begin{bmatrix}  \frac{X'}{dx} + c_x\\  \frac{Y'}{dy}+c_y  \end{bmatrix} $$

dx, dy 分别为图像上每一个像素点在 u 轴、v 轴方向上的物理尺寸（单位为米每像素），通常普通相机的 dx，dy 是相等的，即传感器的一个像素是长宽相等的。

cx,cy 分别为图像物理坐标系原点 O′ 在图像像素坐标系下 u 轴、v 轴的坐标（单位为像素） ，通常为图片像素长宽的的一半。

最后整理可得

$$\begin{bmatrix}  u \\ v  \end{bmatrix} =  \begin{bmatrix}  \frac{f}{dx}\frac{X}{Z} + c_x\\  \frac{f}{dy} \frac{Y}{Z}+c_y  \end{bmatrix}  = \begin{bmatrix}  f_x \frac{X}{Z} + c_x\\ f_y \frac{Y}{Z}+c_y  \end{bmatrix} $$

通常 fx = fy

![](https://pic4.zhimg.com/80/v2-840b26867ec61861a6a17763b42df5f7_720w.jpg)

我们再写成齐次的形式

$$ \begin{bmatrix}  u \\ v \\ 1  \end{bmatrix} =  \frac{1}{Z_c} \begin{bmatrix}  f_x  && 0 && c_x\\ 0  && f_y && c_y\\ 0 && 0 && 1  \end{bmatrix}  \begin{bmatrix} I_{3*3} | 0_{3*1} \end{bmatrix}    \begin{bmatrix}  X_c\\ Y_c\\ Z_c\\ 1  \end{bmatrix} \\ = \frac{1}{Z_c} \begin{bmatrix}  f_x  && 0 && c_x\\ 0  && f_y && c_y\\ 0 && 0 && 1  \end{bmatrix}  \begin{bmatrix} I_{3*3} | 0_{3*1} \end{bmatrix}     \begin{bmatrix}  R && t \\ 0  && 1  \end{bmatrix}  \begin{bmatrix}  X_w\\ Y_w\\ Z_w\\ 1  \end{bmatrix} \\  =  \frac{1}{Z_c} K  \begin{bmatrix} I_{3*3} | 0_{3*1} \end{bmatrix}     \begin{bmatrix}  R && t \\ 0  && 1  \end{bmatrix}  \begin{bmatrix}  X_w\\ Y_w\\ Z_w\\ 1  \end{bmatrix} $$

在上述公式中，我们可以把 transformation 矩阵（Rt）前的矩阵视为相机的内参，transformation 矩阵为相机的外参（它在世界坐标系下的位置）。

所以我们通过将

**世界坐标 -> 相机坐标 ->归一化像平面->物理像平面->像素平面**

完成了把世界坐标中的 3D 点投影到图片像素坐标的 2D 点。

# 鱼眼相机成像模型

上述我们讲完了针孔相机的成像模型，但世界上还存在着其他类型的相机，比如鱼眼相机，由十几个不同的透镜组合成一个鱼眼镜头组，前面的镜头通过折射扩大了相机的视野范围，后面的镜头组是为了像针孔相机一样，景深内的物体能够像小孔成像一样清晰地成像。

我们再来看一看相机坐标系下的物体在鱼眼相机中是怎么成像的。

![](https://pic4.zhimg.com/v2-1c49b58d80b53f3c703ece8670c3fe2f_r.jpg)

鱼眼相机的投影模型为了将尽可能大的场景投影到有限的图像平面内，允许了相机畸变的存在。我们可以把鱼眼相机简化成一个利用球面透镜发生折射的模型（相比于针孔相机是小孔成像，其中符合相似三角形关系）。

![](https://pic2.zhimg.com/80/v2-bf38684a198076bfb16b0859d4157871_720w.jpg)

而由于折射率设计的不同，我们简单介绍几种常见的投影模型。投影模型主要讲解了相机坐标系下的点是如何投影到球面透镜上，然后在图像平面成像的。

## 等距投影模型

![](https://pic1.zhimg.com/80/v2-aeaa153c2963822c4d3c15b9ac3cd4c0_720w.jpg)

$$r_d =f \theta$$

而 OpenCV 中最常用到的投影模型即是等距模型发展出来的，对相机进行畸变标定，而鱼眼相机可以视为只有径向基本，找到标定系数使得

$$\theta_d = k_0 \theta + k_1 \theta ^3 + k_2 \theta ^5 +k_3 \theta ^7+ k_4 \theta ^9$$

$$r =tan(\theta_d)$$

## 等立体角投影模型

![](https://pic1.zhimg.com/80/v2-5dab2b2aefc62c98f836d77888496cac_720w.jpg)

$$r_d =2f sin(\frac{\theta}{2})$$

## 正交投影模型

![](https://pic3.zhimg.com/80/v2-a6f3eaf27c36fc90a31cfc43fb6a3fca_720w.jpg)

$$r_d =f sin(\theta)$$

## 体视投影模型

![](https://pic3.zhimg.com/80/v2-df876dc8ccbf38f04aa615bd8cc6eaca_720w.jpg)

$$r_d =2ftan(\frac{ \theta}{2})$$

我们可以用下图来横向比较不同投影模型直接的关系

![](https://pic3.zhimg.com/v2-bcb8383afc12ef2910a6d8a1f59f44be_r.jpg)

![](https://pic4.zhimg.com/80/v2-39c65395276279413ff6cff5b2dfb61b_720w.jpg)

而鱼眼相机的整个成像模型可以表示为

**世界坐标系 -> 相机坐标系 -> 归一化平面坐标系 -> 物理像平面 -> 像素坐标系**

![](https://pic1.zhimg.com/80/v2-4a8fe2b1989692fe004bf2bb23d5ac04_720w.jpg)

**相机坐标系 -> 归一化平面坐标系**

$$\begin{bmatrix}  x_c  \\ y_c \end{bmatrix}  =\frac{1}{Z_c} \begin{bmatrix}  X_c \\ Y_c  \end{bmatrix} $$

归一化平面坐标系 -> 物理相平面

$$\begin{bmatrix}  X' \\ Y'  \end{bmatrix}  = \begin{bmatrix} r*cos\phi \\r*sin\phi \end{bmatrix} $$

$$\phi = arctan(Y'/X')$$

$$r^2 = X'^2 +Y'^2 $$

$r,f,\theta$ 满足上述之一的投影关系

$$r = t(\theta, f)$$

在 OpenCV 中， $\theta$ 和 r 满足：

$$r = tan(k_0 \theta + k_1 \theta ^3 + k_2 \theta ^5 +k_3 \theta ^7+ k_4 \theta ^9)$$

$$\begin{bmatrix}  u  \\ v \end{bmatrix}  =  \begin{bmatrix}  f_x \frac{\theta_d}{r} x_c + c_x \\ f_y \frac{\theta_d}{r} x_y +c_y  \end{bmatrix} $$

写成齐次式可得

$$\begin{bmatrix}  u \\ v \\ 1  \end{bmatrix} =  \frac{1}{Z_c} \begin{bmatrix}  f_x  \frac{\theta_d}{r} && 0 && c_x\\ 0  && f_y \frac{\theta_d}{r} && c_y\\ 0 && 0 && 1  \end{bmatrix}  \begin{bmatrix} I_{3*3} | 0_{3*1} \end{bmatrix}     \begin{bmatrix}  X_c\\ Y_c\\ Z_c\\ 1  \end{bmatrix}  $$

# 全景相机成像模型

全景相机的成像模型就十分复杂了，这里我们只做简单的介绍镜头成像光路。

- 鱼眼型


![](https://pic1.zhimg.com/80/v2-c10904996e1f693a11b90b10facbf604_720w.jpg)

> 靠多个透镜实现鱼眼

![](https://pic3.zhimg.com/80/v2-1c623b7ef84795e54fc6f23a4d6fc88a_720w.jpg)

> 靠反射实现鱼眼

![](https://pic2.zhimg.com/80/v2-cc33df833dcfb83822204691b6dc9369_720w.jpg)

> 多路相机拼接

---

欢迎在我的专栏「[自律走行](https://www.zhihu.com/column/jiritsu-soko)」中查看更多「键盘摄影」系列文章

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