#  file object = open(file_name [, access_mode][, buffering])
"""fo = open("foo.txt", "wb")
print("Name of the file:", fo.name)
print("cloase or not:", fo.close)
print("open mode:", fo.mode)
fo.close
print("close or not:", fo.close)
"""

# open a file
f = open("foo.txt", "r", encoding= 'UTF-8')
b = f.read()
print(b)

c = f.readline()
print(c)
f.close
# f.read(size)读取一定数目的数据，然后作为字符串或者字节对象返回 ，size是一个可选数字类型参数，当size数值为空或者负时，则读取文件所有内容。
