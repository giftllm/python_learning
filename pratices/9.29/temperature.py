#  C = (F - 32) / 1.8 将华氏温度转为摄氏温度。
'''
f = 0
while f <= 250:
    c = (f - 32)/ 1.8
    print("{:5d} {:7.2f}".format(f, c))
    f = f + 25
'''
#天数和月的转换
'''
days = int(input("Enter days:"))
months = days // 30
days = days % 30
print("Month = {}, Days = {}".format(months, days))
'''
#使用元组来实现：
days = int(input("Enter days:"))
print("Month = {} Days = {}".format(*divmod(days, 30)))
#divmod(a, b) 返回一个元组，这个元组包含两个值，第一个值a 是a//b, 第二个值是 a/b

#100以内 2的n次方值

n = 100
a = 2
while a <= n:
    print(str(a))
    a *= a

#Python 中赋值语句执行时会先对赋值运算符右边的表达式求值，然后将这个值赋值给左边的变量。

a, b = 0 ,1
while b <= 100:
    print(b)
    a , b = b, a + b
