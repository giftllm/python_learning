while True:
    n = int(input("please Enter an integer:"))
    if n < 0:
        continue    #返回到循环开始执行的地方
    elif n == 0:
        break   #如果值为0 则跳出循环
    
    print("Square is ", n ** 2)
print("ok")