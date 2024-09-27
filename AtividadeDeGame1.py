import pygame

pygame.init()

janela = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Roblox RXT ON")

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False