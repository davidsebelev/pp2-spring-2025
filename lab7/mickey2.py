import pygame
import sys
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()


clock_face = pygame.image.load("m.jpeg").convert_alpha()
clock_face = pygame.transform.scale(clock_face, (400, 400))


hand_min = pygame.image.load("f.png").convert_alpha()
hand_sec = pygame.image.load("s.png").convert_alpha()



hand_min = pygame.transform.scale(hand_min, (120, 120))
hand_sec = pygame.transform.scale(hand_sec, (100, 100))



pivot_min = (hand_min.get_width() // 2, int(hand_min.get_height() * 0.9))
pivot_sec = (hand_sec.get_width() // 2, int(hand_sec.get_height() * 0.9))

def blit_rotate(surf, image, pos, pivot, angle):

   
    image_rect = image.get_rect()

    pivot_offset = pygame.math.Vector2(pivot[0] - image_rect.width / 2,
                                       pivot[1] - image_rect.height / 2)

    rotated_offset = pivot_offset.rotate(-angle)
    

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=(pos[0] - rotated_offset.x,
                                                  pos[1] - rotated_offset.y))
    surf.blit(rotated_image, rotated_rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    now = datetime.now()
    sec = now.second
    minute = now.minute

    sec_angle = 90 - sec * 6
    min_angle = 90 - (minute + sec / 60) * 6


    screen.fill((255, 255, 255))
    

    center_x, center_y = WIDTH // 2, HEIGHT // 2


    face_rect = clock_face.get_rect(center=(center_x, center_y))
    screen.blit(clock_face, face_rect.topleft)


    blit_rotate(screen, hand_min, (center_x, center_y), pivot_min, min_angle)
    blit_rotate(screen, hand_sec, (center_x, center_y), pivot_sec, sec_angle)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
