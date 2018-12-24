# coding:utf-8
# pygame4 - 曲线和点
import pygame,sys
import math #导入数学函数，包括sin()
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for x in range(0,640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 +240) #计算每个点的y坐标（垂直坐标）
    pygame.draw.rect(screen, [0,0,0], [x,y,1,1], 1) #使用小矩形来画点

#用线链接点
plotPoins = [] #需要连接的点，空列表
for x in range(0,640): #x不用错开
    y = int(math.sin(x / 640.0 * 4 * math.pi) * 200 + 260) #y坐标错开
    plotPoins.append([x,y]) #循环补齐 ，连接的点列表
pygame.draw.lines(screen, [0,0,0], False, plotPoins, 2) #draw lines 函数画出了整条曲线

#画布翻看呈现，并循环确认pygame 状态
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()