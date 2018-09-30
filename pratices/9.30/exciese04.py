# 在/home/shiyanlou/Code创建一个 名为 FindDigits.py 的Python 脚本，请读取一串字符串并且把其中所有的数字组成一个新的字符串，
# 并且打印出来。我们提供的字符串可以通过在命令行中输入如下代码来获取。
# wget http://labfile.oss.aliyuncs.com/courses/790/String.txt

file = open('D:\python\python_learning\pratices\9.30\String.txt')
txt = file.read()
str = []
for i in txt:
    if i.isdigit() == True:
        str.append(i)
print(' '.join(str))

# 运用知识点：文件提取，读写，循环