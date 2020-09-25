import pygame
from pygame.draw import *
import math
import random

pygame.init()

FPS = 100
screen = pygame.display.set_mode((1200, 400))
clock = pygame.time.Clock()
finished = False

u = (("ЛК", 1.3), ("НК", 1), ("ГК", 1), ("КПМ", 1.5), ("био", 1.4), ("цифра", 1.1), ("арктика", 1.1))


def draw(t, s, x, y, m):
    polygon(screen, (200, 200, 180), [(x, y + m*80), (x + m*300, y + m*80), 
                                      (x + m*300, y + m*300), (x, y + m*300)])
    polygon(screen, (190 + 50*math.sin(6.28*3*t + x), 180 + 30*math.cos(6.28*2*t), 100 + 30*math.sin(6.28*t)), 
                    [(x, y + m*80), (x + m*300, y + m*80), (x + m*200, y), (x + m*100, y)])
    polygon(screen, (100, 100, 100), [(x + m*110, y + m*200), (x + m*110, y + m*300), 
                                      (x + m*190, y + m*300), (x + m*190, y + m*200)])

    f = pygame.font.Font('comic.ttf', int(m * 65))
    text = f.render(s, 0, (0, 30, 100))
    screen.blit(text, (x + m*40, y + m*80))
    



while not finished:
    polygon(screen, (100, 100, 200), [(0, 0), (0,160), (1200, 160), (1200, 0)])
    polygon(screen, (100, 120, 100), [(0, 400), (0,160), (1200, 160), (1200, 400)])

    d = 0

    dt = pygame.time.get_ticks() % 2000 / 2000

    for i in range(len(u)):
        draw(dt, u[i][0], d, 100, 0.35*u[i][1])
        d += u[i][1]*100 + 15
    
    d += 50
    draw(dt, "боманка", d, 100 + pygame.time.get_ticks()/130, 0.4)
    polygon(screen, (100, 120, 100), [(d, 400), (d, 220), (1200, 220), (1200, 400)])

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
