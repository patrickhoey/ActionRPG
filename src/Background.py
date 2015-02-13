import pygame 
from pygame.locals import * 
from sys import exit
import os

background_image_filename = 'data/SFA3_CodyStage.jpg'

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)
SCREENRECT     = Rect(0, 0, 640, 480)

#set the path to current directory
os.chdir('C:/Documents/Website/public_html_old/Game_Dev/Python_Action_RPG/src')

class Hero(pygame.sprite.Sprite):
    speed = 10
    images = []
    animcycle = 12
    """moves character across the screen."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image = pygame.image.load('data/walking1.jpg').convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10,300
        self.move = 0
        self.frame = 0

    def moving(self, direction):
        if direction: 
            self.facing = direction
        self.image = self.images[0]
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame/self.animcycle%2]

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode( SCREEN_SIZE, 0, 32)
    pygame.display.set_caption("Action RPG")
    
    background = pygame.image.load(background_image_filename).convert()
    
    x,y = 0,0
    move_x, move_y = 0,0

    screen.set_clip(0,0,SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.fill( (0,0,0) )
    screen.blit(background, (0,0) )
    pygame.display.flip()
           
    pygame.display.update()
    
    img1 = pygame.image.load('data/walking1.bmp').convert()
    colorkey = img1.get_at((0,0))
    img1.set_colorkey(colorkey, RLEACCEL)
        
    img2 = pygame.image.load('data/walking2.bmp').convert()
    colorkey = img2.get_at((0,0))
    img2.set_colorkey(colorkey, RLEACCEL)
        
    Hero.images = [img1, img2]
  
    hero = Hero()
    
    all = pygame.sprite.RenderUpdates()
    allsprites = pygame.sprite.RenderPlain(hero)
    
    #assign default groups to each sprite class
    Hero.containers = all
    
    x,y = 0,0
    move_x, move_y = 0,0
    #Main Loop
    while 1:
        #lock to 60 fps
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = -1
                elif event.key == K_RIGHT:
                    move_x = +1
                elif event.key == K_UP:
                    move_y = -1
                elif event.key == K_DOWN:
                    move_y = +1
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    move_x = 0
                elif event.key == K_RIGHT:
                    move_x = 0
                elif event.key == K_UP:
                    move_y = 0
                elif event.key == K_DOWN:
                    move_y = 0
            
        x += move_x
        y += move_y
        
        if x < 0:
          x = 0
        
        keystate = pygame.key.get_pressed()
        
         # clear/erase the last drawn sprites
        all.clear(screen, background)

        #update all the sprites
        all.update()
        
        #handle player input
        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        hero.moving(direction)
        
        allsprites.update()
    #Draw Everything
        screen.blit(background, (-x*hero.speed, 0))
        allsprites.draw(screen)
        pygame.display.flip()
      
            
#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()

