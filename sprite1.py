#sprites from kenney.nl
#explosion from thecandyjam.com
#sound effects from http://www.bfxr.net/
#copycat by syncopika retrieved from <http://opengameart.org/content/copycat> licensed under CC-BY 3.0
import pygame
import random
from os import path #commands to set up folder for graphics

img_dir = path.join(path.dirname(__file__), "img")
sound_dir = path.join(path.dirname(__file__), "sound") #path to sound folder so we can look up the sounds

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
pygame.mixer.init() #handles sound effects and music. needed to play sound
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shoot the Fruit!")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('Arial black')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size) #created font object
    text_on = font.render(text, True, white) #surface for writing for pixels, True is set so we can use an anti-aliased font which is cleaner (adds grey pixels)
    text_rect = text_on.get_rect() #surface for rect
    text_rect.midtop = (x, y) #positioning score and lives as found from python documentation
    surf.blit(text_on, text_rect) #blit surfac on location of rect

def draw_life_bar(x, y, pct):
    if pct < 0: #in case bar is less than 0 and bar is incorrectly pictured (negative)
        pct = 0
    barwidth = 100
    barheight = 10
    fill = (pct / 100) * barwidth
    outline_rect = pygame.Rect(x, y, barwidth, barheight)
    fill_rect = pygame.Rect(x, y, fill, barheight)
    pygame.draw.rect(screen, green, fill_rect) #specify surface
    pygame.draw.rect(screen, white, outline_rect, 2) #2 pixels wide for outline

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
        self.shooting_wait = 250
        self.last_shot = pygame.time.get_ticks() #adding continuous shooting ability
        self.lifebar = 100
        #self.lives = 7

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5 #change to speed up
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5 #change to speed up
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > width: #creating a wall so that our right coord. does not get bigger than width
            self.rect.right = width
        if self.rect.left < 0: #coordinate-based screen
            self.rect.left = 0 #constraining player movement to screen

    def shoot(self):
        current = pygame.time.get_ticks()
        if current - self.last_shot > self.shooting_wait: #speeding up shooting delay time
            self.last_shot = current
            bullet = Bullet(self.rect.centerx, self.rect.top) #bottom of bullet at top of the player
            all_sprites.add(bullet) #add to group
            bullets.add(bullet)
            shooting_sound.play() #adding sound to shoot
            shooting_sound.set_volume(.6) #adjusting sound to play at 60% full volume

class Fruit(pygame.sprite.Sprite):
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
        self.speedy = random.randrange(1, 10) #random assignment of speed
  

    def update(self):
        self.rect.y += self.speedy #moves downwards
        if self.rect.top > height + 10:
            self.rect.x = random.randrange(0, width - self.rect.width) #will alwas appear between left and right
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)

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
bullet_img = pygame.image.load(path.join(img_dir, "laserBlue16.png")).convert()
fruit_images = []
fruit_ls = ["banana.png", "apple.png"] #loading game graphics


for i in fruit_ls: #loops through list of files
    fruit_images.append(pygame.image.load(path.join(img_dir, i)).convert()) #loads images

#loading game sounds
shooting_sound = pygame.mixer.Sound(path.join(sound_dir, "Laser_Shoot9.wav")) #smaller sound effect
shot_target = pygame.mixer.Sound(path.join(sound_dir, "Powerup10.wav")) #smaller sound effect
pygame.mixer.music.load(path.join(sound_dir, "copycat(revised).wav")) #adding continuous background music
pygame.mixer.music.set_volume(1) #setting volume to 100% times its original volume

all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player1()
all_sprites.add(player) #add any sprite we create so it gets animated and drawn
for i in range(10):
    f = Fruit() #make a mob
    all_sprites.add(f) #add it to the new groups
    fruits.add(f)

score = 0
#lives = 7
pygame.mixer.music.play(loops=-1) #adding music to the game and plays infinitely

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

    #check to see if laser hits a fruit
    hits = pygame.sprite.groupcollide(fruits, bullets, True, True) #if a bullet hits a fruit, both will be deleted
    for hit in hits:
        score = score + 10 #adding points to score
        shot_target.play() #sound added when laser hits fruit target
        shot_target.set_volume(.7) #adjusting collision sound
        f = Fruit() #create new fruits
        all_sprites.add(f)
        fruits.add(f) #always have 10 fruits because they will be created at the rate they are deleted
        #player.lives -= 1

    #check to see if a fruit hits the player
    hits = pygame.sprite.spritecollide(player, fruits, True, pygame.sprite.collide_circle) #mobs are now removed when they hit the player
    for hit in hits:
        player.lifebar -= hit.radius
        if player.lifebar <= 0:
            running = False

    #draw/render
    screen.fill(deeppink)
    #screen.blit(background, background_rect) #copy pixels from one screen to another
    all_sprites.draw(screen)
    draw_text(screen, "Score: " + str(score), 24, width/2, 10) #fruits behind score. denoting where we want it drawn, str score, font size, centered horizontally, pixels down for "y"
    #draw_text(screen, "Lives: " + str(lives), 24, width/2, 10)
    draw_life_bar(5, 5, player.lifebar) #takes x and y, and what % of bar to fill
    pygame.display.flip() #comes after drawing everything
#test
pygame.quit()