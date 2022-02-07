# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:13:47 2020

@author: genaf
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def conway(x,y,type,iter):
    #dimensions of graph in matplotlib
    display = np.ones([x,y])
    for i in type:
        display[i[0]][i[1]] = float(0)

    #1 = white square, 0 = black square
    plt.imshow(display,interpolation = "nearest", cmap=cm.Greys_r)
    plt.ion()
    plt.show()

    #filling in type of glider w/ black
    blkBoxes = type
    n = 0
    while True:
        n = n + 1
        plt.pause(.01)
        neighbors = []
        change2Blk = []
        change2Wht = []
        for sqr in blkBoxes:
            for i in range(3):
                for j in range(3):
                    neighbors.append([sqr[0] + i - 1, sqr[1] + j - 1])
        neighbors = np.unique(neighbors, axis = 0)

        # checking neighbors
        for carre in neighbors:
            check = 0
            if display[carre[0]][carre[1]] == 1:
                for i in range(3):
                    for j in range(3):
                        check += display[carre[0] + i - 1][carre[1] + j -1]
                if check == 6:
                    change2Blk.append([carre[0],carre[1]])
            else:
                for i in range(3):
                    for j in range(3):
                        check += display[carre[0] + i - 1][carre[1] + j -1]
                if check != 6 and check != 5:
                    change2Wht.append([carre[0],carre[1]])

        for changeSq in change2Wht:
            display[changeSq[0]][changeSq[1]] = 1.
        for changeSq in change2Blk:
            display[changeSq[0]][changeSq[1]] = 0.

        plt.cla()
        plt.imshow(display,interpolation = "nearest", cmap=cm.Greys_r)
        plt.draw()

        for oldSqr in blkBoxes:
            if display[oldSqr[0]][oldSqr[1]] == 0.:
                change2Blk.append(oldSqr)

        change2Blk = np.array(change2Blk)
        change2Blk = np.unique(change2Blk, axis = 0)
        blkBoxes = change2Blk
        if n > iter:
            break

glider = [[1,2],[2,3],[3,1],[3,2],[3,3]]

gliderGun = [[3,24],[7,24],[7,26],[8,26],[3,26],[2,26],[4,36],[5,36],[4,37],[5,37],[6,2],[6,3],[7,2],[7,3],[6,12],[7,12],[8,12],[5,13],[4,14],[4,15],[9,13],[10,14],[10,15],[7,16],[7,18],[6,18],[8,18],[5,17],[9,17],[7,19],[6,22],[5,22],[4,22],[6,23],[5,23],[4,23]]

conway(75,75,gliderGun, 2000)
