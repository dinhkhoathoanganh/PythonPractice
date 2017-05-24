# ConnectFourOriginal.py
# First rather messy version of Connect Four game
# To do next: combine codes in the music, blit display, event handling loop, FPSClock.tick categories

import random, copy, sys, pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

BoardWidth = 7 # No. of max horizontal Tokens allowed
BoardHeight = 6 # No. of max horizontal Tokens allowed

# Set Screen size in pixels
ScreenWidth = 640
ScreenHeight = 450

# Set Title size in the playing board
SpaceSize = 50
SpaceX = int((ScreenWidth - BoardWidth * SpaceSize) / 2)
SpaceY = int((ScreenHeight - BoardHeight * SpaceSize) / 2)

# No. of moves computer calculate ahead
CalculateAheadMove = 2

# Clock speed
FPS = 30

def main():
    global FPSClock, SurfaceDispl, Red_Img, RedRect, Background_Img, Intro_Img, ScreenSize, Black_Img, BlackRect, Board_Img, Arrow_Img, ArrowRect, HumanW_Img, ComputerW_Img, Tie_Img, WinnerRect, speed

    # Put caption
    pygame.display.set_caption('Connect Four')

    # Play background music
    pygame.mixer.music.load("music/music.ogg")
    pygame.mixer.music.play(-1)

    # Set clock
    FPSClock = pygame.time.Clock()
    
    # Set global variables
    SurfaceDispl = pygame.display.set_mode((ScreenWidth, ScreenHeight))
    RedRect = pygame.Rect(int(SpaceSize / 2), ScreenHeight - int(3 * SpaceSize / 2), SpaceSize, SpaceSize)
    BlackRect = pygame.Rect(ScreenWidth - int(3 * SpaceSize / 2), ScreenHeight - int(3 * SpaceSize / 2), SpaceSize, SpaceSize)

    Intro_Img = pygame.image.load('image/intro.png')
    Background_Img = pygame.image.load('image/background.jpg')
    Red_Img = pygame.image.load('image/red.png')
    Black_Img = pygame.image.load('image/black.png')
    Board_Img = pygame.image.load('image/board.png')
    HumanW_Img = pygame.image.load('image/humanwinner.png')
    ComputerW_Img = pygame.image.load('image/computerwinner.png')
    Tie_Img = pygame.image.load('image/tie.png')
    
    ScreenSize = Background_Img.get_rect()
    WinnerRect = HumanW_Img.get_rect()
    WinnerRect.center = (int(ScreenWidth / 2), int(ScreenHeight / 2))

    Arrow_Img = pygame.image.load('image/arrow.png')
    ArrowRect = Arrow_Img.get_rect()
    ArrowRect.left = RedRect.right - 10
    ArrowRect.centery = RedRect.centery - 3

    speed = 10 # Speed for moving objects

    isFirstMove = True

    while True:
        gameRun(isFirstMove)


def gameRun(isFirstMove):
    getIntro()
    turn = 'computer'
    mainBoard = getNewBoard()

    # While playing game
    while True:
        if turn == 'human': # Human's turn
            getHumanMove(mainBoard, isFirstMove)
            if isFirstMove: # Switch off Instruction Arrow after first's move
                isFirstMove = False
            if isWinner(mainBoard, 'red'):  # Check if human wins
                winnerImg = HumanW_Img
                break
            turn = 'computer' # Switch to other player's turn
        
        elif turn == 'computer': #Computer's turn
            column = getComputerMove(mainBoard)
            displayComputerMove(mainBoard, column)
            indicateMove(mainBoard, 'black', column)
            if isWinner(mainBoard, 'black'): # Check if computer wins
                winnerImg = ComputerW_Img
                break
            turn = 'human' # Switch to other player's turn
        
        elif isBoardFull(mainBoard): # Check if it's a tie
            winnerImg = Tie_Img
            break
    
    # Play game over's music
    playMusic("music/gameover.ogg")
    
    # Display results
    while True:
        drawBoard(mainBoard)
        SurfaceDispl.blit(winnerImg, WinnerRect)
        pygame.display.update()
        FPSClock.tick()
        for event in pygame.event.get(): # Event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                return

