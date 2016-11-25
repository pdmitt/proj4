import pygame
import random

width = 800
height = 600
FPS = 30 #frames per second

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Player(pygame.sprite.Sprite): #built-in basic Sprite set up
    def __init__(self): #will run whenever we create the player object
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50)) #needed to know what the sprite looks like
        self.image.fill(green)
        self.rect = self.image.get_rect() #needed rectangle to enclose sprite
        self.rect.center = (width / 2, height / 2) #putting sprite in the center


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
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip() #comes after drawing everything

pygame.quit()