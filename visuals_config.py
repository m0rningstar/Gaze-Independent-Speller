# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 14:05:14 2017

@author: m0rningstar
"""
import os
from psychopy.monitors import Monitor

DIR = os.getcwd() 

FLASH=0.050 # duration of flash, s
PAUSE=0.100
TRIALREPEATS = 2 # cycles of flashes
SIZE=(1680,1050)# resolution    (1280,720)
CENTER=(0,0) # fixmark coordinates, deg
DISTANCE=75 # distance between subject and screen, cm
WIDTH= 47.4 # screen width , cm    (31)
#STIMSIZE= [0.4, 1.0, 2.0] # size of stimuli, deg
LETTERSIZE= [0.8, 1.85, 3.3] # size of letter images, deg

MON = Monitor('Dell') 
MON.setWidth(WIDTH) 
MON.setDistance(DISTANCE)
MON.setSizePix(SIZE)

BACKCOL=(-0.5,-0.5,-0.5) #background color
FIXCOL=(1,1,1) #fixation mark color

C1=[(0,-1.500), (-0.964,-1.149), (-1.477,-0.260), (-1.299,0.750), (-0.513,1.410), 
    (0.513,1.410), (1.299,0.750), (1.477,-0.260), (0.964,-1.149)] # coordinates of inner circle, deg
C2=[(0,3.500),(2.250,2.681),(3.447,0.608),(3.031,-1.750),(1.197,-3.289),
    (-1.197,-3.289),(-3.031,-1.750),(-3.447,0.608),(-2.250,2.681)] # coordinates of middle circle, deg
C3=[(0,-7.000), (-4.500,-5.362), (-6.894,-1.216), (-6.062,3.500), (-2.394,6.578),
    (2.394,6.578), (6.062,3.500), (6.894,-1.216), (4.500,-5.362)] # coordinates of outer circle, deg


CIRCLES={'J':[C1[0], (DIR+r'\Stimuli\10-0.png'), (DIR+r'\Stimuli\10-1.png'), LETTERSIZE[0]], 
              'V':[C1[1], (DIR+r'\Stimuli\22-0.png'), (DIR+r'\Stimuli\22-1.png'), LETTERSIZE[0]], 
              'P':[C1[2], (DIR+r'\Stimuli\16-0.png'), (DIR+r'\Stimuli\16-1.png'), LETTERSIZE[0]], 
              'U':[C1[3], (DIR+r'\Stimuli\21-0.png'), (DIR+r'\Stimuli\21-1.png'), LETTERSIZE[0]], 
              'G':[C1[4], (DIR+r'\Stimuli\7-0.png'), (DIR+r'\Stimuli\7-1.png'), LETTERSIZE[0]], 
              'Y':[C1[5], (DIR+r'\Stimuli\25-0.png'), (DIR+r'\Stimuli\25-1.png'), LETTERSIZE[0]],
              'X':[C1[6], (DIR+r'\Stimuli\24-0.png'), (DIR+r'\Stimuli\24-1.png'), LETTERSIZE[0]], 
              'Z':[C1[7], (DIR+r'\Stimuli\26-0.png'), (DIR+r'\Stimuli\26-1.png'), LETTERSIZE[0]], 
              'star':[C1[8], (DIR+r'\Stimuli\27-0.png'), (DIR+r'\Stimuli\27-1.png'), LETTERSIZE[0]],
              'F':[C2[0], (DIR+r'\Stimuli\6-0.png'), (DIR+r'\Stimuli\6-1.png'), LETTERSIZE[1]], 
              'B':[C2[1], (DIR+r'\Stimuli\2-0.png'), (DIR+r'\Stimuli\2-1.png'), LETTERSIZE[1]], 
              'N':[C2[2], (DIR+r'\Stimuli\14-0.png'), (DIR+r'\Stimuli\14-1.png'), LETTERSIZE[1]], 
              'M':[C2[3], (DIR+r'\Stimuli\13-0.png'), (DIR+r'\Stimuli\13-1.png'), LETTERSIZE[1]], 
              'R':[C2[4], (DIR+r'\Stimuli\18-0.png'), (DIR+r'\Stimuli\18-1.png'), LETTERSIZE[1]], 
              'H':[C2[5], (DIR+r'\Stimuli\8-0.png'), (DIR+r'\Stimuli\8-1.png'), LETTERSIZE[1]], 
              'W':[C2[6], (DIR+r'\Stimuli\23-0.png'), (DIR+r'\Stimuli\23-1.png'), LETTERSIZE[1]],
              'Q':[C2[7], (DIR+r'\Stimuli\17-0.png'), (DIR+r'\Stimuli\17-1.png'), LETTERSIZE[1]], 
              'K':[C2[8], (DIR+r'\Stimuli\11-0.png'), (DIR+r'\Stimuli\11-1.png'), LETTERSIZE[1]],
              'I':[C3[0], (DIR+r'\Stimuli\9-0.png'), (DIR+r'\Stimuli\9-1.png'), LETTERSIZE[2]], 
              'C':[C3[1], (DIR+r'\Stimuli\3-0.png'), (DIR+r'\Stimuli\3-1.png'), LETTERSIZE[2]], 
              'D':[C3[2], (DIR+r'\Stimuli\4-0.png'), (DIR+r'\Stimuli\4-1.png'), LETTERSIZE[2]], 
              'E':[C3[3], (DIR+r'\Stimuli\5-0.png'), (DIR+r'\Stimuli\5-1.png'), LETTERSIZE[2]], 
              'S':[C3[4], (DIR+r'\Stimuli\19-0.png'), (DIR+r'\Stimuli\19-1.png'), LETTERSIZE[2]], 
              'O':[C3[5], (DIR+r'\Stimuli\15-0.png'), (DIR+r'\Stimuli\15-1.png'), LETTERSIZE[2]], 
              'A':[C3[6], (DIR+r'\Stimuli\1-0.png'), (DIR+r'\Stimuli\1-1.png'), LETTERSIZE[2]], 
              'T':[C3[7], (DIR+r'\Stimuli\20-0.png'), (DIR+r'\Stimuli\20-1.png'), LETTERSIZE[2]],
              'L':[C3[8], (DIR+r'\Stimuli\12-0.png'), (DIR+r'\Stimuli\12-1.png'), LETTERSIZE[2]]}

GROUPS = [('A','J','S'), ('B', 'K', 'T'), ('C','L','U'), ('D', 'M', 'V'), ('E', 'N','V'),
        ('F','O','X'), ('G', 'P', 'V'), ('H', 'Q', 'Z'), ('I', 'R', 'star'),
        ('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', 'I'), ('J', 'K', 'L'), ('M', 'N', 'O'),
        ('P', 'Q', 'R'), ('S', 'T', 'U'), ('V','W','X'), ('Y', 'Z', 'star'),
        ('A', 'D','G'), ('B', 'E','H'), ('G', 'F', 'I'), ('J','M','P'), ('K','N','Q'),
        ('L', 'O','R'), ('S', 'V','Y'), ('T','W','Z'), ('U','X','star')] # 'RC' stimuli groups


###############################################################################
####Testing block
#CIRCLES={'J':[C1[0], '', '', LETTERSIZE[0]], 
#              'V':[C1[1], '', '', LETTERSIZE[0]], 
#              'P':[C1[2], '', '', LETTERSIZE[0]], 
#              'U':[C1[3], '', '', LETTERSIZE[0]], 
#              'G':[C1[4], '', '', LETTERSIZE[0]], 
#              'Y':[C1[5], '', '', LETTERSIZE[0]],
#              'X':[C1[6], '', '', LETTERSIZE[0]], 
#              'Z':[C1[7], '', '', LETTERSIZE[0]], 
#              'star':[C1[8], '', '', LETTERSIZE[0]],
#              'F':[C2[0], '', '', LETTERSIZE[1]], 
#              'B':[C2[1], '', '', LETTERSIZE[1]], 
#              'N':[C2[2], '', '', LETTERSIZE[1]], 
#              'M':[C2[3], '', '', LETTERSIZE[1]], 
#              'R':[C2[4], '', '', LETTERSIZE[1]], 
#              'H':[C2[5], '', '', LETTERSIZE[1]], 
#              'W':[C2[6], '', '', LETTERSIZE[1]],
#              'Q':[C2[7], '', '', LETTERSIZE[1]], 
#              'K':[C2[8], '', '', LETTERSIZE[1]],
#              'I':[C3[0], '', '', LETTERSIZE[2]], 
#              'C':[C3[1], '', '', LETTERSIZE[2]], 
#              'D':[C3[2], '', '', LETTERSIZE[2]], 
#              'E':[C3[3], '', '', LETTERSIZE[2]], 
#              'S':[C3[4], '', '', LETTERSIZE[2]], 
#              'O':[C3[5], '', '', LETTERSIZE[2]], 
#              'A':[C3[6], '', '', LETTERSIZE[2]], 
#              'T':[C3[7], '', '', LETTERSIZE[2]],
#              'L':[C3[8],'', '', LETTERSIZE[2]]}
#
#for item in CIRCLES.keys():
#    CIRCLES[item][1]=DIR+r'\Stimuli\1.png'
#    CIRCLES[item][2]=DIR+r'\Stimuli\233-127-76.png'
###############################################################################

