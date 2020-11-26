#created by Lauren Ofa
#14/09/20
import pygame, sys
from pygame.locals import *


ENEMY_W=16
ENEMY_H=16
PLAYER_W=3
PLAYER_H=15

def check_distance(player_rect, enemy_rect):
    if player_rect.x < enemy_rect.x + ENEMY_W/2:
        enemy_rect.x -= 1
 
    if player_rect.x > enemy_rect.x + ENEMY_W/2:
        enemy_rect.x += 1
 
    if player_rect.y < enemy_rect.y + ENEMY_H/2:
        enemy_rect.y -= 1
 
    if player_rect.y > enemy_rect.y + ENEMY_H/2:
        enemy_rect.y += 1
 
    # If the enemy (width = 30, height = 30) interacts with player (width = 5, height = 13)
    if((player_rect.x + PLAYER_W >= enemy_rect.x and player_rect.y + PLAYER_H >= enemy_rect.y) and (player_rect.x <= enemy_rect.x + ENEMY_W and player_rect.y + PLAYER_H >= enemy_rect.y) and (player_rect.x + PLAYER_W >= enemy_rect.x and player_rect.y <= enemy_rect.y + ENEMY_H) and (player_rect.x <= enemy_rect.x + ENEMY_W and player_rect.y <= enemy_rect.y + ENEMY_H)):
        player_rect.x = 100
        player_rect.y = 100
        enemy_rect.x=40
        enemy_rect.y=100
 
    return()

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
dirt_img = pygame.image.load('dirt.png')
bricks_img = pygame.image.load('bricks.png')
spike_img = pygame.image.load('spike.png')
player_img = pygame.image.load('player.png').convert()
player_img.set_colorkey((100,100,100)) #changed color of background 
enemy_img = pygame.image.load('ghost.png')
player_rect = pygame.Rect(100,100,16,16)
enemy_rect = pygame.Rect(20,100,16,16)
while True: # game loop
    display.fill((128,0,0)) # clear screen by filling it with blue
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
                display.blit(bricks_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                display.blit(black_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '3':
                display.blit(spike_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '4':
                display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
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
    display.blit(enemy_img,(enemy_rect.x-scroll[0],enemy_rect.y-scroll[1]))
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

    if(player_rect.y>= 400):
        player_rect.x=100
        player_rect.y=100
        enemy_rect.x=40
        enemy_rect.y=100
    check_distance(player_rect, enemy_rect)
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
