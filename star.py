# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:16:10 2017

@author: m0rningstar
"""

from psychopy.visual import Window, Circle, ImageStim
from psychopy.event import Mouse
from psychopy.core import wait
from random import shuffle

from speller_config import *

def draw_group(stimuli):
    for stimulus in stimuli:
        stimulus.draw()

groups=[('A','J','S'), ('B', 'K', 'T'), ('C','L','U'), ('D', 'M', 'V'), ('E', 'N','V'),
        ('F','O','X'), ('G', 'P', 'V'), ('H', 'Q', 'Z'), ('I', 'R', 'star'),
        ('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', 'I'), ('J', 'K', 'L'), ('M', 'N', 'O'),
        ('P', 'Q', 'R'), ('S', 'T', 'U'), ('V','W','X'), ('Y', 'Z', 'star'),
        ('A', 'D','G'), ('B', 'E','H'), ('G', 'F', 'I'), ('J','M','P'), ('K','N','Q'),
        ('L', 'O','R'), ('S', 'V','Y'), ('T','W','Z'), ('U','X','star')] # 'RC' stimuli groups

groups.extend(TRIALREPEATS*groups)
shuffle(groups)

disp=Window(size=SIZE, monitor=MON, units='deg', color=BACKCOL, fullscr=True)

mouse=Mouse()

fixmark=Circle(disp, radius=0.05 ,edges=32, pos=CENTER, lineColor=FIXCOL)

images = []

for item in CIRCLES.keys():
    image=ImageStim(disp, image=CIRCLES[item][1], pos=CIRCLES[item][0], size=CIRCLES[item][3])
    images.append(image)

fixmark.draw()
draw_group(images)
disp.flip()

while True:
    button=mouse.getPressed()
    if button[0]:
        break

for item in groups:
    flashes=[]
    for i in item:
        flash=ImageStim(disp, image=CIRCLES[i][2], pos=CIRCLES[i][0], size=CIRCLES[i][3])
        flashes.append(flash)
    fixmark.draw()
    draw_group(images)
    draw_group(flashes)
    disp.flip()
    wait(FLASH)

disp.close()