import pygame
import random
import os #commands to set up folder for graphics

width = 800
height = 600
FPS = 30 #frames per second

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink =  (255, 192, 203)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite): #built-in basic Sprite set up
    def __init__(self): #will run whenever we create the player object
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(black) #makes background of graphic transparent
        self.rect = self.image.get_rect() #needed rectangle to enclose sprite
        self.rect.center = (width/2, height/2) #putting sprite in the center
        self.y_speed = 5 

    def update(self):
        self.rect.x += 5
        # self.rect.y += self.y_speed #makes the sprite move up and down
        # if self.rect.bottom > height - 200: #don't want sprite going off the screen so we reverse directions
        #     self.y_speed = -5
        # if self.rect.top < 200: #same as above
        #     self.y_speed = 5
        if self.rect.left > width:
            self.rect.right = 0 #if sprite goes off the screen it will come back on


pygame.init()
pygame.mixer.init() #handles sound effects and music
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#game loop
running = True
while running:


    clock.tick(FPS) #process input, handle updates, draw on the screen should meet FPS
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #game loop ends

    #handle updates
    all_sprites.update()

    #draw/render
    screen.fill(pink)
    all_sprites.draw(screen)
    pygame.display.flip() #comes after drawing everything

pygame.quit()