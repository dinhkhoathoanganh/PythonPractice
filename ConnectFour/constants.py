# constants.py
# global constants for ConnectFour.py, classes.py and process.py

BoardWidth = 7 # No. of max horizontal Tokens allowed
BoardHeight = 6 # No. of max horizontal Tokens allowed

# Set Screen size in pixels
ScreenWidth = 640
ScreenHeight = 450

# Set Title size in the playing board 
SpaceSize = 50
SpaceX = int((ScreenWidth-BoardWidth*SpaceSize)/2)
SpaceY = int((ScreenHeight-BoardHeight*SpaceSize)/2)

# Clock speed
FPS = 30

if __name__ == '__main__':
    main()


