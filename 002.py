#coding:utf-8
import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print "你好 ，我是格林沃德，我有一个秘密！如果你猜到的话，你会得到一份礼物"
print "这是一个猜数字游戏，从1到99，你一共有6次机会"
while guess != secret and tries < 6:
    guess = input("输入你猜的数字？")
    if guess < secret:
        print "低了，蠢货"
    elif guess > secret:
        print "高了，贪心鬼"
        # 冒号后面都有强制缩进#这个空行是代表if结束，然后while结束，也应该有个空行

    tries = tries + 1

if guess == secret:
    print "太聪明了！猜对啦！现在，你可以走啦，放你一条生路！开心点！"
else:
    print "没机会了！来，看看镜子中的你，你看到一头猪了吧？"
    print "我的秘密数字是", secret



