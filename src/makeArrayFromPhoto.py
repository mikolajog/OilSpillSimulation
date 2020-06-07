import cv2
import numpy as np

from src.constants import SEA, LAND
from src.cell import Cell


def makeArrayFromPhoto():
    img = cv2.imread('src/img/map5km5km.png')
    res = cv2.resize(img, dsize=(200, 120), interpolation=cv2.INTER_CUBIC)
    newmap = np.empty((200, 120), dtype=object)
    for i in range(200):
        for j in range(120):
            if np.all(res[j][i] <= [255, 218, 170]) and np.all(res[j][i] >= [255, 218, 170]):
                newmap[i][j] = Cell(SEA)
            else:
                newmap[i][j] = Cell(LAND)

    return newmap

