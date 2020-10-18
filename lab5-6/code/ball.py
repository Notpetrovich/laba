from random import randint
import pygame
import math
import copy
from pygame.draw import *

inbt = pygame.image.load('textures/inb.jpg')
m = []

def getm():
    return m


def new_ball():
    x = randint(100, 1100)
    y = randint(100, 800)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    r = 20
    color = [randint(50, 255), randint(50, 255), randint(50, 255)]
    vc = [randint(1, 10), randint(1, 10), randint(1, 10)]
    vcm = math.sqrt(vc[0]**2 + vc[1]**2 + vc[2]**2)
    for j in range(3):
        vc[j] /= vcm
    jewish = 1
    inbikst = 0
    global m 
    m = m + [[[x, y], [vx, vy], r, color, jewish, vc, inbikst]]


def draw_balls(screen):
    for i in range(len(m)):
        if m[i][6] > 0:
            circle(screen, [255, 255, 255], (int(m[i][0][0]), int(m[i][0][1])) , m[i][2]*10)
            screen.blit(inbt, (int(m[i][0][0]) - 32, int(m[i][0][1]) - 32))
            continue
        circle(screen, m[i][3], (int(m[i][0][0]), int(m[i][0][1])) , m[i][2]*10)
        if m[i][4] == 1:
            m1 = (int(m[i][0][0]), int(m[i][0][1]) - m[i][2]*8)
            m2 = (int(m[i][0][0]) + m[i][2]*5, int(m[i][0][1]) + m[i][2]*4)
            m3 = (int(m[i][0][0]) - m[i][2]*5, int(m[i][0][1]) + m[i][2]*4)
            m4 = (int(m[i][0][0]), int(m[i][0][1]) + m[i][2]*8)
            m5 = (int(m[i][0][0]) + m[i][2]*5, int(m[i][0][1]) - m[i][2]*4)
            m6 = (int(m[i][0][0]) - m[i][2]*5, int(m[i][0][1]) - m[i][2]*4)
            c = (255 - m[i][3][0], 255 - m[i][3][1], 255 - m[i][3][2])
            line(screen, c, m1, m2, 5)
            line(screen, c, m1, m3, 5)
            line(screen, c, m2, m3, 5)
            line(screen, c, m4, m5, 5)
            line(screen, c, m4, m6, 5)
            line(screen, c, m5, m6, 5)

def move_balls(t):
    global m 
    for i in range(len(m)):
        m[i][0][0] += t*m[i][1][0]
        m[i][0][1] += t*m[i][1][1]

        if m[i][0][0] > 1200 - m[i][2]*10:
            m[i][0][0] = 1200 - m[i][2]*10
            m[i][1][0] *= -1

        if m[i][0][0] < m[i][2]*10:
            m[i][0][0] = m[i][2]*10
            m[i][1][0] *= -1

        if m[i][0][1] > 900 - m[i][2]*10:
            m[i][0][1] = 900 - m[i][2]*10
            m[i][1][1] *= -1

        if m[i][0][1] < m[i][2]*10 + 100:
            m[i][0][1] = m[i][2]*10 + 100
            m[i][1][1] *= -1

        v = math.sqrt(m[i][1][0]**2 + m[i][1][1]**2)
        for j in range(3):
            m[i][3][j] = int(m[i][3][j] + t*m[i][5][j]*math.sqrt(v)*5)
            
            if m[i][3][j] < 50:
                m[i][3][j] = 50
                m[i][5][j] *= -1

            if m[i][3][j] > 255:
                m[i][3][j] = 255
                m[i][5][j] *= -1

def ball_hit(i, j, t):
    if i != j:
        l = math.sqrt((m[i][0][0]-m[j][0][0])**2 + (m[i][0][1]-m[j][0][1])**2)
        M = m[i][2]+m[j][2]
        a = (m[i][0][0]-m[j][0][0])/l
        b = (m[i][0][1]-m[j][0][1])/l
        x = 2*((m[i][1][0]-m[j][1][0])*a + (m[i][1][1]-m[j][1][1])*b)/M
        m[i][1][0] -= x*a*m[j][2]
        m[i][1][1] -= x*b*m[j][2]
        m[i][0][0] -= (l-10*M)*a
        m[i][0][1] -= (l-10*M)*b
        m[j][1][0] += x*a*m[i][2]
        m[j][1][1] += x*b*m[i][2]
        m[j][0][0] += (l-10*M)*a
        m[j][0][1] += (l-10*M)*b

def ball_exist(t):
    global m
    move_balls(t)
    for i in range(len(m)):
        for j in range(len(m)):
            if (m[i][0][0]-m[j][0][0])**2 + (m[i][0][1]-m[j][0][1])**2 < 100*(m[i][2]+m[j][2])**2:
                ball_hit(i, j, t)
                if m[i][6] > 0 or m[j][6] > 0:
                    m[i][3] = [100, 100, 255]
                    m[j][3] = [100, 100, 255]
                    m[i][5] = [0, 0, 0]
                    m[j][5] = [0, 0, 0]

    for i in range(len(m)):
        if m[i][6] > 0:
            m[i][6] -= t
            if m[i][6] <= 0:
                m.pop(i)
                break
    
    if randint(0, 800000) == 0:
        m += [[[randint(100, 1100), randint(100, 800)], [randint(-20, 10), randint(-10, 10)], 5, [0, 0, 0], 0, [0, 0, 0], 100]]

def ball_spanking(n):
    global m
    global score
    p = randint (0, 3)
    if m[n][6] != 0:
        m.pop(n)
        return 7
    elif p == 0 and m[n][4] == 0:
        m[n][4] = 1
        return 1
    elif m[n][4] == 0:
        r = int(m[n][2]/2)
        x1 = randint(1, 10)
        y1 = randint(1, 10)
        r1 = math.sqrt(x1**2 + y1**2)
        x1 = int(10*r*x1/(r1))
        y1 = int(10*r*y1/(r1))
        x = m[n][0][0]
        y = m[n][0][1]
        vx = m[n][1][0]
        vy = m[n][1][1]
        color = m[n][3]
        vc = m[n][5]
        if r > 1: 
            m += [[[x + x1, y + y1], [vx + x1/(r), vy + y1/(r)], r, copy.copy(color), randint(0, 1), copy.copy(vc), 0]] + [[[x - x1, y - y1], [vx - x1/(r), vy - y1/(r)], r, copy.copy(color), randint(0, 1), copy.copy(vc), 0]]
        m[len(m) - randint(1, 2)][5][randint(0, 2)] *= -1
        m.pop(n)
        return 1
    else:
        r = int(m[n][2]/3)
        x = m[n][0][0]
        y = m[n][0][1]
        vx = m[n][1][0]
        vy = m[n][1][1]
        color = m[n][3]
        vc = m[n][5]
        if r > 1: 
            for i in range(6):
                m += [[[x + int(2*r*math.sin(6.28*i/6)), y + int(2*r*math.cos(6.28*i/6))], [vx + 10*math.sin(6.28*i/6), vy + 10*math.cos(6.28*i/6)], r, copy.copy(color), randint(0, 1), copy.copy(vc), 0]]
                m[len(m) - 1][5][randint(0, 2)] *= -1
            m.pop(n)
            return 3
        else:
            m[n][4] = 0
            return 2


def ball_attempt(pos):
    for i in range(len(m)):
        if math.sqrt((m[i][0][0] - pos[0])**2 + (m[i][0][1] - pos[1])**2) < m[i][2]*10:
            return ball_spanking(i)
            break
    return (-2)
        
