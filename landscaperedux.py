# Landscape2 (not using loop or if structure)
# A program that shows the changing color of the sky, moon and sun
# as well as their respective positions of the latter two items
# depending on the time input (accepting both integer and decimal inputs and input >24)

def getinput ():
    hoursinput=input("How many hours have passed since midnight? ")
    sunhours=int(int(hoursinput)%24)
    return sunhours


def drawsky(sunhours):
    from graphics import *
    from colorsys import *
    import math
    #Setwindow
    win = GraphWin('Landscape sun moon', 500, 700)

    #Sky color
    rec = Rectangle(Point(0,0), Point(500,400))
    skypara = abs(12-abs(float(sunhours)-12))/12
    r, g, b = hls_to_rgb(.5, skypara, .4)
    r, g, b = [x*255.0 for x in r, g, b]
    SkyColor = color_rgb(r, g, b)
    # SkyColor = hsl(240, 100%, 33%)
    rec.setFill(SkyColor)
    rec.draw(win)

    #Color blending
    mooncolor = color_rgb(166,165,165)
    redshade=int(-9.79*((sunhours)%24)+255)
    suncolor = color_rgb(250,redshade,0)

    #Draw moon
    moonhours = int((sunhours-12)%24)
    v=round(moonhours*500.0/13.0-3000.0/13.0)
    h=round((moonhours**2)*2.5-125.0/2*moonhours+485)
    cir1 = Circle(Point(v,h), 50)
    cir1.setFill(mooncolor)
    cir1.setOutline(SkyColor)
    cir1.draw(win)

    cir2 = Circle(Point(v-25,h-25), 50)
    cir2.setFill(SkyColor)
    cir2.setOutline(SkyColor)
    cir2.draw(win)

    #Draw sun
    x=round(sunhours*45.45-318.19)
    y=round((sunhours**2)*5.0-125.0*sunhours+830)
    cir3 = Circle(Point(x,y), 50)
    cir3.setFill(suncolor)
    cir3.setOutline(SkyColor)
    cir3.draw(win)
    return win

def setlandscape(win):
    from graphics import *
    #draw hills
    hill1 = Oval (Point(20,200), Point(200,700))
    hill1.draw(win)
    hill1.setFill ("brown")
    hill1.setOutline ("brown")

    hill2 = hill1.clone()
    hill2.move (170,-50)
    hill2.draw(win)

    hill3 = hill1.clone()
    hill3.move (120,-75)
    hill3.draw(win)

    hill4 = hill1.clone()
    hill4.move (300,30)
    hill4.draw(win)

    #draw grass
    grass= Rectangle (Point(0,400), Point(500,700))
    grass.draw(win)
    grass.setFill("green")
    grass.setOutline("green")
    
    #draw houses
    house= Rectangle (Point(80,520), Point(240,640))
    house.draw(win)
    house.setFill("yellow")
    house.setOutline("blue")

    roof= Polygon(Point(80,520),Point(240,520),Point(150,490))
    roof.draw(win)
    roof.setFill("red")
    roof.setOutline("blue")

    house2 = house.clone()
    roof2 = roof.clone()
    house2.move(200,-40)
    roof2.move(200,-40)
    house2.draw(win)
    roof2.draw(win)


def main():
    sunhours = getinput()
    win = drawsky(sunhours)
    setlandscape(win)

    print "This is how the sky look like",sunhours,"hours after midnight."
    raw_input ("Have a nice day!")
    win.close()

main()

