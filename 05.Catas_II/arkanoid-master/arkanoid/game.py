from arkanoid.escenas import Portada, Partida, Records
import pygame as pg
from arkanoid import ALTO, ANCHO, FPS


pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.escenas = [Portada(pantalla), Partida(pantalla), Records(pantalla)]

    def start(self):
        i = 0
        while True:
            self.escenas[i].bucle_principal()
            i += 1
            if i == len(self.escenas):
                i = 0
                
            # fórmula matemática equivalente al if de arriba
            # i = (i + 1) % len(self.escenas)
        

