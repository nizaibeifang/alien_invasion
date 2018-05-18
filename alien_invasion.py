#-coding:utf-8-*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats



def run_game():
    #初始化并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    print(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    #创建一个用于存储游戏统计信息的实例
    status = GameStats(ai_settings)

    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    #创建一个外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        if status.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,status,screen,ship,aliens,bullets)

        gf.update_scrren(ai_settings,screen,ship,aliens,bullets)

        #让最近绘制的屏幕可见
        pygame.display.update()

if __name__ == "__main__":
    run_game()
