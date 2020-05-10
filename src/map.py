from random import randint

import numpy as np
from src.constants import SEA, START, LAND, OIL


class Map(object):
    """
    Map class
    """

    def __init__(self):
        self.reset_to_default_Map()


    def reset_to_default_Map(self):
        defaultMap = np.empty((200, 120), dtype=object)
        for i in range(200):
            for j in range(120):
                if i > 50:
                    defaultMap[i][j] = SEA
                else:
                    defaultMap[i][j] = LAND
        defaultMap[150][70] = START

        self.simulationArray = defaultMap

    def get_particular_cells_coordinates(self, cell_type):
        """
        :return list of tuples with coordinates of for example land_cells
        """

        list = []

        for x in range(len(self.simulationArray)):
            column = self.simulationArray[x]
            for y in range(len(column)):
                if column[y] == cell_type:
                    # append coordinated of cells of particular type
                    list.append((x, y))
        return list

    def nextstate(self):
        randomnumber1 = randint(50, 199)
        randomnumber2 = randint(0,119)
        self.simulationArray[randomnumber1][randomnumber2] = OIL

# TODO: We need to have functions to accordingly change our simulationArray over the time, based on data provided before clicking START button.



