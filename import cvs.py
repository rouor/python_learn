import csv

with open("mytest.csv",encoding='utf-8-sig')  as r:
    print("内容如下\n")
    reader = csv.reader(r)
    #使用csv的reader()方法，创建一个reader对象
    for content in reader:
    #遍历reader对象的每一行
        print(content)

print("读取完毕！")
