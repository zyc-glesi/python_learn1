# coding:utf-8
# pygame5 图像照片--动画3，让皮球翻转，从屏幕右边消失，又从左边出来
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("examples/beach_ball.png") #获取图片,my_ball 是一个表面看不到，screen也是一个表面
x = 50
y = 50
x_speed = 10 #这是speed变量
y_speed = 10

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
    #x_speed +=1 # 这个代码会不断加速球的运行，但是当速度足够快的时候，球就会跳出屏幕。因为x超出了屏幕范围
    #如何让皮球下落的时候加速，上扬的时候减速？碰到边的时候轻微加速？然后运行过程减速？


    if x > screen.get_width(): #当球碰到窗口的右边
        x = 0 #...皮球从左边出来

    if y > screen.get_height() - 90 or y < 0: #当球碰到窗口的任意一边
        y_speed = - y_speed #方向翻转

    screen.blit(my_ball,[x,y])
    pygame.display.flip()
pygame.quit() #这个退出 用了个函数。而不是前面的QUIT,测试 quit() =  QUIT
