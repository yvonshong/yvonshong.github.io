---
title: 深入理解线性代数
date: 2017-02-21 00:25:00
---
本文为台交大周志成教授[ccjou.wordpress.com/](https://ccjou.wordpress.com/) 的阅读笔记和总结，感谢周志成教授。

//TODO
<!-- more -->
[強打推薦文章](https://ccjou.wordpress.com/%E9%96%B1%E8%AE%80%E5%B0%8E%E5%BC%95/%E5%BC%B7%E6%89%93%E6%8E%A8%E8%96%A6%E6%96%87%E7%AB%A0/)

[专题研究](https://ccjou.wordpress.com/%E5%B0%88%E9%A1%8C%E6%8E%A2%E7%A9%B6/)

[LaTeX数学公式](https://zh.wikipedia.org/wiki/Help:%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F)




# [矩阵乘法](https://ccjou.wordpress.com/2010/06/18/%E7%B7%9A%E6%80%A7%E4%BB%A3%E6%95%B8%E7%9A%84%E7%AC%AC%E4%B8%80%E5%A0%82%E8%AA%B2-%E7%9F%A9%E9%99%A3%E4%B9%98%E6%B3%95%E7%9A%84%E5%AE%9A%E7%BE%A9/)


$f\begin{pmatrix}x  \\y \end{pmatrix} = \begin{pmatrix}ax+by  \\cx+dy  \end{pmatrix}$

$g\begin{pmatrix}x  \\y \end{pmatrix} = \begin{pmatrix}px+qy  \\rx+sy \end{pmatrix}$

$h\begin{pmatrix}x  \\y \end{pmatrix} =f \begin{pmatrix} \begin{pmatrix}x  \\y  \end{pmatrix}  \end{pmatrix}=f \begin{pmatrix} px+qy\\ rx+sy  \end{pmatrix} = \begin{pmatrix} a(px+qy)+b(rx+sy) \\ c(px+qy)+d(rx+sy)\end{pmatrix}=\begin{pmatrix}(ap+br)x+(aq+bs)y\\ (cp+dr)x+(cq+ds)y\end{pmatrix}$

$F=\begin{bmatrix}a&b\\c&d\end{bmatrix}$

$G=\begin{bmatrix}p&q\\r&s\end{bmatrix}$

$H=\begin{bmatrix}ap+br&aq+bs\\cp+dr&cq+ds\end{bmatrix}$

$F\cdot G=H $

线性复合映射

# [左乘右乘](https://ccjou.wordpress.com/2010/12/24/%E5%B7%A6%E4%B9%98%E9%82%84%E6%98%AF%E5%8F%B3%E4%B9%98%EF%BC%8C%E9%80%99%E5%B0%B1%E6%98%AF%E5%95%8F%E9%A1%8C%E6%89%80%E5%9C%A8/)