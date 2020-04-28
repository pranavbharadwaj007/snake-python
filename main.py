import pygame
import random



pygame.mixer.init()
#pygame.mixer.music.load('outsidegame.mp3')
#pygame.mixer.music.play()
pygame.init()

screen_width=1200
screen_height=600
#color
white=(255,255,255)
blue=(0,0,255)
black=(0,0,0)
redpink=(200,50,155)
green=(0,255,0)
red=(255,0,0)

#display
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("pranav game")
pygame.display.update()

fps=30
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

bgimg=pygame.image.load("insidegame.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
bgimg2=pygame.image.load("insidegame.jpg")
bgimg2=pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()
def plot_snake(gameWindow,color,snk_list,s_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,s_size,s_size])


def screen_text(text ,color,x,y):

    scree_text=font.render(text,True,color)
    gameWindow.blit(scree_text,[x,y])
#welcom screen
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimg,(0,0))
        screen_text("welcom to pranav's snake game",redpink,200,210)
        screen_text("press space bar to play!!",redpink,200,250)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        pygame.mixer.music.load('outsidegame.mp3')
                        pygame.mixer.music.play()



                        gameloop()
        pygame.display.update()
        clock.tick(30)
#game display loop
def gameloop():
    exit_game=False
    game_over=False
    food_x=random.randint(25,screen_width/2)
    food_y=random.randint(24,screen_height/2)
    s_x=45
    s_y=55
    s_size=15
    velocity_x=0
    velocity_y=0
    init_velocity=5
    score=0

    snk_list=[]
    snk_lent=1
    with open("highscore.txt","r") as f:
        hiscscore=f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(hiscscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimg2,(0,0))
            screen_text("!!game over!! press enter to continue",red,200,250)
            screen_text("your score="+str(score),red,200,210)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                        "s_x+=10"
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                        "s_x-=10"
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                        "s_y-=10"
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                        "s_y+=10"


            s_x=s_x+velocity_x
            s_y=s_y+velocity_y





            if(abs(s_x-food_x)<11 and abs(s_y-food_y)<11):
                score+=10
                #print("score=",score)

                food_x=random.randint(25,screen_width/2)
                food_y=random.randint(24,screen_height/2)
                snk_lent+=5
                if score > int(hiscscore):
                    hiscscore=score



            gameWindow.fill(redpink)
            gameWindow.blit(bgimg2,(0,0))
            screen_text("score="+str(score)+"|| high score="+str(hiscscore),blue,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,s_size,s_size])

            head=[]
            head.append(s_x)
            head.append(s_y)
            snk_list.append(head)
            if(len(snk_list)>snk_lent):
                del snk_list[0]


            if head in snk_list[:-1:]:
                game_over=True

            if s_x<0 or s_x>screen_width or s_y<0 or s_y>screen_height:
                game_over=True
                #print("game over!")
            plot_snake(gameWindow,black,snk_list,s_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()


#function to increasee length

#function for printing in score



# Creating a game loop
