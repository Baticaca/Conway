import random

def crear_tablero(y,x):
    """Crea una matriz de acuerdo a las dimensiones que le llegan
    E: Dimensiones
    S: Matriz/tablero
    R: Ninguna
    """
    tablero = []

    for i in range(0,y):
 
        tablero += [[]]
 
        for j in range(0,x):
 
            tablero[i] +=[" "] 

    return oscilador(tablero)

def oscilador(tablero):

    for x in range (4,7):

        tablero[2][x] = '*'
        tablero[7][x] = '*'
        tablero[10][x] ='*'
        tablero[14][x] ='*'

    for x in range (10,13):

        tablero[2][x] = '*'
        tablero[7][x] = '*'
        tablero[10][x] = '*'
        tablero[14][x] = '*'

    for y in range(11,14):

        tablero[y][2] = '*'
        tablero[y][7] = '*'
        tablero[y][9] = '*'
        tablero[y][14] = '*'

    for y in range(4,7):

        tablero[y][2] = '*'
        tablero[y][7] = '*'
        tablero[y][9] = '*'
        tablero[y][14] = '*'

    return imprimir_tablero(tablero)

def imprimir_tablero(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            print(matriz[i][j],end="")
            j += 1
        print()
        i += 1
print(crear_tablero(24,80))
def fijar_celulas(tablero, cantidad,largo, ancho):
    """Fija las celulas de forma random en el tablero
    E: 
        -Tablero
        -Cantidad de celulas
        -Largo del tablero
        -Ancho del tablero
    S:
       Tablero actualizado con celulas
    R: Ninguna
       """
    while cantidad > 0:

        y,x = random.randrange(0, largo),random.randrange(0,ancho)

        if tablero[y][x] != '*':

            tablero[y][x] = '*'

            cantidad-=1
    return tablero

def vive_muere(tablero,y,x):
    """Cada espacio de la matriz es enviado a verificar que tiene alrededor
    Para ver quien vive y quien muere
    E: Tablero, dimensiones (y y x)
    S: Tablero con las celulas 
    R: Ninguna
    """
    i = 0

    while i < len(tablero):

        j = 0
        while j < len(tablero[0]):
            
                vive = ver_vecinos(tablero,i,j,y,x)
                if vive == False:
                    tablero[i][j] = " "
                else:
                    tablero[i][j] = "*"
                j+=1
        i+=1

    return tablero

def ver_vecinos(tablero, y,x,largo,ancho):
    """Se fija cuantas celulas hay alrededor de la actual y las cuenta, asi determina si vive o no
    E: Tablero, dimensiones(largo y ancho) y posicion de la celula en el tablero(y y x)
    S: True o False
    R: Ninguna
    """
    #print("y",y)
    #print("x",x)
 
    celula = tablero[y][x]
 
    celulas = 0
 
    esquinas = [[0,0],[0,ancho-1],[largo-1,0],[largo-1,ancho-1]]
 
    for esquina in esquinas:
        if [y,x] == esquina:
            vive = para_esquina(tablero, esquinas, y,x,celula)
            return vive

    if (y,x) in (0,range(1,ancho-1)): #Para las celulas de la primera fila, ya que son borde
        vecinas = [tablero[y+1][x],tablero[y][x-1],tablero[y][x+1],tablero[y+1][x-1],tablero[y+1][x+1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas+=1
    elif (y,x) in (range(1,largo-1),0): #Para el borde de la primera columna, donde x es siempre 0
        vecinas = [tablero[y][x-1], tablero[y+1][x],tablero[y-1][x],tablero[y-1][x+1],tablero[y+1][x+1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas +=1
    elif x == ancho-1: #Donde x es la ultima posicion de cada fila. Ultima columna de matriz, borde.
        vecinas = [tablero[y][x-1],tablero[y-1][x], tablero[y+1][x],tablero[y-1][x-1],tablero[y+1][x-1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas+=1
    elif y == largo-1:#ultima fila de matriz, borde. Excluyo esquinas
        vecinas = [tablero[y][x-1],tablero[y][x+1],tablero[y-1][x],tablero[y-1][x-1], tablero[y-1][x+1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas +=1
    else: #Todo lo del medio del tablero xD
        vecinas = [tablero[y-1][x],tablero[y+1][x],tablero[y][x-1],tablero[y][x+1],tablero[y-1][x-1],tablero[y-1][x+1],tablero[y+1][x-1], tablero[y+1][x+1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas+=1

    if celulas in range(2,3) or celulas == 6:
        return True

    else: 
        return False

def para_esquina(tablero,esquinas,y,x,celula): 

    """Cuenta las celulas alrededor de cada esquina
    E: Tablero, lista de las esquinas posibles, posicion de celula actual
    S: True o False (vive o muere)
    R: Ninguna
    """
    #print("y",y)
    #print("x",x)
    #celula = tablero[y][x]

    celulas = 0

    if celula == esquinas[0]:
        #print("es",esquinas[0])
        vecinas = [tablero[y+1][x], tablero[y][x-1], tablero[y+1][x+1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas+=1
    elif celula == esquinas[1]:
        vecinas = [tablero[y][x+1],tablero[y+1][x], tablero[y+1][x-1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas+=1
    elif celula == esquinas[2]:
        vecinas = [tablero[y][x-1], tablero[y-1][x], tablero[y-1][x+1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas+=1
    else:
        vecinas = [tablero[y-1][x],tablero[y][x-1],tablero[y-1][x-1]]
        for vecina in vecinas:
            if vecina == '*':
                celulas+=1
    if celulas in range(2,4) or celulas == 6:
        return True
    else:
        return False
