# Github contribution chart on Pimoroni Galactic Unicorn
# Kevin McAleer
# December 2022

from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
from time import sleep
from galactic import GalacticUnicorn
from chart import chart

# Set up the display
gu = GalacticUnicorn()
display = PicoGraphics(display=DISPLAY)
gu.set_brightness(1)

WIDTH, HEIGHT = display.get_bounds()
ONE = {'red':0,'green':32,'blue':0}
TWO = {'red':0,'green':64,'blue':0}
THREE = {'red':0,'green':128,'blue':0}
FOUR = {'red':0,'green':255,'blue':0}
BLACK = {'red':0,'green':0,'blue':0}
WHITE = {'red':64,'green':64, 'blue':64}

def create_pen(display, color):
    """ Create a pen from a colour dictionary """
    return display.create_pen(color['red'],color['green'],color['blue'])

# Create the pens
zero = create_pen(display, WHITE)
one = create_pen(display, ONE)
two = create_pen(display, TWO)
three = create_pen(display, THREE)
four = create_pen(display, FOUR)

x = 0
y = 2

for row in chart:
    x = 0
    for pixel in row:
        if pixel == '0':
            display.set_pen(zero)
        elif pixel == '1':
            display.set_pen(one)
        elif pixel == '2':
            display.set_pen(two)
        elif pixel == '3':
            display.set_pen(three)
        elif pixel == '4':
            display.set_pen(four)
        x += 1
        display.pixel(x, y)
    y += 1
    

gu.update(display)
