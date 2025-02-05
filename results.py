import pygame
import sqlite3


pygame.init()

clock = pygame.time.Clock()
FPS = 60

sc = pygame.display.set_mode((400, 400))
sc.fill((58, 82, 94))

connection = sqlite3.connect('data/infodb.db')
cursor = connection.cursor()

#1
time1 = list()
query1 = cursor.execute("select time from firstlevel where nol = 1").fetchall()
for i in query1:
    time1.append(int(str(i).lstrip("(").rstrip(",)")))
#2
time2 = list()
query2 = cursor.execute("select time from firstlevel where nol = 2").fetchall()
for i in query2:
    time2.append(int(str(i).lstrip("(").rstrip(",)")))
#3
time3 = list()
query3 = cursor.execute("select time from firstlevel where nol = 3").fetchall()
for i in query3:
    time3.append(int(str(i).lstrip("(").rstrip(",)")))
#4
time4 = list()
query4 = cursor.execute("select time from firstlevel where nol = 4").fetchall()
for i in query4:
    time4.append(int(str(i).lstrip("(").rstrip(",)")))

str5 = list()
query5 = cursor.execute("select score from firstlevel").fetchall()
for i in query5:
    str5.append(int(str(i).lstrip("(").rstrip(",)")))

str6 = list()
n = 0
query6 = cursor.execute("select lives from firstlevel").fetchall()
for i in query6:
    str6.append(int(str(i).lstrip("(").rstrip(",)")))
for i in str6:
    if int(i) == 3:
        n += 1

connection.close()


f1 = pygame.font.Font(None, 42)
f2 = pygame.font.Font(None, 35)
text11 = f1.render('1 уровень:', 1, (255, 255, 255))
text21 = f2.render(f'Лучшее время - {min(time1)}', 1, (255, 255, 255))

text12 = f1.render('2 уровень:', 1, (255, 255, 255))
text22 = f2.render(f'Лучшее время - {min(time2)}', 1, (255, 255, 255))

text13 = f1.render('3 уровень:', 1, (255, 255, 255))
text23 = f2.render(f'Лучшее время - {min(time3)}', 1, (255, 255, 255))

text14 = f1.render('4 уровень:', 1, (255, 255, 255))
text24 = f2.render(f'Лучшее время - {min(time4)}', 1, (255, 255, 255))

text5 = f1.render(f'Максимальный счёт - {max(str5)}', 1, (255, 255, 255))

text6 = f2.render(f'Количество игр без смертей - {n}', 1, (255, 255, 255))

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

    sc.blit(text5, (10, 350))
    sc.blit(text6, (10, 300))

    pygame.display.update()
    clock.tick(FPS)