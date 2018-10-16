#Python内建了map()函数
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# ex: f(x)= x2 用map（）把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上

def f(x):   #定义一个函数名为f，变量为x的函数
    return x*x  #返回值为x*x
r = map(f,[1,2,3,4,5,6,7,8,9]) #使用map（）函数，里面有两个参数，第一个是函数，第二个是iter
print(list(r))  #把r的输出结果以list形式打印出来

#不用map（）函数的实现方法：
L = []          #先定义一个全局变量L
for n in [1,2,3,4,5,6,7,8,9]:   #使用for循环语句遍历数组里面的值
    L.append(f(n))#每一次循环，都把f（n）的值末尾添加到L里面
    print('L1=',L)      #print的位置不同，输出的结果不一样
print("L2=", L)      #打印L

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  #把这个list所有数字转为字符串：解析一下：先从map（str，[1, 2, 3, 4, 5, 6, 7, 8, 9]）,通过fuction
# str 把数组里面的值都转化为字符串形式，list（map（）），按照list的格式输出结果
print(list(map(int, ['1','2'])))
