import pygame

pygame.init()

pygame.display.set_mode((600, 400),pygame.DROPFILE | pygame.HWSURFACE | pygame.FULLSCREEN)
pygame.display.set_caption("Первая игра на PyGame")
pygame.display.set_icon(pygame.image.load("app2.bmp"))

clock = pygame.time.Clock()
FPS = 60
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)