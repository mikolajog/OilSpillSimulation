import math
import random

import pygame
import pygame.locals
import pygame_gui

from src.constants import *
from src.simulation_parameters import *
from src.discretized_oil import DiscretizedOil
from src.map import Map


class Board(object):
    """
    Simulation board responsible for:
    providing window (__init__)
    drawing(draw)
    """

    def __init__(self):
        # Initialize surface, backgorund
        self.surface = pygame.display.set_mode(RESOLUTION, 0, 32)
        pygame.display.set_caption('Oil Spill Simulation')
        self.background = pygame.Surface(RESOLUTION)
        self.background.fill(LIGHTBLUE)

        # Initialize manager for buttons
        self.manager = pygame_gui.UIManager(RESOLUTION)

        # Initialize Menu buttons
        self.startButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_STARTBUTTON, SIZE_STARTBUTTON),
            text='START',
            manager=self.manager)
        self.resetButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_RESETBUTTON, SIZE_RESETBUTTON),
            text='RESET',
            manager=self.manager)
        self.documentationButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_DOCUMENTATIONBUTTON, SIZE_DOCUMENTATIONBUTTON),
            text='Documentation',
            manager=self.manager)

        # Initlialize labels
        self.titleLablel = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_TITLELABEL, SIZE_TITLELABEL),
            text='DEEPWATER HORIZON OIL SPILL SIMULATION',
            manager=self.manager,
            tool_tip_text="This is a simulation of DeepWater Horizon Oil Spill by Zuzanna Smiech and Mikolaj Ogarek.")


        # Initialize map
        self.map = Map()

        # Initialize oil points list hardcoded values 100t of oil, start coords
        self.oil_point_list = DiscretizedOil(100, (X_START, Y_START))

        # at the begining all oil poitns are in start cell
        self.map.simulationArray[X_START][Y_START].oil_points = self.oil_point_list.oil_points_array.copy()
        self.total_time = 0


    def draw(self):
        # setting background
        img = pygame.image.load("src/img/background1.jpg")
        img = pygame.transform.scale(img, (1100, 800))
        self.surface.blit(img, (0,0))

        #draw logos
        img = pygame.image.load("src/img/logoagh.jpg")
        img = pygame.transform.scale(img, (135, 135))
        self.surface.blit(img, (48, 660))

        # draw logos
        img = pygame.image.load("src/img/logoOur.png")
        img = pygame.transform.scale(img, (168, 135))
        self.surface.blit(img, (888, 660))

        # draw border lines
        pygame.draw.rect(self.surface, (37, 41, 46), (
            50 - MARGIN_THICKNESS, 50 - MARGIN_THICKNESS, 1000 + 2 * MARGIN_THICKNESS, 600 + 2 * MARGIN_THICKNESS))

        for x, y in self.map.get_particular_cells_coordinates(LAND):
            pygame.draw.rect(self.surface, GREEN,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(SEA):
            pygame.draw.rect(self.surface, DARKBLUE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(OIL):
            pygame.draw.rect(self.surface, ORANGE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(START):
            pygame.draw.rect(self.surface, RED, (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        # updating the display and making visible changes on the screen
        pygame.display.update()

    def drawStates(self):
        # draw border lines
        pygame.draw.rect(self.surface, (37, 41, 46), (
            50 - MARGIN_THICKNESS, 50 - MARGIN_THICKNESS, 1000 + 2 * MARGIN_THICKNESS, 600 + 2 * MARGIN_THICKNESS))

        for x, y in self.map.get_particular_cells_coordinates(LAND):
            pygame.draw.rect(self.surface, GREEN,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(SEA):
            pygame.draw.rect(self.surface, DARKBLUE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(OIL):
            pygame.draw.rect(self.surface, ORANGE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(START):
            pygame.draw.rect(self.surface, RED, (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        # updating the display and making visible changes on the screen
        pygame.display.update()

    def nextstate(self):
        """
        Function performing one step of simulation.
        """
        self.total_time += SIMULATION_STEP_TIME

        for (x,y) in self.map.get_particular_cells_coordinates(OIL):
            for op in self.map.simulationArray[x][y].oil_points:
                op.compute_evaporation(self.map.simulationArray[x][y].temp, len(self.map.simulationArray[x][y].oil_points))
                op.compute_emulsification(self.map.simulationArray[x][y].wind[0])


        self.advection()
        self.spreading()

    def advection(self):
        """
        Function computing and updating position of every oil_point.
        Computation based on wind and concurrent info saved in each cell.
        """

        for op in self.oil_point_list.oil_points_array:
            print(len(self.oil_point_list.oil_points_array))
            (x, y) = op.assigned_cell
            #delta_r w [m]
            delta_r_x = ALPHA * self.map.simulationArray[x][y].concurrent[0] * math.sin(
                self.map.simulationArray[x][y].concurrent[1]) + BETA * self.map.simulationArray[x][y].wind[
                0] * math.sin(self.map.simulationArray[x][y].wind[1])
            delta_r_y = ALPHA * self.map.simulationArray[x][y].concurrent[0] * math.sin(
                90 - self.map.simulationArray[x][y].concurrent[1]) + BETA * self.map.simulationArray[x][y].wind[
                0] * math.sin(90 - self.map.simulationArray[x][y].wind[1])

            self.map.simulationArray[x][y].oil_points.remove(op)
            if len(self.map.simulationArray[x][y].oil_points) == 0:
                self.map.simulationArray[x][y].update_cell_type(SEA)

            op.relatives_coordinates[0] += delta_r_x /1000 #zamiana jednostek z m na km
            op.relatives_coordinates[1] += -1* delta_r_y /1000

            print(op.relatives_coordinates)

            new_x = X_START + round(op.relatives_coordinates[0] / 10)
            new_y = Y_START + round(op.relatives_coordinates[1] / 10)
            op.assigned_cell = (new_x, new_y)

            self.map.simulationArray[new_x][new_y].update_cell_type(OIL)
            self.map.simulationArray[new_x][new_y].oil_points.append(op)

    def spreading(self):
        """
        Function computing and updating position of every oil_point based on interaction between oil_points.
        """
        cells_with_oil = self.map.get_particular_cells_coordinates(OIL)
        print(cells_with_oil)
        for (i, j) in cells_with_oil:
            reference_cell = self.map.simulationArray[i][j]
            left_cell = self.map.simulationArray[i - 1][j]
            right_cell = self.map.simulationArray[i + 1][j]
            up_cell = self.map.simulationArray[i][j - 1]
            down_cell = self.map.simulationArray[i][j + 1]

            for (cell, x, y) in {(left_cell, i - 1, j), (right_cell, i + 1, j), (up_cell, i, j - 1),
                                 (down_cell, i, j + 1)}:
                tmp = delta_mass(cell, reference_cell, self.total_time)
                if tmp > 0:
                    # from cell to reference_cell
                    r = abs(tmp) / cell.oil_mass_in_cell()
                    for op in cell.oil_points:
                        theta = random.randrange(0, 1)
                        if theta < r:
                            reference_cell.oil_points.append(op)
                            reference_cell.update_cell_type(OIL)
                            cell.oil_points.remove(op)

                            # changing oil point assigned cell
                            op.assigned_cell = [i, j]
                            op.relatives_coordinates[0] += (i - x) * 10  # [km]
                            op.relatives_coordinates[1] += (j - y) * 10  # [km] długość cell
                            if len(cell.oil_points) == 0:
                                cell.update_cell_type(SEA)

                elif tmp < 0:
                    # from reference_cell to cell
                    r = abs(tmp) / reference_cell.oil_mass_in_cell()
                    for op in reference_cell.oil_points:
                        theta = random.randrange(0, 1)
                        if theta < r:
                            cell.oil_points.append(op)
                            cell.update_cell_type(OIL)
                            reference_cell.oil_points.remove(op)

                            op.assigned_cell = [x, y]
                            op.relatives_coordinates[0] += (x - i) * 10  # [km]
                            op.relatives_coordinates[1] += (y - j) * 10  # [km] długość cell

                            if len(reference_cell.oil_points) == 0:
                                reference_cell.update_cell_type(SEA)


def delta_mass(cellj, celli, total_time):
    """
    Function responsible for comuputing flowing mass between two cells
    """
    delta_t = SIMULATION_STEP_TIME
    delta_x = CELL_LENGTH
    mass_j = cellj.oil_mass_in_cell()
    mass_i = celli.oil_mass_in_cell()

    total_volume = cellj.oil_volume_in_cell() + celli.oil_volume_in_cell()

    delta_m = 0.5 * (mass_j - mass_i) * (1 - math.exp(-2 * D(total_volume, total_time) * delta_t / pow(delta_x, 2)))
    return delta_m


def D(total_volume, total_time):
    delta_density_ratio = SEA_WATER_DENSITY - INIT_OIL_DENSITY / SEA_WATER_DENSITY  # gestosci[kg/m^3] wody morskiej i crude oil
    return (0.48 / pow(N, 2)) * pow(pow(total_volume, 2) * G * delta_density_ratio / pow(KINEMATIC_VISCOSITY, 1 / 2),
                                    1 / 3) * pow(total_time, -1 / 2)
