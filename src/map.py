from random import randint

import numpy as np
from src.constants import SEA, START, LAND, OIL
from src.makeArrayFromPhoto import makeArrayFromPhoto
from src.oil_point import Oil_point


class Map(object):
    """
    Map class
    """

    def __init__(self):
        self.reset_to_default_Map()

    def reset_to_default_Map(self):
        defaultMap = np.empty((200, 120), dtype=object)
        # for i in range(200):
        #     for j in range(120):
        #         if i > 50:
        #             defaultMap[i][j] = SEA
        #         else:
        #             defaultMap[i][j] = LAND
        # defaultMap[150][70] = START
        # print(np.shape(defaultMap))
        defaultMap = makeArrayFromPhoto()
        print(defaultMap)
        self.simulationArray = defaultMap

    def get_particular_cells_coordinates(self, cell_type):
        """
        :return list of tuples with coordinates of for example land_cells
        """

        list = []

        for x in range(len(self.simulationArray)):
            column = self.simulationArray[x]
            for y in range(len(column)):
                if column[y].cell_type == cell_type:
                    # append coordinated of cells of particular type
                    list.append((x, y))
        return list

    def nextstate(self):
        # randomnumber1 = randint(50, 199)
        # randomnumber2 = randint(0,119)
        # self.simulationArray[randomnumber1][randomnumber2] = OIL
        coords_list = self.get_particular_cells_coordinates(OIL)
        # coords_list.append(self.get_particular_cells_coordinates(START)[0])

        for x, y in coords_list:

            if self.simulationArray[x][y - 1].cell_type != LAND:
                self.simulationArray[x][y - 1].cell_type = OIL
            if self.simulationArray[x][y + 1].cell_type != LAND:
                self.simulationArray[x][y + 1].cell_type = OIL
            if self.simulationArray[x + 1][y ].cell_type != LAND:
                self.simulationArray[x+1][y].cell_type = OIL
            if self.simulationArray[x - 1][y ].cell_type != LAND:
                self.simulationArray[x-1][y].cell_type = OIL

    def set_start_point(self, x_coord, y_coord, total_weight):
        self.simulationArray[x_coord][y_coord].cell_type = OIL
        self.simulationArray[x_coord][y_coord].oil_points = self.split_to_oil_points(total_weight)

    # przyjmuję że całą ropę dyskretuzyje za pomocą 20 równych porcji
    def split_to_oil_points(self, total_weight):
        oil_points_list = []

        for i in range(20):
            oil_points_list.append(Oil_point(total_weight / 20))

        return oil_points_list

# TODO: We need to have functions to accordingly change our simulationArray over the time, based on data provided before clicking START button.
