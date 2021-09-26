#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chess_game.py
#  
#  @emiliosmoreno
#  Clase principal del juego de Ajedrez

import pygame # Import all available pygame modules
from pygame.locals import *

class ChessGame:
    NUM_FILAS=8
    NUM_COLUMNAS=8
    TABLERO=(NUM_FILAS*NUM_COLUMNAS)
    TAMAÑO_CASILLA=50
    MARGEN=6 #Debe ser un numero par

    COLOR_WHITE=(255,255,255)
    COLOR_BLACK=(111,111,111)

    # Método de inicialización   
    def __init__(self, escena):
        self.tablero=list()
        self.escena=escena

    def intercambiar_color(color):
        if (color==ChessGame.COLOR_WHITE):
            return ChessGame.COLOR_BLACK
        else:
            return ChessGame.COLOR_WHITE

    def pintar_tablero(self):
        x_ini=50
        y_ini=50
        color_inicial=ChessGame.COLOR_WHITE
        color=color_inicial
        fila=0
        columna=0
        while (fila < ChessGame.NUM_FILAS):
            while (columna < ChessGame.NUM_COLUMNAS):
                casilla = pygame.Rect(x_ini+fila*ChessGame.TAMAÑO_CASILLA, y_ini+columna*ChessGame.TAMAÑO_CASILLA, ChessGame.TAMAÑO_CASILLA, ChessGame.TAMAÑO_CASILLA)
                pygame.draw.rect(self.escena, color, casilla) 

                color=ChessGame.intercambiar_color(color)

                columna=columna+1
            fila=fila+1
            columna=0
            color=ChessGame.intercambiar_color(color)          

        #Peones blancos
        peon_blanco = pygame.image.load('chess_game/img/w_pawn.png')
        peon_blanco = pygame.transform.scale(peon_blanco , (ChessGame.TAMAÑO_CASILLA-ChessGame.MARGEN,ChessGame.TAMAÑO_CASILLA-ChessGame.MARGEN)) # Scale the loaded card image
        fila=6
        posy=y_ini+fila*ChessGame.TAMAÑO_CASILLA
        while (columna < ChessGame.NUM_COLUMNAS):
            posx=x_ini+columna*ChessGame.TAMAÑO_CASILLA           
            self.escena.blit(peon_blanco,(posx+ChessGame.MARGEN/2,posy+ChessGame.MARGEN/2))
            columna=columna+1

        #Peones negros
        columna=0
        peon_negro = pygame.image.load('chess_game/img/b_pawn.png')
        peon_negro = pygame.transform.scale(peon_negro , (ChessGame.TAMAÑO_CASILLA-ChessGame.MARGEN,ChessGame.TAMAÑO_CASILLA-ChessGame.MARGEN)) # Scale the loaded card image
        fila=1
        posy=y_ini+fila*ChessGame.TAMAÑO_CASILLA
        while (columna < ChessGame.NUM_COLUMNAS):
            posx=x_ini+columna*ChessGame.TAMAÑO_CASILLA           
            self.escena.blit(peon_negro,(posx+ChessGame.MARGEN/2,posy+ChessGame.MARGEN/2))
            columna=columna+1