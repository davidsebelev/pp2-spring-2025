#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.fill(WHITE)
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          DISPLAYSURF.fill(RED)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)


'''
#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
'''

#another adds 
'''
# Импорт необходимых модулей
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Настройка FPS (кадров в секунду)
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов (RGB)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Другие переменные для использования в программе
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # скорость движения врагов, монет и т.д.

# Создание игрового экрана с белым фоном
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Загрузка шрифта для отображения счётчика монет
font = pygame.font.SysFont("Verdana", 20)

# Класс для врага (противника)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Загрузка изображения врага
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        # Начальное положение врага: случайная позиция по горизонтали, верх экрана
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        # Движение врага вниз по экрану
        self.rect.move_ip(0, SPEED)
        # Если враг вышел за нижнюю границу, сбрасываем его в начало
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), 0)

# Класс для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Загрузка изображения игрока
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        # Начальное положение игрока
        self.rect.center = (160, 520)
        
    def move(self):
        # Получение состояния нажатых клавиш
        pressed_keys = pygame.key.get_pressed()
        # Комментарии для движения по вертикали (если понадобится)
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0, 5)
        
        # Движение влево, если игрок не у левого края
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        # Движение вправо, если игрок не у правого края
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Класс для монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Загрузка изображения монеты
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        # Начальное положение монеты: случайная позиция по горизонтали, вверху экрана
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
    
    def move(self):
        # Движение монеты вниз по экрану
        self.rect.move_ip(0, SPEED)
        # Если монета уходит за нижнюю границу экрана, удаляем её
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Создание экземпляров игрока и врага
P1 = Player()
E1 = Enemy()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Группа для монет
coins = pygame.sprite.Group()

# Счётчик собранных монет
coin_count = 0

# Добавляем новое пользовательское событие для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        # При срабатывании события увеличения скорости
        if event.type == INC_SPEED:
            SPEED += 2
        
        # Выход из игры при закрытии окна
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Заливка фона белым цветом
    DISPLAYSURF.fill(WHITE)

    # Рандомное появление монет: с вероятностью 3% каждый кадр
    if random.randint(1, 100) < 3:
        new_coin = Coin()
        coins.add(new_coin)

    # Движение и отрисовка всех спрайтов врагов и игрока
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # Отрисовка и движение монет
    for coin in coins:
        DISPLAYSURF.blit(coin.image, coin.rect)
        coin.move()

    # Проверка столкновения игрока с монетами
    coin_collisions = pygame.sprite.spritecollide(P1, coins, True)
    if coin_collisions:
        # Увеличиваем счётчик собранных монет
        coin_count += len(coin_collisions)

    # Отрисовка текста-счётчика монет в правом верхнем углу
    coin_text = font.render("Coins: " + str(coin_count), True, BLACK)
    coin_rect = coin_text.get_rect()
    coin_rect.topright = (SCREEN_WIDTH - 10, 10)
    DISPLAYSURF.blit(coin_text, coin_rect)

    # Если происходит столкновение игрока с врагом, завершаем игру
    if pygame.sprite.spritecollideany(P1, enemies):
        # Заливаем экран красным цветом
        DISPLAYSURF.fill(RED)
        pygame.display.update()
        # Удаляем все спрайты
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Обновление экрана
    pygame.display.update()
    # Ограничение FPS
    FramePerSec.tick(FPS)

'''