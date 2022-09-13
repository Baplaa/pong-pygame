#Author: Tristan Lingat A0127360
#Date: April 6, 2022
#Course: ACIT 2515 2A

import pygame
import random

from constants import WINDOW_HEIGHT, WINDOW_WIDTH, LIMITS
from .base_screen import Screen
from models import Ball, Paddle

class GameScreen(Screen):
    """Example class for a Pong game screen"""
    def __init__(self, *args, **kwargs):
        """
        the constructor

        set up necessary assets and objects for use in the class
        """
        # Call the parent constructor
        super().__init__(*args, **kwargs)

        # Create objects
        self.ball = Ball(size=WINDOW_HEIGHT/30, color=(0, 255, 0))
        self.ball.launch(direction=random.choice(['right', 'left']), hspeed=3, vspeed=3)

        self.p1 = Paddle("left")
        self.p2 = Paddle("right")

        #p1 and p2 score setup
        self.p1_score = 0
        self.p2_score = 0

        self.score_font=pygame.font.SysFont("New Times Roman", int(WINDOW_HEIGHT/6))
        self.scored=pygame.font.SysFont("New Times Roman", int(WINDOW_HEIGHT/12))

        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.p1, self.p2)
    
        self.ball_direction = 'right'

        #power shot setup
        self.p1_power_shot = False
        self.p2_power_shot = False

        #backgrounds
        background1 = pygame.image.load("assets/off_limits3.png")
        self.background1 = pygame.transform.scale(background1, (WINDOW_HEIGHT, WINDOW_WIDTH))
        self.rect1 = self.background1.get_rect()

        background2 = pygame.image.load("assets/off_limits2.png")
        self.background2 = pygame.transform.scale(background2, (WINDOW_HEIGHT, WINDOW_WIDTH))
        self.rect2 = self.background2.get_rect()

        #paddle bounce sound effect
        self.bounce_paddle = pygame.mixer.Sound('assets/bounce_paddle.mp3')
        self.bounce_paddle.set_volume(0.2)
    
        #off limits ball sound effect
        self.off_limits = pygame.mixer.Sound('assets/off_limits.mp3')
        self.off_limits.set_volume(0.1)

        self.mode = ''

    def process_event(self, event):
        # In this screen, we don't have events to manage - pass
        pass

    def process_loop(self):
        """
        process all the occurences inside the playing game screen
        """
        #blit the base background
        self.window.blit(self.background2, (0, 0))
        self.window.blit(self.background2, self.rect2)

        # Update the ball position
        self.ball.update()

        # Update the paddles' positions
        self.paddles.update()

        # Blit everything
        self.paddles.draw(self.window)
        self.window.blit(self.ball.image, self.ball.rect)

        #player controls
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.p2.up()
        if keys[pygame.K_DOWN]:
            self.p2.down()
        if keys[pygame.K_w]:
            self.p1.up()
        if keys[pygame.K_s]:
            self.p1.down()
        if keys[pygame.K_LSHIFT]:       #power shot
            self.p1_power_shot = True   
        if keys[pygame.K_RSHIFT]:       #power shot
            self.p2_power_shot = True   

        if pygame.sprite.collide_mask(self.ball, self.p1):
            #play the paddle bounce sound effect
            pygame.mixer.Sound.play(self.bounce_paddle)

            #call the power shot ability if the key is pressed
            #otherwise, the ball is bounced regularly
            if self.p1_power_shot == True:
                self.ball.bounce('right', True, True)
                self.p1_power_shot = False
                self.ball_direction = 'right'
            else:
                self.ball.bounce('right', True)
                self.ball_direction = 'right'

        if pygame.sprite.collide_mask(self.ball, self.p2):
            #play the paddle bounce sound effect
            pygame.mixer.Sound.play(self.bounce_paddle)

            #call the power shot ability if the key is pressed
            #otherwise, the ball is bounced regularly
            if self.p2_power_shot == True:
                self.ball.bounce('left', True, True)
                self.p2_power_shot = False
                self.ball_direction = 'left'
            else:
                self.ball.bounce('left', True)
                self.ball_direction = 'left' 

        #render the player who scored a point
        p1_scored = self.scored.render('POINT: PLAYER 1', True, "white")
        p2_scored = self.scored.render('POINT: PLAYER 2', True, "white")

        #ranked gamemode exclusive features
        if self.ranked:
            #render ranked gamemode exclusive score counter for p1 and p2
            self.p1_score_text = self.score_font.render(str(self.p1_score), True, "white")
            self.p2_score_text = self.score_font.render(str(self.p2_score), True, "white") 

            #blit score counters
            self.window.blit(self.p1_score_text, (int(WINDOW_WIDTH/3), int(WINDOW_WIDTH/12)))
            self.window.blit(self.p2_score_text, (int(WINDOW_WIDTH/1.7), int(WINDOW_WIDTH/12))) 

            #if a player reaches a score of 10, set the mode to FINISH and quit the screen
            #return the mode
            if self.p1_score == 1 or self.p2_score == 1:
                self.mode = "FINISH"
                self.running = False

        if self.ball.off_limits:
            #play the off limits ball sound effect
            pygame.mixer.Sound.play(self.off_limits)
            
            #visual effect for when the ball is sent off limits
            #blit visual effect
            self.window.blit(self.background1, (0, 0))
            self.window.blit(self.background1, self.rect1)

            #set player boundaries
            if self.ball.rect.x > WINDOW_WIDTH/2:
                player = "p1"
            elif self.ball.rect.x < WINDOW_WIDTH/2:
                player = "p2"

            #add a point to the scoring player according to boundaries
            if player == "p1":
                self.p1_score += 1
                self.window.blit(p1_scored, (WINDOW_HEIGHT/4, WINDOW_WIDTH/2))
            elif player == "p2":
                self.p2_score += 1
                self.window.blit(p2_scored, (WINDOW_HEIGHT/4, WINDOW_WIDTH/2))
            
            pygame.display.flip()

            #reset ball properties
            self.ball.rect.x = LIMITS["right"] // 2
            self.ball.rect.y = LIMITS["down"] // 2

            self.ball.hspeed = 0
            self.ball.vspeed = 0

            #pause the screen for 3 seconds
            pygame.time.delay(3000)
            self.ball.off_limits = False

            #randomly launch the ball in a new direction
            self.ball.launch(direction=random.choice(['right', 'left']), hspeed=3, vspeed=3)

        return self.mode, self.p1_score, self.p2_score