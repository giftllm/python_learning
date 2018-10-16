#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写
'''
L = ['adam', 'LISA', 'barT'] #定义一个类表
def f(x):   #定义函数f（x）
    x = x.title()       #.title() 每个单词的第一个字母转化为大写，其余小写
    #x = x[0].upper() + x[1:].lower()    #x的第一个字母大写，从第二个字母开始小写，.upper()小写， .lower（）大写
    return x
print(list(map(f,L)))   #以列表行书输出结果，使用map（）函数，把L的值放进f（x）函数中遍历
#print(map(f,L)) 开始没把map（f,L）变成list，运行结果为：<map object at 0x0000000001DC34A8>