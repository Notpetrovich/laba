import pygame
from pygame.draw import *
from pygame.font import *
from ball import *

jt = [0, [0, 0]]
dr = 0
jtt = pygame.image.load('textures/jt.png')
bogdanoff = pygame.image.load('textures/call.jpg')

def jokers_trap(x):
    jt[0] = 2000
    jt[1] = x


def drink():
    global dr
    dr += 3000


def draw_fichi(screen):
    font = pygame.font.SysFont(None, 60)
    img1 = font.render("пкм: ловушка - 15$", True, (200, 200, 150))
    img2 = font.render("пробел: употребить - 10$", True, (70, 200, 250))
    img3 = font.render("enter: позвонить - 17$", True, (250, 50, 10))
    screen.blit(img2, (300, 10))
    screen.blit(img1, (300, 50))
    screen.blit(img3, (700, 50))

    if jt[0] > 0:
        circle(screen, (255, 255, 255), jt[1] , 70)
        screen.blit(jtt, (jt[1][0] - 48, jt[1][1] - 48))

def exist_fichi(t, m):
    global dr
    dr -= t
    if dr < 0:
        dr = 0
    jt[0] -= t
    if jt[0] < 0:
        jt[0] = 0
    
    if jt[0] > 0:
        for i in range(len(m)):
            if math.sqrt((m[i][0][0] - jt[1][0])**2 + (m[i][0][1] - jt[1][1])**2) < m[i][2]*10 + 70:
                ball_spanking(i)
                break

    if dr == 0:
        return 1
    else:
        return 0.3

def call(m, screen):
    c = pygame.time.Clock()
    T = 0
    while T < 1000:
        T += 2*c.tick()
        k = 1 + (T/1000)**4
        b = pygame.transform.scale(bogdanoff, (int(600*k), int(480*k)))
        screen.blit(b, (600 - int(300*k), 500 - int(240*k)))
        pygame.display.update()
    F = 1
    while F == 1:
        F = 0
        for i in range(len(m)):
            if m[i][4] == 0:
                ball_spanking(i)
                F = 1
                break
    

