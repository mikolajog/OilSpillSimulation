import pygame
import pygame.locals
from src.board import Board
from src.simulation_parameters import X_START, Y_START, TOTAL_WEIGHT
import pygame_gui

from src.validators import is_valid_number, is_valid_float


class OilSpillSimulation(object):
    """
    Puts together all parts of the simulation.
    """

    def __init__(self):
        pygame.init()

        # Initialize board
        self.board = Board()

        # Clock responsible for frequency of drawing cells
        self.fps_clock = pygame.time.Clock()

        # To define whether the simulation has started or not
        self.started = False

    def run(self):
        """
        Main loop
        """
        # TODO: read coords for start simulation
        self.board.map.set_start_point(X_START, Y_START)
        while not self.handle_events():

            if self.started:
                print("You have started simulation")
                # TODO: new simulationArray states

    def handle_events(self):
        """
                Function responsible for handling events in game
                for example mouse clicks
                :return True if the simulation should end
        """

        time_delta = self.fps_clock.tick(360)

        for event in pygame.event.get():
            if self.started:
                if event.type == pygame.USEREVENT and event.ui_element == self.board.resetButton:
                    self.started = False
                    self.board.map.reset_to_default_Map()
                    # hardcoded starting point
                    self.board.map.set_start_point(X_START,Y_START,TOTAL_WEIGHT)
                else:
                    self.board.nextstate()
                    self.board.drawStates()
                # TODO: Calling method drawing on map only



            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.board.startButton:
                        # TODO: Check if all fields validation is passed
                        self.started = True

                    # Remove all text entry texts and validation to NOT
                    # TODO: Clear all output files if any and reset map to default state
                    if event.ui_element == self.board.resetButton:
                        self.started = False

                        if self.board.parameter_validation_label1.text== "OK":
                            self.board.parameterEntry1 = self.board.label_to_textentry(self.board.parameterEntry1,
                                                                                       self.board.parameterEntry1.rect,
                                                                                       "")
                        else:
                            self.board.parameterEntry1.set_text("")
                        self.board.parameter_validation_label1.set_text("NOT")

                        if self.board.parameter_validation_label2.text== "OK":
                            self.board.parameterEntry2 = self.board.label_to_textentry(self.board.parameterEntry2,
                                                                                       self.board.parameterEntry2.rect,
                                                                                       "")
                        else:
                            self.board.parameterEntry2.set_text("")
                        self.board.parameter_validation_label2.set_text("NOT")

                        # TODO: The same with all parameters


                    #Parameter 1: Wind
                    if event.ui_element == self.board.parameter_description_button1:
                        if self.board.parameter_validation_label1.text == "OK":
                            self.board.parameter_validation_label1.set_text("NOT")
                            self.board.parameterEntry1 = self.board.label_to_textentry(self.board.parameterEntry1, self.board.parameterEntry1.rect,
                                                          self.board.parameterEntry1.text)
                        elif self.board.parameter_validation_label1.text == "NOT" and (is_valid_number(self.board.parameterEntry1.get_text()) or is_valid_float(self.board.parameterEntry1.get_text())):
                            self.board.parameter_validation_label1.set_text("OK")
                            self.board.parameterEntry1 = self.board.textentry_to_label(self.board.parameterEntry1, self.board.parameterEntry1.rect,
                                                          self.board.parameterEntry1.get_text())
                    # Parameter 2: Tons of oil
                    if event.ui_element == self.board.parameter_description_button2:
                        if self.board.parameter_validation_label2.text == "OK":
                            self.board.parameter_validation_label2.set_text("NOT")
                            self.board.parameterEntry2 = self.board.label_to_textentry(self.board.parameterEntry2, self.board.parameterEntry2.rect,
                                                          self.board.parameterEntry2.text)
                        elif self.board.parameter_validation_label2.text == "NOT" and (is_valid_number(self.board.parameterEntry2.get_text()) or is_valid_float(self.board.parameterEntry2.get_text())):
                            self.board.parameter_validation_label2.set_text("OK")
                            self.board.parameterEntry2 = self.board.textentry_to_label(self.board.parameterEntry2, self.board.parameterEntry2.rect,
                                                          self.board.parameterEntry2.get_text())
                    # Pressed validate button
                    if event.ui_element == self.board.validateButton:
                        # Parameter 1:

                        if self.board.parameter_validation_label1.text == "NOT" and (is_valid_number(self.board.parameterEntry1.get_text()) or is_valid_float(self.board.parameterEntry1.get_text())):
                            self.board.parameter_validation_label1.set_text("OK")
                            self.board.parameterEntry1 = self.board.textentry_to_label(self.board.parameterEntry1, self.board.parameterEntry1.rect,
                                                          self.board.parameterEntry1.get_text())

                        # Parameter 2:
                        if self.board.parameter_validation_label2.text == "NOT" and (is_valid_number(self.board.parameterEntry2.get_text()) or is_valid_float(self.board.parameterEntry2.get_text())):
                            self.board.parameter_validation_label2.set_text("OK")
                            self.board.parameterEntry2 = self.board.textentry_to_label(self.board.parameterEntry2, self.board.parameterEntry2.rect,
                                                          self.board.parameterEntry2.get_text())

            self.board.manager.process_events(event)

        self.board.manager.update(time_delta)
        self.board.surface.blit(self.board.background, (0, 0))
        self.board.draw()
        self.board.manager.draw_ui(self.board.surface)
        pygame.display.update()

        return False
