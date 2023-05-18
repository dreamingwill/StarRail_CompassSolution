# StarRail_CompassSolution
崩坏3：星穹铁道-解密游戏-引航罗盘-通解。思路：矩阵求解同余方程组。

明天再写用法、解法

---------------------

用法：

 <img src="https://github.com/dreamingwill/StarRail_CompassSolution/blob/main/%E7%BB%98%E5%9B%BE1.jpg" alt="compass" width="300"/>
 
如图，需要起点到终点的距离，转动角度（注意：逆时针转240°=顺时针转120°），罗盘控制情况。

即输入：

2 3 2

0 1 1

1 0 1

1 1 0

4 1 4

输出结果为：

最少要转5下

x1 = 3  (内中外)对应控制: 0 1 1

x2 = 2  (内中外)对应控制: 1 0 1

x3 = 0  (内中外)对应控制: 1 1 0


解法：

解方程：

$$ \begin{pmatrix}
2&0&0\\
0&3&0\\
0&0&2\\
\end{pmatrix}
\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&0\\
\end{pmatrix}
\begin{pmatrix}
x_1\\
x_2\\
x_3\\
\end{pmatrix}=
\begin{pmatrix}
6k_1+4\\
6k_2+1\\
6k_3+4\\
\end{pmatrix}$$


