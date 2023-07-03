from buttonClass import Button
import pygame
from time import sleep as zzz

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("STN Phonky Notes v0.1")

noteImg = pygame.image.load("assets/note.png").convert_alpha()
noteImg2 = pygame.image.load("assets/notenext.png").convert_alpha()

def playSong():
    pygame.mixer.music.load("songs/PhonkyNotes/phonkynotes.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()

    points = 0
    # Draw screen color
    screen.fill((50, 50, 50))
    # Draw current note
    note = Button(0,0,noteImg,1)
    note.draw(screen)
    # Draw next note
    note = Button(450,20,noteImg2,1)
    note.draw(screen)
    # Check if clicked

    # Update screen
    pygame.display.update()
    # Wait for next note
    zzz(0.5)
    screen.fill((50, 50, 50))
    note = Button(450,20,noteImg,1)
    note.draw(screen)
    note = Button(123,211,noteImg2,1)
    note.draw(screen) 
    pygame.display.update()
    zzz(0.5)
    screen.fill((50, 50, 50))
    note = Button(123,211,noteImg,1)
    note.draw(screen)
    note = Button(123,445,noteImg2,1)
    note.draw(screen)    
    pygame.display.update()
    zzz(0.5)
    screen.fill((50, 50, 50))
    note = Button(123,445,noteImg,1)
    note.draw(screen)
    note = Button(153,445,noteImg2,1)
    note.draw(screen) 
    pygame.display.update()
    zzz(0.5)
    screen.fill((50, 50, 50))
    note = Button(153,445,noteImg,1)
    note.draw(screen)
    note = Button(333,411,noteImg2,1)
    note.draw(screen)   
    pygame.display.update()
    zzz(0.5)
    screen.fill((50, 50, 50))
    note = Button(333,411,noteImg,1)
    note.draw(screen)
    note = Button(232,10,noteImg2,1)
    note.draw(screen)   
    pygame.display.update()
    zzz(0.5)
    screen.fill((50, 50, 50))
    note = Button(232,10,noteImg,1)
    note.draw(screen)
    note = Button(123,445,noteImg2,1)
    note.draw(screen)
    pygame.display.update()
    zzz(0.5)
    screen.fill((50, 50, 50))
    note = Button(123,445,noteImg,1)
    note.draw(screen)
    
        
        
    pygame.display.update()
    zzz(0.5)
    print(points)
    pygame.mixer.music.stop()
    