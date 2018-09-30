s = "Li li ming1"
print(s.istitle())  #判断是否为标题格式
print(s.title())    #转换成标题格式，即首字母大写
print(s.upper())    #转换字符，全部大写的版本
print(s.lower())    #转换字符串，全部小写的版本
print(s.swapcase())     #转换字符串，大小写
print(s.isalnum())      #检查所有字符是否为字母数字
print(s.isalpha())      #检查字符串是否只有字母
print(s.isdigit())      #检查字符串是否所有字符为数字
print(s.lower())        #检查字符串是否为小写
print(s.isupper())      #检查字符串是否所有未大写

# 回文是一种无论从左还是从右读都一样的字符序列。比如 “madam”。在这个例子中，我们检查用户输入的字符串是否是回文，并输出结果。
s = input("please enter a string:")
z = s[:: -1]
if s == z:
    print("the string is a palindrome")
else:
    print("The string is not a palindrome")
