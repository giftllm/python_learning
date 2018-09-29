# 两个函数的乘积
def product(x, y):
    return  x * y

#多个函数的乘积
def product(x, *args):
    result = 1
    for n in args:
        result = result * n
    return x * result

# *args 可以传递除x以外的所有值，*kwargs 是用来传送键值
