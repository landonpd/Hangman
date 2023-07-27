#landon Dixon hangman game 
import random
import pygame
from pygame import *
from math import *
WHITE= (255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
YELLOW=(239, 225, 28)
init()
size = (900, 700)
screen = display.set_mode(size, RESIZABLE)
display.set_caption("Hang Man!")
clock =time.Clock()
words=["hello", "slug", "eggplant", "sharp", "universe","sleepy","saddle","learning","bomb","illuminate","worship","fate","skillful","decorate","cloudy",\
       "vast","trousers","skid","jittery","wine","vagabond","quack","earthquake","hospital","vomit","pollution","savvy","creepy","implant","mindless","brick","governmnet",\
       "drum","economic","bewildered","enchanting","cheesecake","sprout","terminate","clever","painstaking","giraffe","futuristic","hydrant","cactus","carpenter","sentence",\
       "discreet","mash","number","fan","check","hideous","escape","cagey","decay","infest","cumbersome"]
#list of words for the game
def draw_text(msg, font, size,color):
    text_font= pygame.font.SysFont(font, size, True, False)
    text = text_font.render(msg,True,color)
    text_dim=[]
    text_dim.append(text)
    text_dim.append(text.get_rect().width)
    text_dim.append(text.get_rect().height)
    return text_dim
def button(msg,x,y,w,h,col,font_col, action=None, arg1=None, arg2=None,arg3=None,arg4=None):
    pos_mouse = mouse.get_pos()
    click = mouse.get_pressed()
    text=draw_text(msg, 'Calibri', 20,font_col)
    txt_w=text[1]
    txt_h=text[2]
    pygame.draw.rect(screen, col,(x,y,w,h))
    if  x+w > pos_mouse[0] > x and y+h > pos_mouse[1] > y:
        if click[0]==1 and action!=None:
           action(arg1, arg2 ,arg3, arg4)
    screen.blit(text[0], [(w-txt_w)/2+x,(h-txt_h)/2+y])
def quitgame(a=None, r=None, g=None, s=None):
    pygame.quit()
    quit()

def draw_dashes(num_let):   #check even or odd then subtract *num_let
    if num_let%2==0:
        x=455-(60*(num_let/2))
        x2=x+50
        
    elif num_let%2==1:
        x=425-(60*((num_let-1)/2))
        x2=x+50

    for i in range(num_let):
        draw.line(screen, BLACK, [x, 638], [x2, 638], 3)
        x+=60
        x2+=60

def update_guess(secret_word, current, guess): #Allows you to add letters into dashes o=if the guess is correct
    result=""
    for i in range(len(secret_word)):
        if guess==secret_word[i]:
            result=result+guess
        else:
            result=result+current[i]
    
    return result
def draw_noose():
    draw.line(screen, BLACK, [250, 550], [400, 550], 9)
    draw.line(screen, BLACK, [325,100], [325, 550], 9)
    draw.line(screen, BLACK, [321, 100], [490, 100], 9)
    draw.line(screen, BLACK, [490, 96],[490, 190], 9)
def draw_person(guesses_left):
    if guesses_left==9:
        #face
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
    elif guesses_left==8:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    elif guesses_left==7:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    elif guesses_left==6:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    #leg 2
        draw.line(screen, BLACK, [530,470],[490, 390], 2)
    elif guesses_left==5:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    #leg 2
        draw.line(screen, BLACK, [530,470],[490, 390], 2)
    # arm 1
        draw.line(screen, BLACK, [415,285],[490, 320], 2)
    elif guesses_left==4:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    #leg 2
        draw.line(screen, BLACK, [530,470],[490, 390], 2)
    # arm 1
        draw.line(screen, BLACK, [415,285],[490, 320], 2)
    #arm 2
        draw.line(screen, BLACK, [565,285],[490, 320], 2)
    elif guesses_left==3:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    #leg 2
        draw.line(screen, BLACK, [530,470],[490, 390], 2)
    # arm 1
        draw.line(screen, BLACK, [415,285],[490, 320], 2)
    #arm 2
        draw.line(screen, BLACK, [565,285],[490, 320], 2)
    #foot 1
        draw.line(screen, BLACK, [450,470],[430, 470], 2)
    elif guesses_left==2:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    #leg 2
        draw.line(screen, BLACK, [530,470],[490, 390], 2)
    # arm 1
        draw.line(screen, BLACK, [415,285],[490, 320], 2)
    #arm 2
        draw.line(screen, BLACK, [565,285],[490, 320], 2)
    #foot 1
        draw.line(screen, BLACK, [450,470],[430, 470], 2)
    #foot 2
        draw.line(screen, BLACK, [530,470],[550, 470], 2)
    elif guesses_left==1:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    #leg 2
        draw.line(screen, BLACK, [530,470],[490, 390], 2)
    # arm 1
        draw.line(screen, BLACK, [415,285],[490, 320], 2)
    #arm 2
        draw.line(screen, BLACK, [565,285],[490, 320], 2)
    #foot 1
        draw.line(screen, BLACK, [450,470],[430, 470], 2)
    #foot 2
        draw.line(screen, BLACK, [530,470],[550, 470], 2)
    #hand 1
        draw.line(screen, BLACK, [415,285],[405, 275], 2)
        draw.line(screen, BLACK, [415,285],[400, 285], 2)
        draw.line(screen, BLACK, [415,285],[405, 295], 2)
        draw.line(screen, BLACK, [415,285],[420, 275], 2)
    elif guesses_left==0:
        draw.ellipse(screen, BLACK,[450, 190, 80, 80], 2)
        draw.line(screen, BLACK,[490, 270], [490, 390],2)
    #leg 1
        draw.line(screen, BLACK, [450,470],[490, 390], 2)
    #leg 2
        draw.line(screen, BLACK, [530,470],[490, 390], 2)
    # arm 1
        draw.line(screen, BLACK, [415,285],[490, 320], 2)
    #arm 2
        draw.line(screen, BLACK, [565,285],[490, 320], 2)
    #foot 1
        draw.line(screen, BLACK, [450,470],[430, 470], 2)
    #foot 2
        draw.line(screen, BLACK, [530,470],[550, 470], 2)
    #hand 1
        draw.line(screen, BLACK, [415,285],[405, 275], 2)
        draw.line(screen, BLACK, [415,285],[400, 285], 2)
        draw.line(screen, BLACK, [415,285],[405, 295], 2)
        draw.line(screen, BLACK, [415,285],[420, 275], 2)
    #hand 2
        draw.line(screen, BLACK, [565,285],[575, 275], 2)
        draw.line(screen, BLACK, [565,285],[580, 285], 2)
        draw.line(screen, BLACK, [565,285],[575, 295], 2)
        draw.line(screen, BLACK, [565,285],[560, 275], 2)
def draw_let(let, let_num, num_let):
    lett=draw_text(let, 'calibri', 50, BLACK)
    lett_w=lett[1]
    if let_num%2==0:
        screen.blit(lett[0], [(50-lett_w)/2+(455-(60*(num_let/2))+(60*(let_num-1))), 600])
    else:
        screen.blit(lett[0], [(50-lett_w)/2+((425-(60*((num_let-1)/2)))+(60*(let_num-1))), 600])
def pause(a=None, r=None, g=None, s=None):
    
    paused=True
    
    x=1
    y=1
    while paused==True:    
        pos_mouse= mouse.get_pos()
        x_mouse=pos_mouse[0]
        y_mouse=pos_mouse[1]
        
        for event in pygame.event.get():
            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                paused=False
            
            if x_mouse>400  and y_mouse>200 and y_mouse<225 and event.type==MOUSEBUTTONDOWN:
                paused=False
        draw.rect(screen, BLACK, [300, 100, 300, 400], 0)
        button("continue",400,200,100,25,GREEN, BLACK)
        button("quit",400,400,100,25,RED,BLACK,quitgame)
        button("Restart", 400, 300, 100, 25, YELLOW, BLACK, main)
        display.flip()
     
        
        clock.tick(60)
def intro():
    done = False
    while not done:    
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                done= True
        title= draw_text("Hang Man", 'Calibri', 50, BLACK)
        title_w=title[1]
        screen.blit(title[0], [(900-title_w)/2+0, 50])
        button("Start",300,600,100,50,GREEN,BLACK, main)
        button("quit",500,600,100,50,RED,BLACK,quitgame)
        draw_noose()
        draw_person(0)
        
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
def finish(result, secret_word, a=None, r=None):
    finish_done=False
    while not finish_done:
        
        for event in pygame.event.get():
            if event.type == QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                done= True
        win=draw_text("congratulations you won! The secert word was: " + secret_word, 'calibri', 35, BLACK)
        win_w=win[1]
        lose=draw_text("Sorry you lost, the secert word was: " + secret_word, 'calibri', 35, BLACK)
        lose_w=lose[1]
        if result==True:
            screen.fill(GREEN)
            draw.rect(screen, BLACK, [300, 250, 300, 200], 0)
            screen.blit(win[0], [(900-win_w)/2+0,200])
        else:
            screen.fill(RED)
            draw.rect(screen, BLACK, [300, 250, 300, 200], 0)
            screen.blit(lose[0], [(900-lose_w)/2+0, 200])
        button("quit",400,400,100,25,RED,BLACK,quitgame)
        button("Restart", 400, 300, 100, 25,YELLOW, BLACK, main)
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

def main(a=None, r=None, g=None, s=None):
    main_done = False
    clicks=0
    text=""
    secret_word=random.choice(words)
    dashes=""
    guesses_left=10
    let_guessed=[]
    for i in range(len(secret_word)):  
        dashes=dashes+"-"
        
    guesses=[]
    result=""
    while not main_done:    
        # --- Main event loop
        screen.fill(WHITE)
         #choosing a word
        
        #guesses_left=10
        pos_mouse= mouse.get_pos()
        x_mouse=pos_mouse[0]
        y_mouse=pos_mouse[1]
        click = mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                quitgame()
            
            if event.type==MOUSEBUTTONDOWN and x_mouse>850 and y_mouse>50 and y_mouse<75:
                
                paused=True
                pause()
##            if  click[0] ==1 and x_mouse>600 and x_mouse<800 and y_mouse>300 and y_mouse<375:
##                clicks+=1
##        
##            if clicks%2==1:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    guess=text
                   
                    guess.lower()
                    let_guessed.append(guess)
                    if guess in secret_word:
                        
                            if len(guess)==len(secret_word):
                                if guess==secret_word:
                                    result=True
                                else:
                                    result=False
                                finish(result, secret_word)
                            elif len(guess)!=1 and len(guess)!=0:
                                result=False
                                finish(result, secret_word)
                            
                            elif len(guess)==1 or len(guess)==0:
                                for i in range(len(secret_word)):
                                    if guess==secret_word[i]:
                                        guess_info=[guess, (i+1), len(secret_word)]
                                        guesses.append(guess_info)
                                        
                                        dashes=update_guess(secret_word, dashes, guess)
                                    else:
                                        result=result+dashes[i]
                            else:
                                guesses_left-=1
                
                    else:
                        guesses_left-=1
                    if dashes==secret_word:
                        result=True
                        finish(result, secret_word)
                    elif guesses_left==0:
                        result=False
                        finish(result, secret_word)
                                
                                    
            
                    elif len(guess)!=1 and len(guess)!=0:
                        result=False
                        finish(result, secret_word)
                  #  else: draw person here
                        
                    text = ""
                    clicks+=1
                elif event.key == K_BACKSPACE:
                    text = text[:-1]
                else:
                    text = text+event.unicode
                        
##        let=draw_text("e", 'calibri', 50, BLACK)
##        let_w=let[1]
##        screen.blit(let[0], [(50-let_w)/2+335, 600])
        letter_list=", ".join(let_guessed)
        screen.blit(draw_text(letter_list, 'calibri', 25, BLACK)[0], [177, 675])
        guess_list=draw_text("Letters Guessed:", 'calibri', 25, BLACK)[0]
        screen.blit(guess_list, [1, 675])
        for let in guesses:
            draw_let(let[0], let[1], let[2])
        draw_dashes(len(secret_word))
        guess_text=draw_text("Guess here:", 'calibri', 30, BLACK)
        screen.blit(guess_text[0], [600, 325])
        draw.rect(screen, BLACK, [600, 350, 200, 25], 3)
        button("Pause", 850, 50, 50, 25, RED, BLACK)
        text_print=draw_text(text, 'calibri', 25,BLACK)
        screen.blit(text_print[0], [601, 351])
        draw_noose()
        draw_person(guesses_left)
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)


intro()
quit()
