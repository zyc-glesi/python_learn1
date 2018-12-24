#coding:utf-8
import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",choices = ['Vanilla','Chocolate','Strawberry'])
youChoose = easygui.msgbox("You picked " + flavor)
#print youChoose

#上方按钮窗口，下方选择窗口
#import easygui
flavor = easygui.choicebox("What is your favorite ice cream flavor?",choices = ['Vanilla','Chocolate','Strawberry'])
easygui.msgbox("You choice "+ flavor)

#下方是 Enterbox
flavor2 = easygui.enterbox("你喜欢什么口味的冰淇淋？",default='香草')
easygui.msgbox("You entered "+ flavor2)
