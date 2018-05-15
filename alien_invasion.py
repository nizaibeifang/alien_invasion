#-coding:utf-8-*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    print(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_scrren(ai_settings,screen,ship)

        #让最近绘制的屏幕可见
        pygame.display.update()

if __name__ == "__main__":
    run_game()
