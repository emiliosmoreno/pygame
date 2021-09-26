#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eventos.py
#  
#  @emiliosmoreno
#  Clase que maneja los eventos del juego

import pygame # Import all available pygame modules
import sys
from constantes import * #Importamos nuestro módulo constantes

class ManejadorEventos:

    def run(self):
          
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  #Si se presiona la X para cerrar la ventana
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:   #Si se presiona una tecla
                if (evento.key == pygame.K_p):      #Si la tecla es la 'p' (es case-sensitive)
                    self.en_pausa = not self.en_pausa
            
            