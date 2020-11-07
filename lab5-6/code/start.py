import pygame
from pygame.draw import *
from pygame.font import *
from ball import *

pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Awesome balls")
victory_face = pygame.image.load('textures/v.jpg')
trap = pygame.image.load('textures/jt.png')
bogdanoff = pygame.image.load('textures/call.jpg')
FPS = 20
score = 0
jt = [0, [0, 0]]
dr = 0


def jokers_trap(x):
    global score
    score -= 15
    jt[0] = 2000
    jt[1] = x


def time_dilation():
    global score
    score -= 10
    global dr
    dr += 3000


def call():
    global score
    m = getm()
    score -= 17
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

def draw():
    screen.fill((0, 0, 0))
    rect(screen, (50, 20, 70), (0, 0, 1200, 100))
    font1 = pygame.font.SysFont(None, 54)
    img = font1.render(str(score) + "$", True, (70, 200, 150))
    screen.blit(img, (20, 20))
    font = pygame.font.SysFont(None, 60)
    img1 = font.render("пкм: ловушка - 15$", True, (200, 200, 150))
    img2 = font.render("пробел: замедление - 10$", True, (70, 200, 250))
    img3 = font.render("enter: позвонить - 17$", True, (250, 50, 10))
    screen.blit(img2, (300, 10))
    screen.blit(img1, (300, 50))
    screen.blit(img3, (700, 50))
    if jt[0] > 0:
        circle(screen, (255, 255, 255), jt[1] , 70)
        screen.blit(trap, (jt[1][0] - 48, jt[1][1] - 48))
    draw_balls(screen)    
    pygame.display.update()


def exist(t):
    jt[0] -= t
    if jt[0] < 0:
        jt[0] = 0
    if jt[0] > 0:
        for i in range(len(m)):
            if math.sqrt((m[i][0][0] - jt[1][0])**2 + (m[i][0][1] - jt[1][1])**2) < m[i][2]*10 + 70:
                ball_spanking(i)
                break

    global dr
    dr -= t
    if dr < 0:
        dr = 0
    if dr == 0:
        k=1
    else:
        k= 0.3
    ball_exist(0.05*t*k)


def check_end():
    if score < 0:
        screen.fill((255, 0, 0))
        font2 = pygame.font.SysFont(None, 80)
        img = font2.render("Смэрть.  :<", True, (70, 200, 150))
        screen.blit(img, (200, 200))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        exit()

    if len(getm()) == 0:
        screen.fill((0, 255, 0))
        font2 = pygame.font.SysFont(None, 80)
        img = font2.render("Игра заботана.", True, (70, 200, 150))
        screen.blit(img, (200, 200))
        screen.blit(victory_face, (650, 180))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        exit()


clock = pygame.time.Clock()
dt = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                score += ball_attempt(event.pos)
            elif event.button == 3:
                 jokers_trap(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time_dilation()
            elif event.key == pygame.K_RETURN:
                call()
    check_end()
    t = clock.tick()
    exist(t)
    dt += t
    if dt > FPS:
        dt = 0
        draw()
