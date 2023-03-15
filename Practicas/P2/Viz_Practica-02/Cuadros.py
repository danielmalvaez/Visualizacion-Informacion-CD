# CIENCIA DE DATOS: VISUALIZACIÓN DE LA INFORMACIÓN
# UNAM-IIMAS, SEMESTRE 2023-2

# PRACTICA-02: ESPACIOS DE COLOR E ILUSIONES ÓPTICAS

#ILUSION ÓPTICA COMBINANDO CUADROS NEGROS Y LINEAS ROJAS
import turtle

#Definimos los parámetros de la línea:
#Punto inicial (xFrom,yFrom) a punto final (xTo,yTo):
def drawLine(xFrom, yFrom, xTo, yTo, color, size=1):
    
    global myLapiz
    
    # Grueso de la línea
    myLapiz.pensize(size)
    
    #Alzar lápiz
    myLapiz.penup()
    myLapiz.color(color)
    myLapiz.goto(xFrom,yFrom)
    
    #Bajar lápiz
    myLapiz.pendown()
    myLapiz.goto(xTo,yTo)

#Definimos los parámetros del cuadrado:
def drawSquare(x, y, size, color):
    global myLapiz
    myLapiz.setheading(0)
    
    #Alzar lápiz
    myLapiz.penup()
    myLapiz.goto(x,y)
    myLapiz.color(color)
    myLapiz.fillcolor(color)    
    
    #Bajar lápiz
    myLapiz.pendown()
    
    #Rellenar la figura del color:
    myLapiz.begin_fill()
    myLapiz.forward(size)
    myLapiz.left(90)
    myLapiz.forward(size)
    myLapiz.left(90)
    myLapiz.forward(size)
    myLapiz.left(90)
    myLapiz.forward(size)
    myLapiz.end_fill()
    
myLapiz = turtle.Turtle()

#Establecer la figura del lápiz, flecha o tortuga (turtle)
myLapiz.shape("arrow")

#Velocidad del trazado de la línea:
myLapiz.speed(2)

#Crear un conjunto de cuadros negros y lineas rojas
#de acuerdo a las siguientes coordenadas:

for i in range(4):
    for j in range(12):
        drawSquare(80*j+20,80*i,40,"Black")
        drawLine(0,80*i,600,80*i,"red", size=3)
        drawSquare(80*j,80*i+40,40,"Black")
        drawLine(0,80*i+40,600,80*i+40,"red", size=3)

#¿LAS LINEAS ROJAS SERÁN PARALELAS?
turtle.done()