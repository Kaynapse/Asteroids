import pygame 
from constants import *
from player import *
from asteroids import Asteroid
from circleshape import *
from asteroidfield import *
import sys
from shot import *
import background
from playerscore import *
from button import Button

pygame.font.init()
background_ = background.Background("assets/heic1304c.jpg", [0, 0])
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def get_font(size): # Returns Press-Start-2P in the desired size
    
    return pygame.font.Font("assets/FiraCode-Regular.ttf", size)


def main():
    pygame.init()
    
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
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player_score = PlayerScore(15, 15)
    
    
    
    #game loop
    game_on = True
    while game_on:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player_score.score_sum = 0
                   # main_menu()
                   # game_on = False
                
                
            
       
        

        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print('Game Over')
                pygame.time.wait(1000)
                sys.exit()
            
            for shot in shots:

                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(color='black')
        screen.blit(background_.image, background_.rect)
        player_score.display_score(screen)

        # --------------------------creating a player sprite for later use ---------------------------------

        #screen.blit(player.ship_sprite, player.position)

        # ---------------------------------------------------------------------------------------------------


        for draw in drawable:
            
            draw.draw(screen)   
        
        pygame.display.flip()
        dt = time_clock.tick(60) / 1000
#if __name__ == "__main__":
#    main()

def main_menu(): # Main Menu screen
    pygame.display.set_caption("Menu")

    while True:
        
        screen.blit(background_.image, background_.rect)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, (255, 255, 255))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#----------------------------------- pause screen ---------------------------
def paused():
    pause = True

    largeText = pygame.font.Font("assets/FiraCode-Regular.ttf",32)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)

def resume():

    pass

main_menu()