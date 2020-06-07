import pygame
import pygame.locals
from src.board import Board
from src.discretized_oil import DiscretizedOil
from src.documentationOpener import openDocumentationFile
from src.simulation_parameters import X_START, Y_START, TOTAL_WEIGHT
import pygame_gui


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
        self.board.map.set_start_point(X_START, Y_START)
        while not self.handle_events():

            if self.started:
                print("You have started simulation")

    def handle_events(self):
        """
                Function responsible for handling events in game
                for example mouse clicks
                :return True if the simulation should end
        """

        time_delta = self.fps_clock.tick(1000)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.board.startButton:
                        self.started = True

                    if event.ui_element == self.board.resetButton:
                        print("pressed reset")
                        self.started = False
                        self.board.map.reset_to_default_Map()
                        self.board.__init__()


                    if event.ui_element == self.board.documentationButton:
                        openDocumentationFile()


            self.board.manager.process_events(event)

        if self.started:
            self.board.nextstate()
            self.board.drawStates()

        self.board.manager.update(time_delta)
        self.board.surface.blit(self.board.background, (0, 0))
        self.board.draw()
        self.board.manager.draw_ui(self.board.surface)
        pygame.display.update()

        return False
