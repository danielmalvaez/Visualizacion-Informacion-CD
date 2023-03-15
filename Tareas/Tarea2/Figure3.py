# Alumno: Axel Daniel Malváez Flores
# No. Cuenta: 318315126
# Materia: Visualización de la Información

import turtle

sc = turtle.Screen()
sc.bgcolor('white')

sc.setup(600,600)
sc.setworldcoordinates(-8,-8,6,6)
sc.tracer(0,0)

sc.title('BUCKLING FRAME')
turtle.shape('turtle')

black = 'black'
white = 'white'

def draw_board():
    for x in range(-7, 6, 2):
        for y in range(-7, -5, 2):
            draw_square(x, y, 1, black)
            draw_diag(x, y)
            if x < 5:
                draw_diag(x+1,y)
        for y in range(5, 7, 2):
            draw_square(x, y, 1, black)
            draw_diag(x, y)
            if x < 5:
                draw_diag(x+1,y)
    draw_diag(5, 4)
    draw_diag(-7, -6)

    for x in range(-6, 6, 2):
        for y in range(-6, -4, 2):
            draw_square(x, y, 1, black)
            draw_diag(x, y)
            draw_diag(x+1, y)
        for y in range(4, 6, 2):
            draw_square(x, y, 1, black)
            draw_diag(x, y)
            draw_diag(x-1,y)
    
    for y in range(-5, 5, 2):
        for x in (-7, 5):
            draw_square(x, y, 1, black)
            draw_diag(x, y)
            if x > 0:
                draw_diag(x-1, y)
            else:
                draw_diag(x+1, y)
    
    for y in range(-4, 4, 2):
        for x in (-6, 4):
            draw_square(x, y, 1, black)
            draw_diag(x,y)
            if x < 0:
                draw_diag(x-1, y)
            else:
                draw_diag(x+1, y)

def draw_square(x,y,size,c):
    turtle.up()
    turtle.goto(x-size/2,y-size/2)
    turtle.seth(0)
    turtle.color(c)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(size)
        turtle.left(90)
    turtle.end_fill()

def draw_diag(x,y):
    c = white if (x+y)%2 == 0 else black
    if x*y >= 0:
        draw_square(x-0.3,y+0.3,0.3,c)
        draw_square(x+0.3,y-0.3,0.3,c)
    elif x*y < 0:
        draw_square(x+0.3,y+0.3,0.3,c)
        draw_square(x-0.3,y-0.3,0.3,c)

turtle.speed(0)
draw_board()

turtle.exitonclick()