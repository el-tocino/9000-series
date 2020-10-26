""" 9000 series system status screen display engine """
import random
import time
import pygame

# Init pygame
pygame.init()
#pi 5" display
#screen = pygame.display.set_mode([800, 480])
# testing screen
screen = pygame.display.set_mode([1920, 1080])
## set various colors
white = [255, 255, 255]
red = [255, 0, 0]
brightred = [170, 1, 20]
blue = [51, 51, 255]
green = [0, 255, 0]
yellow = [255, 250, 25]
black = [0, 0, 0]
burgundy = [128, 0, 32]
navy = [0, 0, 153]
purple = [153, 51, 102]
darkblue = [0, 0, 139]
min_time = 5
sysstrings = (COM, VEH, NAV, GDE, CNT, NUC, ATM, HIB, DMG, FLX, LIF, MEM, DMC)
sysbgcolors = ('purple', 'darkblue', 'darkblue', 'navy', 'green', ','darkblue', 'red', 'green', 'brightred', 'navy', 'red', 'blue', 'burgundy')
sysentry = 0


def sub_text():
    """ generate random subtext """
    tlb = random.choices(string.ascii_uppercase, 3)
    ftl = random.choices(string.hexdigits, 2)
    stl = random.choices(string.hexdigits, 2)
    sub_string = tlb + ": " + ftl + " - " + stl
    return sub_string


def set_bgcolor(bgcolor):
    """ fill the screen with a color. """
    pygame.display.flip()
    screen.fill(bgcolor)
    pygame.display.update()


def add_text(text_string, text_color):
    """ write the text to display. """
    font = pygame.font.Font(None, 55)
    text = font.render(text_string, True, text_color)
    text_rect = text.get_rect(center=(960, 540))
    screen.blit(text, text_rect)
    pygame.display.update()


white True:
    next_sys = random.random(0,12)
    if next_sys == sysentry:
        next_sys = sysentry + 1
    

