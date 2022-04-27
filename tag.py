import pygame
import time
# Initialize game engine
pygame.init()

# Different Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (70,130,180)
death_color = (0, 0, 170)
black = (0, 0, 0)
baby_blue = (137, 207, 240)
pink = (255,182,193)

# Sets display resolution2wº
window_width = 1366
window_height = 768

player_size = 50, 90

player1x = window_width/4
player1y = window_height/4

player2x = window_width/1.5
player2y = window_height/1.5

collision_error = 5

# Opens a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("TAG")

clock_tick_rate = 117  # Refresh rate
speed = 3

clock = pygame.time.Clock()  # Saves value for the refresh rate

font = pygame.font.Font('freesansbold.ttf', 32)
timer_font = pygame.font.Font('freesansbold.ttf', 70)
winner_font = pygame.font.Font('freesansbold.ttf', 75)

boy_right = pygame.image.load('boy.png')
boy_left = pygame.transform.flip(boy_right, True, False)

girl_right = pygame.image.load('girl.png')
girl_left = pygame.transform.flip(girl_right, True, False)

p1 = "tagger"
p2 = "player"

p1_text = font.render('''Player1: {}'''.format(p1), True, blue)
p2_text = font.render('''Player2: {}'''.format(p2), True, pink)

p1_winner = winner_font.render("Tagger Win!", True, blue)
p2_winner = winner_font.render("Player Win!", True, pink)

target_time = 20

screen.blit(boy_right, (player1x, player1y))
running = True
start_time = time.time()
last_boy = boy_right
last_girl = girl_right
while running:
    screen.fill(baby_blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()

    timer = timer_font.render("{}".format(round((time.time() - start_time)-target_time)*-1), True, white)
    screen.blit(timer, (window_width/2-20, 0))

    if (time.time() - start_time) > target_time:

        screen.blit(last_boy, (player1x, player1y))
        screen.blit(last_girl, (player2x, player2y))
        screen.blit(p1_text, (5, 5))
        screen.blit(p2_text, (window_width-250, 5))
        screen.blit(p2_winner, (window_width/2 - 200, window_height/2-100))
        pygame.display.update()

        time.sleep(0.25)

        player1x = window_width/4
        player1y = window_height/4

        player2x = window_width/1.5
        player2y = window_height/1.5

        time.sleep(0.25)

        if p1 == "tagger":
            p2 = "tagger"
            p1 = "player"
        elif p2 == "tagger":
            p1 = "tagger"
            p2 = "player"
        p1_text = font.render('''Player1: {}'''.format(p1), True, blue)
        p2_text = font.render('''Player2: {}'''.format(p2), True, pink)

        start_time = time.time()

    
    if player1x > (window_width - player_size[0]):
        player1x = 0
    elif player2x > (window_width - player_size[0]):
        player2x = 0

    elif player1x < 0:
        player1x = window_width - player_size[0]
    elif player2x < 0:
        player2x = window_width - player_size[0]

    elif player1y > (window_height - player_size[1]):
        player1y = 0
    elif player2y > (window_height - player_size[1]):
        player2y = 0

    elif player1y < 0:
        player1y = window_height - player_size[1]
    elif player2y < 0:
        player2y = window_height - player_size[1]


    keys = pygame.key.get_pressed()  
    if keys[pygame.K_a]:
        player1x -= speed
        last_boy = boy_left
        screen.blit(boy_left, (player1x, player1y))
    elif keys[pygame.K_d]:
        player1x += speed
        last_boy = boy_right
        screen.blit(boy_right, (player1x, player1y))
    if keys[pygame.K_w]:
        player1y -= speed
        if not keys[pygame.K_a]:
            last_boy = boy_right
            screen.blit(boy_right, (player1x, player1y))
    elif keys[pygame.K_s]:
        player1y += speed
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            last_boy = boy_left
            screen.blit(boy_left, (player1x, player1y))
    elif not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
        screen.blit(last_boy, (player1x, player1y))


    if keys[pygame.K_LEFT]:
        player2x -= speed
        screen.blit(girl_left, (player2x, player2y))
        last_girl = girl_left
    elif keys[pygame.K_RIGHT]:
        player2x += speed
        screen.blit(girl_right, (player2x, player2y))
        last_girl = girl_right
    if keys[pygame.K_UP]:
        player2y -= speed
        if not keys[pygame.K_LEFT]:
            last_girl = girl_right
            screen.blit(girl_right, (player2x, player2y))
    elif keys[pygame.K_DOWN]:
        player2y += speed
        if not keys[pygame.K_RIGHT]:
            last_girl = girl_left
            screen.blit(girl_left, (player2x, player2y))
    elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        screen.blit(last_girl, (player2x, player2y))
        

    if player1y < (player2y + (player_size[1]-collision_error)) and player1y > (player2y - (player_size[1]-collision_error)):
        if ((player1x > player2x
            and player1x < (player2x + (player_size[0]-collision_error)))
            or ((player1x + (player_size[0]-collision_error)) > player2x
            and (player1x + (player_size[0]-collision_error)) < (player2x + (player_size[0]-collision_error)))):

            screen.blit(p1_text, (5, 5))
            screen.blit(p2_text, (window_width-250, 5))
            screen.blit(p1_winner, (window_width/2 - 200, window_height/2-100))
            pygame.display.update()

            time.sleep(0.25)

            player1x = window_width/4
            player1y = window_height/4

            player2x = window_width/1.5
            player2y = window_height/1.5

            time.sleep(0.25)

            if p1 == "tagger":
                p2 = "tagger"
                p1 = "player"
            elif p2 == "tagger":
                p1 = "tagger"
                p2 = "player"
            p1_text = font.render('''Player1: {}'''.format(p1), True, blue)
            p2_text = font.render('''Player2: {}'''.format(p2), True, pink)

            start_time = time.time()

    screen.blit(p1_text, (5, 5))
    screen.blit(p2_text, (window_width-250, 5))

    pygame.display.flip()
    clock.tick(clock_tick_rate)