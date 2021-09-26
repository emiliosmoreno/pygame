#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  @emiliosmoreno
#  Clase principal que controla el juego


import pygame # Import all available pygame modules
import sys, os
from constantes import * #Importamos nuestro módulo constantes
from eventos import * #Importamos nuestro módulo para gestionar los eventos
from utilidades import * #Importamos nuestro módulo que contiene las utilidades
from chessgame import *
from pygame.locals import *

class Main:
    
     # Método de inicialización   
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Chess Game! by @emiliosmoreno")
        pygame.font.init()
        
        #definición de atributos del juego
        self.escena=pygame.display.set_mode(Constantes.SIZE_WINDOW)
        self.clock = pygame.time.Clock()
        self.en_pausa=False     #Define si el juego está en pause o no
        self.large_font = pygame.font.SysFont("Arial", 50)
        self.small_font = pygame.font.SysFont("Arial", 25)
        Utilidades.pintar_icono(self)

        self.game=ChessGame(self.escena)
        
    # Ejecución del juego      
    def run(self):
        while True: # Bucle principal  

            self.clock.tick(Constantes.VELOCIDAD)
            self.escena.fill(Constantes.COLOR_BLACK) #Se borra toda la escena

            while not self.en_pausa: 
                ManejadorEventos.run(self)
                Utilidades.pintar_pausa_juego(self)
                ChessGame.pintar_tablero(self)
                pygame.display.update() #Se actualiza la escena

            ManejadorEventos.run(self)
            Utilidades.pintar_pausa_juego(self)
            pygame.display.update() #Se actualiza la escena

 

# Llamada principal          
if __name__ == "__main__":
    pygame.init()
    Main().run()