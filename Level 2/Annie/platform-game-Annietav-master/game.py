# Created by Annie

import pygame, sys
from pygame.locals import *

# Constants

PLAYER_W = 5
PLAYER_H = 13
GHOST_W = 16
GHOST_H = 16

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

# Ghost chasing player
def chasing(player_rect, ghost_rect):
    if player_rect.x < ghost_rect.x + GHOST_W/2:
        ghost_rect.x -= 1

    if player_rect.x > ghost_rect.x + GHOST_W/2:
        ghost_rect.x += 1

    if player_rect.y < ghost_rect.y + GHOST_H/2:
        ghost_rect.y -= 1

    if player_rect.y > ghost_rect.y + GHOST_H/2:
        ghost_rect.y += 1

    # If the enemy (width = 30, height = 30) interacts with player (width = 5, height = 13)
    if((player_rect.x + PLAYER_W >= ghost_rect.x and player_rect.y + PLAYER_H >= ghost_rect.y) and (player_rect.x <= ghost_rect.x + GHOST_W and player_rect.y + PLAYER_H >= ghost_rect.y) and (player_rect.x + PLAYER_W >= ghost_rect.x and player_rect.y <= ghost_rect.y + GHOST_H) and (player_rect.x <= ghost_rect.x + GHOST_W and player_rect.y <= ghost_rect.y + GHOST_H)):
        player_rect.x = 100
        player_rect.y = 100
        ghost_rect.x = 50
        ghost_rect.y = 50

    return()
    
clock = pygame.time.Clock()
pygame.init() # initiates pygame 
pygame.display.set_caption('Pygame Platformer')
WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled
moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0
true_scroll = [0,0]
game_map = load_map('map')
grass_img = pygame.image.load('grass.png')
black_img = pygame.image.load('black.png')
chair_img = pygame.image.load('chair.png')
brown_img = pygame.image.load('brown.png')
ghost_img = pygame.image.load('ghost.png')
player_img = pygame.image.load('player.png').convert()
player_img.set_colorkey((255,255,255))
player_rect = pygame.Rect(100,100,5,13)
ghost_rect = pygame.Rect(50,50,16,16)
while True: # game loop
    display.fill((139,0,0)) # clear screen by filling it with red
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
                display.blit(black_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '3':
                display.blit(chair_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '4':
                display.blit(brown_img,(x*16-scroll[0],y*16-scroll[1]))
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
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3
    player_rect,collisions = move(player_rect,player_movement,tile_rects)
    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 0
    else:
        air_timer += 1
    display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
    display.blit(ghost_img,(ghost_rect.x-scroll[0],ghost_rect.y-scroll[1]))

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

    if(player_rect.y>= 300):
        player_rect.x=100
        player_rect.y=100
 
    chasing(player_rect, ghost_rect)

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))

    pygame.display.update()
    clock.tick(60)