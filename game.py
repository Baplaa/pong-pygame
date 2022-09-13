#Author: Tristan Lingat A0127360
#Date: April 6, 2022
#Course: ACIT 2515 2A

import pygame
from pygame import mixer

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from screens.game_screen import GameScreen
from screens.menu_screen import MenuScreen
from screens.finish_screen import FinishScreen

def main():
    """"
    The main game functions of the Pong game
    """
    pygame.init()
    mixer.init() #for music purposes

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    #while loop statement, mainly used so the game over screen can
    #return to the main menu after using "break"
    while True:
        main_menu = MenuScreen(window)
        practice_game = GameScreen(window)
        finish = FinishScreen(window)
        ranked_game = GameScreen(window)

        result = main_menu.loop()

        if result[0] == "RANKED":
            #background music
            mixer.music.load('assets/ranked.mp3')
            mixer.music.set_volume(0.05)
            mixer.music.play(-1)

            ranked_game.mode = result[0]
            ranked_game.ranked = True       #if the ranked button was pressed, set ranked to True
            ranked_game.loop()
        
        if result[0] == "PRACTICE":
            #background music
            mixer.music.load('assets/practice.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play(-1)

            practice_game.mode = result[0]
            practice_game.loop()
        
        if ranked_game.mode == "FINISH":
            #background music
            mixer.music.load('assets/end.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play(-1)

            finish.mode = ranked_game.mode
            finish.p1_score = ranked_game.p1_score
            finish.p2_score = ranked_game.p2_score
            finish.loop()

        if finish.mode == "":
            break
            
if __name__ == "__main__":
    main()