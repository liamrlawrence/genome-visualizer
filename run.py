#------------------------------------------------------------------------------
# File Name    : run.py
# Description  : Converts a sequenced genome into a 2-bit image
# Authors      : Liam Lawrence
# Created      : March 20, 2020
# Project      : Genome Visualizer
# License      : MIT License
# Copyright    : (C) 2020, Liam Lawrence
#------------------------------------------------------------------------------

from itertools import permutations
import numpy as np
import cv2 as cv
import re

HEIGHT = 173
WIDTH  = 173
SCALE  = 5

pairs = ['a', 't', 'c', 'g']
perms = list(permutations(pairs))

for i in range(len(perms)):
    with open("palette.txt", 'r') as palette:
        a = int(palette.readline(), base=16)
        t = int(palette.readline(), base=16)
        c = int(palette.readline(), base=16)
        g = int(palette.readline(), base=16)

    sequence_colors = {
        perms[i][0]: ((a & 0x0000FF), (a & 0x00FF00) >> 8, (a & 0xFF0000) >> 16),
        perms[i][1]: ((t & 0x0000FF), (t & 0x00FF00) >> 8, (t & 0xFF0000) >> 16),
        perms[i][2]: ((c & 0x0000FF), (c & 0x00FF00) >> 8, (c & 0xFF0000) >> 16),
        perms[i][3]: ((g & 0x0000FF), (g & 0x00FF00) >> 8, (g & 0xFF0000) >> 16)
    }


    img = np.zeros((HEIGHT, WIDTH, 3), dtype="uint8")
    index = 0

    with open("COVID19.txt", 'r') as fp:
        for line in fp:
            line = re.sub(r"[\d+ ]", "", line).strip()
            for c in line:
                try:
                    img[int(index/WIDTH)][int(index%WIDTH)] = sequence_colors[c]
                    index += 1
                except:
                    print("BAD DIMENSIONS")
                    exit()

    img = cv.resize(img, (WIDTH*SCALE, HEIGHT*SCALE), interpolation=cv.INTER_AREA)
    filename = str(i+1) + "_" + perms[i][0] + perms[i][1] + perms[i][2] + perms[i][3]
    cv.imwrite("out/" + filename + ".png", img)

