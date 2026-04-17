import sys 

import pygame 

from clock import FPS, HEIGHT, WIDTH, MickeyClock 

def main(): 
    pygame.init()  # initializes Pygame and all its modules

    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption("Mickey's Clock") 
    clock = pygame.time.Clock()# used to control the frame rate (FPS)
    mickey_clock = MickeyClock() # creates a clock object

    running = True
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False

        mickey_clock.draw(screen) 
        pygame.display.flip() # updates the full display surface to the screen 
       
        clock.tick(FPS) # limits the loop to FPS frames per second
    pygame.quit()  # shuts down Pygame and closes all related windows, freeing resources
    sys.exit() # exits the program with code 0 (successful termination)



if __name__ == "__main__": 
    main()