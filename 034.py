# coding:utf-8
# pygame6 动画精灵和碰撞检测 1
import sys,pygame
from random import *

#继承 sprite模块的 Sprite基类 的 子类
#定义Ball子类
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self) #初始化动画精灵
        self.image = pygame.image.load(image_file) #向其中加载图像文件
        self.rect = self.image.get_rect() #得到定义图像边界的矩形
        self.rect.left, self.rect.top = location #设置球队初始位置，location 是一个[x,y]
        self.speed = speed


    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

#设置窗口大小
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "examples/beach_ball.png"
balls = []


#创建列表跟踪所有球
for row in range(0,3):
    for column in range(0,3):
        location = [column * 180 + 10, row * 180 + 10]
        #speed = [choice([-8,8]),choice([-8,8])] #这个choice 是引用random 模块，但是这个速度太均衡了,改用randint
        speed = [randint(-8, 8), randint(-8, 8)]
        ball = MyBallClass(img_file,location,speed)  ### 类实例化
        balls.append(ball)   #将球增加到列表

for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    screen.fill([255,255,255]) #直接循环重新绘制底图，而不是像前面的例子找东西覆盖
    for ball in balls:
        ball.move()
        screen.blit(ball.image,ball.rect)  #blit 不需要速度，只需要图片和方块
    pygame.display.flip()

pygame.quit()