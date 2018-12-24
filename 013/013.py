#coding:utf-8
#skier 滑雪游戏

# Listing_10-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

import pygame, sys, random
skier_images = ["skier_down.png", "skier_right1.png", "skier_right2.png", "skier_left2.png", "skier_left1.png"]
class SkierClass(pygame.sprite.Sprite):#以下7行创建滑雪者
    def __int__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction): #(以下10行)滑雪者转向
        self.angle = self.angle + direction
        if self.angle < -2:
            self.angle = -2
        if self.angle > 2:
            self.angle = 2
        center = self.rect.center
        speed = [self.angle, 6 - abs(self.angle)*2]
        return speed

    def move(self,speed): #(以下4行)滑雪者左右移动
        self.rect.center = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:
            self.rect.centerrx = 20
        if self.rect.centerx > 620:
            self.rect.centerx = 620

class ObstacleClass(pygame.sprite.Sprite): #(以下9行)创建树木和小旗
    def __int__(self, image_file, location, type):
        pygame.sprite.Sprite.__int__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def update(self): #(以下3行) 让场景向上滚动
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery<-32: #(以下2行)删除从屏幕上方滚下的障碍物
            self.kill()

# create one "screen" of obstacles: 640 x 640
# use "blocks" of 64 x 64 pixels, so objects aren't too close together
def create_map():#(以下14行)创建一个窗口，包含随机的树和小旗
    global obstacles
    locations = []
    for i in range(10):
        row = random.randint(0, 9)
        col = random.randint(0,9)
        location = [col*64 + 20, row*64 + 20 + 640]
        if not (location in locations):
            locations.append(location)
            type = random.choice(["tree", "flag"])
            if type == "tree":
                img = "skier_tree.png"
            elif type == "flag":
                img = "skier_flag.png"
            obstacle = ObstacleClass(img,location,type)
            obstacle.add(obstacle)

def animate(): #(以下6行)重绘屏幕
    screen.fill([255,255,255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text,[10,10])
    pygame.display.flip()

# initialize everything
pygame.init() #(以下10行)做好准备
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0, 6]
obstacles = pygame.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None,50)

# main Pygame event loop
running = True #（以下2行）开始主循环
while running:
    clock.tick[30]  #每秒更新30次图形    （以下9行）检查按键或窗口是否关闭
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.type == pygame.K_RIGHT:
                speed = skier.turn(1)
        skier.move(speed) #移动滑雪者

        map_position += speed[1] #滚动场景

        if map_position >=640: #(以下3行)创建一个新窗口，包含场景
            create_map()
            map_position = 0

        hit = pygame.sprite.spritecollide(skier,obstacles.False)
        if hit: #(以下13行 )检查是否碰到树或得到小旗
            if hit[0].type == "tree"and not hit[0].passed:
                points = points - 100
                skier.image = pygame.image.load("skier_crash.png")
                animate()
                pygame.time.delay(1000)
                skier.image = pygame.image.load("skier_down.png")
                skier.angle = 0
                speed = [0,6]
                hit[0].passed = True
            elif hit[0].type == "flag" and not hit[0].passed:
                points += 10
                hit[0].kill()

        obstacles.update()
        score_text = font.render("Score: " +str(points), 1, (0, 0, 0)) #显示得分
        animate()
pygame.quit()