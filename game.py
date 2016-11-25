#Frames per second manipulation

#required 
import pygame
pygame.init(); #pygame library initializes itself

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position vars
x_pos = 0
y_pos = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock() #create an object to help track time

#create a surface
screen = pygame.display.set_mode((600,600)) #width, height creates a surface

#lets add a title, aka "caption"
pygame.display.set_caption("James Bond 007") #title
pygame.display.update()		#only updates portion specified

gameExit = False
while not gameExit:
	screen.fill(red)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		x_delta=0;
		y_delta=0;
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10
	
	x_pos +=x_delta
	y_pos +=y_delta
	screen.fill(black, rect=[x_pos,y_pos, 20,20])
	pygame.display.update()		
	clock.tick(30)

	class Player(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.Surface((50, 50))
			self.image.fill(green)
			self.rect = self.image.get_rect()
			#self.rect.center = (WIDTH / 2, HEIGHT / 2)

	all_sprites = pygame.sprite.Group()
	player = Player()
	all_sprites.add(player)

# class bad(Sprite):
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		self.image = Surface(20, 20) #image or shape to draw for this sprite- a surface
# 		self.rect = Rect(0,0, 40, 50)


#required
pygame.quit()
quit()				#exits python