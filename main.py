import pygame
import data_game
fps = 60
version = "1000"

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LUU BEE VA NHUNG NGUOI BAN")

clock = pygame.time.Clock()
TEST_PLAYER = data_game.entity_lifes(100,100,128,128,"test",0.2)

screen.fill((255, 255, 255))
running = True
while running:
    dt = clock.tick(fps) / 1000
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    TEST_PLAYER.update(dt)
    TEST_PLAYER.draw(screen)
    pygame.display.update()

pygame.quit()