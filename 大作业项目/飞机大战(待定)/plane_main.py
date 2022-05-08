# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:21:22 2022

@author: 30505
"""

import random
import pygame
from plane_sprites import *
j = []
bomb_index = 0

class PlaneGame(object):
    """飞机大战 主程序"""
    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)   
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CRATE_ENEMY_EVENT, 500)
        pygame.time.set_timer(HERO_SHOOT_EVENT, 500)

        # self.explode_index = 0

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建爆炸精灵组
        # bomb = Bomb()
        # self.bomb_group = pygame.sprite.Group(bomb)
        self.bomb_group = pygame.sprite.Group()
        self.hero_bomb_group = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始")
        while True:
            # 1. 设置刷新帧
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__enent_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __enent_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CRATE_ENEMY_EVENT:
                # 创建敌机精灵
                self.enemy = Enemy()
                # 将敌机添加到敌机精灵族
                self.enemy_group.add(self.enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
            # elif event.type == HERO_SHOOT_EVENT:
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.hero.fire()
        # 使用键盘模块提供的方法 - 按键元组
        key_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        elif key_pressed[pygame.K_UP]:
            self.hero.speed2 = -3
        elif key_pressed[pygame.K_DOWN]:
            self.hero.speed2 = 3
        else:
            self.hero.speed = 0
            self.hero.speed2 = 0

    def __check_collide(self):
        # 不可以在这里创建精灵组，但是为什么呢
        bomb_enemies = pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, False, True)
        self.bomb_group.add(bomb_enemies)
        # print(bomb_enemies)
        print(self.bomb_group)
        for enemy1 in self.bomb_group:
            print(enemy1.explode_index)
            if enemy1.explode_index == 0:
                enemy1.explode_index = 1
            elif enemy1.explode_index == 5:
                self.enemy_group.remove_internal(enemy1)
                self.bomb_group.remove_internal(enemy1)


        # 2 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.explode(self.screen)
            # 英雄牺牲，结束游戏
            self.hero.kill()
            PlaneGame.__game_over()



    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        # self.bomb_group.update()
        # self.bomb_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()
# 测试程序部分
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game() 