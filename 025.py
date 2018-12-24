# coding:utf-8
# pygame - while 启动事件循环

import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
#启动事件循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()