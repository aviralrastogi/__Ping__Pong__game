import pygame,sys,random
pygame.init()
playerptr=0
opponentptr=0
#popsound

popsound=pygame.mixer.Sound('ppsound1.wav')


def ballanimation():
    global ballspeedhorizontal,ballspeedvertical,playerscore,opponentscore,scoretime,playerptr,opponentptr

    ball.x += ballspeedhorizontal
    ball.y += ballspeedvertical
    if ball.top <= 0 or ball.bottom >= 600:
        ballspeedvertical *= -1
    if ball.left <= 0:

        playerscore=playerscore+1

        scoretime=pygame.time.get_ticks()

    if ball.right>=800:
        opponentscore=opponentscore+1

        scoretime=pygame.time.get_ticks()
    if playerscore<4:
        playerptr=15
        opponentptr=20
    elif playerscore<4 and playerscore<11:
        playerptr=10
        opponentptr=30
    else:
        playerptr=5
        opponentptr=35


    if ball.colliderect(player) and ballspeedhorizontal>0:
        popsound.play()
        #ACCURACY OF COLLISON OF BALL
        if abs(ball.right-player.left)<playerptr:
            ballspeedhorizontal *= -1
        elif abs(ball.bottom-player.top)<playerptr and ballspeedvertical>playerptr:
            ballspeedvertical*=-1
        elif abs(ball.top-player.bottom)<playerptr and ballspeedvertical>playerptr:
            ballspeedvertical*=-1

    if ball.colliderect(opponent) and ballspeedhorizontal<0:
        popsound.play()
        if abs(ball.left-opponent.right)<opponentptr:
            ballspeedhorizontal*=-1
        elif abs(ball.bottom-player.top)<opponentptr and ballspeedvertical>opponentptr:
            ballspeedvertical*=-1
        elif abs(ball.top-player.bottom)<opponentptr and ballspeedvertical>opponentptr:
            ballspeedvertical*=-1





def playermovement():
    global playerspeed,playerspeedmovement

    player.y += playerspeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= 600:
        player.bottom = 600
def opponentai():
    global opponentspeed
    if opponent.top<ball.y:
        opponent.top += opponentspeed+2
    if opponent.bottom>ball.y:
        opponent.bottom -= opponentspeed+2
    if opponent.top<=0:
        opponent.top=0
    if opponent.bottom>=600:
        opponent.bottom=600

d1=800/2-15
d2=400/2+80

def ballrestart():

    global ballspeedvertical,ballspeedhorizontal,currentime,scoretime,ratespeed
    currentime=pygame.time.get_ticks()
    ball.center = (800 / 2, 400 / 2)
    if currentime-scoretime<700:
        numberthree=gamefont.render("3",False,grey)
        screen.blit(numberthree,(d1,d2))
        if playerscore==4:
            levelup()
        elif playerscore==10:
            levelup()
    if 700<currentime-scoretime<1400:
        numberfour=gamefont.render("2",False,grey)
        screen.blit(numberfour,(d1,d2))
    if 1400<currentime-scoretime<2100:
        numberone=gamefont.render("1",False,grey)
        screen.blit(numberone,(d1,d2))

    if currentime-scoretime<2100:
        ballspeedhorizontal=0
        ballspeedvertical=0
    else:
        if playerscore<3:
            ratespeed=3
            scoretime=None
        elif playerscore>3 and playerscore<12:
            ratespeed=4.5
        ballspeedvertical = ratespeed * random.choice((1, -1))
        ballspeedhorizontal = ratespeed * random.choice((1, -1))
        scoretime=None
def levelup():
    global currentime,scoretime
    currentime=pygame.time.get_ticks()

    if currentime-scoretime<700:
        levelup1=gamefont.render("LEVEL UP",False,black)
        screen.blit(levelup1,(d1,d2))


#Text Variables

gamefont=pygame.font.Font("freesansbold.ttf",32)
gamefont1=pygame.font.Font("freesansbold.ttf",32)
gamefonta=pygame.font.Font("freesansbold.ttf",16)
gamefont1a=pygame.font.Font("freesansbold.ttf",16)
opponent2 ="OPPONENT"
player2="PLAYER"

#1
clock= pygame.time.Clock()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Ping pong ")
#Game Rectangles
ball=pygame.Rect(800/2-15,400/2+60,30,30)
player=pygame.Rect(800-20,600/2-50,10,140)
opponent=pygame.Rect(10,600/2-50,10,140)

#defining the pygamecolor
# Colour function
color1=pygame.Color('grey12')
black=(0,0,0)
grey=(200,200,200)
red=(255,0,0)
blue=(0,181,226)
white=(255,255,255)
lime=(0,255,0)
color3=pygame.Color(lime)
color2=pygame.Color(blue)

ballspeedhorizontal=7
ballspeedvertical=7
playerspeed=0
opponentspeed=10
opponentscore=0
playerscore=0
#Score timer
scoretime=None


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                playerspeed+=7
            if event.key==pygame.K_UP:
                playerspeed-=7
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                playerspeed-=7
            if event.key==pygame.K_UP:
                playerspeed+=7

    #calling the function for  the ball animation
    ballanimation()
    #giving the movement speed through the line
    playermovement()
    #giving the opponent ai()level1
    opponentai()

    #LEVELS DEFINED
    #visuals
    #2
    if playerscore<4:

        screen.fill(color1)
        pygame.draw.ellipse(screen, grey, ball)
        pygame.draw.aaline(screen, grey, (800 / 2, 0), (800 / 2, 600))
        pygame.draw.rect(screen, grey, player)
        pygame.draw.rect(screen, red, opponent)

    elif playerscore<10 :

        screen.fill(color2)
        pygame.draw.ellipse(screen, black, ball)
        pygame.draw.aaline(screen, black, (800 / 2, 0), (800 / 2, 600))
        pygame.draw.rect(screen, red, opponent)
        pygame.draw.rect(screen, grey, player)

    else:
        screen.fill(color3)
        pygame.draw.ellipse(screen, red, ball)
        pygame.draw.aaline(screen,black,(800/2,0),(800 / 2,600))
        pygame.draw.rect(screen,white,player)
        pygame.draw.rect(screen,black,opponent)

    if playerscore==20:

        playerscore=0
        opponentscore=0

    elif opponentscore==20:

        playerscore=0
        opponentscore=0

    #4
    playertext=gamefont.render(f"{playerscore}",True,white)
    screen.blit(playertext,(700,20))
    playertext1=gamefonta.render(f"{player2}",True,white)
    screen.blit(playertext1,(700,0))
    opponenttext=gamefont1.render(f"{opponentscore}",True,red)
    screen.blit(opponenttext,(10,30))
    opponenttext2=gamefont1a.render(f"{opponent2}",True,red)
    screen.blit(opponenttext2,(10,0))
    if scoretime:
        ballrestart()






    #updating the window
    pygame.display.flip()
    clock.tick(60)































