import pygame
from pygame import mixer
import random
from player import player
from map import MapF

mixer.init()
pygame.init()
pygame.display.set_caption("top down grid map game")
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

p1 = player()

A = 0
D = 1
W = 2
S = 3
SPACE = 4
F = 5
keys = [False, False, False, False, False, False]

worker = pygame.image.load('worker.png') #load your spritesheet
worker.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of

poster = pygame.image.load('poster.png') #load your spritesheet
poster.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of

fnaf = pygame.image.load('fnaf_poster.png')

#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False
button2 = False
button3 = False
button4 = False
button5 = False
button6 = False

movie1 = False

mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

ticket = False

ticker = 0

mapNum = 1

Counter = 0

Money = 150

Green = False
Yellow = False
Red = False

userText = ''

input_rect = pygame.Rect(225, 250, 100, 50)
Color_active = pygame.Color('lightskyblue3')
Color_passive = pygame.Color('grey15')
Color = Color_passive

active = False

def pls(counter):
    if mousePos[0] > 300 and mousePos[0] < 347 and mousePos[1] > 270 and mousePos[1] < 345 and mouseDown == True:
        counter += 1

#dialog = False
#dialog2 = False

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,2,2,2,2,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,2,2,2,2,2,2,2,2,4,4,2,2,2,2,2,2,2,2,2]]

map2 = [[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]]

map3 = [[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]]

map4 = [[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18],
       [18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18]]

text_font = pygame.font.SysFont("Sans", 30, bold = True)
text_font2 = pygame.font.SysFont("Sans", 24, bold = True)
text_font3 = pygame.font.SysFont("Sans", 22, bold = True)

my_font = pygame.font.SysFont('Comic Sans MS', 40)
text_surface = my_font.render('Money:', False, (0, 0, 0))
text2 = my_font.render(str(int(Money)), 1, (0, 0, 0))

pc = pygame.image.load('pc.png') #load your spritesheet
pc.set_colorkey((255, 0, 255))



def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

