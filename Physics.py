import random
import time
import pygame
import math
from enum import Enum

mouse_x = 0
mouse_y = 0
mouse_x_last = 0
mouse_y_last = 0
mouse_x_delta = 0
mouse_y_delta = 0
mouseDown = False

display_width = 1300
display_height = 768
viewport_width = 900
viewport_height = display_height

black = (0, 0, 0)
white = (215, 215, 215)
red = (200, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 255)
yellow = (215, 215, 0)
bright_red = (255, 0, 0)
bright_green = (0, 215, 0)
light_blue = (12, 249, 255)
grey = (180, 180, 180)
light_grey = (200, 200, 200)
dark_grey = (100, 100, 100)
pure_white = (255, 255, 255)
purple = (224, 42, 255)
light_green = (26*6, 215, 12*6)

size1 = 1
size2 = 2
size3 = 3
size4 = 4
size5 = 5

output = ""

pi = 3.14159
origin = (0, 0)
g = 9.81
metre = 20  # 1 metre = 20 pixels
frame_time = 1 / 20  # length of one engine frame in seconds
frame_count = 1
running = False
events = None
last_events = None

tabs = []
tab_buttons = []
currentTab = ""

objects = []  # All objects (Oblongs etc) are stored here
elements = []  # All dynamic interface elements (Graphs, Text Boxes etc) are stored here

# Debugging flags
draw_coordinates = False
draw_normals = False
draw_suvat = False
draw_angular = False
draw_forces = False
highlight_intersections = False
debug = False

pygame.init()

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Experimental Physics by Rahul Jhuree')  # Title of windows

clock = pygame.time.Clock()  # Built In Clock


def nothing():
    pass

def drawAxis():
    pygame.draw.line(screen, red, (20, viewport_height - 20), (viewport_width - 20, viewport_height - 20))
    pygame.draw.line(screen, red, (20, 20), (20, viewport_height - 20))


