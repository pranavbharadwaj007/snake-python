import pygame
pygame.init()
screen_width=1200
screen_height=600
#color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
redpink=(255,25,55)


#display
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("pranav game")
pygame.display.update()
exit_game=False
game_over=False
s_x=45
s_y=55
s_size=10

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


    gameWindow.fill(redpink)
    pygame.draw.rect(gameWindow,black,[s_x,s_y,s_size,s_size])
    pygame.display.update()

pygame.quit()
quit()
