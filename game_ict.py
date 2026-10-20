import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("My Tower Defense Game")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background.image='Grass (2).pixil'
    pygame.display.flip()
    clock.tick(60)
pygame.quit()