#Author: Tristan Lingat A0127360
#Date: April 6, 2022
#Course: ACIT 2515 2A

import pygame
import pygame.locals

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from .base_screen import Screen
from pygame import mixer

pygame.init()
mixer.init()

class MenuScreen(Screen):
    """Main Menu Screen class (MenuScreen)"""
    def __init__(self, window, fps=60, bgcolor=None):
        """
        the constructor

        set up necessary assets and objects for use in the class
        """
        super().__init__(window, fps, bgcolor)

        #load and backgroud music
        mixer.music.load('assets/bgm.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)

        #background
        background = pygame.image.load("assets/rat.png")
        self.background = pygame.transform.scale(background, (WINDOW_HEIGHT, WINDOW_WIDTH))
        self.rect = self.background.get_rect()

        #font setups
        self.myfont=pygame.font.SysFont("New Times Roman", int(WINDOW_WIDTH/24))
        self.myfont2=pygame.font.SysFont("New Times Roman", int(WINDOW_WIDTH/12))

        self.mode = ""
        self.ranked = None

    def process_event(self, event):
        """
        process all the events inside the main menu screen
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #if the player presses the practice button, set the mode to PRACTICE and quit the screen
            #if the player presses the ranked button, set the mode to RANKED and quit the screen
            if self.practice_button.collidepoint(pos):
                self.mode = "PRACTICE"
                self.running = False
            if self.ranked_button.collidepoint(pos):
                self.mode = "RANKED"
                self.running = False

    def process_loop(self):
        """
        process all the occurences inside the main menu screen
        """
        #blit the background
        self.window.blit(self.background, (0, 0))

        #blit the practice and quit buttons
        self.practice_button = pygame.Rect((int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/2.4)), (int(WINDOW_HEIGHT/3.33), int(WINDOW_HEIGHT/20)))
        self.ranked_button = pygame.Rect((int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/1.8)), (int(WINDOW_HEIGHT/3.75), int(WINDOW_HEIGHT/20)))

        self.window.blit(self.background, self.rect)

        #blit game title texts
        self.window.blit(self.myfont.render('what may be the dumbest pong game to have ever been', True, 'white'), (int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/6)))
        self.window.blit(self.myfont.render("created in humanity's existence.", True, 'white'), (int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/4.8)))
        self.window.blit(self.myfont.render('i yoouerly dont do this.', True, 'white'), (int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/3.4)))

        #blit text
        self.window.blit(self.myfont2.render('PRACTICE', True, 'white'), (int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/2.4)))
        self.window.blit(self.myfont2.render('RANKED', True, 'red'), (int(WINDOW_HEIGHT/12), int(WINDOW_HEIGHT/1.8)))

        return self.mode, self.ranked