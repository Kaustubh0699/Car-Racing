
import pygame
import time
import random
#-------------------------------------------------------------------------INITIALIZING PYGAME AND PYGAME DISPLAY WINDOW------------------------------------------------
high_score=[0]
pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("car_running.wav")
main_menu_sound = pygame.mixer.Sound("main_menu.wav")
countdown_sound = pygame.mixer.Sound("countdown.wav")


display_width=600
display_height=600

white=(255,255,255)
black=(0,0,0)
grey=(105,105,105)
b_red = (255,0,0)
red = (200,0,0)
b_green = (0,255,0)
green = (0,200,0)

car_width=130

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Racer")
clock=pygame.time.Clock()



#-------------------------------------------------------------------------BLIT OR PLACE CAR IMAGE ON THE SCREEN--------------------------------------------------------
carImg=pygame.image.load('car.png')
carIcon=pygame.image.load('car_icon.png')
pygame.display.set_icon(carIcon)
objImg = pygame.image.load('obj.png')
start_line = pygame.image.load('start_line.png')
road_divider = pygame.image.load('road_divider.png')
boundary_pic = pygame.image.load('boundary.png')

#-------------------------------------------------------------------------BOUNDARY FUNCTION----------------------------------------------------------------------------
def boundary(b_x,b_y):
    gameDisplay.blit(boundary_pic,(b_x,b_y))
#-------------------------------------------------------------------------ROAD DIVIDER---------------------------------------------------------------------------------

def display_road_divider(divider_x,divider_y):
    gameDisplay.blit(road_divider,(divider_x,divider_y))
    
#-------------------------------------------------------------------------START LINE FUNCTION--------------------------------------------------------------------------

def display_start(startline_y):
    gameDisplay.blit(start_line,(0,startline_y))
    
#-------------------------------------------------------------------------SCORING--------------------------------------------------------------------------------------

def score_record(score):
    font_style = pygame.font.SysFont("Comic Sans MS",27)
    text = font_style.render("Score: "+str(score),True,white)
    gameDisplay.blit(text,(0,0))

#-------------------------------------------------------------------------CREATING OTHER OBJECTS-----------------------------------------------------------------------

def objects(obj_x,obj_y):
    gameDisplay.blit(objImg,(obj_x,obj_y))


#-------------------------------------------------------------------------FUNCTION FOR CONTINOUSLY REFRESHING IMAGE POSITION TO GIVE EFFECT OF MOVEMENT----------------
def carload(x,y):
    gameDisplay.blit(carImg,(x,y))

#------------------------------------------------------------------------TO DISPLAY CRASH MESSAGE----------------------------------------------------------------------

def text_display(text,font_style):
    textSurf = font_style.render(text,True,b_red)
    return textSurf,textSurf.get_rect()

    
def message_display(text):
    font_style = pygame.font.SysFont("Comic Sans MS",72)
    textSurf,textRect = text_display(text,font_style)
    textRect = (10,(display_height/3))
    gameDisplay.blit(textSurf,textRect)

    pygame.display.flip()

    time.sleep(2)
    
def countdown_display(text):
    font_style = pygame.font.SysFont("Comic Sans MS",72)
    textSurf,textRect = text_display(text,font_style)
    textRect = (260,(display_height/3))
    gameDisplay.blit(textSurf,textRect)

    pygame.display.flip()

    time.sleep(1)
#------------------------------------------------------------------------WHAT TO DO AFTER CRASHING---------------------------------------------------------------------

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    global score
    global high_score
    message_display("YOU CRASHED")
    gameDisplay.fill(grey)
    message_display("YOUR SCORE: "+str(score))
    gameDisplay.fill(black)
    high_score.append(score)
    start(max(high_score))


#------------------------------------------------------------------------START COUNTDOWN-------------------------------------------------------------------------------

def start_countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        message_display("STARTING IN...")
        gameDisplay.fill(black)
        pygame.mixer.Sound.play(countdown_sound)
        countdown_display("5")
        gameDisplay.fill(black)
        countdown_display("4")
        gameDisplay.fill(black)
        countdown_display("3")
        gameDisplay.fill(black)
        countdown_display("2")
        gameDisplay.fill(black)
        countdown_display("1")
        gameDisplay.fill(black)
        message_display("      LET'S GO")
        mainGameloop()

#------------------------------------------------------------------------PAUSE MENU-----------------------------------------------------------------------------------

