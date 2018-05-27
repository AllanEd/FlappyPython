import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FLAPPY_PYTHON_PLAYER_IMG_WIDTH = 100
FLAPPY_PYTHON_PLAYER_IMG_HEIGHT = 100
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Python')
clock = pygame.time.Clock()

img = pygame.image.load('assets/flappy_python_player.png')
x = 100
y = 100

# initial move => no move
y_move = 0


def game_over():
    pygame.quit()
    quit()


def flappy_python(x, y, image):
    screen.blit(img, (x, y))


def ifKeyUpIsDown():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            return True


def ifKeyUpIsUp():
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            return True


game_over_state = False

# game loop
while not game_over_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_state = True

        if (ifKeyUpIsDown()):
            y_move = -5

        if (ifKeyUpIsUp()):
            y_move = 5

    y += y_move

    # fills background
    screen.fill(BLACK)
    # add flappy python
    flappy_python(x, y, img)

    # quits game if user hits bottom or top screen
    if y > (SCREEN_HEIGHT - FLAPPY_PYTHON_PLAYER_IMG_WIDTH) or y < 0:
        game_over()

    # update() => updates specific areas in the screen
    pygame.display.update()
    # set to 60 fps
    clock.tick(FPS)

game_over()
