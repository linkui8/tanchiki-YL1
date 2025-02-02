import pygame
from pygame.locals import *
from game import Game
from config import *
from util import Direction



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    sound_in = pygame.mixer.Sound('data/souds/inmusic.ogg')
    sound_in.play()
    a = open("level.txt", "r")
    game = Game(a.read())
    a.close()
    pygame.mixer.music.load("data/souds/background.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)
    sound_shoot = pygame.mixer.Sound('data/souds/shoot.ogg')
    sound_move = pygame.mixer.Sound('data/souds/move.ogg')


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_t:
                    game.switch_my_tank()
                elif event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    game.fire()
                    sound_move.stop()
                    sound_shoot.play()
                    sound_move.play()
                elif event.key == K_r:
                    game = Game()
                elif event.key == K_p:
                    game.testus()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            game.my_tank_move_to_direction = Direction.UP
            sound_move.play()
            sound_move.set_volume(0.1)
        elif keys[pygame.K_s]:
            game.my_tank_move_to_direction = Direction.DOWN
            sound_move.play()
            sound_move.set_volume(0.1)
        elif keys[pygame.K_a]:
            game.my_tank_move_to_direction = Direction.LEFT
            sound_move.play()
            sound_move.set_volume(0.1)
        elif keys[pygame.K_d]:
            game.my_tank_move_to_direction = Direction.RIGHT
            sound_move.play()
            sound_move.set_volume(0.1)
        else:
            game.my_tank_move_to_direction = None
            sound_move.stop()
        
        screen.fill((128, 128, 128))

        game.update()
        game.render(screen)

        if DEBUG:
            pygame.draw.circle(screen, (0, 255, 255), game.my_tank.gun_point, 4, 1)

        pygame.display.flip()

    pygame.quit()
