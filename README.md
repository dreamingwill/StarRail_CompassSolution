# StarRail_CompassSolution
崩坏3：星穹铁道-解密游戏-引航罗盘-通解。思路：矩阵求解同余方程组。

明天再写用法、解法

---------------------

用法：


![绘图1](https://github.com/dreamingwill/StarRail_CompassSolution/assets/55878187/c85b0dc2-db9b-44a9-9ab4-48426cf17866 =240)

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


