import pygame
import pygame.locals
import pygame_gui
import math
import random

from src.constants import *
from src.map import Map
from src.discretized_oil import DiscretizedOil


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
        self.validateButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_VALIDATEBUTTON, SIZE_VALIDATEBUTTON),
            text='VALIDATE',
            manager=self.manager)

        # Initlialize labels
        self.titleLablel = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_TITLELABEL, SIZE_TITLELABEL),
            text='DEEPWATER HORIZON OIL SPILL SIMULATION',
            manager=self.manager,
            tool_tip_text="This is a simulation of DeepWater Horizon Oil Spill by Zuzanna Smiech and Mikolaj Ogarek.")
        # Initlialize parameters entries
        self.parameterEntry1 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY1, SIZE_PARAMETER_ENTRY1),
            manager=self.manager)
        self.parameterEntry2 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY2, SIZE_PARAMETER_ENTRY2),
            manager=self.manager)
        self.parameterEntry3 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY3, SIZE_PARAMETER_ENTRY3),
            manager=self.manager)
        self.parameterEntry4 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY4, SIZE_PARAMETER_ENTRY4),
            manager=self.manager)
        self.parameterEntry5 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY5, SIZE_PARAMETER_ENTRY5),
            manager=self.manager)
        self.parameterEntry6 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY6, SIZE_PARAMETER_ENTRY6),
            manager=self.manager)
        self.parameterEntry7 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY7, SIZE_PARAMETER_ENTRY7),
            manager=self.manager)
        self.parameterEntry8 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY8, SIZE_PARAMETER_ENTRY8),
            manager=self.manager)
        self.parameterEntry9 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY9, SIZE_PARAMETER_ENTRY9),
            manager=self.manager)
        self.parameterEntry10 = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(POSITION_PARAMETER_ENTRY10, SIZE_PARAMETER_ENTRY10),
            manager=self.manager)

        # Initlialize parameters button - descriptions
        self.parameter_description_button1 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON1, SIZE_PARAMETER_DESCRIPTION_BUTTON1),
            text='Wind (m/s)',
            tool_tip_text="This is a wind parameter. Please enter integer or float value.",
            manager=self.manager)
        self.parameter_description_button2 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON2, SIZE_PARAMETER_DESCRIPTION_BUTTON2),
            text='Tons of oil [t]',
            manager=self.manager)
        self.parameter_description_button3 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON3, SIZE_PARAMETER_DESCRIPTION_BUTTON3),
            text='Parameter 3',
            manager=self.manager)
        self.parameter_description_button4 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON4, SIZE_PARAMETER_DESCRIPTION_BUTTON4),
            text='Parameter 4',
            manager=self.manager)
        self.parameter_description_button5 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON5, SIZE_PARAMETER_DESCRIPTION_BUTTON5),
            text='Parameter 5',
            manager=self.manager)
        self.parameter_description_button6 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON6, SIZE_PARAMETER_DESCRIPTION_BUTTON6),
            text='Parameter 6',
            manager=self.manager)
        self.parameter_description_button7 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON7, SIZE_PARAMETER_DESCRIPTION_BUTTON7),
            text='Parameter 7',
            manager=self.manager)
        self.parameter_description_button8 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON8, SIZE_PARAMETER_DESCRIPTION_BUTTON8),
            text='Parameter 8',
            manager=self.manager)
        self.parameter_description_button9 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON9, SIZE_PARAMETER_DESCRIPTION_BUTTON9),
            text='Parameter 9',
            manager=self.manager)
        self.parameter_description_button10 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_PARAMETER_DESCRIPTION_BUTTON10, SIZE_PARAMETER_DESCRIPTION_BUTTON10),
            text='Parameter 10',
            manager=self.manager)

        # Initialize parameters validation labels
        self.parameter_validation_label1 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL1, SIZE_PARAMETER_VALIDATION_LABEL1),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL2, SIZE_PARAMETER_VALIDATION_LABEL2),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL3, SIZE_PARAMETER_VALIDATION_LABEL3),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL4, SIZE_PARAMETER_VALIDATION_LABEL4),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label5 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL5, SIZE_PARAMETER_VALIDATION_LABEL5),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label6 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL6, SIZE_PARAMETER_VALIDATION_LABEL6),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label7 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL7, SIZE_PARAMETER_VALIDATION_LABEL7),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label8 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL8, SIZE_PARAMETER_VALIDATION_LABEL8),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label9 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL9, SIZE_PARAMETER_VALIDATION_LABEL9),
            text='NOT',
            manager=self.manager)
        self.parameter_validation_label10 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(POSITION_PARAMETER_VALIDATION_LABEL10, SIZE_PARAMETER_VALIDATION_LABEL10),
            text='NOT',
            manager=self.manager)

        # Initialize map
        self.map = Map()

        # Initialize oil points list hardcoded values 100t of oil, start coords
        self.oil_point_list = DiscretizedOil(100, (X_START, Y_START))

        # at the begining all oil poitns are in start cell
        # coords = self.map.get_particular_cells_coordinates(OIL)
        self.map.simulationArray[X_START][Y_START].oil_points = self.oil_point_list.oil_points_array.copy()
        self.total_time = 0
    def textentry_to_label(self, textentry, rect, text):
        textentry.kill()
        textentry = pygame_gui.elements.UILabel(
            relative_rect=rect,
            text=text,
            manager=self.manager)
        return textentry

    def label_to_textentry(self, textentry, rect, text):
        textentry.kill()
        textentry = pygame_gui.elements.UITextEntryLine(
            relative_rect=rect,
            manager=self.manager)
        textentry.set_text(text)
        return textentry

    def draw(self):
        # setting background
        self.surface.fill(LIGHTBLUE)

        # draw border lines
        pygame.draw.rect(self.surface, (37, 41, 46), (
            50 - MARGIN_THICKNESS, 50 - MARGIN_THICKNESS, 1000 + 2 * MARGIN_THICKNESS, 600 + 2 * MARGIN_THICKNESS))

        for x, y in self.map.get_particular_cells_coordinates(LAND):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, GREEN,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(SEA):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, DARKBLUE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(OIL):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, ORANGE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(START):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, RED, (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        # updating the display and making visible changes on the screen
        pygame.display.update()

    def drawStates(self):
        # draw border lines
        pygame.draw.rect(self.surface, (37, 41, 46), (
            50 - MARGIN_THICKNESS, 50 - MARGIN_THICKNESS, 1000 + 2 * MARGIN_THICKNESS, 600 + 2 * MARGIN_THICKNESS))

        for x, y in self.map.get_particular_cells_coordinates(LAND):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, GREEN,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(SEA):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, DARKBLUE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(OIL):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, ORANGE,
                             (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(START):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, RED, (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        # updating the display and making visible changes on the screen
        pygame.display.update()

    def nextstate(self):
        self.total_time += 3600
        self.advection()
        # time.sleep(1)
        self.spreading()
        # time.sleep(3)
        print("#####################"+self.total_time.__str__())

    def advection(self):
        alfa = 1.1
        beta = 0.03
        print("computing advection")
        for op in self.oil_point_list.oil_points_array:
            print("hejka")
            print(len(self.oil_point_list.oil_points_array))
            (x, y) = op.assigned_cell
            delta_r_x = alfa * self.map.simulationArray[x][y].concurrent[0] * math.sin(self.map.simulationArray[x][y].concurrent[1]) + beta * self.map.simulationArray[x][y].wind[0] * math.sin(self.map.simulationArray[x][y].wind[1])
            delta_r_y = alfa * self.map.simulationArray[x][y].concurrent[0] * math.sin(90 - self.map.simulationArray[x][y].concurrent[1]) + beta * self.map.simulationArray[x][y].wind[0] * math.sin(90 - self.map.simulationArray[x][y].wind[1])

            self.map.simulationArray[x][y].oil_points.remove(op)
            if len(self.map.simulationArray[x][y].oil_points) == 0:
                self.map.simulationArray[x][y].update_cell_type(SEA)

            op.relatives_coordinates[0] += delta_r_x
            op.relatives_coordinates[1] += delta_r_y

            print(op.relatives_coordinates)

            new_x = X_START + round(op.relatives_coordinates[0] / 10)
            new_y = Y_START + round(op.relatives_coordinates[1] / 10)
            op.assigned_cell = (new_x, new_y)

            self.map.simulationArray[new_x][new_y].update_cell_type(OIL)
            self.map.simulationArray[new_x][new_y].oil_points.append(op)


    def spreading(self):
        cells_with_oil = self.map.get_particular_cells_coordinates(OIL)
        print(cells_with_oil)
        for (i,j) in cells_with_oil:
            reference_cell = self.map.simulationArray[i][j]
            left_cell = self.map.simulationArray[i-1][j]
            right_cell = self.map.simulationArray[i+1][j]
            up_cell = self.map.simulationArray[i][j-1]
            down_cell = self.map.simulationArray[i][j+1]

            for (cell,x,y) in {(left_cell,i-1,j),(right_cell,i+1,j),(up_cell,i,j-1),(down_cell,i,j+1)}:
                tmp = delta_mass(cell,reference_cell,self.total_time)
                # print(tmp)
                # print(cell.oil_mass_in_cell())
                # print(reference_cell.oil_mass_in_cell())
                if (tmp > 0):
                    # from cell to reference_cell
                    r = abs(tmp) / cell.oil_mass_in_cell()
                    for op in cell.oil_points:
                        theta = random.randrange(0,1)
                        if theta < r :
                            reference_cell.oil_points.append(op)
                            reference_cell.update_cell_type(OIL)
                            cell.oil_points.remove(op)

                            #changing oil point assigned cell
                            op.assigned_cell = [i,j]
                            op.relatives_coordinates[0] += (i-x) * 10 #[km]
                            op.relatives_coordinates[1] += (j-y) * 10 #[km] długość cell
                            if len(cell.oil_points)==0:
                                cell.update_cell_type(SEA)

                elif(tmp<0):
                    #from reference_cell to cell
                    r = abs(tmp) / reference_cell.oil_mass_in_cell()
                    for op in reference_cell.oil_points:
                        theta = random.randrange(0,1)
                        if theta < r :
                            cell.oil_points.append(op)
                            cell.update_cell_type(OIL)
                            reference_cell.oil_points.remove(op)

                            op.assigned_cell = [x, y]
                            op.relatives_coordinates[0] += (x - i) * 10  # [km]
                            op.relatives_coordinates[1] += (y - j) * 10  # [km] długość cell

                            if len(reference_cell.oil_points)==0:
                                reference_cell.update_cell_type(SEA)
"""
Function responsible for comuputing flowing mass beteen two cells
"""
def delta_mass(cellj, celli, total_time):
    delta_t = 60 #[s]
    delta_x = 10000 #[m]
    mj = cellj.oil_mass_in_cell()
    mi = celli.oil_mass_in_cell()
    total_volume = cellj.oil_volume_in_cell() + celli.oil_volume_in_cell()
    delta_m = 0.5*(mj -mi)*(1 - math.exp(-2*D(total_volume,total_time)*delta_t/pow(delta_x,2)))
    return delta_m

def D(total_volume,total_time):
    n = 3 #jakiś tam współczynnik
    g = 9.81 #[m/s^2]
    delta_density_ratio =  1029 - 900 / 1029 #gestosci[kg/m^3] wody morskiej i crude oil
    kinematic_viscosity = 1.1889 * pow(10,-6) #[m^2/s] dla wody o zasoleniu 35g na 1kg wody
    return (0.48/pow(n,2))*pow(pow(total_volume,2)*g*delta_density_ratio/pow(kinematic_viscosity,1/2),1/3)*pow(total_time,-1/2)