import cv2
import numpy as np

from src.constants import SEA, LAND
from src.cell import Cell


def makeArrayFromPhoto():
    img = cv2.imread('src/img/final_map.png')
    res = cv2.resize(img, dsize=(120, 60), interpolation=cv2.INTER_CUBIC)
    newmap = np.empty((120, 60), dtype=object)
    for i in range(120):
        for j in range(60):
            if np.all(res[j][i] <= [255, 218, 170]) and np.all(res[j][i] >= [255, 218, 170]):
                newmap[i][j] = Cell(SEA)
            else:
                newmap[i][j] = Cell(LAND)

    return newmap

