""" 9000 series system status screen display engine """
import random
import time
import pygame

# Init pygame
pygame.init()
# get screen res
screentraits = pygame.display.Info()
wres = screentraits.current_w
hres = screentraits.current_h
screen = pygame.display.set_mode([wres, hres])
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
sysstrings = ('COM', 'VEH', 'NAV', 'GDE', 'CNT', 'NUC', 'ATM', 'HIB', 'DMG', 'FLX', 'LIF', 'MEM', 'DMC')
sysbgcolors = ('purple', 'darkblue', 'darkblue', 'navy', 'green', 'darkblue', 'red', 'green', 'brightred', 'navy', 'red', 'blue', 'burgundy')
sysentry = 0


def sub_text():
    """ generate random subtext """
    tlb1 = random.choice(string.ascii_uppercase)
    tlb2 = random.choice(string.ascii_uppercase)
    tlb3 = random.choice(string.ascii_uppercase)
    ftl1 = random.choice(string.hexdigits)
    ftl2 = random.choice(string.hexdigits)
    stl1 = random.choice(string.hexdigits)
    stl2 = random.choice(string.hexdigits)
    sub_string = tlb1 + tlb2 + tlb3 + ": " + ftl1 + ftl2 + " - " + stl1 + stl2
    return sub_string


def set_bgcolor(bgcolor):
    """ fill the screen with a color. """
    pygame.display.flip()
    screen.fill(bgcolor)
    pygame.display.update()

def add_text(text_string, text_color):
    """ write the text to display. """
    font = pygame.font.SysFont("moki", 128, bold=True)
#    font = pygame.font.Font(None, 55)
    text = font.render(text_string, True, text_color)
    text_rect = text.get_rect(center=(int(wres / 2), int(hres / 2)))
    screen.blit(text, text_rect)
    pygame.display.update()

def add_subtext(text_string, text_color):
    """ add sub-text to display. """
    st = sub_text

               
while True:
    next_sys = random.random(0,12)
    if next_sys == sysentry:
        next_sys = sysentry + 1
    sysitem = sysstrings[next_sys]
    syscolor = sysbgcolors[next_sys]
    set_bgcolor(syscolor)
    add_text(sysitem, 'white')
    add_subtext()
    display_time = random.random(0,15) + min_time
    time.sleep(display_time)