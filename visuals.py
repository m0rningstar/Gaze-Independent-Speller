# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:16:10 2017

@author: m0rningstar
"""

from psychopy.visual import Window, Circle, ImageStim
from psychopy.event import Mouse
from psychopy.core import wait
from random import shuffle

from visuals_config import *

def draw_group(stimuli):
    for stimulus in stimuli:
        stimulus.draw()

def create_stim_sequence(block1, block2, block3, repeats):
    seq=[]
    for i in range(repeats):
        g=create_groups(BLOCK1, BLOCK2, BLOCK3)
        seq+=g
    return seq
    
def main():
    groups=create_stim_sequence(BLOCK1, BLOCK2, BLOCK3, TRIALREPEATS)
    print groups
    
    disp=Window(size=SIZE, monitor=MON, units='deg', color=BACKCOL, screen =1, fullscr=True)
    
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
        fixmark.draw()
        draw_group(images)
        wait(PAUSE)
        disp.flip()

    disp.close()


main()