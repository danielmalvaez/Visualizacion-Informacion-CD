# Alumno: Axel Daniel Malváez Flores
# No. Cuenta: 318315126
# Materia: Visualización de la Información

import turtle

sc = turtle.Screen()
sc.setup(600,600)
sc.bgcolor("white")
sc.title('CIRCLES')

def circulo(radio, x, y):
    turtle.speed("fastest")
    turtle.shape('turtle')
    turtle.color('black')
    turtle.penup()
    turtle.goto(x, y - radio)
    turtle.pendown()
    turtle.circle(radio)

def drawLine(xFrom, yFrom, xTo, yTo, color, size=1):
    turtle.pensize(size)
    turtle.penup()
    turtle.color(color)
    turtle.goto(xFrom,yFrom)
    turtle.pendown()
    turtle.goto(xTo,yTo)

x = 0
y = -100
for i in range(9):
    # circulo
    circulo(50, x, y)
    circulo(40, x, y)
    circulo(30, x, y)
    circulo(20, x, y)
    circulo(10, x, y)
    # linea
    drawLine(x - 50, y, x, y + 50, "purple", 3)
    drawLine(x, y + 50, x + 50, y, "purple", 3)
    drawLine(x + 50,y, x, y-50, "purple", 3)
    drawLine(x, y-50, x-50, y, "purple", 3)

    y += 100
    if i == 2:
        x = - 100
        y = -100
    if i == 5:
        x = 100
        y = -100


turtle.exitonclick()