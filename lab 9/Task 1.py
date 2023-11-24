import pygame
import sys
import datetime

pygame.init()
width, height = 900, 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mickey Mouse Clock')

right_hand = pygame.image.load('right-hand.png').convert_alpha()
left_hand = pygame.image.load('left-hand.png').convert_alpha()
clock_face = pygame.image.load('main-clock.png').convert_alpha()

center = (width // 2, height // 2)
radius = 150

def rotate_hand(image, angle):
    return pygame.transform.rotate(image, -angle)

running = True
clock = pygame.time.Clock()

while running:
    window.fill((255, 255, 255)) 

    current_time = datetime.datetime.now()
    current_minute = current_time.minute
    current_second = current_time.second

    min_angle = (360 * current_minute) // 60
    sec_angle = (360 * current_second) // 60

    rot_right_hand = rotate_hand(right_hand, min_angle)
    rot_left_hand = rotate_hand(left_hand, sec_angle)

    righthand_positive = (center[0] - rot_right_hand.get_width() // 2,
                      center[1] - rot_right_hand.get_height() // 2)
    lefthand_positive = (center[0] - rot_left_hand.get_width() // 2,
                     center[1] - rot_left_hand.get_height() // 2)

    window.blit(clock_face, (width // 2 - clock_face.get_width() // 2, height // 2 - clock_face.get_height() // 2))
    window.blit(rot_right_hand, righthand_positive)
    window.blit(rot_left_hand, lefthand_positive)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
