import pygame
import random
import time
import threading
# Initialize game engine
pygame.init()

# Different Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

# Sets display resolution
window_width = 750
window_height = 750

player_x = window_width/20
player_y = window_height/20

player1_posx = window_width/1.5
player1_posy = window_height/1.5

player2_posx = window_width/4
player2_posy = window_height/4

# Opens a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("AVE")

clock_tick_rate = 350  # Refresh rate

clock = pygame.time.Clock()  # Saves value for the refresh rate

def food():
    for i in range(2):
        foodx = round(random.randint(0, window_width - int(player_x)))
        foody = round(random.randint(0, window_height - int(player_y)))
        pygame.draw.rect(screen, white, [foodx, foody, player_x, player_y])

running = True
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1_posx -= 1
    if keys[pygame.K_d]:
        player1_posx += 1
    if keys[pygame.K_w]:
        player1_posy -= 1
    if keys[pygame.K_s]:
        player1_posy += 1

    if keys[pygame.K_LEFT]:
        player2_posx -= 1
    if keys[pygame.K_RIGHT]:
        player2_posx += 1
    if keys[pygame.K_UP]:
        player2_posy -= 1
    if keys[pygame.K_DOWN]:
        player2_posy += 1
    
    if player1_posx > (window_width - player_x):
        player1_posx = 0
    if player2_posx > (window_width - player_x):
        player2_posx = 0

    if player1_posy > (window_height - player_y):
        player1_posy = 0
    if player2_posy > (window_height - player_y):
        player2_posy = 0

    if player1_posy < 0:
        player1_posy = window_height - player_y
    if player2_posy < 0:
        player2_posy = window_height - player_y

    if player1_posx < 0:
        player1_posx = window_height - player_x
    if player2_posx < 0:
        player2_posx = window_height - player_x

    pygame.draw.rect(screen, white, [player1_posx, player1_posy, player_x, player_y])
    pygame.draw.rect(screen, green, [player2_posx, player2_posy, player_x, player_y])
    food()


    pygame.display.flip()
    clock.tick(clock_tick_rate)
