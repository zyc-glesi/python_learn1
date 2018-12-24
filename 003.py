#coding:utf-8
#验证 Phthon 引号的用法

first = 5
second = 8
third = first + second
print third

first = '5'
second = '8'
third = first + second
print third

first = "5"
second = "8"
third = first + second
print third

# 结果 13 58 58 。单引号 双引号没有区别

#Score = 7
#Score = Score + '1'
#print Score

#上面这个是错误的 int + str

#计算
print 7/2
print 7.0/2

print 7 ** 5
#很多语言使用^ 符号，在python中这个符号另外有意义。

print 7 % 2
#求取余数

a = 2.5e6
b = 1.2e7
print a+b
