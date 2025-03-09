import pygame
from constants import *


class PlayerScore():
    
    def __init__(self, x, y):
        pygame.font.init()
        self.score_sum = 0
        
        self.font = pygame.font.Font("assets/FiraCode-Regular.ttf", 32)
        self.fontX = x
        self.fontY = y

    def display_score(self, screen):

        text = self.font.render(f"Player Score: {str(self.score_sum)}", True, (255, 255, 255))
        screen.blit(text, (self.fontX, self.fontY))
        
    def add_player_score(self, radius):

    # adding points based on asteroid size
        if radius == ASTEROID_MAX_RADIUS:
                self.score_sum += 5
        if radius < ASTEROID_MAX_RADIUS and radius > ASTEROID_MIN_RADIUS:
                self.score_sum += 15
        if radius == ASTEROID_MIN_RADIUS:
                self.score_sum += 30

    