# CIENCIA DE DATOS: VISUALIZACIÓN DE LA INFORMACIÓN
# UNAM-IIMAS, SEMESTRE 2023-2

# PRACTICA-02: ESPACIOS DE COLOR E ILUSIONES ÓPTICAS

#ILUSION ÓPTICA USANDO LINEAS NEGRAS Y ROJAS
import turtle

#Definimos los parámetros de las líneas:
def drawLine(xFrom, yFrom, xTo, yTo, color, size=1):
    
    # Definimos la variable global
    global mylapiz
    
    # Grueso de la línea
    mylapiz.pensize(size)
    
    #Alzar el lápiz
    mylapiz.penup()
    mylapiz.color(color)
    
    #Establecer el punto (x,y) de origen:
    mylapiz.goto(xFrom,yFrom)
    
    #Bajar el lápiz
    mylapiz.pendown()
    
    #Moverse al segundo punto
    mylapiz.goto(xTo,yTo)

mylapiz = turtle.Turtle()

#Forma del lapiz: flecha o tortuga (turtle)
mylapiz.shape("arrow")

#Velocidad del trazo de línea
mylapiz.speed(2)

#Crear varias líneas a partir de un solo punto de origen:
for i in range(20):
    drawLine(0,150,300,20*i + 150,'Black')
    drawLine(0,150,300,-20*i + 150,'Black')

#Dibujar un rectángulo de acuerdo a las siguientes coordenadas:
    # drawLine(xFrom,yFrom,xTo,yTo,"color")
    
drawLine(80,100,250,100,'red', size=3)
drawLine(250,100,250,200,'red', size=3)
drawLine(250,200,80,200,'red', size=3)
drawLine(80,200,80,100,'red', size=3)

turtle.done()

