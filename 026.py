# coding:utf-8
# pygame2 - 画圆 和 矩形

import pygame,sys
pygame.init() #可以联想为初始化
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255]) #用白色背景填充窗口
#画一个圆，画在什么面上，什么颜色，什么位置开始画，圆的半径，0线宽代表填充
pygame.draw.circle(screen,[255,0,0],[100,100],30,0) #circle 画圆
#再来画一个矩形[200,200,80,50]---[left,top,width,height]

my_list = [250,250,80,50]
my_rect = pygame.Rect(150,150,80,50)
pygame.draw.rect(screen,[255,155,100],my_rect,0) #rect 画方形
pygame.draw.rect(screen,[200,155,100],my_list,2)

pygame.display.flip() #把你的监视器翻过来......开玩笑的，别当真

#启动事件循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()