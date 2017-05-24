# classes.py
# class definitions for ConnectFour.py

import sys, pygame, random, copy
from pygame.locals import *
from constants import *

pygame.init()
pygame.mixer.init()


class BaseClass(pygame.sprite.Sprite):
	allSprites = pygame.sprite.Group()
	def __init__(self, x, y, width, height, img_string):
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allSprites.add(self)

		self.image = pygame.image.load(img_string)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.width = width
		self.height = height
class ConstantDisplay(BaseClass):
	List = pygame.sprite.Group()

	def __init__(self, x, y, width, height, img_string, boardList=None, indicator=None):
		BaseClass.__init__(self, x, y, width, height, img_string)
		ConstantDisplay.List.add(self)
		if boardList is None:
			self.boardList = []
			self.indicator = ''
		else: 
			self.boardList = boardList
			self.indicator = indicator

	def DrawTiles(boardList, indicator, img_string):
		print(boardList)
		for i in range(BoardWidth):
			for j in range(BoardHeight):
				if boardList[i][j] == indicator:
					topleft = (SpaceX + (i * SpaceSize), SpaceY + (j * SpaceSize))
					pygame.Surface.blit(img_string, topleft)


			
class GameMusic:
    def __init__(self,track):
        self.track = ''
    def backgroundMusic(track):
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(-1)
    def soundEffect (track):
        soundTrack = pygame.mixer.Sound(track)
        soudnTrack.play()

class Board:
    def __init__(self):
        self.board = []
        
    def getNewBoard(self):
        for x in range(BoardWidth):
            self.board.append([None] * BoardHeight)
        return self.board

if __name__ == '__main__':
    main()

