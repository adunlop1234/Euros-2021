import csv
import os, sys
import pygame
from pygame.locals import *
import time
import random
from playsound import playsound
from gtts import gTTS

with open(os.path.join("data", "draw.csv"), "r") as f:
    reader = csv.reader(f)
    team_assignment = list(reader)

def voice(text):
    tts = gTTS(text=text, lang='en')
    tts.save("text.mp3")
    playsound("text.mp3")
    os.system("rm text.mp3")

GAMESTATE = 0

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

pygame.init()
myfont = pygame.font.SysFont('Arial', 50)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Euros 2021 Sweepstake Draw')

while True: 

    if len(team_assignment) == 0:
        GAMESTATE = 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if GAMESTATE == 0:

        # Get the latest name
        person_name, team_name = team_assignment.pop(random.randint(0, len(team_assignment)-1))

        # Clear background
        DISPLAYSURF.fill((0,0,0))
        pygame.display.update()
        time.sleep(3)

        # Display person name
        person = myfont.render(person_name, False, (255, 255, 255))
        DISPLAYSURF.blit(person, (SCREEN_WIDTH/4 - person.get_width()/2, SCREEN_HEIGHT/2 - person.get_height()/2))
        pygame.display.update()
        voice(person_name)
        time.sleep(3)

        # Display team name
        team = myfont.render(team_name, False, (255, 255, 255))
        DISPLAYSURF.blit(team,(3*SCREEN_WIDTH/4 - team.get_width()/2, SCREEN_HEIGHT/2 - team.get_height()/2))
        pygame.display.update()
        voice(team_name)
        time.sleep(3)
    
    else:

        # Show end game text
        DISPLAYSURF.fill((0,0,0))
        end_text = "Draw complete. Good luck to everyone!"
        end_font = myfont.render(end_text, False, (255, 255, 255))
        DISPLAYSURF.blit(end_font,(SCREEN_WIDTH/2 - end_font.get_width()/2, SCREEN_HEIGHT/2 - end_font.get_height()/2))
        pygame.display.update()
        voice(end_text)