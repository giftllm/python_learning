#利用map和reduce,把把符串'123.456'转换成浮点数123.456
#昨天学了map（）和reduce（）函数，map（f，L）是把L的每一个元素在f函数里面遍历，reduce（f，L）函数是将L里面的每个元素与上个f函数的结果在f里面运行
#先要把字符串转化为数字，

from functools import reduce #引用reduce函数，惯例
def strfloat(s):    #定义strfloat函数
    def strnum(s):  #定义个字典，字符创里面的’1‘对应整数1，以此类推
        return{'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}
    def f1(x,y):    #定义一个f1，x，y是小数点前面的数字
        return x*10 + y
    def f2(x, y):   #定义一个f2，x，月是小数点后面的数字
        return  x/10 + y
    pointIndex = s.index('.')    #.index('.')是确定字符串里面小数点的位置
    L1 = list(map(strnum, s[:pointIndex]))
    L2 = list(map(strnum,s[pointIndex+1:]))

    return reduce(f1, L1) + reduce(f2, L2)


#map（strnum，s[:pointIndex]），选出小数点前面的数字，s[:a]代表去s里面0到a-1的值
#reduce（f1，map），把小数点前面的值算出来
s =( '123.456')
print(s)

