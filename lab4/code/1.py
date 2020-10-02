import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 100
screen = pygame.display.set_mode((500, 900))
clock = pygame.time.Clock()
finished = False



def draw(x, y, m):
    #типо рисует зайца
    #x, y - координаты левой верхей точки
    #m - размер
    x = x + m
    draw1(x, y, m)
    draw1(x + 1.4*m, y, m)
    pygame.draw.ellipse(screen, (0xA0, 0x95, 0x90), (x - 0.2*m, y + 2.5*m, 2.4*m, 6*m))
    pygame.draw.circle(screen, (0x90, 0x90, 0x90), (x + m, y + 3*m), m)
    pygame.draw.rect(screen, (0x70, 0x40, 0x40), (x + m/2, y + 3.2*m, m, 0.1*m))
    pygame.draw.ellipse(screen, (0x40, 0x40, 0x50), (x + 0.8*m, y + 2.7*m, 0.4*m, 0.6*m))
    draw2(x+0.5*m, y+1.6*m, m)
    draw2(x+1.3*m, y+1.6*m, m)
    draw3(x, y+4*m,m)
    draw3(x+1.4*m, y+4*m,m)
    draw4(x+0.5*m, y+7.5*m,m)
    draw4(x+1.7*m, y+7.5*m,m)
    
def draw1(x, y, m):
    #типо рисует ухо
    #x, y - координаты левой верхей точки
    #m - размер
    pygame.draw.ellipse(screen, (0x90, 0x90, 0x90), (x, y, 0.6*m, 2.7*m))
    pygame.draw.ellipse(screen, (0xB0, 0x90, 0x90), (x + 0.1*m, y + 0.1*m, 0.4*m, 2.5*m))

def draw2(x, y, m):
    #типо рисует глаз
    #x, y - координаты левой верхей точки
    #m - размер
    pygame.draw.circle(screen, (0xFF, 0xFF, 0xFF), (int(x + m/10), int(y + m)), int(m/10))
    pygame.draw.circle(screen, (0x00, 0x00, 0x00), (int(x + m/10), int(y + m)), int(m/20))

def draw3(x, y, m):
    #типо рисует конечность
    #x, y - координаты левой верхей точки
    #m - размер
    pygame.draw.ellipse(screen, (0x90, 0xA0, 0xA0), (x - 0.1*m, y, 0.8*m, 2.7*m))
    for i in range(3):
        pygame.draw.ellipse(screen, (0xD0, 0xD0, 0xD0), (x + 0.1*m+0.15*i*m, y + 2.4*m, 0.1*m, 0.5*m))

def draw4(x, y, m):
    #типо рисует конечность, по-другому
    #x, y - координаты левой верхей точки
    #m - размер
    pygame.draw.ellipse(screen, (0x90, 0xA0, 0xA0), (x - 0.5*m, y, 0.8*m, 2*m))
    pygame.draw.ellipse(screen, (0x90, 0xA0, 0xA0), (x - 0.5*m, y + 0.7*m, 0.8*m, 2*m))
    
    



while not finished:
    draw(0, 0, 80)
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
