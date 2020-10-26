""" 9000 series system status screen display engine """
#!python3
import random
import string
import time
import pygame

# Init pygame
pygame.init()
# get screen res
screentraits = pygame.display.Info()
wres = screentraits.current_w
hres = screentraits.current_h
screen = pygame.display.set_mode([wres, hres])
white = [200, 200, 200]
#red = '#950000'
#brightred = '#aa0114'
#blue = '#3333ff'
#green = '#006600'
#burgundy = '#800020'
#navy = '#000099'
#purple = '#993366'
#darkblue = '#00008b'
min_time = 5
sysstrings = ('COM', 'VEH', 'NAV', 'GDE', 'CNT', 'NUC', 'ATM', 'HIB', 'DMG',
              'FLX', 'LIF', 'MEM', 'DMC')
sysbgcolors = ('#993366', '#00008b', '#00008b', '#000099', '#006600', '#00008b',
               '#950000', '#006600', '#aa0114', '#000099', '#950000', '#3333ff', '#800020')

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
    sub_string = tlb1 + tlb2 + tlb3 + ": " + ftl1 + ftl2 + " - " + stl1 + stl2
    return str(sub_string)

def set_bgcolor(bgcolor):
    """ fill the screen with a color. """
    pygame.display.flip()
    screen.fill(pygame.Color(bgcolor))
    pygame.display.update()

def add_text(text_string):
    """ write the text to display. """
    font = pygame.font.SysFont("moki", int(wres / 8), bold=True)
    text = font.render(text_string, True, white)
    text_rect = text.get_rect(center=(int(wres / 2), int(hres / 2 + (wres / 40))))
    screen.blit(text, text_rect)
    pygame.display.update()

def add_subtext():
    """ add sub-text to display. """
    st = sub_text()
    font = pygame.font.SysFont("moki", int(wres / 64), bold=True)
    text = font.render(st, True, white)
    text_rect = text.get_rect(center=(int(wres / 5), int(hres / 2 - (wres / 20))))
    screen.blit(text, text_rect)
    pygame.display.update()

while True:
    next_sys = random.randint(0, 12)
    if next_sys == sysentry:
        next_sys = sysentry + 1
    sysitem = sysstrings[next_sys]
    set_bgcolor(sysbgcolors[next_sys])
    print(sysbgcolors[next_sys])
    sep = " "
    add_text(sep.join(sysitem))
    add_subtext()
    display_time = random.randint(0, 15) + min_time
    time.sleep(display_time)
