# CIENCIA DE DATOS: VISUALIZACIÓN DE LA INFORMACIÓN
# UNAM-IIMAS, SEMESTRE 2023-2

# PRACTICA-02: ESPACIOS DE COLOR E ILUSIONES ÓPTICAS

# ILUSION ÓPTICA PARA GENERAR UN EFECTO DE PLANTA Y FLOR

import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
t.speed(3)
s.bgcolor('black')
h=0
n=80

for i in range(90):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.left(134)
    t.fd(i)
    
    for j in range(3):
        t.left(5)
        t.fd(i*2)
        t.left(22)
        
turtle.done()