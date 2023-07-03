from buttonClass import Button
import pygame
from time import sleep as zzz
from random import randint as rand

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("STN Phonky Notes v0.1")

noteImg = pygame.image.load("assets/note.png").convert_alpha()
noteImg2 = pygame.image.load("assets/notenext.png").convert_alpha()

def playSong():
    screen.fill((50, 50, 50))
    note2 = Button(50,344,noteImg2,1)
    note2.draw(screen)
    pygame.display.update()
    zzz(3)
    pygame.mixer.music.load("songs/phonkynotes.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    points = 0
    clicked = False
    for _ in range(100):
        # Draw screen color
        screen.fill((50, 50, 50))
        # Draw current note
        if clicked == False:
            note = Button(50,344,noteImg,1)
            note.draw(screen)
        # Draw next note
        note2 = Button(100,252,noteImg2,1)
        note2.draw(screen)
        # Check if clicked
        if note.clicked == True:
            points = points + 1
            clicked = True
        # Update screen
        pygame.display.update()
       # Wait for next note
        zzz(0.005)
    for _ in range(100):
        # Draw screen color
        screen.fill((50, 50, 50))
        # Draw current note
        if clicked == False:
            note = Button(100,252,noteImg,1)
            note.draw(screen)
        # Draw next note
        note2 = Button(332,124,noteImg2,1)
        note2.draw(screen)
        # Check if clicked
        if note.clicked == True:
            points = points + 1
            clicked = True
        # Update screen
        pygame.display.update()
       # Wait for next note
        zzz(0.005)
    clicked = False
    print(points)
    pygame.mixer.music.stop()
    