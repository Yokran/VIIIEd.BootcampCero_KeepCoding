import pygame as pg
from random import randrange

TAMANNO = (800, 600)

class Movil():
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    @property
    def izquierda(self):
        return self.x

    @izquierda.setter
    def izquierda(self, valor):
        self.x = valor

    @property
    def derecha(self):
        return self.x + self.w

    @derecha.setter
    def derecha(self, valor):
        self.x = valor - self.w

    @property
    def arriba(self):
        return self.y
    
    @arriba.setter
    def arriba(self, valor):
        self.y = valor

    @property
    def abajo(self):
        return self.y + self.h

    @abajo.setter
    def abajo(self, valor):
        self.y = valor - self.h

    def actualizate(self):
        pass

    def dibujate(self, lienzo):
        pg.draw.rect(lienzo, self.color, 
                pg.Rect(self.x, self.y, self.w, self.h))

    def procesa_eventos(self, lista_eventos=[]):
        pass

class Raqueta(Movil):
    def __init__(self, x, y, color=(255, 255, 255)):
        Movil.__init__(self, x, y, 20, 130, color)
        self.tecla_arriba = pg.K_UP
        self.tecla_abajo = pg.K_DOWN
        
    def procesa_eventos(self, lista_eventos=[]):
        if pg.key.get_pressed()[self.tecla_arriba]:
            self.y -= 5

        if self.arriba <= 0:
            self.y = 0

        if pg.key.get_pressed()[self.tecla_abajo]:
            self.y += 5

        if self.abajo >= TAMANNO[1]:
            self.abajo = TAMANNO[1]

            # self.y = TAMANNO[1] - self.h
      
class Bola(Movil):
    def __init__(self, x, y, color=(255, 255, 255)):
        super().__init__(x, y, 20, 20, color)
       
        self.swDerecha = True
        self.swArriba = True

        self.incremento_x = 5
        self.incremento_y = 5

    def actualizate(self):
               
        if self.swDerecha:
            self.x += 5
        else:
            self.x -= 5

        if self.izquierda >= TAMANNO[0]:
            self.swDerecha = False

        if self.derecha <= 0:
            self.swDerecha = True

        if self.swArriba:
            self.y -= 5
        else:
            self.y += 5

        if self.abajo >= TAMANNO[1]:
            self.swArriba = True

        if self.arriba <= 0:
            self.swArriba = False
        
        """
        self.x += self.incremento_x
        self.y += self.incremento_y
       
        if self.x + self.w > TAMANNO[0] or self.x < 0:
           self.incremento_x *= -1
        if self.y + self.h > TAMANNO[1] or self.y < 0:
           self.incremento_y *= -1
        """

        print("X - Posicion: {} Derecha: {}".format(self.x, self.swDerecha))
    
    def comprobar_choque(self, algo):
        return self.derecha >= algo.izquierda and self.izquierda <= algo.derecha and \
            self.abajo >= algo.arriba and self.arriba <= algo.abajo
       

class Game():

    def __init__(self):
        self.pantalla = pg.display.set_mode(TAMANNO)
        self.reloj = pg.time.Clock()
        self.todos = []   

        self.player1 = Raqueta(10, (TAMANNO[1] -120) //2)
        self.player1.tecla_arriba = pg.K_w
        self.player1.tecla_abajo = pg.K_s
        self.player2 = Raqueta(TAMANNO[0] - 30, (TAMANNO[1] - 120) //2)

        self.todos.append(self.player1)
        self.todos.append(self.player2)


        self.bola = Bola(TAMANNO[0] // 2 - 10, TAMANNO[1] // 2 - 10, (255, 255, 0))
        
        self.todos.append(self.bola)
    
    def bucle_principal(self):
        game_over = False
        pg.init()

        while not game_over:
            self.reloj.tick(60)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            for movil in self.todos:
                movil.procesa_eventos(eventos)

            if self.bola.comprobar_choque(self.player1) or \
                self.bola.comprobar_choque(self.player2):
                self.bola.swDerecha = not self.bola.swDerecha

            for movil in self.todos:
                movil.actualizate()


            self.pantalla.fill((0, 0, 0))

            for movil in self.todos:
                movil.dibujate(self.pantalla)
              
            pg.display.flip()
        
        pg.quit()


if __name__ == '__main__':
    juego = Game()
    juego.bucle_principal()

print(__name__)

        
