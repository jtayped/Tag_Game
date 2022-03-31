import pygame
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

player_posx = window_width/2
player_posy = window_height/2

# Opens a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("AVE")

clock_tick_rate = 100  # Refresh rate

clock = pygame.time.Clock()  # Saves value for the refresh rate

running = True
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player_posx -= player_x
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player_posx += player_x
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player_posy -= player_y
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player_posy += player_y
    
    if player_posx > (window_width - player_x):
        player_posx = 0
    elif player_posx < 0:
        player_posx = window_width - player_x

    if player_posy > (window_height - player_y):
        player_posy = 0
    elif player_posy < 0:
        player_posy = window_height - player_y

    pygame.draw.rect(screen, white, [player_posx, player_posy, player_x, player_y])
    
    
    pygame.display.flip()
    clock.tick(clock_tick_rate)
