# coding:utf-8
# pygame3 - draw.rect 艺术创作
import pygame,sys,random
from pygame.color import THECOLORS #导入
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])

for i in range(150):
    width =random.randint(0,250)
    height = random.randint(0,100)
    top=random.randint(0,400)
    left=random.randint(0,500)
    line_width=random.randint(1,3)
    color_name = random.choice(THECOLORS.keys()) #随机获取颜色
    color = THECOLORS[color_name]
    pygame.draw.rect(screen,color,[left,top,width,height],line_width)
pygame.display.flip()

running =True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
pygame.quit()