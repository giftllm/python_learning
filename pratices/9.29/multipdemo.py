"""练习 10 以内的乘法表"""
i = 1
print("-"*50)
while i < 11:
    n = 1
    while n <= 10:
        print("{:4d}".format(i * n), end = '')       # end 的作用将结果输出到同一行，或者输出的末尾添加不同的字符
        n += 1
    print()
    i += 1
print("-"*50)


