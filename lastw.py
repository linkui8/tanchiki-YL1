import pygame
import sqlite3


pygame.init()

clock = pygame.time.Clock()
FPS = 60

sc = pygame.display.set_mode((400, 400))
sc.fill((58, 82, 94))



fout = open("data/last.txt", "r")
text = fout.readline()
info = text.split("_")
score = str(info[0])
time = str(info[1])
lives = str(info[2])
nol = str(info[3])






f1 = pygame.font.Font(None, 42)
f2 = pygame.font.Font(None, 35)
text11 = f1.render('Cчёт: ', 1, (255, 255, 255))
text21 = f2.render(f'{score}', 1, (255, 255, 255))

text12 = f1.render('Время:', 1, (255, 255, 255))
text22 = f2.render(f'{time}', 1, (255, 255, 255))

text13 = f1.render('Количество жизней:', 1, (255, 255, 255))
text23 = f2.render(f'{lives}', 1, (255, 255, 255))

text14 = f1.render('Номер уровня:', 1, (255, 255, 255))
text24 = f2.render(f'{nol}', 1, (255, 255, 255))


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    sc.blit(text11, (10, 10))
    sc.blit(text21, (30, 40))

    sc.blit(text12, (10, 80))
    sc.blit(text22, (30, 110))

    sc.blit(text13, (10, 150))
    sc.blit(text23, (30, 180))

    sc.blit(text14, (10, 220))
    sc.blit(text24, (30, 250))

    pygame.display.update()
    clock.tick(FPS)