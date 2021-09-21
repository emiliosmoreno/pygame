#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  memory_card_game.py
#  
#  @emiliosmoreno
#  Clase principal que controla el juego

from card import * #Importamos nuestro módulo que representa una carta
from constantes import * #Importamos nuestro módulo que representa una carta
import random
from pygame.locals import *

class MemoryCardGame:
    MAX_CARDS=5
    MAX_CARDS_IN_TABLE=MAX_CARDS*2

    # Método de inicialización   
    def __init__(self, escena):
        self.mesa=list()    #inicialización de las cartas
        self.escena=escena
        self.carta_seleccionada=None #Las cartas seleccionadas

        for numero in range(1,13):
            for palo in ('c','d','h','s'):
                carta=Card('00','x')
                if (numero<10):
                    carta.numero='0'+str(numero);
                else:
                    carta.numero=numero;
                carta.palo=palo 
                carta.setPosX(0)
                carta.setPosY(0)
                self.mesa.append(carta)

        #se desordenan las cartas
        for todas in range (0,len(self.mesa)):
            random.shuffle(self.mesa)

        #Se copian exactamente la mitad de cartas posibles
        mesa_temporal=self.mesa[0:MemoryCardGame.MAX_CARDS]
        for carta in self.mesa[0:MemoryCardGame.MAX_CARDS]:
            copia_carta=Card('00','x')
            copia_carta.numero=carta.numero
            copia_carta.palo=carta.palo
            copia_carta.posx=carta.posx
            copia_carta.posy=carta.posy
            mesa_temporal.append(copia_carta)
        self.mesa=mesa_temporal

        #se desordenan, de nuevo, las cartas
        for todas in range (0,len(mesa_temporal)):
            random.shuffle(self.mesa)


    def colocar_cartas_mesa(self):
        #Setear las posiciones
        x_inicial=50
        y_inicial=50
        x=x_inicial
        y=y_inicial
        ncartas=0
        while (y < Constantes.HEIGHT and ncartas<MemoryCardGame.MAX_CARDS_IN_TABLE):
            cartas_por_fila=0
            while (x < Constantes.WIDTH and cartas_por_fila<MemoryCardGame.MAX_CARDS): 
                self.mesa[ncartas].setPosX(x)
                self.mesa[ncartas].setPosY(y)
                ncartas=ncartas+1
                x=x+Card.ANCHO+25  
                cartas_por_fila=cartas_por_fila+1        
            y=y+Card.ALTO+10    #Se salta de linea
            x=x_inicial     #Se empieza de nuevo al inicio de la fila 

    def pintar_cartas(self, mesa, escena):
        self.mesa=mesa
        for pos in range(0,MemoryCardGame.MAX_CARDS_IN_TABLE):
            Card.pintar_carta(self.mesa[pos], self.escena)

    def manejar_eventos(self, evento):
        # handle MOUSEBUTTONUP
        if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos() 
                MemoryCardGame.cambiar_cartas(self, pos[0], pos[1]) 

    def cambiar_cartas(self, x, y): 
        for pos in range(0,MemoryCardGame.MAX_CARDS_IN_TABLE):
            carta=self.game.mesa[pos]
            if (x >= carta.posx and x<=carta.posx+Card.ANCHO):
                if (y>=carta.posy and y<=carta.posy+Card.ALTO):
                    if (self.game.carta_seleccionada==None):
                        self.game.carta_seleccionada=carta
                        Card.cambiar_carta(carta)
                    else:
                        print("Carta seleccionada: "+str(self.game.carta_seleccionada.numero)+"-"+str(self.game.carta_seleccionada.palo))
                        print("Carta: "+str(carta.numero)+"-"+str(carta.palo))
                        esIgual=False
                        if (carta.numero==self.game.carta_seleccionada.numero and carta.palo==self.game.carta_seleccionada.palo):
                            esIgual=True
                            print("Son iguales")
                        
                        if (esIgual):
                            
                            Card.cambiar_carta(carta)
                            self.escena.fill(Constantes.COLOR_BLACK) #Se borra toda la escena 
                            MemoryCardGame.pintar_cartas(self, self.game.mesa, self.escena)                
                            pygame.display.update() #Se actualiza la escena
                            pygame.time.wait(2000)

                            self.game.carta_seleccionada.setPintar(False)
                            carta.setPintar(False)
                            self.game.carta_seleccionada=None
                            
                        else:
                            esIgual=False
                            Card.cambiar_carta(carta)
                            self.escena.fill(Constantes.COLOR_BLACK) #Se borra toda la escena 
                            MemoryCardGame.pintar_cartas(self, self.game.mesa, self.escena)                
                            pygame.display.update() #Se actualiza la escena
                            pygame.time.wait(2000)

                            Card.cambiar_carta(self.game.carta_seleccionada)
                            Card.cambiar_carta(carta)
                            self.game.carta_seleccionada=None
            
