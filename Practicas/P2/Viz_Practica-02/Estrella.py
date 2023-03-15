# CIENCIA DE DATOS: VISUALIZACIÓN DE LA INFORMACIÓN
# UNAM-IIMAS, SEMESTRE 2023-2

# PRACTICA-02: ESPACIOS DE COLOR E ILUSIONES ÓPTICAS

# ILUSION ÓPTICA DE LINEAS PARA FORMAR UNA ESTRELLA
import turtle as ts

ts.setup(800,800)

# Vamos a definir una función que dibuje cuadrados
def draw_line(xFrom, yFrom, xTo, yTo, color, size = 1):
    
    # Definimos la variable global
    global mylapiz

    # Grueso de la línea
    mylapiz.pensize(size)
    
    # Alzar el lápiz
    mylapiz.penup() 
    
    # Definir color 
    mylapiz.color(color)

    #Establecer el punto (x,y) de origen:
    mylapiz.goto(xFrom,yFrom)
    
    #Bajar el lápiz
    mylapiz.pendown()
    
    #Moverse al segundo punto
    mylapiz.goto(xTo,yTo)

mylapiz = ts.Turtle()

for x in range(0, 401, 10):
    draw_line(x, 400, 400, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(-x, 400, -400, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(400, x - 400, x, -400, 'black')

for x in range(0, 401, 10):
    draw_line(-400, x - 400, -x, -400, 'black')


# ESTRELLA
for x in range(0, 401, 10):
    draw_line(x, 0, 0, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(-x, 0, 0, -400 + x, 'black')

for x in range(0, 401, 10):
    draw_line(-x, 0, 0, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(x, 0, 0, -400 + x, 'black')

ts.getscreen()