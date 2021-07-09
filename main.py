#Author: April Miller 7/8/21

#Imports
import pygame
from pygame.event import wait
from pygame.locals import *

screen = pygame.display.set_mode([704,518])
panda = pygame.Rect(100,100,105,105)
VEL = 3

def drawWindow(panda):
    #Load the background
    image = pygame.image.load(r'boop.png')
    screen.blit(image, (0, 0))
        
    #Load the panda
    image2 = pygame.image.load(r'beep.png')
    screen.blit(image2, (panda.x, panda.y))

    #Load the carrot
    image3 = pygame.image.load(r'carrot.png')
    screen.blit(image3, (500, 0))

    #Load the apple
    image4 = pygame.image.load(r'apple.png')
    screen.blit(image4, (530, 0))

    pygame.display.update()


def main():
    #While the program is running, do this
    #Initialize the window
    
    clock = pygame.time.Clock()
    #While the program is running, do this...
    running = True
    while running:
        
        #Increment clock
        clock.tick(60)
        #Allows user to close window when exit button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            panda.y -= VEL
        if pressed[pygame.K_DOWN]:
            panda.y += VEL
        if pressed[pygame.K_LEFT]:
            panda.x -= VEL
        if pressed[pygame.K_RIGHT]:
                panda.x += VEL

        #Update the display
        drawWindow(panda)
        
    #Done!
    pygame.quit()

if __name__ == "__main__":
    main()