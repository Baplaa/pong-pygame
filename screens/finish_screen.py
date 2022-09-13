#Author: Tristan Lingat A0127360
#Date: April 6, 2022
#Course: ACIT 2515 2A

import pygame
import pygame.locals
import sys

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from pygame import mixer
from .base_screen import Screen

pygame.init()
mixer.init()

class FinishScreen(Screen):
    """Game Over Screen class (FinishScreen)"""
    def __init__(self, window, fps=60, bgcolor=None):
        """
        the constructor

        set up necessary assets and objects for use in the class
        """ 
        super().__init__(window, fps, bgcolor)

        #background
        background = pygame.image.load("assets/finish.png")
        self.background = pygame.transform.scale(background, (WINDOW_HEIGHT, WINDOW_WIDTH))
        self.rect = self.background.get_rect()
        
        #font setups
        self.myfont=pygame.font.SysFont("New Times Roman", int(WINDOW_HEIGHT/6))
        self.myfont2=pygame.font.SysFont("New Times Roman", int(WINDOW_HEIGHT/12))
        self.scored=pygame.font.SysFont("New Times Roman", int(WINDOW_HEIGHT/12))

        self.mode = ""

    def process_event(self, event):
        """
        process all the events inside the game over screen
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #if the player presses the play again button, set the mode to PLAY AGAIN and quit the screen
            #if the player presses the quit button, the game exits
            if self.play_again_button.collidepoint(pos):
                self.mode = "PLAY AGAIN"
                self.running = False
            if self.quit_button.collidepoint(pos):
                sys.exit()

    def process_loop(self):
        """
        process all the occurences inside the game over screen
        """
        #blit background
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.background, self.rect)

        #blit buttons
        self.play_again_button = pygame.Rect((int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/2.4)), (int(WINDOW_HEIGHT/3.33), int(WINDOW_HEIGHT/20)))
        self.quit_button = pygame.Rect((int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/1.8)), (int(WINDOW_HEIGHT/3.75), int(WINDOW_HEIGHT/20)))

        #blit text
        self.window.blit(self.myfont.render('GAME OVER', True, 'white'), (int(WINDOW_HEIGHT/12), int(WINDOW_WIDTH/6)))
        self.window.blit(self.myfont2.render('PLAY AGAIN', True, 'white'), (int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/2.4)))
        self.window.blit(self.myfont2.render('QUIT', True, 'red'), (int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/1.8)))

        #render the player scores
        self.p1_score_text = self.myfont.render(str(self.p1_score), True, "white")
        self.p2_score_text = self.myfont.render(str(self.p2_score), True, "white") 

        #blit the player scores
        self.window.blit(self.p1_score_text, ((WINDOW_HEIGHT/3 + WINDOW_HEIGHT/6), (WINDOW_WIDTH/8 + WINDOW_WIDTH/1.7)))
        self.window.blit(self.p2_score_text, ((WINDOW_HEIGHT/3 + WINDOW_HEIGHT/6), (WINDOW_WIDTH/4 + WINDOW_WIDTH/1.7)))

        #render the player score headers
        self.p1_finish = self.myfont2.render('P1 SCORE', True, 'white')
        self.p2_finish = self.myfont2.render('P2 SCORE', True, 'white')

        #blit the player score headers
        self.window.blit(self.p1_finish, (int(WINDOW_HEIGHT/12), int(WINDOW_WIDTH/1.364)))
        self.window.blit(self.p2_finish, (int(WINDOW_HEIGHT/12), int(WINDOW_WIDTH/1.165)))

        return self.mode