# Axel Daniel Malváez Flores
# 318315126
# Visualización de la Información

import turtle

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

#Se establecen las coordenadas del primer conjunto de circulos:
drawCircle(-90, 0, 20 , "green")
drawCircle(-90, 70, 35, "purple")
drawCircle(-90, -70, 35, "purple")
drawCircle(-160, 0, 35, "purple")
drawCircle(-20, 0, 35, "purple")

#Se establecen las coordenadas del segundo conjunto de circulos:
drawCircle(80, 0, 20 , "green")
drawCircle(80, 35, 10, "purple")
drawCircle(80, -35, 10, "purple")
drawCircle(115, 0, 10, "purple")
drawCircle(45, 0, 10, "purple")

turtle.done()