def drawGridlines():
    spacing = 30  # Number of pixels between each gridline
    for i in range(viewport_height // spacing):
        pygame.draw.line(screen, grey, (0, i * spacing), (viewport_width, i * spacing))

    for i in range(viewport_width // spacing):
        pygame.draw.line(screen, grey, (i * spacing, 0), (i * spacing, viewport_height))
    pass


def drawForce(origin, direction, magnitude):
    direction = degToRad(direction)
    origin = roundPoint(origin)

    point1 = origin
    point2 = addPoint(origin, (magnitude * math.cos(direction), -magnitude * math.sin(direction)))
    pygame.draw.line(screen, purple, point1, point2)
    pygame.draw.circle(screen, purple, roundPoint(origin), 3)


def displayMessage(text, size, x, y, colour=black):
    font = pygame.font.SysFont(None, size)
    image = font.render(text, True, colour)
    screen.blit(image, (x, y))


def refreshScreen():
    pygame.draw.rect(screen, white, pygame.Rect((0, 0), (850, display_height)))
    pygame.draw.rect(screen, white, pygame.Rect((0, 0), (850, display_height)))


def midpoint(point1, point2):
    x = int((point1[0] + point2[0]) // 2)
    y = int((point1[1] + point2[1]) // 2)
    return (x, y)


def addPoint(point1, point2):
    x = point1[0] + point2[0]
    y = point1[1] + point2[1]
    return (x, y)


def subPoint(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return (x, y)


def roundPoint(point, decimal_places=0):  # Rounds points to the nearest integer
    x = point[0]
    y = point[1]

    if decimal_places == 0:
        x = int(x)
        y = int(y)
    else:
        x = round(x, decimal_places)
        y = round(y, decimal_places)
    return (x, y)


def checkNumberInput():
    output = ""

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                output += "0"
            if event.key == pygame.K_1:
                output += "1"
            if event.key == pygame.K_2:
                output += "2"
            if event.key == pygame.K_3:
                output += "3"
            if event.key == pygame.K_4:
                output += "4"
            if event.key == pygame.K_5:
                output += "5"
            if event.key == pygame.K_6:
                output += "6"
            if event.key == pygame.K_7:
                output += "7"
            if event.key == pygame.K_8:
                output += "8"
            if event.key == pygame.K_9:
                output += "9"
            if event.key == pygame.K_PERIOD:
                output += "."
            if event.key == pygame.K_SPACE:
                output += " "
    return output

def checkKeyInput():
    output = ""

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                output += "a"
            if event.key == pygame.K_b:
                output += "b"
            if event.key == pygame.K_c:
                output += "c"
            if event.key == pygame.K_d:
                output += "d"
            if event.key == pygame.K_e:
                output += "e"
            if event.key == pygame.K_f:
                output += "f"
            if event.key == pygame.K_g:
                output += "g"
            if event.key == pygame.K_h:
                output += "h"
            if event.key == pygame.K_i:
                output += "i"
            if event.key == pygame.K_j:
                output += "j"
            if event.key == pygame.K_k:
                output += "k"
            if event.key == pygame.K_l:
                output += "l"
            if event.key == pygame.K_m:
                output += "m"
            if event.key == pygame.K_n:
                output += "n"
            if event.key == pygame.K_o:
                output += "o"
            if event.key == pygame.K_p:
                output += "p"
            if event.key == pygame.K_q:
                output += "q"
            if event.key == pygame.K_r:
                output += "r"
            if event.key == pygame.K_s:
                output += "s"
            if event.key == pygame.K_t:
                output += "t"
            if event.key == pygame.K_u:
                output += "u"
            if event.key == pygame.K_v:
                output += "v"
            if event.key == pygame.K_w:
                output += "w"
            if event.key == pygame.K_x:
                output += "x"
            if event.key == pygame.K_y:
                output += "y"
            if event.key == pygame.K_z:
                output += "z"
            if event.key == pygame.K_PERIOD:
                output += "."
            if event.key == pygame.K_SPACE:
                output += " "

    return output

def checkBackspace():
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return True


def drawSegment(segment, x, y, colour, w=7, h=2):
    o = w - h

    if segment == 1:
        pygame.draw.rect(screen, colour, pygame.Rect((x, y), (w, h)))
    if segment == 2:
        pygame.draw.rect(screen, colour, pygame.Rect((x + o, y), (h, w)))
    if segment == 3:
        pygame.draw.rect(screen, colour, pygame.Rect((x + o, y + o), (h, w)))
    if segment == 4:
        pygame.draw.rect(screen, colour, pygame.Rect((x, y + 2 * o), (w, h)))
    if segment == 5:
        pygame.draw.rect(screen, colour, pygame.Rect((x, y + o), (h, w)))
    if segment == 6:
        pygame.draw.rect(screen, colour, pygame.Rect((x, y), (h, w)))
    if segment == 7:
        pygame.draw.rect(screen, colour, pygame.Rect((x, y + o), (w, h)))


def drawDigit(digit, x, y, colour, w=7, h=2):  # Dres a digit on screen in seven-segment form using pygame rects
    segments = []
    if digit == 0:
        segments = [1, 2, 3, 4, 5, 6]
    if digit == 1:
        segments = [2, 3]
    if digit == 2:
        segments = [1, 2, 4, 5, 7]
    if digit == 3:
        segments = [1, 2, 3, 4, 7]
    if digit == 4:
        segments = [2, 3, 6, 7]
    if digit == 5:
        segments = [1, 3, 4, 6, 7]
    if digit == 6:
        segments = [1, 3, 4, 5, 6, 7]
    if digit == 7:
        segments = [1, 2, 3]
    if digit == 8:
        segments = [1, 2, 3, 4, 5, 6, 7]
    if digit == 9:
        segments = [1, 2, 3, 4, 6, 7]

    for s in segments:
        drawSegment(s, x, y, colour, w, h)


def drawNumber(number, x, y, colour=black, size=1):
    digits = splitDigits(number)

    spacing = 11
    w = 7
    h = 2
    if size == 1:
        spacing = 11
        w = 7
        h = 2
    elif size == 2:
        spacing = 14
        w = 9
        h = 3
    elif size == 3:
        spacing = 17
        w = 10
        h = 4
        print("sss")

    print((w,h))

    for i, d in enumerate(digits):
        drawDigit(d, x + i * spacing, y, colour, w, h)


def degToRad(angle):
    return (angle * math.pi / 180)


def radToDeg(angle):
    return (angle * 180 / math.pi)


def splitDigits(number):  # Converts int to string, splits into characters, converts characters back to ints
    return ([int(d) for d in str(number)])


def checkIntersection(point1, point2, point3, point4):
    # I do not know WHY this code works. I just know that it DOES WORK
    # Also, this algorithm seems to have problems with points containing decimals
    point1 = roundPoint(point1)
    point2 = roundPoint(point2)
    point3 = roundPoint(point3)
    point4 = roundPoint(point4)

    p = point3
    q = point1
    r = subPoint(point4, point3)
    s = subPoint(point2, point1)

    # t = (q - p) * s / (r * s)
    # u = (q - p) * r / (r * s)
    # Where  "*"  means vector cross product

    if vectorCrossProduct(r,
                          s) == 0:  # If r * s = 0, the lines are either parallel or collinear (parallel and touching)

        if vectorCrossProduct(subPoint(q, p), r) == 0:  # If (q - p) * r = 0, the lines are collinear
            return True
        else:  # The lines are parallel (do not intersect)
            return False
    else:
        t = vectorCrossProduct(subPoint(q, p), s) / vectorCrossProduct(r, s)
        u = vectorCrossProduct(subPoint(q, p), r) / vectorCrossProduct(r, s)
        if (0 <= t <= 1) and (0 <= u <= 1):  # The segments intersect
            return True
        else:  # Not parallel, but do not intersect
            return False


def vectorCrossProduct(point1, point2):
    # Let U = (ux,uy), V = (vx,vy)
    # U x V = ux*vy - uy*vx

    product = point1[0] * point2[1] - point1[1] * point2[0]
    return product
    pass


def calculateNormal(point1, point2):  # Returns normal as degrees. ((0,0),(10,0)) returns 90
    if point1[0] > point2[0]:  # Normal points downwards (-180 < a < 0)
        angle = -radToDeg(math.atan((point2[1] - point1[1]) / (point2[0] - point1[0])))
        normal = angle - 90

    elif point1[0] < point2[0]:  # Normal points upwards (0 < a < 180)
        angle = -radToDeg(math.atan((point2[1] - point1[1]) / (point2[0] - point1[0])))
        normal = angle + 90

    else:
        if point1[1] < point2[1]:  # Normal points EXACTLY right (a = 0)
            normal = 0
        elif point1[1] > point2[1]:  # Normal points EXACTLY left (a = 180)
            normal = 180
    return normal
    pass


# Takes coordinates x and y and returns angle in degrees, in this coordinate system:
#   x 1 2 3 4 5
# y + - - - - - >
# 1 |
# 2 |
# 3 |
# 4 |
# 5 |
# So getAngle(3,3) returns -45, getAngle(3,-3) returns 45
def getAngle(x, y):
    if y > 0 and x > 0:
        angle = math.atan(y / x) * (180 / math.pi)
    elif y < 0 and x > 0:
        angle = math.atan(y / x) * (180 / math.pi)
    elif y < 0 and x < 0:
        angle = math.atan(y / x) * (180 / math.pi) - 180
    elif y > 0 and x < 0:
        angle = math.atan(y / x) * (180 / math.pi) - 180
    else:
        if (x == 0):
            if (y > 0):
                angle = 90.0
            elif (y < 0):
                angle = -90.0
        elif (y == 0):
            if (x > 0):
                angle = 0.0
            elif (x < 0):
                angle = 180.0
    return angle


class Object(Enum):
    platform = 0
    oblong = 1


class TabGroup:
    name = ""

    def __init__(self, name):
        self.elements = []
        self.name = name

    def addItem(self, item):
        self.elements.append(item)

    def draw(self):
        for i in range(len(self.elements)):
            self.elements[i].draw()

    def update(self):
        for i in range(len(self.elements)):
            self.elements[i].update()


class Window:

    maximised = True
    titleBarHeight = 20
    titleBarColour = white

    activeAndMouseDown = False
    wasAlreadyClicked = False

    def __init__(self, title, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.elements = []

    def addItem(self, item):
        item.x += self.x
        item.y += self.y + self.titleBarHeight
        self.elements.append(item)

    def drawTitleBar(self):
        if self.activeAndMouseDown:
            if mouseDown:
                self.x += mouse_x_delta
                self.y += mouse_y_delta
                for i in range(len(self.elements)):
                    self.elements[i].x += mouse_x_delta
                    self.elements[i].y += mouse_y_delta

            else:
                self.activeAndMouseDown = False

    def drawMinimiseButton(self):
        if self.x + self.width - self.titleBarHeight < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.titleBarHeight:
            pygame.draw.rect(screen, red, pygame.Rect((self.x + self.width - self.titleBarHeight, self.y), (self.titleBarHeight, self.titleBarHeight)))
            # Some code to debounce the button
            if mouseDown and not self.wasAlreadyClicked:
                self.maximised = not self.maximised
                self.wasAlreadyClicked = True
            if not mouseDown and self.wasAlreadyClicked:
                self.wasAlreadyClicked = False
        else:
            pygame.draw.rect(screen, white, pygame.Rect((self.x + self.width - self.titleBarHeight, self.y), (self.titleBarHeight, self.titleBarHeight)))
        pygame.draw.rect(screen, black, pygame.Rect((self.x + self.width - self.titleBarHeight, self.y), (self.titleBarHeight, self.titleBarHeight)), 2)


    def draw(self):
        if self.x < mouse_x < self.x + self.width - self.titleBarHeight and self.y < mouse_y < self.y + self.titleBarHeight:
            self.titleBarColour = light_green
            if mouseDown:
                self.activeAndMouseDown = True
        else:
            self.titleBarColour = white

        if self.maximised:
            self.drawTitleBar()
            pygame.draw.rect(screen, white, pygame.Rect((self.x, self.y), (self.width, self.height + self.titleBarHeight)))
            pygame.draw.rect(screen, black, pygame.Rect((self.x, self.y), (self.width, self.height + self.titleBarHeight)), 2)
            pygame.draw.rect(screen, self.titleBarColour, pygame.Rect((self.x, self.y), (self.width, self.titleBarHeight)))
            pygame.draw.rect(screen, black, pygame.Rect((self.x, self.y), (self.width, self.titleBarHeight)), 2)
            self.drawMinimiseButton()
            displayMessage(self.title, 20, self.x + 10, self.y + 5, dark_grey)
            for i in range(len(self.elements)):
                self.elements[i].draw()
        else:
            self.drawTitleBar()
            pygame.draw.rect(screen, self.titleBarColour, pygame.Rect((self.x, self.y), (self.width, self.titleBarHeight)))
            pygame.draw.rect(screen, black, pygame.Rect((self.x, self.y), (self.width, self.titleBarHeight)), 2)
            self.drawMinimiseButton()
            displayMessage(self.title, 20, self.x + 10, self.y + 5, dark_grey)

    def update(self):
        for i in range(len(self.elements)):
            self.elements[i].update()



class Label:  # A simple class version of the "displayMessage" function that can be added to a TabGroup
    def __init__(self, text, size, x, y, colour=black):
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.colour = colour

    def update(self):
        pass

    def draw(self):
        displayMessage(self.text, self.size, self.x, self.y, self.colour)


class Button:
    x = 0
    y = 0
    width = 0
    height = 0
    colour = 0
    text = ""
    mouseIsOn = False
    action = 0
    wasAlreadyClicked = False

    def __init__(self, text, x, y, width, height, colour, action, scale=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.action = action
        self.scale = scale  # Scale is used to change size of the text. A scale of 1 means the text will fit perfectly

        self.preRenderText()

    def preRenderText(self):
        # Calculates the text size needed to make the text fit inside the button
        font = pygame.font.SysFont(None, 50)
        text_width, text_height = font.size(self.text)
        size = int((self.height / (text_height + 20)) * 50 * self.scale)

        # Renders the text in the right size and gets the dimensions
        font = pygame.font.SysFont(None, size)
        self.text_image = font.render(self.text, True, black)
        self.text_width, self.text_height = font.size(self.text)

    def draw(self):
        # Checks if the mouse is hovering over the item
        if self.x < mouse_x < (self.x + self.width) and self.y < mouse_y < (self.y + self.height):
            self.mouseIsOn = True
            self.colour = light_blue

            # Some code to debounce the button
            if mouseDown and not self.wasAlreadyClicked:
                self.action(self)
                self.wasAlreadyClicked = True
            if not mouseDown and self.wasAlreadyClicked:
                self.wasAlreadyClicked = False

        else:
            self.mouseIsOn = False
            self.colour = white

        # Draws the containing box and then the text over it
        pygame.draw.rect(screen, self.colour, pygame.Rect((self.x, self.y), (self.width, self.height)))
        pygame.draw.rect(screen, black, pygame.Rect((self.x, self.y), (self.width, self.height)), 2)
        horizontal_centre = self.x + self.width / 2
        vertical_centre = self.y + self.height / 2
        screen.blit(self.text_image, (horizontal_centre - self.text_width / 2, vertical_centre - self.text_height / 2))

    def update(self):
        pass


class Slider:
    # Class constants
    knob_height = 22
    knob_width = 12

    # If the mouse goes down when it is hovering on the slider knob, this becomes true. This is so as long as the mouse
    # stays down, the slider will follow the mouse, even when the mouse moves outside the slider knob
    activeAndMouseDown = False

    def __init__(self, x, y, width, pos=0, function=None, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.pos = pos

        def linear(x):
            return x

        def nothing(slider):
            pass

        if function == None:
            self.function = linear
        else:
            self.function = function

        if action == None:
            self.action = nothing
        else:
            self.action = action

    def value(self,x=0):
        y = self.function(self.pos)
        return y

    def draw(self):
        # Knob constants
        kw = self.knob_width
        kh = self.knob_height

        pygame.draw.rect(screen, black, pygame.Rect((self.x, self.y - 1), (self.width, 2)))  # Slider line

        if self.activeAndMouseDown:
            if mouseDown:
                if mouse_x < self.x:
                    self.pos = 0
                elif mouse_x > (self.x + self.width):
                    self.pos = self.width
                else:
                    self.pos = mouse_x - self.x
                displayMessage(str(self.value()), 20, self.x, self.y + 20)
                self.action(self)
            else:
                self.activeAndMouseDown = False

        x_pos = self.pos + self.x

        # Outside border of slider knob
        pygame.draw.rect(screen, dark_grey, pygame.Rect((x_pos - kw / 2, self.y - kh / 2), (kw, kh)))

        # If the mouse is hovering over the slider knob
        if (x_pos + kw / 2) > mouse_x > (x_pos - kw / 2) and (self.y + kh / 2) > mouse_y > (self.y - kh / 2):
            # Draw the inside as light blue
            pygame.draw.rect(screen, light_blue, pygame.Rect((x_pos - 3, self.y - 8), (6, 16)))
            if mouseDown:
                self.activeAndMouseDown = True
        else:
            # Draw the inside as white
            pygame.draw.rect(screen, white, pygame.Rect((x_pos - 3, self.y - 8), (6, 16)))

    def update(self):
        pass

class Input:
    focused = False
    colour = pure_white

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = "0"
        self.renderText()

    def renderText(self):
        # Calculates the text size needed to make the text fit inside the button
        font = pygame.font.SysFont(None, 50)
        text_width, text_height = font.size(self.text)
        size = int((self.height / (text_height + 20)) * 50)

        # Renders the text in the right size and gets the dimensions
        font = pygame.font.SysFont(None, size)
        self.text_image = font.render(self.text, True, black)
        self.text_width, self.text_height = font.size(self.text)

    def changeText(self, text):
        self.text = text
        self.renderText()

    def update(self):
        pass

    def draw(self):
        if self.x < mouse_x < (self.x + self.width) and self.y < mouse_y < (self.y + self.height):
            self.colour = light_grey
        else:
            self.colour = white

        if mouseDown:
            if self.x < mouse_x < (self.x + self.width) and self.y < mouse_y < (self.y + self.height):
                self.focused = True
            else:
                self.focused = False

        if self.focused == True:
            self.colour = yellow
            input = checkNumberInput()
            self.text += input
            if not input == "": # If there was any input, render the text again
                self.renderText()
            if checkBackspace() == True:
                self.text = self.text[:-1]
                self.renderText()
        pass

        pygame.draw.rect(screen, self.colour, pygame.Rect((self.x, self.y), (self.width, self.height)))
        pygame.draw.rect(screen, black, pygame.Rect((self.x, self.y), (self.width, self.height)), 3)
        horizontal_centre = self.x + self.width / 2
        vertical_centre = self.y + self.height / 2
        screen.blit(self.text_image, (horizontal_centre - self.text_width / 2, vertical_centre - self.text_height / 2))


class Graph:  # Interface element that allows small graphs to be easily drawn
    x_count = 0
    # y_values = []

    def __init__(self, x, y, width, height, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = function

        self.y_values = []
        pass

    def draw(self):
        self.colour = green

        # Draws the axis
        pygame.draw.line(screen, black, (self.x - 20, self.y + self.height),
                         (self.x + self.width, self.y + self.height))
        pygame.draw.line(screen, black, (self.x, self.y), (self.x, self.y + self.height + 5))

        values = []

        # If the number of y_values exceeds the graph width...
        if len(self.y_values) > self.width:
            values = self.y_values[-self.width:]
        else:
            values = self.y_values

        for i in range(len(values)):
            # Calculates where the points should be on screen
            x_coord = i + self.x + 1
            y_coord = self.y + self.height - values[i]
            # Plots the data
            if mouse_x == x_coord:  # If the mouse is hovering over a value
                pygame.draw.line(screen, red, (x_coord, self.y + self.height - 1), (x_coord, y_coord))
                # Display the coordinates of the matching value
                value = (i, int(values[i]))
                displayMessage(str(value), 20, self.x, self.y + self.height + 10, black)
            else:
                pygame.draw.line(screen, self.colour, (x_coord, self.y + self.height - 1), (x_coord, y_coord))

    def update(self):
        x = self.x_count
        y = self.function(x)

        if y > self.height:  # If the calculated points exceed the graph height
            y = self.height
            colour = red  # Plot red, to show the graph has been truncated
        else:
            colour = green

        self.y_values.append(y)

        self.x_count += 1


class Force:
    x = 0
    y = 0
    x_global = 0
    y_global = 0
    name = ""
    angle = 0
    magnitude = 0

    def __init__(self, name, x, y, angle, magnitude):
        self.name = name
        self.x = x
        self.y = y
        self.angle = angle
        self.magnitude = magnitude


class Platform:
    x = 0
    y = 0
    width = 0
    height = 0

    colour = green

    top_left = (0, 0)
    top_right = (0, 0)
    bottom_left = (0, 0)
    bottom_right = (0, 0)

    type = Object.platform

    def __init__(self, x, y, width, height, name=""):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        # Calculates the vertex coordinates
        self.top_left = (x - width / 2, y - height / 2)
        self.top_right = (x + width / 2, y - height / 2)
        self.bottom_left = (x - width / 2, y + height / 2)
        self.bottom_right = (x + width / 2, y + height / 2)

    def draw(self):
        pygame.draw.line(screen, self.colour, self.top_left, self.top_right)
        pygame.draw.line(screen, self.colour, self.top_right, self.bottom_right)
        pygame.draw.line(screen, self.colour, self.top_left, self.bottom_left)
        pygame.draw.line(screen, self.colour, self.bottom_left, self.bottom_right)

        # vert = [self.top_left, self.top_right, self.bottom_left, self.bottom_right]
        # print(vert)
        pass

    def update(self):
        pass


class Oblong:
    initial_values = None

    mass = 1

    colour = black

    type = Object.oblong

    # forces = []

    # Object points
    top_left = (0, 0)
    top_right = (0, 0)
    bottom_left = (0, 0)
    bottom_right = (0, 0)
    vertices = []

    def __init__(self, x, y, width, height, angle=0, name=""):
        self.name = name  # This should never change
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.forces = []

        self.x_vel = 0
        self.y_vel = 0
        self.x_acc = 0
        self.y_acc = 0

        self.ang_vel = 1  # Radians per second?
        self.ang_acc = 0
        self.moi = 1  # Moment of inertia

        # The angle is taken in degrees, but must be stored in radians
        self.angle = angle * (pi / 180)

        # Calculates the vertex coordinates
        self.top_left = (x - width / 2, y - height / 2)
        self.top_right = (x + width / 2, y - height / 2)
        self.bottom_left = (x - width / 2, y + height / 2)
        self.bottom_right = (x + width / 2, y + height / 2)
        self.rotateObject(self.angle)

        # Adds a force to the object to represent weight
        self.forces.append(Force("weight", 0, 0, -90, self.mass * g / 10))

        # Stores the initial state, so if the object needs to be reset, the starting values can be recalled
        self.storeInitialValues()

    def storeInitialValues(self):
        initial_values = {"name": self.name,
                          "x": self.x,
                          "y": self.y,
                          "height": self.height,
                          "width": self.width,
                          "x_vel": self.x_vel,
                          "y_vel": self.y_vel,
                          "x_acc": self.x_acc,
                          "y_acc": self.y_acc,
                          "ang_vel": self.ang_vel,
                          "ang_acc": self.ang_acc,
                          "moi": self.moi,
                          "angle": self.angle,
                          "forces": self.forces[:]}

        self.initial_values = initial_values

    def reset(self):
        ivs = self.initial_values

        self.name = ivs["name"]
        self.x = ivs["x"]
        self.y = ivs["y"]
        self.height = ivs["height"]
        self.width = ivs["width"]
        self.x_vel = ivs["x_vel"]
        self.y_vel = ivs["y_vel"]
        self.x_acc = ivs["x_acc"]
        self.y_acc = ivs["y_acc"]
        self.ang_vel = ivs["ang_vel"]
        self.ang_acc = ivs["ang_acc"]
        self.moi = ivs["moi"]
        self.angle = ivs["angle"]
        self.forces = ivs["forces"][:]

        # Calculates the vertex coordinates
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        self.top_left = (x - width / 2, y - height / 2)
        self.top_right = (x + width / 2, y - height / 2)
        self.bottom_left = (x - width / 2, y + height / 2)
        self.bottom_right = (x + width / 2, y + height / 2)
        self.rotateObject(self.angle)

    def vertices(self):
        v = [self.top_left, self.top_right, self.bottom_right, self.bottom_left]
        return v

    def checkCollisions(self):
        # self.colour = black
        v = [self.top_left, self.top_right, self.bottom_right, self.bottom_left, self.top_left]

        # "objects" is a list that contains all of the world objects
        # This checks through the list to see if this object has collided with another object
        for o in objects:

            if o.name == self.name:  # If the next object is itself, skip it
                continue
            if o.type == Object.platform or o.type == Object.oblong:
                object_v = [o.top_left, o.top_right, o.bottom_right, o.bottom_left, o.top_left]

                for j in range(4):  # Four edges for platforms and oblongs. Represents the object being intersected with
                    intersections = []

                    for i in range(4):  # One for each edge. Represents this object
                        intersects = checkIntersection(v[i], v[i + 1], object_v[j], object_v[j + 1])

                        if intersects:
                            vrtx = [roundPoint(v[i]), roundPoint(v[i + 1]), roundPoint(object_v[j]),
                                    roundPoint(object_v[j + 1])]
                            intersections.append(True)

                            if highlight_intersections == True:
                                pygame.draw.line(screen, bright_red, v[i], v[i + 1])
                                pygame.draw.line(screen, bright_green, object_v[j], object_v[j + 1])
                        else:
                            intersections.append(False)
                            pass
                        pass

                    intersections.append(intersections[0])
                    for i in range(4):
                        if intersections[i] and intersections[
                                    i + 1]:  # If two adjacent lines intersect with an outside edge
                            normal = calculateNormal(object_v[j], object_v[j + 1])
                            x = v[i + 1][0]
                            y = v[i + 1][1]
                            self.addForce("reaction", x, y, -normal, g)

    def resolveMoments(self):
        # Resolves moments
        # self.ang_acc = 0

        for force in self.forces:
            # If the force is at the origin, there is no moment
            # This is to avoid doing getAngle(0,0), which will try and divide by zero
            if not (force.x == 0 and force.y == 0):
                l = math.sqrt(force.x ** 2 + force.y ** 2) / metre
                l_angle = getAngle(force.x, force.y)
                angle = (l_angle - force.angle - 90) / 180 * pi
                moment = l * force.magnitude * math.cos(angle) / self.moi
                self.ang_acc += moment
            pass

    def res(self):
        # Resolves forces
        self.y_acc = 0
        self.x_acc = 0

        for force in self.forces:
            # Angles need to be converted to radians first
            s = -math.sin(force.angle / 180 * pi)
            c = math.cos(force.angle / 180 * pi)

            y = (force.magnitude * s) / self.mass
            x = (force.magnitude * c) / self.mass

            self.y_acc += y
            self.x_acc += x
        pass

    def move(self, time=frame_time):
        # After forces are resolved, resolve kinematics.
        x = 0
        y = 0
        self.y_vel += self.y_acc * time
        self.x_vel += self.x_acc * time
        y = (self.y_vel * time) * metre
        x = (self.x_vel * time) * metre

        self.y += y
        self.x += x
        self.top_left = (self.top_left[0] + x, self.top_left[1] + y)
        self.top_right = (self.top_right[0] + x, self.top_right[1] + y)
        self.bottom_left = (self.bottom_left[0] + x, self.bottom_left[1] + y)
        self.bottom_right = (self.bottom_right[0] + x, self.bottom_right[1] + y)

        # Resolve rotational motion
        self.ang_vel += self.ang_acc * time
        d_angle = self.ang_vel * time
        self.angle += d_angle
        self.rotateObject(d_angle)
        pass

    def addForce(self, name, x, y, angle, magnitude):
        self.forces.append(Force(name, x, y, angle, magnitude))
        pass

    def removeForce(self, name):
        pass

    def rotatePoint(self, point, centre, angle):
        # Gives the point relative to the object centre
        x = point[0] - self.x - centre[0]
        y = point[1] - self.y - centre[1]

        s = math.sin(angle)
        c = math.cos(angle)

        # Matrix formula for rotation
        xnew = x * c - y * s
        ynew = x * s + y * c

        x = self.x + xnew + centre[0]
        y = self.y + ynew + centre[1]
        return (x, y)

    def rotateObject(self, angle):
        self.top_left = self.rotatePoint(self.top_left, origin, angle)
        self.top_right = self.rotatePoint(self.top_right, origin, angle)
        self.bottom_left = self.rotatePoint(self.bottom_left, origin, angle)
        self.bottom_right = self.rotatePoint(self.bottom_right, origin, angle)
        pass

    def update(self):
        self.res()
        self.resolveMoments()
        self.move()
        self.checkCollisions()
        pass

    def draw(self):
        # origin = (300,200)
        v = [self.top_left, self.top_right, self.bottom_right, self.bottom_left, self.top_left]

        # Draws the edges clockwise, starting from the top left corner
        pygame.draw.line(screen, self.colour, self.top_left, self.top_right)
        pygame.draw.line(screen, self.colour, self.top_right, self.bottom_right)
        pygame.draw.line(screen, self.colour, self.top_left, self.bottom_left)
        pygame.draw.line(screen, self.colour, self.bottom_left, self.bottom_right)

        # Calculates and draws the normals for each edge
        if draw_normals == True:
            for i in range(4):
                normal = degToRad(calculateNormal(v[i], v[i + 1]))
                mid = midpoint(v[i], v[i + 1])
                pygame.draw.line(screen, red, mid, addPoint(mid, (20 * math.cos(normal), -20 * math.sin(normal))))
                pass

        if draw_coordinates == True:
            vertices = [self.top_left, self.top_right, self.bottom_right, self.bottom_left]
            for v in vertices:
                displayMessage(str(roundPoint(v)), 15, v[0], v[1], red)

        if draw_suvat == True:
            a = roundPoint((self.x_acc, self.y_acc), 2)
            v = roundPoint((self.x_vel, self.y_vel), 2)
            s = roundPoint((self.x, self.y))

            displayMessage(str(s), 20, self.x, self.y - 15, red)
            displayMessage("a: " + str(a), 20, self.x, self.y, blue)
            displayMessage("v: " + str(v), 20, self.x, self.y + 15, blue)
            # displayMessage("a.y: " + str(self.y_acc), 15, self.x, self.y + 60, blue)

        if draw_angular == True:
            displayMessage("angle: " + str(round(self.angle, 2)), 20, self.x, self.y + 35, green)
            displayMessage("ang_vel: " + str(round(self.ang_vel, 2)), 20, self.x, self.y + 50, green)
            displayMessage("ang_acc: " + str(round(self.ang_acc, 2)), 20, self.x, self.y + 65, green)

        if draw_forces == True:
            for i, f in enumerate(self.forces):
                origin = (self.x, self.y)
                direction = f.angle
                magnitude = f.magnitude * 20
                drawForce(origin, direction, magnitude)
                displayMessage("ang: " + str(round(direction, 2)), 20, self.x - 80, self.y + 15 * i, purple)
                if debug:
                    print("Object " + self.name + " has " + str(len(self.forces)) + " forces: " + str(self.forces))


box = Oblong(300, 200, 200, 80, 0, "main")
box.addForce("horiz", 20, 20, 0, 0)
objects.append(box)

for i in range(3):
    objects.append(Oblong(150 + 150 * i, 400, 50, 100, i * 20, "box" + str(i)))
    pass

floor = Platform(400, 700, 800, 60, "floor")
celing = Platform(400, 60, 800, 60, "celing")
left = Platform(30, 350, 60, 700, "left")
right = Platform(760, 350, 60, 700, "right")
# objects.append(left)
# objects.append(right)
# objects.append(celing)
objects.append(floor)


def linear(x):
    return x


def squared(x):
    y = 0.01 * x ** 2
    return y


def exp(x):
    y = 0.01 * math.e ** (x * 0.1)
    return y


def sin(x):
    y = 50 * (math.sin(degToRad(3 * x)) + 1)
    return y


def ln(x):
    y = 20 * math.log(x / 20 + 0.000001)
    return y


def box_y(x):
    return (objects[0].y_acc)


def sins(x):
    x = degToRad(2 * x)
    y = math.sin(x) + math.sin(2 * x) + math.sin(3 * x) + math.sin(4 * x) + math.sin(5 * x) + 5
    y = 5 * y
    return y


def noOfForces(x):
    return (3 * len(objects[0].forces))


def pause(button):
    global running
    running = not running


def doNothing(button):
    pass


def exit(button):
    pygame.quit()
    quit()


def reInit(button):
    global screen
    global display_width
    display_width += 100
    screen = pygame.display.set_mode((display_width, display_height))


def resetAll(button):
    global objects
    for o in objects:
        if o.type == Object.oblong:
            o.reset()


def toggleNormals(button):
    global draw_normals
    draw_normals = not draw_normals


def toggleCoordinates(button):
    global draw_coordinates
    draw_coordinates = not draw_coordinates


def toggleSuvat(button):
    global draw_suvat
    draw_suvat = not draw_suvat


def toggleAngular(button):
    global draw_angular
    draw_angular = not draw_angular


def toggleAll(button):
    toggleNormals(button)
    toggleCoordinates(button)
    toggleSuvat(button)
    toggleAngular(button)
    toggleForces(button)


def toggleForces(button):
    global draw_forces
    draw_forces = not draw_forces


def toggleDebug(button):
    global debug
    debug = not debug

def changeX(slider):
    input_x.changeText(str(slider.value()))

def changeY(slider):
    input_y.changeText(str(slider.value()))

def changeWidth(slider):
    input_width.changeText(str(slider.value()))

def changeHeight(slider):
    input_height.changeText(str(slider.value()))

def addOblong(button):
    x = int(input_x.text)
    y = int(input_y.text)
    width = int(input_width.text)
    height = int(input_height.text)
    oblong = Oblong(x,y,width,height)
    objects.append(oblong)

def x5(x):
    return(5*x)

def moveEverything(time):
    for o in objects:
        if o.type == Object.oblong:
            o.res()
            o.resolveMoments()
            o.move(time)
            o.checkCollisions()

def moveabit(button):
    moveEverything(0.1)

slidervalue = 0

def moveObjects(slider):
    global slidervalue
    delta = slider.value() - slidervalue
    time = delta / 40
    moveEverything(time)
    slidervalue = slider.value()

graph = Graph(950, 50, 150, 150, sin)
box_graph = Graph(950, 250, 230, 60, noOfForces)
sins_graph = Graph(950, 320, 230, 75, sins)
btn_pause = Button("Pause", 1100, 30, 150, 40, black, pause)
btn_exit = Button("Exit", 1100, 90, 150, 40, black, exit)
btn_reinit = Button("Reinitialise", 1100, 150, 150, 40, black, reInit)
btn_normals = Button("Toggle Normals", 1100, 210, 150, 30, black, toggleNormals)
btn_coords = Button("Toggle Coordinates", 1100, 270, 150, 30, black, toggleCoordinates)
btn_suvat = Button("Toggle SUVAT", 1100, 330, 150, 30, black, toggleSuvat)
btn_reset = Button("Reset Oblongs", 1100, 390, 150, 30, black, resetAll)
btn_angular = Button("Toggle Angular", 1100, 450, 150, 30, black, toggleAngular)
btn_toggleall = Button("Toggle All", 1100, 510, 150, 30, black, toggleAll)
btn_toggleforces = Button("Toggle Forces", 1100, 570, 150, 30, black, toggleForces)
btn_toggledebug = Button("Toggle Debug", 1100, 630, 150, 30, black, toggleDebug)
btn_move = Button("Move", 1100, 700, 150, 30, black, moveEverything)
slider_test = Slider(950, 700, 150, 0, linear)
slider_move = Slider(20, 740, 700, 0, None, moveObjects)
slider_graph = Graph(950, 420, 230, 200, slider_test.value)

main = TabGroup("Main")
main.addItem(btn_pause)
main.addItem(btn_exit)
main.addItem(btn_reinit)
main.addItem(btn_normals)
main.addItem(btn_coords)
main.addItem(btn_suvat)
main.addItem(btn_reset)
main.addItem(btn_angular)
main.addItem(btn_toggleall)
main.addItem(btn_toggleforces)
main.addItem(btn_toggledebug)
#main.addItem(btn_move)
main.addItem(slider_move)

graphs = TabGroup("Graphs")
graphs.addItem(graph)
graphs.addItem(box_graph)
graphs.addItem(sins_graph)
graphs.addItem(slider_graph)
graphs.addItem(slider_test)

new = TabGroup("New")
label_x = Label("X: ", 30, 970, 203, black)
label_y = Label("Y: ", 30, 970, 253, black)
input_x = Input(1000, 200, 50, 25)
input_y = Input(1000, 250, 50, 25)
slider_x = Slider(1070, 215, 170, 0, x5, changeX)
slider_y = Slider(1070, 265, 170, 0 ,x5, changeY)
label_width = Label("Width: ", 30, 930, 403, black)
label_height = Label("Height: ", 30, 923, 453, black)
input_width = Input(1000, 400, 50, 25)
input_height = Input(1000, 450, 50, 25)
slider_width = Slider(1070, 415, 170, 0, None, changeWidth)
slider_height = Slider(1070, 465, 170, 0 ,None, changeHeight)
btn_place = Button("Place Box", 1000, 600, 200, 40, black, addOblong)
new.addItem(label_x)
new.addItem(label_y)
new.addItem(input_x)
new.addItem(input_y)
new.addItem(slider_x)
new.addItem(slider_y)
new.addItem(label_width)
new.addItem(label_height)
new.addItem(input_width)
new.addItem(input_height)
new.addItem(slider_width)
new.addItem(slider_height)

new.addItem(btn_place)

tabs.append(main)
tabs.append(graphs)
tabs.append(new)

first = Window("Test", 700, 300, 200, 200)
slider_window = Slider(20,20, 100)
btn_window = Button("Pause", 20, 50, 100, 30, black, pause)
input_window = Input(20, 95, 75, 25)
graph_window = Graph(30, 130, 150, 50, sins)
first.addItem(slider_window)
first.addItem(btn_window)
first.addItem(input_window)
first.addItem(graph_window)
#elements.append(first)

toggle = Window("Toggle", 720, 300, 150, 300)
btn_normals = Button("Normals", 10, 10, 130, 25, black, toggleNormals)
btn_coords = Button("Corner Coords", 10, 45, 130, 25, black, toggleCoordinates)
btn_suvat = Button("SUVAT", 10, 80, 130, 25, black, toggleSuvat)
btn_angular = Button("Angular", 10, 115, 130, 25, black, toggleAngular)
btn_toggleall = Button("All", 10, 150, 130, 25, black, toggleAll)
btn_toggleforces = Button("Forces", 10, 185, 130, 25, black, toggleForces)
btn_toggledebug = Button("Debug Mode", 10, 220, 130, 25, black, toggleDebug)
toggle.addItem(btn_normals)
toggle.addItem(btn_coords)
toggle.addItem(btn_suvat)
toggle.addItem(btn_angular)
toggle.addItem(btn_toggleall)
toggle.addItem(btn_toggleforces)
toggle.addItem(btn_toggledebug)
elements.append(toggle)

# For each TabGroup added to the "tabs" array, a Button is made and added to the "tab_buttons" array
for i, t in enumerate(tabs):
    def action(button):
        global currentTab
        currentTab = button.text

    x = viewport_width + 5 + i * 80
    btn = Button(t.name, x, 0, 80, 40, black, action, 0.8)
    tab_buttons.append(btn)

currentTab = tabs[0].name

print(objects)

pygame.draw.rect(screen, white, pygame.Rect((0, 0), (display_width, display_height)))

while True:
    # Refreshes the rendering area with a white rectangle
    # pygame.draw.rect(screen, white, pygame.Rect((0, 0), (850, display_height)))
    pygame.draw.rect(screen, white, pygame.Rect((0, 0), (display_width, display_height)))

    last_events = events
    events = pygame.event.get()
    for event in events:  # Gets any events that happens

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # If the left mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
            if event.button == 4:
                print("Scrolling up")
            if event.button == 5:
                print("Scrolling down")

        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

        # If the user presses a key...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_p:
                pause(None)
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

        # If the user releases a key...
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass

    mouse_x_last = mouse_x
    mouse_y_last = mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x_delta = mouse_x - mouse_x_last
    mouse_y_delta = mouse_y - mouse_y_last

    # drawGridlines()

    # Interface elements drawn here
    # pygame.draw.rect(screen, black, pygame.Rect((viewport_width, 0), (5, display_height)))
    pygame.draw.rect(screen, light_grey,
                     pygame.Rect((viewport_width, 0), (display_width - viewport_width, display_height)))
    for t in tab_buttons:
        t.draw()

    for t in tabs:
        if t.name == currentTab:
            t.draw()
        if running:
            t.update()

    for e in elements:
        if running:
            e.update()
        e.draw()


    # Objects are drawn here
    for o in objects:
        if running:
            o.update()
        o.draw()
    # floor.draw()

    # Messages and labels drawn here
    displayMessage("Experimental Physics Engine by Rahul Jhuree", 40, 0, 0, black)
    displayMessage("FPS: " + str(round(clock.get_fps(), 1)), 40, 0, 40, black)
    #drawNumber(int(clock.get_fps()), 20, 20, black, size3)
    # displayMessage("a = " + str(round(box.y_acc, 2)), 30, 900, 20, black)
    # displayMessage("v = " + str(round(box.y_vel, 2)), 30, 900, 50, black)
    # displayMessage("y = " + str(round(box.y / metre, 0)), 30, 900, 80, black)
    # displayMessage("angle = " + str(round(box.angle * 180 / pi, 0)), 30, 900, 110, black)
    # displayMessage("ang_vel = " + str(round(box.ang_vel * 180 / pi, 1)), 30, 900, 140, black)
    # displayMessage("ang_acc = " + str(round(box.ang_acc, 1)), 30, 900, 170, black)
    # drawNumber(31415926535,200,200)
    displayMessage(output, 40, 0, 700, black)

    # Update the display and tick the clock
    pygame.display.update()
    clock.tick()
    frame_count += 1
    if debug:
        print("End of frame")
        # time.sleep(0.2)

print("")
print("Reached end of program")
input("")
