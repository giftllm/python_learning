def starbar(num):
    print(" * " * num)

def hashbar(num):
    print(' # ' * num)

def simplebar(num):
    print(' _ ' * num)

'''
在解释器中导入模块，import Moudlar_bar
必须使用模块名来访问模块中的函数
1. Moudlar_bar.starbar(num)
2. from Moudlar_bar import simplebar, starbar

'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))