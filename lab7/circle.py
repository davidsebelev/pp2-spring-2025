import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True

x = 250
y = 250
clock = pygame.time.Clock()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:y -=5
    if pressed[pygame.K_s]: y+=5
    if pressed[pygame.K_a]:x -=5
    if pressed[pygame.K_d]:x +=5


    x = max(25, min(x, 500-25))
    y = max(25, min(y, 500-25))



    screen.fill((255,255,255))

    pygame.draw.circle(screen,(255,0,0),(x,y),25)

    pygame.display.flip()
    clock.tick(30)
