import pygame, sys, time

from pygame.locals import *

# CONSTANTS

CREEPER_W = 35 
CREEPER_H = 20
PLAYER_W = 3
PLAYER_H = 15

def load_map(path):

    f = open(path + '.txt','r')
    data = f.read()
    f.close()

    data = data.split('\n')
    game_map = []

    for row in data:
        game_map.append(list(row))
    return game_map
    
def collision_test(rect,tiles):

    hit_list = []

    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):

    collision_types = {'top':False,'bottom':False,'right':False,'left':False}

    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)

    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)

    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types
    
def creeper_chase(player_rect, creeper_rect):
    
    if player_rect.x < creeper_rect.x + CREEPER_W/2:
        creeper_rect.x -= 1 
        
    if player_rect.x > creeper_rect.x + CREEPER_W/2:
        creeper_rect.x += 1
 
    if player_rect.y < creeper_rect.y + CREEPER_H/2:
        creeper_rect.y -= 1
 
    if player_rect.y > creeper_rect.y + CREEPER_H/2:
        creeper_rect.y += 1
 
    # If the enemy (width = 30, height = 30) interacts with player (width = 5, height = 13)
    if((player_rect.x + PLAYER_W >= creeper_rect.x and player_rect.y + PLAYER_H >= creeper_rect.y) and (player_rect.x <= creeper_rect.x + CREEPER_W and player_rect.y + PLAYER_H >= creeper_rect.y) and (player_rect.x + PLAYER_W >= creeper_rect.x and player_rect.y <= creeper_rect.y + CREEPER_H) and (player_rect.x <= creeper_rect.x + CREEPER_W and player_rect.y <= creeper_rect.y + CREEPER_H)):
        player_rect.x = 164
        player_rect.y = 483
 
    return()    

clock = pygame.time.Clock()

pygame.init() # initiates pygame
pygame.display.set_caption('Escape The Crepper!')
WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

moving_right = False
moving_left = False

vertical_momentum = 0
air_timer = 0
true_scroll = [0,0]

game_map = load_map('map')

floor_img = pygame.image.load('IMAGES/floor.png')
top_locker_img = pygame.image.load('IMAGES/top_locker.png')
middle_locker_img = pygame.image.load('IMAGES/middle_locker.png')
bottom_locker_img = pygame.image.load('IMAGES/bottom_locker.png')
concrete_img = pygame.image.load('IMAGES/concrete.png')
spring_img = pygame.image.load('IMAGES/spring.png')
portal_img = pygame.image.load('IMAGES/portal.png')
player_img = pygame.image.load('IMAGES/player.png').convert()
creeper_img = pygame.image.load('IMAGES/creeper.png')
finish_img = pygame.image.load('IMAGES/finish.png')
player_img.set_colorkey((255,255,255))
player_rect = pygame.Rect(164,483,5,13)
creeper_rect = pygame.Rect(0,483,35,20)

while True: # game loop

    display.fill((49, 54, 50))

    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20 # a number lower than 20 speeds up the parallax
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20 # a number higher than 20 slows down the parallax

    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(floor_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                display.blit(top_locker_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '3':
                display.blit(middle_locker_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '4':
                display.blit(bottom_locker_img,(x*16-scroll[0],y*16-scroll[1])) 
            if tile == '5':
                display.blit(concrete_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '6':
                display.blit(spring_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '7':
                display.blit(portal_img,(x*16-scroll[0],y*16-scroll[1])) 
            if tile == '8':
                display.blit(finish_img,(x*16-scroll[0],y*16-scroll[1]))     
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1
    player_movement = [0,0]

    if moving_right == True:
        player_movement[0] += 2
    if moving_left == True:
        player_movement[0] -= 2

    player_movement[1] += vertical_momentum
    vertical_momentum += 0.3

    if vertical_momentum > 5:
        vertical_momentum = 5
    player_rect,collisions = move(player_rect,player_movement,tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 0
    else:
        air_timer += 1
    
    
    display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
    display.blit(creeper_img,(creeper_rect.x-scroll[0],creeper_rect.y-scroll[1]))

    print(player_rect.x, player_rect.y)

    if(player_rect.x == 2395 and player_rect.y == 515):
        player_rect.x = 32 
        player_rect.y = 147 

    if(player_rect.y == 467 and player_rect.x > 1120 and player_rect.x < 1136):
          if air_timer < 6:
            vertical_momentum = -8   

    if(player_rect.y == 371 and player_rect.x > 1391 and player_rect.x < 1407):
          if air_timer < 6:
                vertical_momentum = -7

    if(player_rect.y == 307 and player_rect.x > 1365 and player_rect.x < 1381):
          if air_timer < 5:
                vertical_momentum = -7  

    if(player_rect.y == 259 and player_rect.x > 2143 and player_rect.x < 2159):
          if air_timer < 5:
            vertical_momentum = -8           

    for event in pygame.event.get(): # event loop

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    vertical_momentum = -5

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    creeper_chase(player_rect, creeper_rect)

        
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)