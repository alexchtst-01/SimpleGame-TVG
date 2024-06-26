import pygame as pg 
from math import * 
from pygame.math import Vector2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TRANSARENT = (0, 0, 0, 0)
DELAY = 5000

class Helper:
    def __init__(self):
        pass
    
    def calculateFitSize(self):
        pass
    
    def getFixPosition(self):
        pass

class HeroPlayer(pg.sprite.Sprite):
    def __init__(self, pos):
        super(HeroPlayer, self).__init__()
        
        self.space_pressed = False
        
        self.angle = 0
        self.vel = 0.4
        
        self.px = pos[0]
        self.py = pos[1]
        
        self.image = pg.Surface((120, 50), pg.SRCALPHA)
        self.image.fill(TRANSARENT)
        # pg.draw.circle(self.image, RED, (50, 50), 50)
        # self.obj = pg.load
        image = pg.image.load("rectangle.png")
        self.image.blit(image, (10, 0))
        
        self.original_image = self.image
        
        # get the center of the surface
        self.rect = self.image.get_rect(center=pos)
        
    # rotation
    def rotateCW(self):
        self.angle -= 0.05
        self.image = pg.transform.rotate(self.original_image, angle=self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def rotateCCW(self):
        self.angle += 0.05
        self.image = pg.transform.rotate(self.original_image, angle=self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    # translation
    def forward(self):
        self.px += cos(self.angle * pi / 180) * self.vel
        self.py -= sin(self.angle * pi / 180) * self.vel
        self.rect.center = (self.px, self.py)
    
    def backward(self):
        self.px -= cos(self.angle * pi / 180) * self.vel
        self.py += sin(self.angle * pi / 180) * self.vel
        self.rect.center = (self.px, self.py)
    
    # reflection
    def reflect(self):
        self.image = pg.transform.flip(self.image, flip_x=True, flip_y=False)

def main():
    pg.init()
    clock = pg.time.Clock()
    
    screen = pg.display.set_mode((720, 480))
    run = True
    
    player = HeroPlayer(pos=(100, 100))
    playerhero = pg.sprite.RenderPlain((player))
    
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        screen.fill(WHITE)
        pg.display.set_caption("505820 - Alex Cinatra")
        key = pg.key.get_pressed()
        
        if key[pg.K_RIGHT] or key[pg.K_d]:
            player.rotateCW()
        
        if key[pg.K_LEFT] or key[pg.K_a]:
            player.rotateCCW()
        
        if key[pg.K_UP] or key[pg.K_w]:
            player.forward()
            
        
        if key[pg.K_DOWN] or key[pg.K_s]:
            player.backward()
        
        if key[pg.K_SPACE] and not player.space_pressed:
            player.reflect()
            player.space_pressed = True
        elif not key[pg.K_SPACE]:
            player.space_pressed = False
        
        playerhero.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()
    pg.quit()
        