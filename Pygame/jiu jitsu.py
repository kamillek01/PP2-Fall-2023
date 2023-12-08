import pygame
import random
pygame.init()

winWidth, winHeight = 859, 480
reset = False
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Jiu Jitsu")

walkRight = [pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A1.png"), (150, 150)),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A2.png"),(150, 150)),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A3.png"), (150,150 )),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A4.png"), (150, 150)),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A1.png"), (150, 150)),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A2.png"), (150, 150)),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A3.png"), (150, 150)),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A4.png"), (150, 150)),
             pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A1.png"), (150, 150))]


walkLeft =[pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A10.png"), (150, 150)),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A20.png"),(150, 150)),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A30.png"), (150,150 )),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A40.png"), (150, 150)),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A10.png"), (150, 150)),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A20.png"), (150, 150)),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A30.png"), (150, 150)),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A40.png"), (150, 150)),
           pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\A10.png"), (150, 150))]

original_bg = pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\kbtu_bg.jpg")
bg = pygame.transform.scale(original_bg, (winWidth, winHeight))

bulletSound = pygame.mixer.Sound(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\music\music_bullet.wav")
hitSound = pygame.mixer.Sound(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\music\music_hit.wav")
music = pygame.mixer_music.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\music\music.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
score = 0

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height  
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.killed = 0
        self.life = 3 

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 30, self.y + 11, 29, 52)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 330
        self.walkCount = 0
        self.life -= 1  
        student.x = random.randint(0 , winWidth)
        pygame.time.delay(1000)


class Projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

        if facing == 1:
            self.x = x + 64  
        else:
            self.x = x - self.radius

        self.y = y + 32  


    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkRight = [pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B1.png"), (170, 170)),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B2.png"),(150, 150)),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B3.png"), (150,150 )),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B4.png"), (150, 150)),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B1.png"), (170, 170)),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B2.png"), (150, 150)),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B3.png"), (150, 150)),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B4.png"), (150, 150)),
                 pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B1.png"), (170, 170))]

    walkLeft =[pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B10.png"), (150, 150)),
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B20.png"),(150, 150)),
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B30.png"), (150,150 )),
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B40.png"), (150, 150)),
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B10.png"), (150, 150)),
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B20.png"), (150, 150)), 
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B30.png"), (150, 150)),
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B40.png"), (150, 150)),
               pygame.transform.scale(pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\B10.png"), (150, 150))]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.end = end
        self.path = [0, self.end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()

        if self.visible:

            if self.walkCount + 1 >= 25:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 60, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 60 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 47, self.y + 2, 31, 57)

        else:
            arnur.killed >= 3
            purple_belt_image = pygame.image.load(r"C:\Users\Kamila\OneDrive - Autonomous Educational Organization Nazarbayev Intellectual Schools\Рабочий стол\PP2\Pygame\images\Belt.PNG")
            scaled_width = purple_belt_image.get_width() // 2
            scaled_height = purple_belt_image.get_height() // 2
            purple_belt_image = pygame.transform.scale(purple_belt_image, (scaled_width, scaled_height))
            win.blit(purple_belt_image, (winWidth/2 - purple_belt_image.get_width()/2+50, winHeight/2 - purple_belt_image.get_height()/2-15))
            pygame.display.update()
            pygame.time.delay(5000)
            run=False
             
          
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1] - self.width:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        global score

        score += 1
        self.health -= 1

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render(f"Score: {score}", 1, (0,0,0))
    win.blit(text, (690, 10))
    life_text = font.render(f"Life: {arnur.life}", 1, (255, 0, 0)) 
    win.blit(life_text, (10, 10))
    arnur.draw(win)
    student.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

font = pygame.font.SysFont("comicsans", 30, True)
arnur = Player(random.randint(0, winWidth), 330, 64, 64)
arnur.vel = 8  
student = enemy(random.randint(0, winWidth), 330, 64, 64, winWidth - 64)
shootLoop = 0
bullets = []
run = True
JUMP_HEIGHT_MODIFIER = 1.5
game_over = False
game_over_time = 0

def game_over_screen():
    font_game_over = pygame.font.SysFont("comicsans", 60)
    text_game_over = font_game_over.render("Game Over", 1, (255, 255, 255)) 
    text_rect = text_game_over.get_rect()
    text_rect.center = (winWidth // 2, winHeight // 2) 
    pygame.draw.rect(win, (255, 0, 0), text_rect)  
    win.blit(text_game_over, text_rect)  
    pygame.display.update()  

    button_font = pygame.font.SysFont("comicsans", 30)
    button_text = button_font.render("Restart", 1, (255, 255, 255))
    button_width, button_height = button_text.get_width(), button_text.get_height()
    button_x, button_y = winWidth/2 - button_width/2, winHeight/2 + text_game_over.get_height()
    pygame.draw.rect(win, (0, 0, 255), (button_x - 10, button_y - 10, button_width + 20, button_height + 20))
    win.blit(button_text, (button_x, button_y))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    return True 

        pygame.time.Clock().tick(15)

    return False

run = True

while run:
    clock.tick(27)
    if arnur.hitbox[1] < student.hitbox[1] + student.hitbox[3] and arnur.hitbox[1] + arnur.hitbox[3] > student.hitbox[1]:
        if arnur.hitbox[0] + arnur.hitbox[2] > student.hitbox[0] and arnur.hitbox[0] < student.hitbox[0] + student.hitbox[2]:
            arnur.hit()
           
    if arnur.life <= 0:
        if game_over_screen():
            arnur = Player(random.randint(0, winWidth), 330, 64, 64)
            arnur.vel = 8  
            student = enemy(random.randint(0, winWidth), 330, 64, 64, winWidth - 64)
            shootLoop = 0
            bullets = []
            score = 0
            run = True
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    run = True

    win.fill((0, 0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < student.hitbox[1] + student.hitbox[3] and bullet.y + bullet.radius > student.hitbox[1]:
            if bullet.x + bullet.radius > student.hitbox[0] and bullet.x - bullet.radius < student.hitbox[0] + student.hitbox[2]:
                if student.health > 0:
                    hitSound.play()
                    student.hit()
                    bullets.pop(bullets.index(bullet))
                else: student.visible = False

        if bullet.x < winWidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:

        if arnur.left: facing = -1
        else: facing = 1

        if len(bullets) < 1:
            bulletSound.play()

            bullets.append(Projectile(round(arnur.x + arnur.width // 2), round(arnur.y + arnur.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and arnur.x > arnur.vel:
        arnur.x -= arnur.vel
        arnur.left = True
        arnur.right = False
        arnur.standing = False
    elif keys[pygame.K_RIGHT] and arnur.x < winWidth - arnur.width - arnur.vel and arnur.x < winWidth - 150:
        arnur.x += arnur.vel
        arnur.right = True
        arnur.left = False
        arnur.standing = False
    else:
        arnur.standing = True
        arnur.walkCount = 0
    

    if not(arnur.isJump):
        if keys[pygame.K_UP]:
            arnur.isJump = True
            arnur.right = False
            arnur.left = False
            arnur.walkCount = 0
    else:
        if arnur.jumpCount >= -10:
            neg = 1
            if arnur.jumpCount < 0:
                neg = -1
            arnur.y -= (arnur.jumpCount ** 2) * 0.5 * neg * JUMP_HEIGHT_MODIFIER
            arnur.jumpCount -= 1
        else:
            arnur.isJump = False
            arnur.jumpCount = 10

    redrawGameWindow()

pygame.quit()