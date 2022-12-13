import pygame, controls
import sys
from pushka import Gun
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Space game by Iliyas")
    bg_color = (0, 0, 0)
    pushka = Gun(screen)
    bullets = Group()    

    while True:
        controls.events(screen, pushka, bullets)
        pushka.update_pushka()
        controls.update(bg_color, screen, pushka, bullets)
        controls.update_bullets(bullets)
run()