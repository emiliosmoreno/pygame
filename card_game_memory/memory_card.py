#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  memory_card_game.py
#  
#  @emiliosmoreno
#  Clase principal que controla el juego

from card import * #Importamos nuestro módulo que representa una carta

class MemoryCardGame:

    # Método de inicialización   
    def __init__(self, escena):
        self.mesa=list()    #inicialización de las cartas
        self.escena=escena

        carta1=Card('01','c',100,160)
        carta2=Card('01','d',250,160)
        carta3=Card('01','h',400,160)
        carta4=Card('01','s',550,160)

        self.mesa.append(carta1)
        self.mesa.append(carta2)
        self.mesa.append(carta3)
        self.mesa.append(carta4)

    def pintar_cartas(self, mesa, escena):
        self.mesa=mesa
        for carta in self.mesa:
            Card.pintar_carta(carta, self.escena)

    def manejar_eventos(self, evento):

        # handle MOUSEBUTTONUP
        if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos() 
                MemoryCardGame.cambiar_cartas(self, self.mesa, pos[0], pos[1]) 

    def cambiar_cartas(self, mesa, x, y):
        self.mesa=mesa
        for carta in self.mesa:
            if (x >= carta.posx and x<=carta.posx+100):
                if (y>=carta.posy and y<=carta.posy+160):
                    Card.cambiar_carta(carta)
            
