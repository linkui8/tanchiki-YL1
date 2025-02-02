import sys
import pygame
import subprocess


pygame.init()
clock = pygame.time.Clock()


window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Танчики')
font = pygame.font.Font(None, 24)
title = pygame.image.load("data/title.png")
prav = pygame.image.load("data/prav1.png")
tank1 = pygame.image.load("data/tank1.png")

#1button
button_surface1 = pygame.Surface((150, 50))

text1 = font.render("1 уровень", True, (0, 0, 0))
text_rect = text1.get_rect(
    center=(button_surface1.get_width() / 2,
            button_surface1.get_height() / 2))

button_rect1 = pygame.Rect(30, 250, 150, 50)

#2button
button_surface2 = pygame.Surface((150, 50))

text2 = font.render("2 уровень", True, (0, 0, 0))
text_rect = text2.get_rect(
    center=(button_surface2.get_width() / 2,
            button_surface2.get_height() / 2))

button_rect2 = pygame.Rect(220, 250, 150, 50)

#3button
button_surface3 = pygame.Surface((150, 50))

text3 = font.render("3 уровень", True, (0, 0, 0))
text_rect = text3.get_rect(
    center=(button_surface3.get_width() / 2,
            button_surface3.get_height() / 2))

button_rect3 = pygame.Rect(30, 320, 150, 50)

#4button
button_surface4 = pygame.Surface((150, 50))

text4 = font.render("4 уровень", True, (0, 0, 0))
text_rect = text4.get_rect(
    center=(button_surface4.get_width() / 2,
            button_surface4.get_height() / 2))

button_rect4 = pygame.Rect(220, 320, 150, 50)


while True:
    clock.tick(60)
    screen.fill((58, 82, 94))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect1.collidepoint(event.pos):
                a = open("level.txt", "w")
                a.write("1")
                a.close()
                subprocess.run(['python', 'main.py'])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect2.collidepoint(event.pos):
                b = open("level.txt", "w")
                b.write("2")
                b.close()
                subprocess.run(['python', 'main.py'])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect3.collidepoint(event.pos):
                b = open("level.txt", "w")
                b.write("3")
                b.close()
                subprocess.run(['python', 'main.py'])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect4.collidepoint(event.pos):
                b = open("level.txt", "w")
                b.write("4")
                b.close()
                subprocess.run(['python', 'main.py'])

    if button_rect1.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface1, (255, 255, 255), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface1, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface1, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface1, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface1, (0, 100, 0), (1, 48, 148, 10), 2)
    if button_rect2.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface2, (255, 255, 255), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface2, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface2, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface2, (0, 100, 0), (1, 48, 148, 10), 2)
    if button_rect3.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface3, (255, 255, 255), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface3, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface3, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface3, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface3, (0, 100, 0), (1, 48, 148, 10), 2)
    if button_rect4.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface4, (255, 255, 255), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface4, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface4, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface4, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface4, (0, 100, 0), (1, 48, 148, 10), 2)

    button_surface1.blit(text1, text_rect)

    screen.blit(button_surface1, (button_rect1.x, button_rect1.y))

    button_surface2.blit(text2, text_rect)

    screen.blit(button_surface2, (button_rect2.x, button_rect2.y))

    button_surface3.blit(text3, text_rect)

    screen.blit(button_surface3, (button_rect3.x, button_rect3.y))

    button_surface4.blit(text4, text_rect)

    screen.blit(button_surface4, (button_rect4.x, button_rect4.y))

    screen.blit(title, (10, 23))
    screen.blit(prav, (20, 80))
    screen.blit(tank1, (200, 10))

    pygame.display.update()
