1.map（）和reduce（）的运用，str-float这个用例里面，用到了map（） reduce（） s.index('')检索参数，s[:]切片。map（x, y）:x为函数，y为列表；reduce（x，y），记住[1,2,3]怎么变成123就可以了，s.index('')可以检索字符串里面的元素；

2.filter()函数和map（）的相同和区别，
相同点，都是接收一个函数和一个序列，并且输出结果也是一个list。
不同点，filter函数是一个刷选函数，根据返回值是True还是False决定保留还是丢弃该元素，map（）直接返回一个list
