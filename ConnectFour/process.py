# process.py
# event process for ConnectFour.py

import sys, pygame, random, copy
from pygame.locals import *
from classes import *
from constants import *

pygame.init()

def process():
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
            

# PlayBoard = Board()
#         FPSCLOCK.tick()
#         redToken.displayImage()



if __name__ == '__main__':
    main()


