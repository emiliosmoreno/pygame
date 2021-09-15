#!/usr/bin/env python

import pygame # Import all available pygame modules
import sys
from pygame.locals import *

class PyGameClass:
    # Método de inicialización   
    def __init__(self):
        pygame.display.set_mode((400, 300))
        pygame.display.set_caption('Hello World!')
    
     # Ejecución del juego      
    def run(self):
        while True: # main game loop
            #for evento in pygame.event.get():
            #    if evento.type == K_p:
            #        pygame.quit()
            #        sys.exit()
            pygame.display.update()

# Llamada principal          
if __name__ == "__main__":
    pygame.init()
    PyGameClass().run()