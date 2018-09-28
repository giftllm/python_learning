#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-9))

from defdemo import my_abs  #调用函数

#计算圆的面积
"""
r = int(input("请输入圆的半径:"))
def area_of_circle(s):
    if r >= 0:
    return r
    s = 3.14*r**2
    print('圆的面积为：'.format(s))
    else:
    print("您输入的数值有误，请重新输入")
"""


import math
r = int(input("请输入圆的半径："))
s = math.pi*r*r
print("圆的面积为:{:.2f}".format(s))







