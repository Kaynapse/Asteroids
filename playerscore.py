import pygame



class PlayerScore():

    def __init__(self, x, y):
        pygame.font.init()

        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.fontX = x
        self.fontY = y

    def display_score(self, screen):

        text = self.font.render("Player Score: " + str(int(self.score)), True, (255, 255, 255))
        screen.blit(text, (self.fontX, self.fontY))