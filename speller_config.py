# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 14:05:14 2017

@author: m0rningstar
"""
import os
from psychopy.monitors import Monitor

DIR = os.getcwd() #current directory

FLASH=0.1 # duration of flash, ms
TRIALREPEATS = 2 # 0 for 1 cycle of flashes
SIZE=(1920,1080) # resolution (1680,1050)
CENTER=(0,0) # fixmark coordinates, deg
DISTANCE=60 # distance between subject and screen
WIDTH=31 # screen width 47.4, cm
STIMSIZE= [0.4, 1.0, 2.0] #size of stimuli, deg
LETTERSIZE= [0.8, 1.6, 3.0] # seze of letter images, deg SIZE ADJASTMENT NEEDED! [0.9, 1.8, 2.6]

MON = Monitor('ProBook') #('BlOne')
MON.setWidth(WIDTH) 
MON.setDistance(DISTANCE)
MON.setSizePix(SIZE)

BACKCOL=(-1,-1,-1)
FIXCOL=(0,0,0)

C1=[(0,-1.500), (-0.964,-1.149), (-1.477,-0.260), (-1.299,0.750), (-0.513,1.410), 
       (0.513,1.410), (1.299,0.750), (1.477,-0.260), (0.964,-1.149)] # coordinates of inner circle, deg
C2=[(0,-3.000), (-1.928,-2.298), (-2.954,-0.521), (-2.598,1.500), (-1.026,2.819), (1.026,2.819), 
       (2.598,1.500), (2.954,-0.521), (1.928,-2.298)] # coordinates of middle circle, deg
C3=[(0,-5.000), (-3.214,-3.830), (-4.924,-0.868), (-4.330,2.500), (-1.710,4.698), 
       (1.710,4.698), (4.330,2.500), (4.924,-0.868), (3.214,-3.830)] # coordinates of outer circle, deg

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