while 1 and p1.HP > 0: #GAME LOOP######################################################
    clock.tick(60) # fps
    ticker+=1
    #C.xpos += .1
    #input section--------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
            if event.key == pygame.K_f:
                keys[F] = True
             
            
            if event.key == pygame.K_a:
                keys[A] = True
                #RowNum = 0
            if event.key == pygame.K_d:
                keys[D] = True
                #RowNum = 3
            if event.key == pygame.K_w:
                keys[W] = True
                #RowNum = 1
            if event.key == pygame.K_s:
                keys[S] = True
                #Rowum = 2
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                keys[SPACE] = False
            if event.key == pygame.K_f:
                keys[F] = False

            if event.key == pygame.K_a:
                keys[A] = False
                #RowNum = 0
            if event.key == pygame.K_d:
                keys[D] = False
                #RowNum = 3
            if event.key == pygame.K_w:
                keys[W] = False
                #RowNum = 1
            if event.key == pygame.K_s:
                keys[S] = False
                #RowNum = 2
            
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True

            if mapNum == 2 and Counter <= 10:
                if mousePos[0] > 300 and mousePos[0] < 347 and mousePos[1] > 270 and mousePos[1] < 345 and mouseDown == True:
                    Counter += 1

            if mapNum == 3 and Counter >= 11:
                Counter += 1
            
            if mapNum == 4:
                if mousePos[0] > 150 and mousePos[0] < 300 and mousePos[1] > 850 and mousePos[1] <950:
                    Counter += 1

        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input (more needed for actual game)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1]
                else:
                    userText += event.unicode 
            #if event.key == pygame.K_q:
                #quitGame = True
        #if event.type == pygame.KEYUP:
            #if event.key == pygame.K_q:
                #quitGame = False
    #physics section-------------------------------------------------------

    if mapNum == 1:
        p1.move(keys, map)
    #elif mapNum == 2:
        #p1.move(keys , map2)
    #elif mapNum == 3:
        #p1.move(keys , map3)
    
        
    print(mousePos[0], mousePos[1])
       

     #ANIMATION-------------------------------------------------------------------
     
    if state == 1 and mousePos[0]>400 and mousePos[0]<670 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False
    
    if state == 1 and mousePos[0]>50 and mousePos[0]<320 and mousePos[1]>50 and mousePos[1]<200:
        button2 = True
    else:
        button2 = False
    
    if state == 1 and mousePos[0]>700 and mousePos[0]<970 and mousePos[1]>50 and mousePos[1]<200:
        button3 = True
    else:
        button3 = False
    
    if state == 1 and mousePos[0]>700 and mousePos[0]<970 and mousePos[1]>700 and mousePos[1]<950:
        button4 = True
    else:
        button4 = False
    
    if state == 1 and mousePos[0]>50 and mousePos[0]<320 and mousePos[1]>700 and mousePos[1]<950:
        button5 = True
    else:
        button5 = False

    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    if state == 1 and button2 == True and mouseDown == True:
        state = 2
    if state == 1 and button3 == True and mouseDown == True:
        state = 2
    if state == 1 and button4 == True and mouseDown == True:
        state = 2
    if state == 1 and button5 == True and mouseDown == True:
        state = 2
    
    if state == 2 and mapNum == 1 and mousePos[0]>50 and mousePos[0]<250 and mousePos[1]>150 and mousePos[1]<350 and mouseDown == True:
        mapNum = 2

    if mapNum == 2 and mousePos[0]>70 and mousePos[0]<170 and mousePos[1]>70 and mousePos[1]<100 and mouseDown == True:
        mapNum = 1

    if mapNum == 2 and mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>200 and mousePos[1]<300 and mouseDown == True:
        mapNum = 3
    if mapNum == 3 and mousePos[0]>70 and mousePos[0]<170 and mousePos[1]>70 and mousePos[1]<100 and mouseDown == True:
        mapNum = 2
    
    if mapNum == 2 and mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>425 and mousePos[1]<525 and mouseDown == True:
        mapNum = 4
    if mapNum == 4 and mousePos[0]>70 and mousePos[0]<170 and mousePos[1]>70 and mousePos[1]<100 and mouseDown == True:
        mapNum = 2
    
    if movie1 == False:
        if mapNum == 3 and mousePos[0]>200 and mousePos[0]<300 and mousePos[1]>200 and mousePos[1]<250 and mouseDown == True:
            Money -= 100
            button6 = True
            movie1 = True
    
    if userText.isdigit():
        int_data = int(userText)
        #if int_data > 2:
            #print("test")
    else:
        print("The string cannot be converted to an integer.")
    
    #if userText > 10:
        #print("test")
    
    #print(int_data)
    
    
    

    

   
    #render section-----------------------------------------------------------
    if state == 1:
        screen.fill((100,100,230))# Clear the screen pink

        #Location 1
        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 270, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (400, 400, 270, 150))
        
        draw_text("location 1:", text_font, (0,0,0), 400, 400)
        draw_text("Average commute: 16 mins", text_font2, (0,0,0), 400, 430)
        draw_text("Theaters in the area: 2", text_font2, (0,0,0), 400, 460)
        draw_text("People in need of jobs: 6", text_font2, (0,0,0), 400, 490)

        #Location 2
        if button2 == False:
            pygame.draw.rect(screen, (100, 230, 100), (50, 50, 270, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (50, 50, 270, 150))
        
        draw_text("location 2:", text_font, (0,0,0), 50, 50,)
        draw_text("Average commute: 26 mins", text_font2, (0,0,0), 50, 80,)
        draw_text("Theaters in the area: 0", text_font2, (0,0,0), 50, 110,)
        draw_text("People in need of jobs: 4", text_font2, (0,0,0), 50, 140,)

        #Location 3
        if button3 == False:
            pygame.draw.rect(screen, (100, 230, 100), (700, 50, 270, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (700, 50, 270, 150))
        
        draw_text("location 3:", text_font, (0,0,0), 700, 50,)
        draw_text("Average commute: 12 mins", text_font2, (0,0,0), 700, 80,)
        draw_text("Theaters in the area: 1", text_font2, (0,0,0), 700, 110,)
        draw_text("People in need of jobs: 13", text_font2, (0,0,0), 700, 140,)

        #Location 4
        if button4 == False:
            pygame.draw.rect(screen, (100, 230, 100), (700, 800, 270, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (700, 800, 270, 150))
        
        draw_text("location 4:", text_font, (0,0,0), 700, 800,)
        draw_text("Average commute: 5 mins", text_font2, (0,0,0), 700, 830,)
        draw_text("Theaters in the area: 3", text_font2, (0,0,0), 700, 860,)
        draw_text("People in need of jobs: 7", text_font2, (0,0,0), 700, 890,)

        #Location 5
        if button5 == False:
            pygame.draw.rect(screen, (100, 230, 100), (50, 800, 270, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (50, 800, 270, 150))
        
        draw_text("location 5:", text_font, (0,0,0), 50, 800,)
        draw_text("Average commute: 17 mins", text_font2, (0,0,0), 50, 830,)
        draw_text("Theaters in the area: 2 ", text_font2, (0,0,0), 50, 860,)
        draw_text("People in need of jobs: 17", text_font2, (0,0,0), 50, 890,)
    
        
    if state == 2:

        if mapNum == 1:
            MapF(screen, map)
            
            screen.blit(text_surface, (0,-10))
            text2 = my_font.render(str(int(Money)), 1, (0, 0, 0))
            screen.blit(text2, (150, -10))

            screen.blit(pc, (50, 150, 200, 200))

            if movie1 == True:
                draw_text("FNAF", text_font, (0,0,0), 670, 20,)
                screen.blit(fnaf, (750, 0, 100, 100))


            #for i in range(1000, 200):


            p1.draw(screen)

        
        #if mapNum == 2:
            #MapF(screen, map2)

            #p1.draw(screen)

            #screen.blit(corn, (500, 500, 50, 100 ))
            
           

        if mapNum == 2:
            MapF(screen, map2)

            pygame.draw.rect(screen, (200, 20, 20), (70, 70, 100, 50))
            draw_text("X", text_font, (0,0,0), 110, 75,)

            pygame.draw.rect(screen, (50, 200, 50), (300, 200, 200, 100))
            draw_text("Movies", text_font, (0,0,0), 350, 225,)

            pygame.draw.rect(screen, (50, 200, 50), (300, 400, 200, 100))
            draw_text("Prices", text_font, (0,0,0), 350, 425,)
            #p1.draw(screen)
        
        if mapNum == 3:
            MapF(screen, map3)
            pygame.draw.rect(screen, (200, 20, 20), (70, 70, 100, 50))
            draw_text("X", text_font, (0,0,0), 110, 75,)

            pygame.draw.rect(screen, (255, 215, 0), (200, 50, 100, 50) )
            draw_text("FNAF", text_font, (0,0,0), 225, 60,)
            screen.blit(poster, (200, 100, 100, 100))
            pygame.draw.rect(screen, (25, 215, 25), (200, 200, 100, 50) )
            if button6 == False:
                draw_text("$100", text_font, (0,0,0), 225, 215,)
            else:
                draw_text("bought", text_font, (0,0,0), 215, 215,)
        
        if mapNum == 4:
            MapF(screen, map4)

            if active == True:
                Color = Color_active
            else:
                Color = Color_passive

            pygame.draw.rect(screen, (200, 20, 20), (70, 70, 100, 50))
            draw_text("X", text_font, (0,0,0), 110, 75,)
            pygame.draw.rect(screen, (186, 85, 211), (200, 200, 250, 150) )
            draw_text("FNAF ticket price:", text_font, (0,0,0), 225, 200,)
            draw_text("Average price: $11", text_font2, (0,0,0), 225, 300,)

            pygame.draw.rect(screen,Color,input_rect, 2)
            text_surface = text_font.render(userText, True, (255, 255, 255))
            screen.blit(text_surface, (input_rect.x +5, input_rect.y + 5))

            input_rect.w = max(100,text_surface.get_width() + 10)


        

    pygame.display.flip()#this actually puts the pixel on the screen


#end game loop#############################################################################
pygame.quit()