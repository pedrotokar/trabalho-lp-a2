from pygame.locals import *
import pygame as pg
from settings import SCREEN_DIMENSIONS, TILE_SIZE, FPS, PX_SCALE
from player import Player
from utils import load_image, load_map
from map_ import Map
import sys
from camera import Camera, SmoothCamera
from weapons import Gun
from cursor import Cursor
from enemies import Apache

pg.init()
pg.mouse.set_visible(False)
clock = pg.time.Clock()
screen = pg.display.set_mode(SCREEN_DIMENSIONS)

clock = pg.time.Clock()
map_layout = load_map('../trabalho-lp-a2/maps/map.json')["tiles"]
map = Map(map_layout)
player = Player(("..", "trabalho-lp-a2", "Sprites", "Player", "player.png"), (0,0), map.dimensions)
cursor = Cursor(("..", "trabalho-lp-a2", "Sprites", "cursors", "cursor1.png"), 3, (TILE_SIZE* 9.5, TILE_SIZE*5.5), player)
gun = Gun(("..", "trabalho-lp-a2", "Sprites", "weapons", "player_weapons", "math_gun.png"), cursor)
player.set_weapon(gun)
enemy = Apache((0,10), 2)
enemy2 = Apache((0,20), 1)
camera = Camera(screen, map, player)
camera = SmoothCamera(screen, map, player, cursor.rect.center)
cursor.set_camera(camera)
delta_time = 0

bullet_group = pg.sprite.Group()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or pg.key.get_pressed()[K_ESCAPE]:
            pg.quit()
            sys.exit()

    screen.fill('#F6E5CA')

    #enemy.update(player.rect, delta_time)
    #enemy2.update(player.rect, delta_time)
    #camera.render(enemy)
    camera.update()
    player.update()
    cursor.update()
    camera.render_map()
    camera.render_entity(player)
    camera.render_sprite_no_offset(cursor)
    #bullet_group.draw(screen)
    #camera.prepare_map_tiles()
    #camera.render_tiles()
    #camera.render_group(gun.bullet_group)
    #camera.render(player)
    #camera.render(gun)
    #camera.set_cursor_position(cursor.rect.center)


    #screen.blit(cursor.image, cursor.rect)

    #pg.draw.line(screen, (255, 0, 0), (0, SCREEN_DIMENSIONS[1] // 2), (SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1] // 2), 1)
    #pg.draw.line(screen, (255, 0, 0), (SCREEN_DIMENSIONS[0] // 2, 0), (SCREEN_DIMENSIONS[0] // 2, SCREEN_DIMENSIONS[1]), 1)

    pg.display.update()
    delta_time = clock.tick(FPS)
