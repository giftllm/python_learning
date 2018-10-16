#Python内建的filter()函数用于过滤序列 filter()接收一个函数和一个序列
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):  #定义函数，is_odd
    return n % 2 == 1   #如果n 是2的倍数，则false，反之则返回true

L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))    #filter函数中，后面序列里面的值，在is_odd函数里面运行，
# 如果n 是2的倍数，则false，丢弃该元素，反之保留该元素。
print(L)

#用filter()这个函数，关键在于正确实现一个“筛选”函数
