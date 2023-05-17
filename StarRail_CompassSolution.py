import sympy
from sympy import symbols


sympy.init_printing()
x1, x2, x3 = symbols('x1 x2 x3')  # 定义自变量x1, x2, x3
k1, k2, k3 = symbols('k1 k2 k3')  # 定义任意整数k
AA = sympy.zeros(3,3)

def input_load():
    b1,b2,b3 = map(int,input('请输入初始位置，内、中、外圈，即分别与终点差了几个60°，以空格隔开：').split(' ')) # 初始位置
    a11,a12,a13 =  map(int,input('请输入第一种转法控制的内中外圈，以空格隔开：').split(' '))
    a21,a22,a23 =  map(int,input('请输入第二种转法控制的内中外圈，以空格隔开：').split(' '))
    a31,a32,a33 =  map(int,input('请输入第三种转法控制的内中外圈，以空格隔开：').split(' '))
    a1,a2,a3 = map(int,input('请输入内、中、外圈顺时针方向转了几个60°角，以空格隔开：').split(' '))

    A1 = sympy.Matrix([[a1,0,0],
                    [0,a2,0],
                    [0,0,a3],])
    global AA
    AA = sympy.Matrix([[a11,a12,a13],
                    [a21,a22,a23],
                    [a31,a32,a33],])
    AA_t = AA.T
    A = A1*AA_t
    b = sympy.Matrix([b1,b2,b3])
    k = sympy.Matrix((6*k1,6*k2,6*k3))
    b = b+k
    Ab = A.col_insert(3,b) # 增广矩阵
    # 样例：
    # b = sympy.Matrix((3,3,2)) # 初始位置 
    # Ab = sympy.Matrix((  # 方程参数矩阵，为系数阵的增广矩阵
    #     (3, 3, 0, 6*k1+3),
    #     (3, 0, 3, 6*k2+3),
    #     (0, 2, 2, 6*k3+2),
    # ))
    return Ab


def solve(Ab):
    min_k = [-1,-1,-1]
    dict_x123 = sympy.solve_linear_system(Ab, x1, x2, x3) #求解 Ax = b 返回一个字典，x1 x2 x3 是关于k1，k2，k3的表达式 我们要求 x1 x2 x3 都大于0 且为整数
    #print(dict_x123)
    k_vals = [(k1, k2, k3) for k1 in range(6) for k2 in range(6) for k3 in range(6)] # 生成一个k1, k2, k3的遍历，[0~5,0~5,0~5] 
    min = 99999 # 记录最少移动次数
    for k in k_vals:
        move_sum = 0
        for key, value in dict_x123.items():  # 输出方程结果 需要遍历k，使x1 x2 x3 都为整数
            x_n = value.subs([(k1,k[0]),(k2,k[1]),(k3,k[2])]) # 
            isInt = sympy.simplify(x_n).is_integer
            if(x_n>=0 and isInt):            
                move_sum += x_n
            else:
                move_sum = 9999
                break
        
        if(move_sum < min and move_sum != 9999):
            #print(xx)
            min = move_sum
            min_k = k
            print('取正整数(k1,k2,k3) = ',min_k)

    print('最少要转{}下'.format(min))

    for i, (key, value) in enumerate(dict_x123.items()):  # 输出方程结果 需要遍历k，使x1 x2 x3 都为整数
        min_x_n = value.subs([(k1,min_k[0]),(k2,min_k[1]),(k3,min_k[2])])
        print('x{} = {}'.format(i+1,min_x_n), '\t(内中外)对应控制:', AA.row(i)[0], AA.row(i)[1], AA.row(i)[2])


# 测试用例
# in:
# 3 3 2
# 1 1 0
# 1 0 1
# 0 1 1
# 3 3 2
# out:
# (k1,k2,k3) =  (0, 1, 1)
# 最少要转4下
# x1 = 0
# x2 = 1
# x3 = 3

if __name__ == '__main__':
    Ab = input_load() # Ab是求解的增广矩阵
    solve(Ab)
    
