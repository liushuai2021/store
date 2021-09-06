
'''
    w:写
    r:读取
    +：
    a:附加

    b:字节

'''
'''
    代码示例：

str = "hello world"
before = str.split(" ")[0]
print(before)
输出：

hello
'''
try:
    file = open(file="baidu_x_system.log", mode="r+", encoding="utf-8")

    # data = file.read()  # read() 一下读取全文数据
    # readline() 读取一行数据

    # data = file.readline()
    # data1 = file.readline()
    data = file.readlines()  # readlines()将所有行的数据放在列表里

    # 写：w+  write()

    # file.write("\n\t赠汪伦")
    list=[]
    list0=[]
    list1=[]
    dect={}
    for i in range(len(data)):
        before = data[i].split(" ")[0]
        list.append(before)
    for key,value in enumerate(list):
        if list[key] in list[:key]:
            continue
        else:
            list0.append(list.count(list[key]))
            list1.append(list[key])
            dect[list[key]]=list.count(list[key])

    # print(list)
    # print(list1)
    print(dect)




except FileNotFoundError:
    print("没有这个文件！重新适配文件！")
finally:
    file.close()  # 关闭资源


