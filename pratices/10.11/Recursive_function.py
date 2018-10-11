#递归函数：
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#计算阶乘n! = 1 x 2 x 3 x ... x n
def fact(n):    #定义fact函数
    if n == 1:  #如果n 的值等于1，则函数返回值为1
        return 1
    return n * fact(n - 1)  #返回值n*fact（n - 1），在函数内部调用本身函数，n的值没循环一次，n- 1，直到n的值变为1

print(fact(3))
#print(fact(1000))      使用递归函数需要注意防止栈溢出,函数调用是通过栈（stack）这种数据结构实现的
# 每当进入一个函数调用，栈就会加一层栈帧
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#解决递归调用栈溢出的方法是通过尾递归优化

def fact_1(n):      #定义face_1函数
    return fact_2(n, 1) #函数返回值 fact_1(n ,1)
def fact_2(num, product):    #一定函数fact_2(num,product),里面有两个变量，num，product
    if num == 1:        #如果num的值为1，返回product值
        return product
    return fact_2(num - 1, num * product)   #fact_2(num - 1, num * product)
print(fact_1(100))
#尾递归优化也不能结果fact（1000）的栈溢出问题。

