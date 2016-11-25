import pygame
import random
import os #commands to set up folder for graphics

width = 500
height = 600
FPS = 60 #frames per second

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink =  (255, 192, 203)

pygame.init()
pygame.mixer.init() #handles sound effects and music
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Base Shapes")
clock = pygame.time.Clock()

class JamesBond(pygame.sprite.Sprite): #built-in basic Sprite set up
    def __init__(self): #will run whenever we create the player object
        pygame.sprite.Sprite.__init__(self) #needed for sprite to work
        self.image = pygame.Surface((50, 40))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height-10 #10 pixels from bottom of screen
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > width: #creating a wall so that our right coord. does not get bigger than width
            self.rect.right = width
        if self.rect.left < 0: #coordinate-based screen
            self.rect.left = 0 #constraining player movement to screen

all_sprites = pygame.sprite.Group()
player = JamesBond()
all_sprites.add(player) #add any sprite we create so it gets animated and drawn
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