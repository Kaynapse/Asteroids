import pygame 
from constants import *
from player import *
from asteroids import Asteroid
from circleshape import *
from asteroidfield import *

def main():
    pygame.init
    time_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill(color='black')
        for draw in drawable:
            draw.draw(screen)   
        
        pygame.display.flip()
        dt = time_clock.tick(60) / 1000
if __name__ == "__main__":
    main()