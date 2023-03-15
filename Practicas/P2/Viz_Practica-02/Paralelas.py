# CIENCIA DE DATOS: VISUALIZACIÓN DE LA INFORMACIÓN
# UNAM-IIMAS, SEMESTRE 2023-2

# PRACTICA-02: ESPACIOS DE COLOR E ILUSIONES ÓPTICAS

# ILUSION ÓPTICA USANDO LINEAS NEGRAS Y PURPURAS

# Primero vamos a definir una función que nos dibuje una linea
import turtle as ts

ts.setup(840,440)

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

# Vamos a definir a 'Mylapiz' como un objeto de la clase Turtle 
mylapiz = ts.Turtle()

# Vamos a crear un ciclo que nos permita crear varias líneas trazadas a diferentes rotaciones:
for x in range(-400, 400, 50):
    draw_line(x, 200, -x, -200, 'black')

for y in [-100, 100]:
    draw_line(400, y, -400, y, 'purple', size = 3)

ts.getscreen()