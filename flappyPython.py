import pygame

pygame.init()

surface = pygame.display.set_mode((800, 400))

pygame.display.set_caption('Flappy Python')

clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #update() => updates specific areas in the screen
    pygame.display.update()

    #set to 60 fps
    clock.tick(60)

pygame.quit()
quit()