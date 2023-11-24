import pygame
import sys
pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

radius = 25
color = (255, 0, 0)  
ball_x, ball_y = width // 2, height // 2  

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - 20 >= radius:
        ball_y -= 20
    if keys[pygame.K_DOWN] and ball_y + 20 <= height - radius:
        ball_y += 20
    if keys[pygame.K_LEFT] and ball_x - 20 >= radius:
        ball_x -= 20
    if keys[pygame.K_RIGHT] and ball_x + 20 <= width - radius:
        ball_x += 20

    screen.fill((255, 255, 255)) 

    pygame.draw.circle(screen, color, (ball_x, ball_y), radius)

    pygame.display.flip()

    clock.tick(60)