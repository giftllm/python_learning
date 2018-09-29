# print("X value must be small than 1.0, please Enter x value again, Thanks")
x = float(input("X value must be smaller than 1.0, Enter the value: "))
n = term = num = 1
result = 1
while n <= 100:

    term *= x / n   # term = (x / n) * term
    result = result + term # result += term
    n += 1
    if term < 0.0001:
        break
print("No of time {} and Sum = {} ".format(n, result))
"""单独的if不能使用continue和break"""
"""10以内的乘法表"""
a = [2,3,'a',4]
a.append(45)
a.insert(1,23)
print(a)
print(a.count(23))
