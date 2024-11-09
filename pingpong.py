
import pygame, sys, random
from pygame import mixer





def ball_animation():
    global ball_speed_y,ball_speed_x
    # controls balls speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # allows ball to bounce at edges
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        #this next part restarts ball position to centre after it hits the walls on the side (after goal is scored)
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_y *= random.choice((1,-1)) #allows ball to restart at random direction after goal is scored
        ball_speed_x *= random.choice((1,-1))



    # allows ball to collide with the 2 rectangles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height





def opponent_animation():

    #if opponent.top < ball.y:
        #opponent.top += opponent_speed
    #if opponent.bottom > ball.y:
        #opponent.bottom -= opponent_speed

    #this next part makes sure opponent doesn't go off the screen
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height







pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ahahahahhahahaha u suck')

ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

bg_color = pygame.image.load('bigshaq.png') #background image
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1)) #allows ball to start at random direction
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 0



while True:

    screen.blit(bg_color, (0,0)) #background image
    #handling input (takes in user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #this code is for when the user PRESSES DOWN on the the button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        #this code is for when the user RELEASES the button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


        #this code is for when the opponent PRESSES DOWN on the button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed += 7
            if event.key == pygame.K_w:
                opponent_speed -= 7

        # this code is for when the opponent RELEASES the button
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_speed -= 7
            if event.key == pygame.K_w:
                opponent_speed += 7


    ball_animation()
    player_animation()
    opponent_animation()

    #visuals
    pygame.draw.rect(screen,light_grey, player)
    pygame.draw.rect(screen,light_grey, opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0), (screen_width/2,screen_height))

    #updating the window
    pygame.display.flip()
    clock.tick(60)

    #mixer.music.load("Big Shaq - Man's Not Hot lyrics.wav")
    #mixer.music.play()








