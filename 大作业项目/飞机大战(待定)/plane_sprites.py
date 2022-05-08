# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:43:26 2022

@author: 30505
"""

import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 400, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CRATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_SHOOT_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name="./images/background.png", speed=1, speed2=1):

        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed2 = speed2
    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__()
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1. 调用父类的方法实现
        super().update()
        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片。
        super().__init__("./images/enemy1.png")

        # 2.指定敌机的初始随机速度 1-3
        self.speed = random.randint(1, 6)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, (SCREEN_RECT.width-self.rect.width))
        self.explode_index = 0

    def update(self):
        # 1.调用父类方法，保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，需要从精灵中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
        # print(self.explode_index)
        if self.explode_index == 5:
            # self.kill()
            return
        if self.explode_index != 0:
            new_rect = self.rect
            super().__init__("./images/enemy1_down%d.png" % self.explode_index)
            self.explode_index += 1
            print(self.explode_index)
            self.rect = new_rect

    def __del__(self):
        print("销毁敌机")

class Hero(GameSprite):
    def __init__(self):
        # 1.调用父类方法，同时指定英雄图片。
        super().__init__("./images/me1.png")
        # 2.指定英雄出现的位置，在屏幕的水平正中间，距离底部 120 象素
        self.rect.x = SCREEN_RECT.width/2 - self.rect.width/2
        self.rect.bottom = SCREEN_RECT.height - 120
        self.speed = 0
        self.speed2 = 0
        self.bullets = pygame.sprite.Group()
        self.hero_bomb_index = 0
        self.clock = pygame.time.Clock()


    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed
        self.rect.y += self.speed2

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

        if self.hero_bomb_index == 5:
            return

        if self.hero_bomb_index != 0:
            new_h_rect = self.rect
            super().__init__("./images/me_destroy_%d.png" % self.hero_bomb_index)
            self.hero_bomb_index += 1
            self.rect = new_h_rect

    def explode(self, screen):
        new_rect = self.rect
        for i in (1, 2, 3, 4):
            self.clock.tick(20)
            super().__init__("./images/me_destroy_%d.png" % i)
            self.rect.centerx = new_rect.centerx
            self.rect.centery = new_rect.centery
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pygame.display.update()



    def fire(self):
        #for i in (0, 1, 2):
        # 1.创建子弹精灵
        bullet = Bullet()
        # 2.设置精灵的位置
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.y - 20
        # 3.将精灵添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        # 指定子弹图片，初始速度等于 -3
        super().__init__("./images/bullet1.png", -3)

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()


class Enemy_Bomb(GameSprite):
    def __init__(self, x, y):
         super().__init__("./images/enemy1_down1.png", 0, 0)
         self.rect.centerx = x
         self.rect.centery = y
         self.explode_index = 0
         self.a =1

    def update(self):
        pass