def pause_menu():
    pygame.mixer.music.pause()
    intro = False
    while not intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        font_style = pygame.font.SysFont("Comic Sans MS",72)
        textSurf,textRect = text_display("PAUSE",font_style)
        textRect = (80,(display_height/3))
        gameDisplay.blit(textSurf,textRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if((150+100 > mouse[0] >100) and (450+50 > mouse[1]>450)):
            pygame.draw.rect(gameDisplay , b_green ,(150,450,100,50))
            if(click[0] == 1):
                pygame.mixer.music.unpause()
                return
        else:
            pygame.draw.rect(gameDisplay , green ,(150,450,100,50))
        button_text("RESUME",150,450)
        pygame.display.update()
        buttons("QUIT?",350,450,100,50,red,b_red,quitgame)
        pygame.display.update()
    
#------------------------------------------------------------------------BUTTON TEXT----------------------------------------------------------------------------------
def button_text_display(text,font_style):
    textSurf = font_style.render(text,True,black)
    return textSurf,textSurf.get_rect()

def button_text(text,x,y):
    font_style = pygame.font.SysFont("Comic Sans MS",20)
    textSurf,textRect = button_text_display(text,font_style)
    textRect.center = (x+(100/2),y+(50/2))
    gameDisplay.blit(textSurf,textRect)

    pygame.display.update()
#------------------------------------------------------------------------QUIT GAME FUNCTION----------------------------------------------------------------------------
def quitgame():
    pygame.quit()
    quit()
#-------------------------------------------------------------------------BUTTON FUNCTION------------------------------------------------------------------------------

def buttons(msg,x,y,w,h,color,h_color,func):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if((x+w > mouse[0] >x) and (y+h > mouse[1]>y)):
        pygame.draw.rect(gameDisplay , h_color ,(x,y,w,h))
        if(click[0] == 1):
            func()
            
    else:
        pygame.draw.rect(gameDisplay , color ,(x,y,w,h))
    button_text(msg,x,y)
    pygame.display.update()


#------------------------------------------------------------------------START MENU------------------------------------------------------------------------------------
def start(max_score):
    pygame.mixer.Sound.play(main_menu_sound)
    intro = False
    while not intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        font_style = pygame.font.SysFont("Comic Sans MS",72)
        textSurf,textRect = text_display("CAR RACING",font_style)
        textRect = (80,(display_height/3))
        gameDisplay.blit(textSurf,textRect)

        h_s = "High Score: " + str(max_score)
        
        font_style2 = pygame.font.SysFont("Comic Sans MS",42)
        textSurf2,textRect2 = text_display(h_s,font_style2)
        textRect = (80,(display_height/2))
        gameDisplay.blit(textSurf2,textRect2)
#-----------------------------------------------------------------------BUTTONS----------------------------------------------------------------------------------------

        buttons("GO!",150,450,100,50,green,b_green,start_countdown)
        buttons("QUIT?",350,450,100,50,red,b_red,quitgame)
        pygame.display.update()
#------------------------------------------------------------------------MAIN GAME LOOP--------------------------------------------------------------------------------
def mainGameloop():
    pygame.mixer.Sound.stop(main_menu_sound)
    pygame.mixer.music.play(-1)
    global score
    x=display_width*0.40
    y=display_height*.75
    x_move = 0
#------------------------------------------------------------------------SETTING DIMENSIONS FOR THE BLOCK--------------------------------------------------------------
    object_width = 112
    object_x = 63
    object_y = -300
    object_speed = 5
    object_height = 146
    score=0

#-------------------------------------------------------------------------START LINE-----------------------------------------------------------------------------------
    startline_y = display_width/3
#-------------------------------------------------------------------------ROAD DIVIDER---------------------------------------------------------------------------------
    divider_width = 52
    divider_x = -100
    divider_y = -100
    divider_height = 175
    divider_speed = 7

#--------------------------------------------------------------------------BOUNDARY_LEFT------------------------------------------------------------------------------------
    b_width = 61
    b_x_left = -361
    b_y_left = -40
    b_height = 600
#---------------------------------------------------------------------------BOUNDARY_RIGHT-----------------------------------------------------------------------------
    b_x_right = 180
    b_y_right = -40
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    endGame=False
    
    while not endGame:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_move=-10
                if event.key==pygame.K_RIGHT:
                    x_move=10
                if event.key == pygame.K_ESCAPE:
                    pause_menu()
            if event.type==pygame.KEYUP:
                if (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                    x_move=0
        x = x + x_move
        gameDisplay.fill(grey)

        boundary(b_x_left,b_y_left)
        b_y_left += divider_speed
        boundary(b_x_right,b_y_right)
        b_y_right += divider_speed

        
        display_road_divider(divider_x,divider_y)
        divider_y += divider_speed
        
        display_start(startline_y)
        startline_y += divider_speed
        
        objects(object_x, object_y)
        object_y += object_speed

        carload(x,y)
        score_record(score)
        if(x>display_width - object_width or x<0):
            crash()
        if(divider_y > display_height):
            divider_y = 0 - divider_height/2

        if(b_y_left > display_height/15):
            b_y_left = -100
            b_y_right = -100 
            b_x = 0
        
        if(object_y > display_height):
            object_y = 0 - object_height
            object_x = random.randrange(0,display_width)
            score+=1
            if(score>1 and score % 5 ==0):
                object_speed += 2 
                divider_speed += 2
        
#--------------------------------------------------------------------------------FOR COLLISION-------------------------------------------------------------------------
        if(y < object_y + object_height):
            if((x >= object_x and x <= object_x + object_width) or (x + car_width >= object_x and x + car_width <= object_x + object_width)):
                crash()
            
        pygame.display.flip()
        clock.tick(60)

start(max(high_score))
pygame.quit()
quit()
