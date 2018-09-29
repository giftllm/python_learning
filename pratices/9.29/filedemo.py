def wfile():     #定义写文件函数
    try:
        filename = "D:\python\shiyanlou\9.29" + "test.html" #定义文件路劲和文件名变量
    except IOError:
        print("file create error")
    else:
        fp = open(filename, 'wb')       #打开写文件
        fp.write('test'.encode('utf-8'))        #将test字符串写入到文件中
        fp.close()      #关闭写文件

def rfile():
    try:
        filename = "D:\python\shiyanlou\9.29" + "test.html"
        fp = open(filename, 'r')#定义读文件路劲和文件名变量
    except IOError:
        print('file open error')
    else:
        for f in fp:    #循环读取每行数据
            print("file date is " +  f)
        fp.close()
if __name__ == '__main__':
    #readSQL()
    wfile()
    rfile()
    print("Done")