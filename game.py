import pygame
from random import randint as rand
import time
from buttonClass import Button
import phonkynotes
pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("STN Main Menu v0.1")

noteImg = pygame.image.load("assets/note.png").convert_alpha()
pnImg = pygame.image.load("assets/pn.png").convert_alpha()

running = True
firstFrame = True
songname = ""
button = Button(10,10,pnImg,0.5)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if songname == "PhonkyNotes":
        if firstFrame == True:
            phonkynotes.playSong()
            firstFrame = False
            songname = ""
    if songname == "":
        screen.fill((0, 100, 255))
        button.draw(screen)
        if button.clicked == True:
            songname = "PhonkyNotes"
            firstFrame = True
    pygame.display.update()
pygame.quit()