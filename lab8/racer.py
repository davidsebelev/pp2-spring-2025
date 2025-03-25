import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

screen_width = 400
screen_height = 600
speed = 5

screen  = pygame.display.set_mode((400,600))
screen.fill(white)
pygame.display.set_caption("Racer")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rus.jpeg")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip(-5,0)
        if self.rect.left > 0:
            if pressed_keys[K_d]:
                self.rect.move_ip(5,0)
        if self.rect.left > 0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0,-5)
        if self.rect.left > 0:
            if pressed_keys[K_s]:
                self.rect.move_ip(0,5)
    

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("beer.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,screen_width-40),0) 
 
    def move(self):
        self.rect.move_ip(0,10)#чем выше значение правой части тем быстрее
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)



p1 = Player()
p2 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(p2)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(p2)

#creating new event
INC_SPEED = pygame.USEREVENT + 1
pygame.time,set_timer(INC_SPEED,1000)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    p1.update()
    p2.move()

    screen.fill(white)
    p1.draw(screen)
    p2.draw(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)
    