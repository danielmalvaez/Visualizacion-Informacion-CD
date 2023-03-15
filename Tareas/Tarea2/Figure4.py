# Alumno: Axel Daniel Malváez Flores
# No. Cuenta: 318315126
# Materia: Visualización de la Información


import turtle

sc = turtle.Screen()
sc.bgcolor('white')

sc.setup(500,500)

sc.title('BLACK POINTS ON A GRID')
turtle.shape('turtle')

def draw_line(xFrom, yFrom, xTo, yTo, color = 'grey', size = 6):
    # Grueso de la línea
    turtle.pensize(size)
    # Alzar el lápiz
    turtle.penup() 
    # Definir color 
    turtle.color(color)
    #Establecer el punto (x,y) de origen:
    turtle.goto(xFrom,yFrom)
    #Bajar el lápiz
    turtle.pendown()
    #Moverse al segundo punto
    turtle.goto(xTo,yTo)

def drawCircle(x, y, radius, color):
    turtle.setheading(0)
    #Alzar Lápiz
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.pencolor('white')
    #Moverse al siguiente punto
    turtle.goto(x,y-radius)
    #Realizar figura
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    #Bajar Lápiz
    turtle.pendown()

turtle.speed(0)

# lineas horizontales
for i in range(-300, 250, 50):
    draw_line(-300, i+50, 300, i+50)    
# lineas verticales
for i in range(-300, 250, 50):
    draw_line(i+50, -300, i+50, 300)
# lineas diagonales m +
for line in range(-300, 300, 100):
    draw_line(-300, line, -line, 300)
    draw_line(line, -300, 300, -line)    
# lineas diagonales m -
for x in range(-300, 300, 100):
    draw_line(x, -300, -300, x)
    draw_line(300, x, x, 300)

# Circulos negros
drawCircle(-200, -200, 6 , "white smoke")
drawCircle(-200, -200, 5 , "black")
drawCircle(-200, 0, 6 , "white smoke")
drawCircle(-200, 0, 5 , "black")
drawCircle(-200, 200, 6 , "white smoke")
drawCircle(-200, 200, 5 , "black")

drawCircle(0, -200, 6 , "white smoke")
drawCircle(0, -200, 5 , "black")
drawCircle(0, 0, 6 , "white smoke")
drawCircle(0, 0, 5 , "black")
drawCircle(0, 200, 6 , "white smoke")
drawCircle(0, 200, 5 , "black")

drawCircle(200, -200, 6 , "white smoke")
drawCircle(200, -200, 5 , "black")
drawCircle(200, 0, 6 , "white smoke")
drawCircle(200, 0, 5 , "black")
drawCircle(200, 200, 6 , "white smoke")
drawCircle(200, 200, 5 , "black")

turtle.hideturtle()
turtle.exitonclick()