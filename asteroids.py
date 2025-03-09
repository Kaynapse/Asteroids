from circleshape import *
from constants import *
import pygame
import random
import playerscore


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, color=(255, 255, 255)):
        super().__init__(x, y, radius)
        self.color = color  

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, width=2)
        

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        # adding points based on asteroid size
        if self.radius == ASTEROID_MAX_RADIUS:
            playerscore.PlayerScore.score_sum += 5
        if self.radius < ASTEROID_MAX_RADIUS and self.radius > ASTEROID_MIN_RADIUS:
            playerscore.PlayerScore.score_sum += 15
        if self.radius == ASTEROID_MIN_RADIUS:
            playerscore.PlayerScore.score_sum += 30

        
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        if self.radius >= ASTEROID_MIN_RADIUS:
            self.kill()
            random_angle = random.uniform(20, 50)
            
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            new_smaller_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            new_smaller_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            new_smaller_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            new_smaller_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2


        
        

        
        
        
        
