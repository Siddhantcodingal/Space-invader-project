import pygame
pygame.init()

screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invader Game")

WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)

bg=pygame.image.load("Space.jpeg")
rocket=pygame.image.load("take-off.png")
meteor=pygame.image.load("meteorite.png")

bg=pygame.transform.scale(bg,(screen_width,screen_height))
rocket=pygame.transform.scale(rocket,(60,60))
meteor=pygame.transform.scale(meteor,(35,35))

rocket_x=screen_width//2
rocket_y=screen_height-100

rocket_speed=7

meteor=[]
meteor_speed=5

lives=3
score=0

font=pygame.font.Font(None,40)

clock=pygame.time.Clock()

game_over=False

while not game_over:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           pygame.quit()
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT] and rocket_x>0:
        rocket_x=rocket_x-rocket_speed
    if key[pygame.K_RIGHT] and rocket_x<screen_width-60:
        rocket_x=rocket_x+rocket_speed
        pygame.display.update()
