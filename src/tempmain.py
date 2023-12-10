import pygame
from settings import SCREEN_DIMENSIONS
from menu import Menu
from game import Game
from cursor import Cursor
from settings import HIT_SOUND

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("sounds/ironmain.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Guerreiros Integrais")
pygame.mouse.set_visible(True)

menu = Menu(screen)
game = Game(screen)

cursor = Cursor(("Sprites", "cursors", "cursor2.png"), (0,0))

while True:

    click = False

    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        quit()

    screen.fill("white")

    cursor.update()

    if menu.on_menu:
        for event in pygame.event.get(pygame.MOUSEBUTTONUP):
            if event.button == 1:
                click = True
        menu.update(click)
    else:
        game.run(delta_time)

    screen.blit(cursor.image, cursor.rect)

    pygame.display.update()
    delta_time = clock.tick(60)
    

