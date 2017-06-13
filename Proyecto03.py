import curses
import random

screen = curses.initscr()
screen.border(0)
dims = screen.getmaxyx()
screen.keypad(1)#True
curses.noecho()#Que no salga en pantalla lo que el usuario digite
curses.curs_set(0)

def iniciar():

    screen.nodelay(0)
    opcion, usuario, user = 0,0,0
    bv = curses.newwin(10, 50, 8, 20)
    bv.box()    
    bv.addstr(1,8,"Bienvenido al Juego de la Vida!")
    bv.addstr(3,2,"1. Modo Aleatorio")
    bv.addstr(4,2,"2. Modificado")
    bv.addstr(5,2,"3. Configurado")
    bv.addstr(6,2,"4. Salir")
    bv.addstr(7,2,"Elige tu opcion!:")
    screen.refresh()
    bv.refresh()

    while opcion == 0  or opcion in range (49, 54):#mientras me ponga un 1,2,3 4 o 5

        opcion = screen.getch()

        if opcion == 49:

            bv.clear()
            bv.box()
            bv.addstr(1,2,"Cuantas celulas?")
            screen.refresh()
            bv.refresh()
            k = screen.getstr()
            tablero,posiciones = crear_tablero(dims[0],dims[1])
            fijar_celulas(tablero,posiciones, int((k)))

        elif opcion == 50:

            bv.clear()
            bv.box()
            bv.addstr(1,2,"Cual sera la altura del cuadro?")
            screen.refresh()
            bv.refresh()
            k = screen.getstr()
            bv.clear()
            bv.box()
            bv.addstr(1,2,"Cual sera el ancho del cuadro?")
            screen.refresh()
            bv.refresh()
            z = screen.getstr()
            cambiar_ventana(k,z)

        elif opcion == 51:
            cambios.fijar_celulas(cerote)

        else:
            curses.endwin()#Salga de ahi we

def crear_tablero(y,x):

    tablero = []
    posiciones = []

    for i in range(0,x):
 
        tablero += [[]]
 
        for j in range(0,y):
 
            tablero[i] +=[" "] 

    for i in range(0,x):

        for j in range(0,y):

            posiciones += [[i,j]]

    return tablero,posiciones

def fijar_celulas(tablero, posiciones, cantidad):

    screen.clear()

    for posicion in range(0,cantidad-1):

        print(posiciones)
        print(len(posiciones))

        celula = random.randint(0, len(posiciones)-1)

        print("Cel", celula)

        tablero[posiciones[celula][0]][posiciones[celula][1]] = '*'
        print(tablero[posiciones[celula][0]][posiciones[celula][1]])

        print("posi antes",posiciones)

        posiciones = posiciones.pop(celula)

        print("posi despues",posiciones)
        break #Era para ver que pasaba en la primer vuelta nada mas

    #encontrar_celula()

def encontrar_celula():

    i = 0

    posiciones = []

    while i < dims[0]:

        j = 0

        while j < dims[1]:

                vive = ver_vecinos(i,j)

                if vive == True:

                    posiciones += [i,j]

                j+=1

        i+=1

    return nuevo_tablero(posiciones)

def ver_vecinos(y,x):

    celula = (y,x)
    arriba = [y-1,x]
    abajo = [y+1,x]
    lado_dcho = [y,x-1]
    lado_izq = [y,x+1]
    esq_s_i = [y-1,x-1]
    esq_s_d = [y-1,x+1]
    esq_i_i = [y+1,x-1]
    esq_i_d = [y+1,x+1]
    vecinas = [arriba,abajo,lado_dcho, lado_izq,esq_s_i, esq_s_d,esq_i_i, esq_i_d]
    celulas = 0

    for vecina in vecinas:

        if tablero[vecina[0]][vecina[1]] == '*':
            celulas+=1

    if celulas in range(2,3) or celulas == 6:

        return True

    else: 
        return False

def imprimir_tablero():
     tablero = crear_tablero(24,80)
     for i in range(0,len(tablero)-1):
        j = 0

        while j < len(tablero[0]):

            screen.addstr(tablero[i][j])
            j += 1

        screen.addstr("\n")
        i += 1
    
imprimir_tablero()
