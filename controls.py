import pygame, sys
from bullet import Bullet

def events(screen, pushka, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pushka.mright = True
            elif event.key == pygame.K_a:
                pushka.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, pushka)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                pushka.mright = False
            elif event.key == pygame.K_a:
                pushka.mleft = False


def update(bg_color, screen, pushka, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pushka.output()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)




