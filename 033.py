# coding:utf-8
# pygame5 图像照片--动画4，
# 如何让皮球下落的时候加速，上扬的时候减速？碰到边的时候轻微加速？然后运行过程减速？
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("examples/beach_ball.png") #获取图片,my_ball 是一个表面看不到，screen也是一个表面
x = 50
y = 50
x_speed = 100 #这是speed变量
y_speed = 100

# 为了球永远循环，我们把代码加入到原本代码段的 while 循环中去。
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x = x + x_speed
    y = y + y_speed
    # 这个代码会不断减速球的横向运行,不管左右方向
    if x_speed > 0:
        x_speed -=2
    if x_speed < 0:
        x_speed +=2
    #纵轴上，上扬减速，下降加速
    if y_speed > 0:
        y_speed -=1
    if y_speed < 0:
        y_speed +=2


    if x > screen.get_width() - 90 or x < 0: #当球碰到窗口的任意一边
        x_speed = - x_speed #方向翻转
        if x_speed > 0:
            x_speed = x_speed + 6
        if x_speed < 0:
            x_speed = x_speed - 6

    if y > screen.get_height() - 90 or y < 0: #当球碰到窗口的任意一边
        y_speed = - y_speed #方向翻转
        if y_speed > 0:
            y_speed += 4
        if y_speed < 0:
            y_speed -= 6


    screen.blit(my_ball,[x,y])
    pygame.display.flip()
pygame.quit() #这个退出 用了个函数。而不是前面的QUIT,测试 quit() =  QUIT