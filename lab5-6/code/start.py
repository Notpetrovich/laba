import pygame
from pygame.draw import *
from pygame.font import *
score = 0
from ball import *
from fichi import*
pygame.init()
FPS = 20
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Awesome balls")
v = pygame.image.load('textures/v.jpg')




def draw():
    screen.fill((0, 0, 0))
    rect(screen, (50, 20, 70), (0, 0, 1200, 100))
    font1 = pygame.font.SysFont(None, 54)
    img = font1.render(str(score) + "$", True, (70, 200, 150))
    screen.blit(img, (20, 20))
    draw_fichi(screen)
    draw_balls(screen)    
    pygame.display.update()

def exist(t):
    k = exist_fichi(t, getm())
    ball_exist(0.05*t*k)


new_ball()


clock = pygame.time.Clock()
finished = False
dt = 0

while not finished:
    t = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                score += ball_attempt(event.pos)
            elif event.button == 3:
                 score -= 15
                 jokers_trap(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score -= 10
                drink()
            elif event.key == pygame.K_RETURN:
                score -= 17
                call(getm(), screen)

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
        screen.blit(v, (650, 180))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        exit()
    exist(t)
    dt += t
    if dt > FPS:
        dt = 0
        draw()
    
pygame.quit()
