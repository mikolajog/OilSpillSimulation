import pygame
import pygame.locals
import pygame_gui

from src.constants import *
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
        self.validateButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_VALIDATEBUTTON, SIZE_VALIDATEBUTTON),
            text='VALIDATE',
            manager=self.manager)

        # Initlialize labels
        self.titleLablel = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_TITLELABEL, SIZE_TITLELABEL),
            text='DEEPWATER HORIZON OIL SPILL SIMULATION',
            manager=self.manager,
            tool_tip_text="This is a simulation of DeepWater Horizon Oil Spill by Zuzanna Smiech and Mikolaj Ogarek." )
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
        pygame.draw.rect(self.surface, (37, 41, 46),(50-MARGIN_THICKNESS, 50-MARGIN_THICKNESS, 1000+2*MARGIN_THICKNESS, 600+2*MARGIN_THICKNESS))

        for x, y in self.map.get_particular_cells_coordinates(LAND):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, GREEN, (x * CELLSIZE + X_MARGIN , y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(SEA):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, DARKBLUE, (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

        for x, y in self.map.get_particular_cells_coordinates(OIL):
            # size = (self.box_size, self.box_size)
            # position = (x * self.box_size, y * self.box_size)
            # thickness = 1
            pygame.draw.rect(self.surface, ORANGE, (x * CELLSIZE + X_MARGIN, y * CELLSIZE + Y_MARGIN, CELLSIZE, CELLSIZE))

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



