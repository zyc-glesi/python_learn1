#coding:utf-8
#再看数字游戏
import random, easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox('''呼哈，我是格林沃德，我有一个秘密！如果你猜到的话，你会得到一份礼物。这是一个猜数字游戏，从1到99，你一共有6次机会。''')
while guess != secret and tries < 6:
    guess = easygui.integerbox('你猜的数字是什么，麻瓜？')
    if not guess:
        break
    if guess < secret:
        easygui.msgbox(str(guess) + ' 低了，你想变成鼻涕虫吗？')
    elif guess > secret:
        easygui.msgbox(str(guess) + ' 高了，我觉得你合适做我的扫帚原料，瘦又高')
    tries = tries + 1

if guess == secret:
    easygui.msgbox("太聪明了！你猜对啦！现在，你可以走啦，放你一条生路！开心点！")
else:
    easygui.msgbox("哦哟 ,没机会了！正确的数字是"+ str(secret) +'Aklie MoDelaa~~ 变成我的跟屁虫！')


