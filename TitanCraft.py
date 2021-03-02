#imports
import pygame
import time
from pygame.locals import *

#pritingDataOfTheWorld
print("""
WORLD DATA:
0 -> AIR
1 -> DIRT
2 -> GRASS
3 -> TREE
4 -> LEAVES
5 -> BRICKS
6 -> PLANKS
""")

#settingUpVariables
pygame.init()
screen_width = 480
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TitanCraft')
grass_icon = pygame.image.load('./img/grass_block.png')
clock = pygame.time.Clock()
global fps
fps = 30
global canWalk
canWalk = False

#drawingGrid
def draw_grid():
	for line in range(0, 60):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

#creatingWorldClass
class World():
    def __init__(self, data):
        self.tile_list = []
        
        dirt_img = pygame.image.load('./img/dirt_block.png')
        grass_img = pygame.image.load('./img/grass_block.png')
        tree_img = pygame.image.load('./img/tree_block.png')
        leaves_img = pygame.image.load('./img/leaves_block.png')
        bricks_img = pygame.image.load('./img/bricks.png')
        planks_img = pygame.image.load('./img/planks.png')
        bar_img = pygame.image.load('./img/barrier.png')
        p_img = pygame.image.load('./img/purple.png')
        r_img = pygame.image.load('./img/red.png')
        b_img = pygame.image.load('./img/blue.png')
        row_count = 0
        for row in data:
                col_count = 0
                for tile in row:
                        if tile == 1:
                                img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 2:
                                img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 3:
                                img = pygame.transform.scale(tree_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                                canWalk = True
                        if tile == 4:
                                img = pygame.transform.scale(leaves_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                                canWalk = True
                        if tile == 5:
                                img = pygame.transform.scale(bricks_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 6:
                                img = pygame.transform.scale(planks_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 7:
                                img = pygame.transform.scale(bar_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 8:
                                img = pygame.transform.scale(p_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 9:
                                img = pygame.transform.scale(r_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 10:
                                img = pygame.transform.scale(b_img, (tile_size, tile_size))
                                img_rect = img.get_rect()
                                img_rect.x = col_count * tile_size
                                img_rect.y = row_count * tile_size
                                tile = (img, img_rect)
                                self.tile_list.append(tile)
                        if tile == 0:
                            pass
                        col_count += 1
                row_count += 1
    def draw(self):
            for tile in self.tile_list:
                    screen.blit(tile[0], tile[1])

#creatingPlayerClass
class Player():
        def __init__(self, x, y):
                self.images_right = []
                self.images_left = []
                self.index = 0
                self.counter = 0
                for num in range(1, 3):
                        img_right = pygame.image.load(f'img/player{num}.png')
                        img_right = pygame.transform.scale(img_right, (tile_size, tile_size*2))
                        img_left = pygame.transform.flip(img_right, True, False)
                        self.images_right.append(img_right)
                        self.images_left.append(img_left)
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.sprint = False
                self.stand = True
                self.direction = 0
        def update(self):
                dx = 0
                dy = 0
                walk_cooldown = 5

                #getKeypressed
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] and self.jumped == False and self.stand == True:
                        self.vel_y = -15
                        self.jumped = True
                        self.stand = False
                if key[pygame.K_SPACE] == False:
                        self.jumped = False
                if key[pygame.K_RIGHT]:
                        dx += 5
                        self.counter += 1
                        self.direction = 1
                if key[pygame.K_LEFT]:
                        dx += -5
                        self.counter += 1
                        self.direction = -1
                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                        self.counter = 0
                        self.index = 0
                        if self.direction == 1:
                                self.image = self.images_right[self.index]
                        if self.direction == -1:
                                self.image = self.images_left[self.index]


                #handleAnimation
                if self.counter > walk_cooldown:
                        self.counter = 0
                        self.index += 1
                        if self.index >= len(self.images_right):
                                self.index = 0
                        if self.direction == 1:
                                self.image = self.images_right[self.index]
                        if self.direction == -1:
                                self.image = self.images_left[self.index]

		#addGravity
                self.vel_y += 1
                if self.vel_y > 10:
                        self.vel_y = 10
                dy += self.vel_y

                #checkForCollusion
                for tile in world.tile_list:
                        #checkForCollisionX
                        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                                if canWalk == False:
                                    dx = 0
                                else:
                                    pass
                        #checkForCollusionY
                        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                #jumping
                                if self.vel_y < 0:
                                        if canWalk == False:
                                            dy = tile[1].bottom - self.rect.top
                                            self.vel_y = 0
                                        else:
                                            pass
                                #falling
                                elif self.vel_y >= 0:
                                        if canWalk == False:
                                            dy = tile[1].top - self.rect.bottom
                                            self.vel_y = 0
                                            self.stand = True
                                        else:
                                            self.stand = False
                                
                self.rect.x += dx
                self.rect.y += dy
                if self.rect.bottom > screen_height:
                        self.rect.bottom = screen_height
                        dy = 0
                screen.blit(self.image, self.rect)

#creatingWaterClass


#definingWorldData                
world_data =[
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 5, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 7],
[4, 4, 4, 4, 0, 0, 0, 0, 4, 4, 4, 5, 0, 0, 7],
[4, 4, 4, 4, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 7],
[0, 3, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 5, 7],
[0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 7],
[0, 3, 0, 0, 0, 10, 0, 0, 0, 3, 0, 0, 0, 0, 7],
[8, 3, 0, 9, 0, 2, 2, 0, 0, 3, 8, 0, 5, 0, 7],
[2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#loadingSkyImageAndSettingUpGameVariables
bg_img = pygame.image.load('img/sky.png')
tile_size = 32
run = True
world = World(world_data)
player = Player(232, 320)
pygame.display.set_icon(grass_icon)

#mainloop
while run == True:
    screen.blit(bg_img, (0, 0))
    clock.tick(fps)
    world.draw()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

