import pygame
import random
pygame.init()

screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invader Game")

WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)

bg=pygame.image.load("Space.jpeg")
rocket=pygame.image.load("take-off.png")
meteor=pygame.image.load("meteorite.png")

bg=pygame.transform.scale(bg,(screen_width,screen_height))
rocket_img=pygame.transform.scale(rocket,(60,60))
meteor_img=pygame.transform.scale(meteor,(35,35))

rocket_x=screen_width//2
rocket_y=screen_height-100

rocket_speed=7

metoerss=[]
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
           game_over=True
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT] and rocket_x>0:
        rocket_x=rocket_x-rocket_speed
    if key[pygame.K_RIGHT] and rocket_x<screen_width-60:
        rocket_x=rocket_x+rocket_speed
    if random.randint(0,40)==0:
        meteor_x=random.randint(0,screen_width-35)
        meteor_y=0
        metoerss.append([meteor_x,meteor_y])
    for meteor in metoerss:
        meteor[1]=meteor[1]+meteor_speed
        if meteor[1]>screen_height:
            metoerss.remove(meteor)
            score+=1
        elif(meteor[0]<rocket_x+60 and meteor[0]+35>rocket_x and meteor[1]<rocket_y+60 and meteor[1]+35>rocket_y):
            
            metoerss.remove(meteor)
            lives-=1
            if lives<=0:
                game_over=True
    for meteor in metoerss:
        screen.blit(meteor_img,(meteor[0],meteor[1]))
    screen.blit(rocket_img,(rocket_x,rocket_y))
    lives_text=font.render(f"Lives Left:{lives}",True,WHITE)
    screen.blit(lives_text,(10,50))
    score_text=font.render(f"Score:{score}",True,WHITE)
    screen.blit(score_text,(10,10))

    pygame.display.update()

    clock.tick(60)
screen.fill(BLACK)
game_over_text=font.render("GAME OVER",True,RED)
screen.blit(game_over_text,(300,250))
final_score_text=font.render(f"Final Score:{score}",True,BLUE)
screen.blit(final_score_text,(280,320))
pygame.display.update()
pygame.time.delay(5000)
pygame.quit()
