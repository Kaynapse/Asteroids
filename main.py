import pygame 
from constants import *
from player import *
from asteroids import Asteroid
from circleshape import *
from asteroidfield import *
import sys
from shot import *
import background


def main():
    pygame.init
    time_clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add groups to classes
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # create objects
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    background_ = background.Background("assets/heic1304c.jpg", [0, 0])
    

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print('Game Over')
                sys.exit()
            
            for shot in shots:

                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(color='black')
        screen.blit(background_.image, background_.rect)
        for draw in drawable:
            
            draw.draw(screen)   
        
        pygame.display.flip()
        dt = time_clock.tick(60) / 1000
if __name__ == "__main__":
    main()