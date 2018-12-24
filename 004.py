#coding:utf-8
#数据的类型
a = 36.78
b = int(a) #取整，非四舍五入
c = float(a)
d = str(a)
e = '0'
f = d+e
print a,b,c,f
print type(f) #确定类型

#coding:utf-8
#验证 Phthon 引号的用法#coding:utf-8
#验证 Phthon 引号的用法

#写一个程序，把温度从华氏度转换为摄氏度。转换公式是 C=5/9*（F-32）。（提示：当心整除问题！）

cel = 5.0/9*(fahr - 32)
cel = float(5)/9.0*(fahr - 32)
cel = 5/float(9)*(fahr - 32)