# Axel Daniel Malváez Flores
# 318315126
# Visualización de la Información

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

#Definimos los parámetros del círculo 
def drawCircle(x, y, radius, color):
    global mylapiz
    mylapiz.setheading(0)
    
    #Alzar Lápiz
    mylapiz.penup()
    
    mylapiz.color(color)
    mylapiz.fillcolor(color)
    
    #Moverse al siguiente punto
    mylapiz.goto(x,y-radius)
    
    #Realizar figura
    mylapiz.begin_fill()
    mylapiz.circle(radius)
    mylapiz.end_fill()
    
    #Bajar Lápiz
    mylapiz.pendown()

mylapiz = turtle.Turtle()

#Forma del lapiz: flecha o tortuga (turtle)
mylapiz.shape("arrow")

#Velocidad del trazo de línea
mylapiz.speed(7)

t = turtle.Turtle()
 
s = 200# int(input("Enter the length of the side of the Square: "))
 
# drawing first side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing second side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing third side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing fourth side
t.forward(s) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree

for i in range(5):
    drawLine(0 + (40*i), 0 , 200, 200 - (40 * i), 'black', size=1)

for i in range(5):
    drawLine(0, 40 * i , 200 - (40 * i), 200, 'black', size=1)

# for i in range(3):

# Primeras veticales
drawLine(20, 10 , 20, 30, 'black', size=1)
drawLine(100, 10 , 100, 30, 'black', size=1)
drawLine(180, 10 , 180, 30, 'black', size=1)
# Primeras horizontales
drawLine(50, 20 , 70, 20, 'black', size=1)
drawLine(130, 20 , 150, 20, 'black', size=1)

# Segundas verticales
drawLine(10, 60 , 30, 60, 'black', size=1)
drawLine(90, 60 , 110, 60, 'black', size=1)
drawLine(170, 60 , 190, 60, 'black', size=1)
# segundas horizontales
drawLine(60, 50 , 60, 70, 'black', size=1)
drawLine(140, 50 , 140, 70, 'black', size=1)


# Terceras verticales
drawLine(20, 90 , 20, 110, 'black', size=1)
drawLine(100, 90 , 100, 110, 'black', size=1)
drawLine(180, 90 , 180, 110, 'black', size=1)
# Terceras horizontales
drawLine(50, 100 , 70, 100, 'black', size=1)
drawLine(130, 100 , 150, 100, 'black', size=1)

# Cuartas verticales
drawLine(10, 140 , 30, 140, 'black', size=1)
drawLine(90, 140 , 110, 140, 'black', size=1)
drawLine(170, 140 , 190, 140, 'black', size=1)
# Cuartas horizontales
drawLine(60, 130 , 60, 150, 'black', size=1)
drawLine(140, 130 , 140, 150, 'black', size=1)

# Quintas veticales
drawLine(20, 170 , 20, 190, 'black', size=1)
drawLine(100, 170 , 100, 190, 'black', size=1)
drawLine(180, 170 , 180, 190, 'black', size=1)
# Quintas horizontales
drawLine(50, 180 , 70, 180, 'black', size=1)
drawLine(130, 180 , 150, 180, 'black', size=1)

turtle.done()