def getIntro():
    while True:
        SurfaceDispl.blit(Intro_Img, ScreenSize)
        pygame.display.update()
        FPSClock.tick()
        for event in pygame.event.get(): # Event handling loop
            if event.type == MOUSEBUTTONUP:
                return

def playMusic(soundtrack):
    track = pygame.mixer.Sound(soundtrack)
    track.play()

def indicateMove(board, player, column):
    lowest = getLowestEmptySpace(board, column)
    if lowest != -1:
        board[column][lowest] = player


def drawBoard(board, newToken=None):
    SurfaceDispl.blit(Background_Img, ScreenSize)    

    # Draw existing tokens
    spaceRect = pygame.Rect(0, 0, SpaceSize, SpaceSize)
    for x in range(BoardWidth):
        for y in range(BoardHeight):
            spaceRect.topleft = (SpaceX + (x * SpaceSize), SpaceY + (y * SpaceSize))
            if board[x][y] == 'red':
                SurfaceDispl.blit(Red_Img, spaceRect)
            elif board[x][y] == 'black':
                SurfaceDispl.blit(Black_Img, spaceRect)

    # Draw the new token
    if newToken != None:
        if newToken['color'] == 'red':
            SurfaceDispl.blit(Red_Img, (newToken['x'], newToken['y'], SpaceSize, SpaceSize))
        elif newToken['color'] == 'black':
            SurfaceDispl.blit(Black_Img, (newToken['x'], newToken['y'], SpaceSize, SpaceSize))

    # Draw the tiles
    for x in range(BoardWidth):
        for y in range(BoardHeight):
            spaceRect.topleft = (SpaceX + (x * SpaceSize), SpaceY + (y * SpaceSize))
            SurfaceDispl.blit(Board_Img, spaceRect)

    # Draw 2 samples Tokens at the side
    SurfaceDispl.blit(Red_Img, RedRect)
    SurfaceDispl.blit(Black_Img, BlackRect)


def getNewBoard():
    board = []
    for x in range(BoardWidth):
        board.append([None] * BoardHeight)
    return board


def getHumanMove(board, isFirstMove):
    draggingToken = False
    tokenx, tokeny = None, None
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and not draggingToken and RedRect.collidepoint(event.pos):
                # Start dragging red token
                draggingToken = True
                tokenx, tokeny = event.pos
            elif event.type == MOUSEMOTION and draggingToken:
                # While red token being dragged
                tokenx, tokeny = event.pos
            elif event.type == MOUSEBUTTONUP and draggingToken:
                # Red token is let go
                if tokeny < SpaceY and tokenx > SpaceX and tokenx < ScreenWidth - SpaceX:
                    # If the token is let go on top of the board
                    column = int((tokenx - SpaceX) / SpaceSize)
                    if isValidMove(board, column):
                        displayTokenDrop(board, column, 'red')
                        board[column][getLowestEmptySpace(board, column)] = 'red'
                        drawBoard(board)
                        pygame.display.update()
                        playMusic("music/shoot.ogg")
                        return
                tokenx, tokeny = None, None
                draggingToken = False
        if tokenx != None and tokeny != None:
            drawBoard(board, {'x':tokenx - int(SpaceSize / 2), 'y':tokeny - int(SpaceSize / 2), 'color':'red'})
        else:
            drawBoard(board)

        if isFirstMove: # Show the Instruction arrow for the first move.
            SurfaceDispl.blit(Arrow_Img, ArrowRect)

        pygame.display.update()
        FPSClock.tick()


def displayTokenDrop(board, column, color):
    x = SpaceX + column * SpaceSize
    y = SpaceY - SpaceSize
    lowestEmptySpace = getLowestEmptySpace(board, column)

    while True:
        y += int(speed)
        if int((y - SpaceY) / SpaceSize) >= lowestEmptySpace:
            return
        drawBoard(board, {'x':x, 'y':y, 'color':color})
        pygame.display.update()
        FPSClock.tick()


