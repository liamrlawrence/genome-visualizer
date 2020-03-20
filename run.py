#------------------------------------------------------------------------------
# File Name    : run.py
# Description  : Converts a sequenced genome into a 2-bit image
# Authors      : Liam Lawrence
# Created      : March 20, 2020
# Project      : Genome Visualizer
# License      : MIT License
#------------------------------------------------------------------------------

import numpy as np
import cv2 as cv
import re

HEIGHT = 173
WIDTH  = 173
SCALE  = 5

sequence_colors = {
    'a': (101,  27, 114),
    't': ( 90,  97, 248),
    'c': (104, 217, 255),
    'g': ( 87,  13, 184)
}


img = np.zeros((HEIGHT, WIDTH, 3), dtype="uint8")
index = 0

with open('COVID19.txt', 'r') as fp:
    for line in fp:
        line = re.sub(r'[\d+ ]', '', line).strip()
        for c in line:
            try:
                img[int(index/WIDTH)][int(index%WIDTH)] = sequence_colors[c]
                index += 1
            except:
                print("BAD DIMENSIONS")
                exit()

img = cv.resize(img, (WIDTH*SCALE, HEIGHT*SCALE), interpolation=cv.INTER_AREA)
cv.imwrite("out.png", img)

