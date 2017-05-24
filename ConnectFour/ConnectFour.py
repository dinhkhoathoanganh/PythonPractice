# ConnectFour.py
# Connect Four Game
# accompanied with classes.py, process.py and Image and Music folders

import sys, pygame, random, copy
from pygame.locals import *
from classes import *
from process import *
from constants import *

pygame.init()
pygame.mixer.init()

# Clock speed
FPSClock = pygame.time.Clock()

# Set screen
Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight),0, 32) 

#Set difficulty of the game
PreCalculateMove = 2

def main():

    img_background = BaseClass(0, 0, ScreenWidth, ScreenHeight, 'image/background.jpg')
    img_red = ConstantDisplay(SpaceX, SpaceY, SpaceSize, SpaceSize, 'image/4row_red.png')
    
    mainBoard = Board()
    # ConstantDisplay.DrawTiles(mainBoard, None, 'img/4row_board.png')

    GameMusic.backgroundMusic('music/music.ogg')
    pygame.display.set_caption('Connect Four')
    # redToken.Display('4row_red.png',(SpaceSize,SpaceSize))

    while True:
        # Keep looping until player clicks the mouse or quits.
        process()

        BaseClass.allSprites.draw(Screen)



        pygame.display.flip()

        FPSClock.tick(FPS)
            

# PlayBoard = Board()
#         FPSCLOCK.tick()
#         redToken.displayImage()



if __name__ == '__main__':
    main()


