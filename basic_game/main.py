#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  @emiliosmoreno
#  Clase principal que controla el juego

import pygame # Import all available pygame modules
import sys
from constantes import * #Importamos nuestro módulo constantes
from eventos import * #Importamos nuestro módulo para gestionar los eventos
from utilidades import * #Importamos nuestro módulo que contiene las utilidades
class Main:
    
     # Método de inicialización   
    def __init__(self):
        
        pygame.display.set_caption("Hello World! by @emiliosmoreno")
        pygame.font.init()
        
        #definición de atributos del juego
        self.escena=pygame.display.set_mode(Constantes.SIZE_WINDOW)
        self.clock = pygame.time.Clock()
        self.en_pausa=False     #Define si el juego está en pause o no
        self.font = pygame.font.SysFont("Arial", 50)

    # Ejecución del juego      
    def run(self):
        while True: # main game loop  

            self.clock.tick(Constantes.VELOCIDAD)
            self.escena.fill(Constantes.COLOR_BLACK) 

            while not self.en_pausa: 
                ManejadorEventos.run(self)
                Utilidades.pintar_pausa_juego(self)
                pygame.display.update()

            ManejadorEventos.run(self)
            Utilidades.pintar_pausa_juego(self)
            pygame.display.update()

 

# Llamada principal          
if __name__ == "__main__":
    pygame.init()
    Main().run()