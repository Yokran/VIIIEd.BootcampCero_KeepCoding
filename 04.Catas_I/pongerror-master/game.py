import pygame as pg

TAMANNO = (800, 600)

class Bola():
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.derecha = True
        self.arriba = True

        self.incremento_x = 5
        self.incremento_y = 5

    def actualizate(self):
        
       '''
        if self.derecha:
            self.x += 5
        else:
            self.x -= 5

        if self.x +self.w >= TAMANNO[0]:
            self.derecha = False

        if self.x <= 0:
            self.derecha = True

        if self.arriba:
            self.y -= 5
        else:
            self.y += 5

        if self.y + self.h >= TAMANNO[1]:
            self.arriba = True

        if self.y <= 0:
            self.arriba = False
       '''

       self.x += self.incremento_x
       self.y += self.incremento_y
       
       if self.x + self.w > TAMANNO[0] or self.x < 0:
           self.incremento_x *= -1
       if self.y + self.h > TAMANNO[1] or self.y < 0:
           self.incremento_y *= -1
       

class Game():

    def __init__(self, w, h):
        self.pantalla = pg.display.set_mode(TAMANNO)
        self.reloj = pg.time.Clock()
      
    def bucle_principal(self):
        bola = Bola(TAMANNO[0] // 2, TAMANNO[1] // 10, 20, 20)
        game_over = False
        pg.init()

        while not game_over:
            self.reloj.tick(60)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            bola.actualizate()
            
            self.pantalla.fill((0, 0, 0))
            pg.draw.rect(self.pantalla, bola.color, pg.Rect(bola.x, bola.y, bola.w, bola.h))

            pg.display.flip()
        
        pg.quit()
        
pg.init()


if __name__ == '__main__':
    juego = Game(800, 600)
    juego.bucle_principal()

print(__name__)

        
