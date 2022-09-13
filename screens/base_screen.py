import pygame
import sys

class Screen:
    """
    Use the Screen class as a parent class for your own screens
    """

    def __init__(self, window, fps=60, bgcolor=None, ranked=False, p1_score=0, p2_score=0):
        """Constructor must receive the window"""
        self.window = window
        self.running = True
        self.fps = 60
        self.bgcolor = bgcolor
        if not self.bgcolor:
            self.bgcolor = (255, 255, 255)
        self.ranked = ranked
        self.p1_score = p1_score
        self.p2_score = p2_score

    def loop(self):
        """Main screen loop: deals with Pygame events"""

        clock = pygame.time.Clock()

        while self.running:
            clock.tick(self.fps)

            # Fill the screen
            self.window.fill(self.bgcolor)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                else:
                    # Override this method to customize your screens!
                    self.process_event(event)

            # Override this method to customize what happens in your screens!
            result = self.process_loop()

            # Update display
            pygame.display.update()

        return result

    def process_event(self, event):
        """This method should be overriden by your child classes"""
        print("YOU SHOULD IMPLEMENT 'process_event' IN YOUR SCREEN SUBCLASS!")

    def process_loop(self):
        """This method should be overriden by your child classes"""
        raise NotImplementedError("YOU MUST IMPLEMENT 'process_loop' IN YOUR SUBCLASS!")