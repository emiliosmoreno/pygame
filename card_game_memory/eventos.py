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
from memory_card import * #Importamos el juego de cartas 'Memory'

class ManejadorEventos:

    def run(self):
        eventos = pygame.event.get()  
        for evento in eventos:

            if evento.type == pygame.QUIT:  #Si se presiona la X para cerrar la ventana
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:   #Si se presiona una tecla
                if (evento.key == pygame.K_p):      #Si la tecla es la 'p' (es case-sensitive)
                    self.en_pausa = not self.en_pausa
            
            MemoryCardGame.manejar_eventos(self, evento)