# coding:utf-8
# pygame8 动画精灵和碰撞检测 3 -- 碰撞 优化--帧速率
import sys,pygame
from random import *

#继承 sprite模块的 Sprite基类 的 子类
#定义Ball子类
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self) #初始化动画精灵（关键）
        self.image = pygame.image.load(image_file) #向其中加载图像文件
        self.rect = self.image.get_rect() #得到定义图像边界的矩形
        self.rect.left, self.rect.top = location #设置球队初始位置，location 是一个[x,y]
        self.speed = speed  #也是一个[x,y]

#move()做两件事，一个计算移动的偏移量结果rect.move()，类似于x=x+x_speed.另外一件事，是做碰撞后速度方向改变。
    def move(self):
        self.rect = self.rect.move(self.speed) #self.speed 是个[x,y]
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

#animate 完成球部分的动画，还有碰撞检测,使用Pygame 中的group类。据说这个东西可以帮助监测碰撞,animate 继承group类
def animate(group):
    screen.fill([255,255,255])
    for ball in group:
        ball.move()   #先移动所有球,然后再完成碰撞检测
    for ball in group:
        group.remove(ball) #删除精灵
        if pygame.sprite.spritecollide(ball,group,False):#监测精灵 与 组之间的碰撞
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball) #将球再添加回原来的组中
        screen.blit(ball.image,ball.rect)

    pygame.display.flip()
    #pygame.time.delay(20)  不用这个，使用clock去

#设置窗口大小--------------主程序从这里开始
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "examples/beach_ball.png"

clock = pygame.time.Clock() #创建Clock的实例

#创建精灵组
group = pygame.sprite.Group() #创建Group类的实例
for row in range(0,2):
    for column in range(0,2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [randint(-8, 8), randint(-8, 8)]
        ball = MyBallClass(img_file, location, speed)  ### 类实例化
        group.add(ball)  # 将各个球添加到组

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            frame_rate = clock.get_fps()  #检查帧速率
            print "frame rate=",frame_rate
    animate(group)  #调用animate()函数，并传入group.#相比于033的代码，这里一个方法调用就搞定了，看上去非常的简洁
    clock.tick(30) #clock.tick 现在控制帧速率

pygame.quit()