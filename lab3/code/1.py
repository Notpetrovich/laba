import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
finished = False

def draw(t):
    circle(screen, (255, 218, 185), (200, 200), 150)

    circle(screen, (250, 200 - 50*math.sin(t*6.28), 200 - 50*math.sin(t*6.28)), (130, 140), 40)
    circle(screen, (250, 200 - 50*math.cos(t*6.28), 200 - 50*math.cos(t*6.28)), (270, 140), 40)
    circle(screen, (0, 0, 0), (130, 140), 20)
    circle(screen, (0, 0, 0), (270, 140), 20)

    polygon(screen, (50, 50, 50), [(70, 80), (170, 100), (170, 80), (70, 60)])
    polygon(screen, (50, 50, 50), [(330, 80), (230, 100), (230, 80), (330, 60)])

    polygon(screen, (170, 80, 100), [(300, 280), (200, 250), (200, 230), (300, 260)])
    polygon(screen, (170, 80, 100), [(100, 280), (200, 250), (200, 230), (100, 260)])

    pygame.display.update()



while not finished:
    draw(pygame.time.get_ticks()%2000/2000)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
