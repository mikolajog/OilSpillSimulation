from random import randint

import numpy as np
from src.constants import SEA, START, LAND, OIL
from src.makeArrayFromPhoto import makeArrayFromPhoto


# from src.oil_point import Oil_point


class Map(object):
    """
    Map class
    """

    def __init__(self):
        self.reset_to_default_Map()

    def reset_to_default_Map(self):
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

    def set_start_point(self, x_coord, y_coord):
        self.simulationArray[x_coord][y_coord].cell_type = OIL

# TODO: We need to have functions to accordingly change our simulationArray over the time, based on data provided before clicking START button.
