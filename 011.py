#coding:utf-8
#循环
for looper in [1,2,3,4,5]:
    print looper,"times 8=",looper*8

for looper in range(1,5):
    print looper, "times 8=", looper * 8

#按照步长 2 计数
for i in range(0,20,2):
    print i

#倒计时器
import time
for i in range(10,0, -1):
    print i
    time.sleep(1)
print "BLAST OFF!"
