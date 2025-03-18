import pygame
import sys
from datetime import datetime

clock = pygame.time.Clock()

pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True


#back_mickey_img = pygame.image.load("m.jpeg").convert_alpha()
#back_mickey_img = pygame.transform.scale(back_mickey_img,(800,800))


hand_min = pygame.image.load("f.png").convert_alpha()
hand_sec = pygame.image.load("s.png").convert_alpha()

def blit_rotate_center(surf, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    surf.blit(rotated_image, new_rect.topleft)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    now = datetime.now()
    sec = now.second
    min = now.minute


    sec_angle = 90 - sec*6
    min_angle = 90 - (min + sec / 60)*6

    screen.fill((255, 255, 255))

    center_x, center_y = WIDTH // 2, HEIGHT // 2

    minute_hand_pos = (center_x - hand_min.get_width() // 2,
                       center_y - hand_min.get_height() // 2)
    second_hand_pos = (center_x - hand_sec.get_width() // 2,
                       center_y - hand_sec.get_height() // 2)

    blit_rotate_center(screen, hand_min, minute_hand_pos, min_angle)
    blit_rotate_center(screen, hand_sec, second_hand_pos, sec_angle)
    #screen.blit(back_mickey_img,(0,0))

    pygame.display.flip()
    clock.tick(30)