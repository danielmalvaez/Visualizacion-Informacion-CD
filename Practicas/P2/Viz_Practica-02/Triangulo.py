# CIENCIA DE DATOS: VISUALIZACIÓN DE LA INFORMACIÓN
# UNAM-IIMAS, SEMESTRE 2023-2

# PRACTICA-02: ESPACIOS DE COLOR E ILUSIONES ÓPTICAS

# ILUSION ÓPTICA DE ESPIRAL MEDIANTE TRAZADO DE TRIANGULOS ROTADOS

import turtle

# Seleccionar el color de fondo de pantalla
scr=turtle.Screen()
scr.bgcolor("black")

colors = ['red', 'purple', 'cyan', 'green', 'orange', 'yellow']

dist = 1
flag = 500
spiral = turtle.Turtle()
spiral.speed(10)
while flag:
    spiral.pencolor(colors[flag%6])
    spiral.forward(5+dist)
    spiral.right(120)
    spiral.left(1)
    dist += 1
    flag -= 1
    
turtle.done()