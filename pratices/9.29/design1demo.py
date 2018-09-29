row = int(input("please Enter lows: "))
n = m = row
while n >= 0:
    x = "* " * n
    print(x)
    n -= 1
    if n == 0:
        break

i = 1
while i <= m:
    x = "* " * i
    print(x)
    i += 1