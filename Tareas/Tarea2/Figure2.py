# Alumno: Axel Daniel Malváez Flores
# No. Cuenta: 318315126
# Materia: Visualización de la Información

import turtle

sc = turtle.Screen()
sc.setup(600,600)
sc.setworldcoordinates(-200,-200,200,200)
sc.title('SPIRAL SIMULATION')
turtle.shape('turtle')

colors = ['lime', 'red', 'blue violet', 'yellow']
t = turtle.Pen()
t.speed(0)

turtle.bgcolor('black')
for x in range(150):
    t.pencolor(colors[x%4])
    t.width(x//100 + 1)
    t.forward(x)
    t.right(89)
    
turtle.exitonclick()