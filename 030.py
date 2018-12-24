# coding:utf-8
# pygame5 图像照片--动画1，移动
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("examples/beach_ball.png") #获取图片,my_ball 是一个表面看不到，screen也是一个表面
x = 50
y = 50

screen.blit(my_ball,[x,y]) #把my_ball复制到 screen上面。
pygame.display.flip()

#动起来
for looper in range(1,100):
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0) #擦掉，盖住原来的球
    x = x + 5
    screen.blit(my_ball, [x, y]) #块移动
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.QUIT


