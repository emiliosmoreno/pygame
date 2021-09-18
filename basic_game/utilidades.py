#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utilidades.py
#  
#  @emiliosmoreno
#  Clase que contiene utilidades

import pygame # Import all available pygame modules
import sys
from constantes import * #Importamos nuestro módulo constantes

class Utilidades:

    # Método encargado de gestionar el aviso de pausa en el juego
    # requisito: debe existir un atributo denominado 'en_pausa', de tipo boolean
    def pintar_pausa_juego(self):

        if (self.en_pausa): 
            self.escena.blit(
                self.font.render("PAUSA",-1,Constantes.COLOR_WHITE),
                                (Constantes.WIDTH/2 - 50, 50)) 
            
            