import random

def crear_tablero(y,x):
    """Crea una matriz de acuerdo a las dimensiones que le llegan
    E: Dimensiones
    S: Matriz/tablero
    R: Ninguna
    """
    tablero = []

    for i in range(0,y+2):
 
        tablero += [[]]
 
        for j in range(0,x+2):
 
            tablero[i] +=[" "] 

    return tablero

def oscilador(tablero):
    '''
    E:Tablero
    S: Tablero con celulas prefijadas
    R: Ninguna 
    Es el modo oscilador de juego
    '''
    for x in range (4,7):

        tablero[2][x] = "\u25A0"
        tablero[7][x] = "\u25A0"
        tablero[10][x] ="\u25A0"
        tablero[14][x] ="\u25A0"

    for x in range (10,13):

        tablero[2][x] = "\u25A0"
        tablero[7][x] = "\u25A0"
        tablero[10][x] = "\u25A0"
        tablero[14][x] = "\u25A0"

    for y in range(11,14):

        tablero[y][2] = "\u25A0"
        tablero[y][7] = "\u25A0"
        tablero[y][9] = "\u25A0"
        tablero[y][14] = "\u25A0"

    for y in range(4,7):

        tablero[y][2] = "\u25A0"
        tablero[y][7] = "\u25A0"
        tablero[y][9] = "\u25A0"
        tablero[y][14] = "\u25A0"

    return tablero

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

        if tablero[y][x] != "\u25A0":

            tablero[y][x] = "\u25A0"

            cantidad-=1
    return tablero

def vive_muere(tablero,y,x,mini,maxi,nace):

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
            
                vive = ver_vecinos(tablero,i,j,y,x,mini,maxi,nace)
                if vive == False:
                    tablero[i][j] = " "
                else:
                    tablero[i][j] = "\u25A0"
                j+=1
        i+=1

    return tablero

def ver_vecinos(tablero, y,x,largo,ancho,mini,maxi,nace):

    """Se fija cuantas celulas hay alrededor de la actual y las cuenta, asi determina si vive o no
    E: Tablero, dimensiones(largo y ancho) y posicion de la celula en el tablero(y y x)
    S: True o False
    R: Ninguna
    """
    celula = tablero[y][x]
 
    celulas = 0
 
    esquinas = [[0,0],[0,ancho-1],[largo-1,0],[largo-1,ancho-1]]
 #Entra primero a ver si esquina, luego bordes, luego normal
    for esquina in esquinas:
        if [y,x] == esquina:
            vive = para_esquina(tablero, esquinas, y,x,celula,mini,maxi,nace)
            return vive

    if y == 0: #Para las celulas de la primera fila, ya que son borde
        vecinas = [tablero[y+1][x],tablero[y][x-1],tablero[y][x+1],tablero[y+1][x-1],tablero[y+1][x+1],tablero[ancho-1][x-1],tablero[ancho-1][x],tablero[ancho-1][x+1]]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas+=1
    elif x == 0: #Para el borde de la primera columna, donde x es siempre 0
        vecinas = [tablero[y][x-1], tablero[y+1][x],tablero[y-1][x],tablero[y-1][x+1],tablero[y+1][x+1],tablero[y-1][largo-1],tablero[y][largo-1],tablero[y+1][largo-1]]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas +=1
    elif x == ancho-1: #Donde x es la ultima posicion de cada fila. Ultima columna de matriz, borde.
        vecinas = [tablero[y][x-1],tablero[y-1][x], tablero[y+1][x],tablero[y-1][x-1],tablero[y+1][x-1],tablero[y-1][0],tablero[y][0],tablero[y+1][0]]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas+=1
    elif y == largo-1:#ultima fila de matriz, borde. Excluyo esquinas
        vecinas = [tablero[y][x-1],tablero[y][x+1],tablero[y-1][x],tablero[y-1][x-1], tablero[y-1][x+1],tablero[0][x-1],tablero[0][x],tablero[0][x+1]]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas +=1
    else: #Todo lo del medio del tablero xD
        vecinas = [tablero[y-1][x],tablero[y+1][x],tablero[y][x-1],tablero[y][x+1],tablero[y-1][x-1],tablero[y-1][x+1],tablero[y+1][x-1], tablero[y+1][x+1]]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas+=1

    if celula == "\u25A0":
        if celulas in range(mini,maxi+1):
            return True

        else: 
            return False
    if celula == " ":
        if celulas == nace:
            return True
        else:
            return False

def para_esquina(tablero,esquinas,y,x,celula,mini,maxi,nace): 

    """Cuenta las celulas alrededor de cada esquina
    E: Tablero, lista de las esquinas posibles, posicion de celula actual
    S: True o False (vive o muere)
    R: Ninguna
    """
    celulas = 0

    if celula == esquinas[0]: #esquinas[0][0]

        col = [1,largo-1]
        fila = [0,1,ancho-1]
        vecinas = []
        for pos in col:
            for posi in fila:
                vecinas+=[tablero[pos][posi]]
        vecinas+=[vecina[0][1]]
        vecinas+=[vecinas[0][ancho-1]]
        #vecinas = [tablero[1][0],tablero[1][1],tablero[0][ancho-1],tablero[1][ancho-1],tablero[0][1],tablero[largo-1][ancho-1],tablero[largo-1][0],tablero[largo-1][1]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas+=1
    elif celula == esquinas[1]:
        #esquinas[0][ancho-1]
        col = [1,largo-1]
        fila = [0,x,x-1]
        vecinas = []
        for pos in col:
            for posi in fila:
                vecinas+=[tablero[pos][posi]]
        vecinas += [tablero[0][x-1]]
        vecinas += [tablero[0][0]]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas+=1
    elif celula == esquinas[2]:#[largo-1,0],

        col = [y-1,0]
        fila = [0,1,ancho-1]
        vecinas = []

        for pos in col:

            for posi in fila:
                vecinas+=[tablero[pos][posi]]

        #vecinas = [tablero[y][1], tablero[y-1][0], tablero[y-1][1],tablero[0][0],tablero[0][1],tablero[0][ancho-1],tablero[y-1][ancho-1],tablero[y][ancho-1]]
        vecinas+=[tablero[y][1]]
        vecinas += [tablero[y][ancho-1]]

        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas+=1

    else:#[largo-1,ancho-1]]
        col = [y-1,0]
        fila = [x,0,x-1]
        vecinas = []
        #vecinas = [tablero[y-1][x],tablero[y][x-1],tablero[y-1][x-1],tablero[0][0],tablero[0][x],tablero[0][x-1],tablero[y-1][0],tablero[y][0]]
        for pos in col:
            for posi in fila:
                vecinas += [tablero[pos][posi]]
        vecinas += [tablero[y][x-1]]
        vecinas += [tablero[y][0]]
        for vecina in vecinas:
            if vecina == "\u25A0":
                celulas+=1

    if celula == "\u25A0":
        if celulas in range(mini,maxi+1):
            return True

        else: 
            return False

    else:
        if celulas == nace:
            return True

        else:
            return False
