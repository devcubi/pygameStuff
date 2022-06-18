# Rectangulo con bordes -Fabrizio Cubilla- 
import pygame as pg
import sys, time
from math import pi, sin, cos

# Colors 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRIS = (100, 100, 100)
ROJO = (255, 10, 10)
VERDE = (57, 255, 20)
YELLOW = (255,233,0)

P_Alto = 600
P_Ancho = 800

# Window center
center = {
    'x': P_Ancho/2,
    'y': P_Alto/2
}

def linea(punto1, punto2, bordes):
    x1,y1 = punto1
    x2,y2 = punto2

    # Diagonal conecta p1 con p2
    pg.draw.aaline(screen, ROJO, (x1 ,y1), (x2, y2))

    # Linea Horizontal Superior
    pg.draw.aaline(screen, WHITE, (x1 +bordes*(x2-x1)/2,y1), (x2-bordes*(x2-x1)/2, y1))
    pg.draw.circle(screen, BLUE, (x2,y2-(y2-y1)), 2)

    # Linea Horizontal Inferior
    pg.draw.aaline(screen, WHITE, (x1+bordes*(x2-x1)/2,y2), (x2-bordes*(x2-x1)/2, y2))
    pg.draw.circle(screen, BLUE, (x1,y1+(y2-y1)), 2)

    # Linea Vertical Izquierda
    pg.draw.aaline(screen, WHITE, (x1,y1+bordes*(y2-y1)/2), (x1, y2-bordes*(y2-y1)/2))
    pg.draw.circle(screen, VERDE, (x2-(x2-x1), y2), 2)
    
    # Linea Vertical Derecha
    pg.draw.aaline(screen, WHITE, (x2,y1+bordes*(y2-y1)/2), (x2, y2-bordes*(y2-y1)/2))
    pg.draw.circle(screen, VERDE, (x2, y2), 2)

    # Puntos Originales Dados
    pg.draw.circle(screen, ROJO, (x1,y1), 1.0)
    pg.draw.circle(screen, ROJO, (x2,y2), 1.0)


def bordes(punto1, punto2, bordes, cantidad_rectas):
    x1,y1 = punto1
    x2,y2 = punto2

    # Ubicacion en Superior-Izquierda
    pg.draw.circle(screen, ROJO , (x1 +bordes*(x2-x1)/2,y1+bordes*(y2-y1)/2), 2)
    drawBorder(punto1, punto2, x1 +bordes*(x2-x1)/2 , y1+bordes*(y2-y1)/2, bordes, cantidad_rectas, 0.5, pi)

    # Ubicacion en Superior-Derecha
    pg.draw.circle(screen, BLUE , (x2-bordes*(x2-x1)/2, y1+bordes*(y2-y1)/2), 2)
    drawBorder(punto1, punto2, x2-bordes*(x2-x1)/2, y1+bordes*(y2-y1)/2, bordes, cantidad_rectas, -0.5, 0)

    # Ubicacion en Inferior-Derecha 
    pg.draw.circle(screen, YELLOW , (x2-bordes*(x2-x1)/2, y2-bordes*(y2-y1)/2), 2)
    drawBorder(punto1, punto2, x2-bordes*(x2-x1)/2, y2-bordes*(y2-y1)/2, bordes, cantidad_rectas, 0.5, 0)

    # Ubicacion en Inferior-Izquierda 
    pg.draw.circle(screen, VERDE , (x1+bordes*(x2-x1)/2, y2-bordes*(y2-y1)/2), 2)
    drawBorder(punto1, punto2, x1+bordes*(x2-x1)/2, y2-bordes*(y2-y1)/2, bordes, cantidad_rectas, -0.5, pi)
   

def drawBorder(punto1, punto2,  r1, r2 , bordes, cantidad_rectas, sector, dS):
    x1, y1 = punto1
    x2, y2 = punto2
    #print(f'{punto1} - {punto2} , R1 = {r1} - R2 = {r2} - {bordes} ')
    #pg.draw.circle(screen, VERDE, (r1,r2), 2)
    for i in range(0, cantidad_rectas):
        # Calculamos los cuatro puntos para la siguiente recta.
        angulo1 =  i* (sector*pi/cantidad_rectas) + dS
        angulo2 =  (i+1) * (sector*pi/cantidad_rectas) + dS
        Xa = r1 + (bordes*(x2-x1)/2)*cos(angulo1)
        Ya = r2 + (bordes*(y2-y1)/2)*sin(angulo1)
        Xb = r1 + (bordes*(x2-x1)/2)*cos(angulo2)
        Yb = r2 + (bordes*(y2-y1)/2)*sin(angulo2)
        #print(f'{i} (x1 = {cos(angulo1)}, y1 = {sin(angulo1)}| x2={cos(angulo2)}, y2={sin(angulo2)}')
        #print(f'Puntos=<{i}-- {Xa},{Ya} ---- {Xb},{Yb}')
        pg.draw.aaline(screen, WHITE, (Xa, Ya), (Xb, Yb))        
        #pg.draw.circle(screen, VERDE, (Xa,Ya), 1)
        #pg.draw.circle(screen, ROJO, (Xb,Yb), 2)


        
   

def main():
    pg.init()
    PUNTO1 = (100, 100)
    PUNTO2 = (200, 200)
    #PUNTO1 = (100, 100)
    #PUNTO2 = (600, 500)
    # 0 <= x <= 1    // 0 == Rectangulo, 1 == Ovalo
    BORDE = 0.15
    CANTIDAD_RECTAS = 64

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill(BLACK)

        linea( PUNTO1, PUNTO2, BORDE )
        bordes( PUNTO1, PUNTO2, BORDE, CANTIDAD_RECTAS )

        pg.display.update()

if __name__ == "__main__":
    pg.display.set_caption("Rectangulo con bordes")
    screen = pg.display.set_mode((P_Ancho, P_Alto))
    main()