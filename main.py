import pygame
import random
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
player = pygame.image.load('Purple fly.png')


#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

class pipeb:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.red = random.randrange(0, 200)
        self.blue = random.randrange(100, 200)
        self.green = random.randrange(0,100)
       
    def draw(self):
        pygame.draw.rect(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos, 20, 800))
        #if you want this to be a picture use the blit function instead
       
    def move(self):
        self.xpos -= 3
        if self.xpos < -20: #reset to right side if you move off the left
            self.xpos = random.randrange(800, 1000) #reset to random location off screen
           
    def collision(self, playerx, playery, width, height):
        if playerx + width > ex and playerx < ex  + weight and playery + height > ey and playery < ey + height:
            



class piped:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.red = random.randrange(0, 200)
        self.blue = random.randrange(100, 200)
        self.green = random.randrange(0,100)
       
    def draw(self):
        pygame.draw.rect(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos, 20, 800))
        #if you want this to be a picture use the blit function instead
       
    def move(self):
        self.xpos -= 3
        if self.xpos < -20: #reset to right side if you move off the left
            self.ypos = random.randrange(-600, -400)
            self.xpos = random.randrange(800, 900) #reset to random location off screen
           
    def collision(self, playerx, playery):
        if playerx + width > ex and playerx < ex  + weight and playery + height > ey and playery < ey + height #bounding box collision


#instantiate a pipe
p1 = pipeb(800, 500)
p2 = pipeb(900, 600)
p3 = piped(800, 500)
p4 = piped(900, 600)

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
framewidth = 24
frameheight = 17
rownum = 0
framenum = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform



while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
   
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
             
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True

            elif event.key == pygame.K_UP:
                keys[UP]=True
                
        if event.type == pygame.KEYUP:
                
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
         
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True: #only jump when on the ground
        vy = -4
 
    #gravity
    if isOnGround == False:
        vy+=.10 #notice this grows over time, aka ACCELERATION
   

    #update player position
    xpos+=vx
    ypos+=vy
   
    #update pipes
    p1.move()
    p2.move()
    p3.move()
    p4.move()
    # RENDER Section--------------------------------------------------------------------------------
           
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
 
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40)) #draw player
    screen.blit(player,(xpos, ypos), (framewidth * framenum, rownum * frameheight, framewidth, frameheight))

    #draw pipes
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()