def displayComputerMove(board, column):
    x = BlackRect.left
    y = BlackRect.top
    # Black token going up
    while y > (SpaceY - SpaceSize):
        y -= int(speed)
        drawBoard(board, {'x':x, 'y':y, 'color':'black'})
        pygame.display.update()
        FPSClock.tick()
    # Black token going across
    y = SpaceY - SpaceSize
    while x > (SpaceX + column * SpaceSize):
        x -= int(speed)
        drawBoard(board, {'x':x, 'y':y, 'color':'black'})
        pygame.display.update()
        FPSClock.tick()
    # Black token going down
    displayTokenDrop(board, column, 'black')
    playMusic("music/shoot.ogg")


def getComputerMove(board):
    potentialMoves = getPotentialMoves(board, 'black', CalculateAheadMove)
    # Get the best fitness from the potential moves
    bestMoveFitness = -1
    for i in range(BoardWidth):
        if potentialMoves[i] > bestMoveFitness and isValidMove(board, i):
            bestMoveFitness = potentialMoves[i]
    # Find all potential moves that have this best fitness
    bestMoves = []
    for i in range(len(potentialMoves)):
        if potentialMoves[i] == bestMoveFitness and isValidMove(board, i):
            bestMoves.append(i)
    return random.choice(bestMoves)


def getPotentialMoves(board, tile, lookAhead):
    if lookAhead == 0 or isBoardFull(board):
        return [0] * BoardWidth

    if tile == 'red':
        enemyTile = 'black'
    else:
        enemyTile = 'red'

    # Figure out the best move to make.
    potentialMoves = [0] * BoardWidth
    for firstMove in range(BoardWidth):
        dupeBoard = copy.deepcopy(board)
        if not isValidMove(dupeBoard, firstMove):
            continue
        indicateMove(dupeBoard, tile, firstMove)
        if isWinner(dupeBoard, tile):
            # A winning move automatically gets a perfect fitness
            potentialMoves[firstMove] = 1
            break # Don't bother calculating other moves
        else:
            # Do other player's counter moves and determine best one
            if isBoardFull(dupeBoard):
                potentialMoves[firstMove] = 0
            else:
                for counterMove in range(BoardWidth):
                    dupeBoard2 = copy.deepcopy(dupeBoard)
                    if not isValidMove(dupeBoard2, counterMove):
                        continue
                    indicateMove(dupeBoard2, enemyTile, counterMove)
                    if isWinner(dupeBoard2, enemyTile):
                        # A losing move automatically gets the worst fitness
                        potentialMoves[firstMove] = -1
                        break
                    else:
                        # Do the recursive call to getPotentialMoves()
                        results = getPotentialMoves(dupeBoard2, tile, lookAhead - 1)
                        potentialMoves[firstMove] += (sum(results) / BoardWidth) / BoardWidth
    return potentialMoves


def getLowestEmptySpace(board, column):
    # Return the row number of the lowest empty row in the given column.
    for y in range(BoardHeight-1, -1, -1):
        if board[column][y] == None:
            return y
    return -1


def isValidMove(board, column):
    # Returns True if there is an empty space in the given column.
    # Otherwise returns False.
    if column < 0 or column >= (BoardWidth) or board[column][0] != None:
        return False
    return True


def isBoardFull(board):
    # Returns True if there are no empty spaces anywhere on the board.
    for x in range(BoardWidth):
        for y in range(BoardHeight):
            if board[x][y] == None:
                return False
    return True


def isWinner(board, tile):
    # Check horizonal line
    for x in range(BoardWidth - 3):
        for y in range(BoardHeight):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True
    # Check vertical line
    for x in range(BoardWidth):
        for y in range(BoardHeight - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True
    # Check / line
    for x in range(BoardWidth - 3):
        for y in range(3, BoardHeight):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True
    # Check \ line
    for x in range(BoardWidth - 3):
        for y in range(BoardHeight - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True
    return False


if __name__ == '__main__':
    main()
