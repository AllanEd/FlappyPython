import pygame

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
surface = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Flappy Python')
clock = pygame.time.Clock()


def flappy_python(x, y, image):
    surface.blit(img, (x, y))


img = pygame.image.load('assets/flappy_python_player.png')
x = 150
y = 200

game_over = False

# game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # fills background
    surface.fill(black)
    # add flappy python
    flappy_python(x, y, img)

    # update() => updates specific areas in the screen
    pygame.display.update()
    # set to 60 fps
    clock.tick(60)

pygame.quit()
quit()
