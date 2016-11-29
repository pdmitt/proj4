import pygame
import random
from os import path #commands to set up folder for graphics

img_dir = path.join(path.dirname(__file__), "img")

width = 600
height = 600
FPS = 60 #frames per second

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
deeppink =  (255, 20, 147)
yellow = (255, 255, 0)

pygame.init()
pygame.mixer.init() #handles sound effects and music
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shoot the Fruit")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size) #created font object
    text_on = font.render(text, True, white) #surface for writing for pixels, True is set so we can use an anti-aliased font which is cleaner (adds grey pixels)
    text_rect = text_on.get_rect() #surface for rect
    text_rect.midtop = (x, y)
    surf.blit(text_on, text_rect) #blit surfac on location of rect

class Player1(pygame.sprite.Sprite): #built-in basic Sprite set up
    def __init__(self): #will run whenever we create the player object
        pygame.sprite.Sprite.__init__(self) #needed for sprite to work
        self.image = player_img
        self.image.set_colorkey(white) #removing outline of graphic
        self.rect = self.image.get_rect()
        self.radius = 30 #making collisions more accurate (smaller than half of pixel diameter)
        #pygame.draw.circle(self.image, green, self.rect.center, self.radius)
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

class Fruit(pygame.sprite.Sprite): #don't know graphics yet
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.transform.scale(mob1_img, (59, 33))
        self.image = random.choice(fruit_images) #randomly chooses between apples and bananas
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.9/2)
        #pygame.draw.circle(self.image, green, self.rect.center, self.radius)
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
        self.image = bullet_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10 #bullet travles upwards so negative

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0: #if it goes off the screen
            self.kill() #method? #removes any sprite from any group

#loading all game graphics
#background = pygame.image.load(path.join(img_dir, "background.bmp")).convert()
#background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "monkey.png")).convert()
#mob1_img = pygame.image.load(path.join(img_dir, "banana.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserBlue16.png")).convert()
fruit_images = []
fruit_ls = ["banana.png", "apple.png"]

for i in fruit_ls: #loops through list of files
    fruit_images.append(pygame.image.load(path.join(img_dir, i)).convert()) #loads images

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player1()
all_sprites.add(player) #add any sprite we create so it gets animated and drawn
for i in range(8):
    m = Fruit()
    all_sprites.add(m)
    mobs.add(m)

score = 0

#game loop
running = True
while running:
    clock.tick(FPS) #process input, handle updates, draw on the screen should meet FPS
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #game loop ends
        elif event.type == pygame.KEYDOWN: #bullet will shoot when a key is pressed
            if event.key == pygame.K_SPACE: #if the key was the space bar
                player.shoot() #function shoot is defined on line 46

    #handle updates
    all_sprites.update()

    #check to see if bullet hits a mob
    hits = pygame.sprite.groupcollide(mobs,bullets, True, True) #if a bullet hits a mob, both will be deleted
    for hit in hits:
        score = score + 10 #adding points to score
        m = Fruit() #create new mob
        all_sprites.add(m)
        mobs.add(m) #always have 8 mobs because they will be created at the rate they are deleted

    #check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False,pygame.sprite.collide_circle) #returns list of any mobs which hit player with circle collisions
    if hits:
        running = False

    #draw/render
    screen.fill(deeppink)
    #screen.blit(background, background_rect) #copy pixels from one screen to another
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, width/2, 10) #fruits behind score. denoting where we want it drawn, str score, font size, centered horizontally, pixels down for "y"
    pygame.display.flip() #comes after drawing everything

pygame.quit()