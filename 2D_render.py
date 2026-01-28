import math
import pygame
from system import *

pygame.init()


WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption("Solar System Simulation")
YELLOW = (255,255, 0)
BLACK = (0,0,0)
BLUE  = (0,0, 255)



def main():
    run = True
    clock = pygame.time.Clock()

    solsys = SolarSystem()
   

    while run:
        clock.tick(60)
        #INDOW.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for planet in solsys.planets:
            planet.update_position(solsys.planets)
            planet.draw(WINDOW, WIDTH, HEIGHT)

        pygame.display.update()  
    
    pygame.quit()

main()