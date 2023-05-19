# StarRail_CompassSolution
崩坏3：星穹铁道-解密游戏-引航罗盘-通解。思路：矩阵求解同余方程组。

---------------------

## 用法：

 <img src="https://github.com/dreamingwill/StarRail_CompassSolution/blob/main/compass.jpg" alt="compass" width="300"/>
 
如图，需要起点到终点的距离，转动角度（注意：逆时针转240°=顺时针转120°），罗盘控制情况。

即输入：

2 3 2

0 1 1

1 1 0

1 0 1

4 1 4

输出结果为：

最少要转5下

x1 = 3  (内中外)对应控制: 0 1 1

x2 = 0  (内中外)对应控制: 1 1 0

x3 = 2  (内中外)对应控制: 1 0 1




## 解法：

解方程：

$$ \begin{pmatrix}
4&0&0\\
0&1&0\\
0&0&4\\
\end{pmatrix}
\begin{pmatrix}
0&1&1\\
1&1&0\\
1&0&1\\
\end{pmatrix}^{\mathrm{T}}
\begin{pmatrix}
x_1\\
x_2\\
x_3\\
\end{pmatrix}=
\begin{pmatrix}
6k_1+2\\
6k_2+3\\
6k_3+2\\
\end{pmatrix}$$

得出
$x_1,x_2,x_3$
关于
$k_1,k_2,k_3$
的表达式，再取整数。得出最优解（总步数最小）。
