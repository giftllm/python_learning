"""请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0
的两个解。
提示：计算平方根可以调用math.sqrt()函数：
"""
import math
#a = int(input("input value a"))
#b = input("input value b")
#c= input("input value c")
def my_quardratic(a,b,c):   #记得打冒号
    if not isinstance(a, (int , float)):
        print("a is not a number, please try again")
    if not isinstance(b, (int, float)):
        print("b is not a number, please try again")
    if not isinstance(c, (int, float)):
        print("c is not a number, please try again")
    d = b*b - 4*a*c
    if d < 0:
        return 'b*b - 4*a*c', d , "小于零，方程无解"
    else:
        if a == 0:
            if b == 0:
                if c == 0:
                    return '解为全体实数'
                else:
                    return '无解'
            else:
                x1 = -c/b
                x2 = x1
                return x1,x2
        else:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            return x1, x2
print(my_quardratic(2,3,1))
print(my_quardratic(0,0,0))
print(my_quardratic(1,0,1))
print(my_quardratic(2,0,0))