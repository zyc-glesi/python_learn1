#coding:utf-8
#输入
print "输入你的名字"
somebody = raw_input()
print "Hi",somebody,"今天过得如何？"

#使用逗号，将多个print语句合并到同一行，并输出空格

someissue = raw_input("你会过得更好吧？")
print '相信你说的',someissue,'！'

print "请输入一个数：",
#somenumber = float(raw_input())
somenumber2 = int(raw_input())
print '聪明的我收到你的这个数：',somenumber2

#int 不能像上面那样用？不是，确切的说，这样的用法组合，实际上要求了输入者输入时候的数字类型，而不是我想象的会对任何数字类型进行转换。
#天啊 最重要的问题，其实是  raw_input 获取的是字符串