#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  card.py
#  
#  @emiliosmoreno
#  Clase que representa una carta
import pygame # Import all available pygame modules

class Card:

    ANCHO=100
    ALTO=160

    # Método de inicialización 
    # Constructor parametrizado  
    def __init__(self,n, p, x, y):
        self.visible=False
        self.numero=n
        self.palo=p
        self.posx=x
        self.posy=y
        
    def __init__(self,n, p):
        self.visible=False
        self.numero=n
        self.palo=p

    def pintar_carta(self,escena):
        self.escena=escena
        if (not self.visible):
            self.img = pygame.image.load('card_game_memory/img/cards/card_back_red.png')
        else:
            self.img = pygame.image.load('card_game_memory/img/cards/'+str(self.palo)+str(self.numero)+'.png')

        self.img = pygame.transform.scale(self.img , (Card.ANCHO,Card.ALTO)) # Scale the loaded card image
        self.escena.blit(self.img,(self.posx,self.posy))  
    
    def mostrar_carta(self):
        self.visible=True

    def ocultar_carta(self):
        self.visible=False

    def cambiar_carta(self):
        self.visible=not self.visible

    def setPosX(self,x):
        self.posx=x
    
    def setPosY(self,y):
        self.posy=y