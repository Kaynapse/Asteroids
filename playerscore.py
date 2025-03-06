import pygame



class PlayerScore():
    score_sum = 0
    def __init__(self, x, y):
        pygame.font.init()

        
        self.font = pygame.font.Font("assets/FiraCode-Regular.ttf", 32)
        self.fontX = x
        self.fontY = y

    def display_score(self, screen):

        text = self.font.render(f"Player Score: {str(self.score_sum)}", True, (255, 255, 255))
        screen.blit(text, (self.fontX, self.fontY))
        
        