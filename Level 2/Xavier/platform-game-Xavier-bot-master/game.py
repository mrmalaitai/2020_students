import pygame, sys
from pygame.locals import *
def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = [] 
    for row in data:
        game_map.append(list(row))
    return game_map


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


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
        player_rect.x = 54
        player_rect.y = 323
        enemy_rect.x = -50
        enemy_rect.y = 400
    return()

clock = pygame.time.Clock()
pygame.init() # initiates pygame
pygame.display.set_caption('You Mad Yet?')
WINDOW_SIZE = (1000,600)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled
moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0
true_scroll = [0,0]
game_map = load_map('map')

#   Gets the images from the 
floor_img = pygame.image.load('floor.png')
bounce_img = pygame.image.load('bounce.png')
slide_img = pygame.image.load('slide.png')
wall_img = pygame.image.load('wall.png')


player_img = pygame.image.load('player.png').convert()
player_img.set_colorkey((255,255,255))

#   Player_H = Player Height, Player_W = Player Width
PLAYER_W = 5
PLAYER_H = 13

#   Enemy_H = Enemy Height, Enemy_W = Enemy Width
ENEMY_W = 9
ENEMY_H = 18

player_rect = pygame.Rect(60,275,5,13)
enemy_rect = pygame.Rect(40, 275, 9, 18)
enemy_img = pygame.image.load('chaser.png').convert()

while True: # game loop
    display.fill((101,35,122)) # clear screen by filling it with Purple
    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20 # a number lower than 20 speeds up the parallax
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20 # a number higher than 20 slows down the parallax
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        #   In the map text file, whenever there's a number other than 0, depending on the number, an image linked to the number (eg. the number 1 is the image of floor) an image will be placed there
        for tile in layer:
            if tile == '1':
                display.blit(floor_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                display.blit(bounce_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '3':
                display.blit(slide_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '4':
                display.blit(wall_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1

    #   The Player movement code controls the speed of the player when moving left or right
    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] += 2
    if moving_left == True:
        player_movement[0] -= 2
    player_movement[1] += vertical_momentum

    #   The Vertical momentum code controls the height of the player's jumps
    vertical_momentum += 0.35
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

    #print(player_rect.x, player_rect.y)
    check_distance(player_rect,enemy_rect)
    # Respawn after falling
    if player_rect.y > 370:
        player_rect.x = 54 #54
        player_rect.y = 323 #323

        enemy_rect.x = -50
        enemy_rect.y = 400

    # These codes are for the bounce blocks that the player jumps onto so that they can bounce onto a higher platform
    if player_rect.y == 307 and player_rect.x > 668 and player_rect.x < 704:
        if air_timer < 6:
            vertical_momentum = -6.5

    if player_rect.y == 243 and player_rect.x > 27 and player_rect.x < 48:
        if air_timer < 6:
            vertical_momentum = -10

    if player_rect.y == 163 and player_rect.x > 427 and player_rect.x < 448:
        if air_timer < 6:
            vertical_momentum = -6.5


    #   These codes are for the sliding blocks that the player will move left and right much faster when they are on the platform
    if player_rect.x >= 219 and player_rect.x <= 256 and player_rect.y == 227:
        if (moving_right):
            player_rect.x += 7
        if (moving_left):
            player_rect.x-= 7

    if player_rect.x >= 123 and player_rect.x <= 160 and player_rect.y == 227:
        if (moving_right):
            player_rect.x += 7
        if (moving_left):
            player_rect.x-= 7

    if player_rect.x >= 251 and player_rect.x <= 272 and player_rect.y == 99:
        if (moving_right):
            player_rect.x += 7
        if (moving_left):
            player_rect.x-= 7


    if player_rect.x >= 299 and player_rect.x <= 320 and player_rect.y == 99:
        if (moving_right):
            player_rect.x += 7
        if (moving_left):
            player_rect.x-= 7

    if player_rect.x >= 491 and player_rect.x <= 512 and player_rect.y == 99:
        if (moving_right):
            player_rect.x += 7
        if (moving_left):
            player_rect.x-= 7

    if player_rect.x >= 971 and player_rect.x <= 992 and player_rect.y == 323:
        if (moving_right):
            player_rect.x += 7
        if (moving_left):
            player_rect.x-= 7

    # Finish line Coordinates
    # x = 1195 - 1248
    # y = 323

    if player_rect.x >= 1195 and player_rect.x <=1248 and player_rect.y == 323:
        escaped()


    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)

    