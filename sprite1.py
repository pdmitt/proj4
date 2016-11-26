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
yellow = (255, 255, 0)

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
            self.speedx = -5 #change to speed up
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5 #change to speed up
        self.rect.x += self.speedx
        if self.rect.right > width: #creating a wall so that our right coord. does not get bigger than width
            self.rect.right = width
        if self.rect.left < 0: #coordinate-based screen
            self.rect.left = 0 #constraining player movement to screen

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top) #bottom of bullet at top of the player
        all_sprites.add(bullet) #add to group
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite): #don't know graphics yet
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width) #will alwas appear between left and right
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
  

    def update(self):
        self.rect.y += self.speedy #moves downwards
        if self.rect.top > height + 10:
            self.rect.x = random.randrange(0, width - self.rect.width) #will alwas appear between left and right
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite): #bullet is inheritting from the general class sprite
    def __init__(self, x, y): #x and y so we know player location
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 #bullet travles upwards so negative

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill() #removes any sprite from any group it is in if it goes off the screen

            #7:22 of Part 3


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = JamesBond()
all_sprites.add(player) #add any sprite we create so it gets animated and drawn
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#game loop
running = True
while running:
    clock.tick(FPS) #process input, handle updates, draw on the screen should meet FPS
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #game loop ends
        elif event.type == pygame.KEYDOWN: #bullet will shoot when a key is pressed
            if event.key == pygame.K_SPACE:
                player.shoot()

    #handle updates
    all_sprites.update()

    #check to see if bullet hits a mob
    hits = pygame.sprite.groupcollide(mobs,bullets, True, True) #if a bullet hits a mob, both will be deleted
    for hit in hits:
        m = Mob() #create new mob
        all_sprites.add(m)
        mobs.add(m) #always have 8 mobs because they will be created at the rate they are deleted

    #check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False) #returns list of any mobs which hit player
    if hits:
        running = False

    #draw/render
    screen.fill(pink)
    all_sprites.draw(screen)
    pygame.display.flip() #comes after drawing everything

pygame.quit()