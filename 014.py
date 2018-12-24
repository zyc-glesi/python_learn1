#coding:utf-8
#乘法表 和 外循环
for multiplier in range(1, 3):
    for i in range(1, 10):
        print i ,"x",multiplier,"=",i*multiplier
    print

#可变循环
numStarts = int(float(raw_input("How many stars do you want?")))
for i in range(1, numStarts+1):
    print i,

numLines = int(float(raw_input('How many lines of stars do you want? ')))
numStars = int(float(raw_input('How many stars per line? ')))
for line in range(0, numLines):
    for star in range(0, numStars):
        print '*',
    print

