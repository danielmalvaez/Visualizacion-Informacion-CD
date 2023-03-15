# CIENCIA DE DATOS: VISUALIZACIÓN DE LA INFORMACIÓN
# UNAM-IIMAS, SEMESTRE 2023-2

# PRACTICA-02: ESPACIOS DE COLOR E ILUSIONES ÓPTICAS

# ILUSION ÓPTICA DE UN BENZENO ARCOIRIS

import turtle
colors = ['red', 'orange', 'purple', 'blue', 'green', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%4])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(859)
    
turtle.done()
turtle.exitonclick()