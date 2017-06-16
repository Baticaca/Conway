import curses
import time
import Tablero

screen = curses.initscr()
screen.border(0)
screen.keypad(1)#True
curses.noecho()#Que no salga en pantalla lo que el usuario digite
curses.curs_set(0)

def iniciar():
    '''
    E: Ninguna
    S: Tablero?
    R: Recibir numeros enteros
    Despliega el menu y pide medidas o cantidades al usuario y llama
    a funciones necesarias para hacer lo que se le pide
    '''
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

    opcion = screen.getch()

    if opcion == 49:

        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cuantas celulas?")
        screen.refresh()
        bv.refresh()
        k = screen.getstr()
        dims = screen.getmaxyx()
        tablero = Tablero.crear_tablero(dims[0],dims[1])
        tablero = Tablero.fijar_celulas(tablero, int(k),dims[0],dims[1])
        imprimir_tablero(tablero)

    elif opcion == 50:

        dims = screen.getmaxyx()
        tablero  = Tablero.crear_tablero(dims[0],dims[1])
        tablero = Tablero.oscilador(tablero,dims[0],dims[1])
        imprimir_tablero(tablero)

    elif opcion == 51:
            pass

    else:

        curses.endwin()#Salga de ahi we

def imprimir_tablero(tablero):
 
    """Imprime el tablero a la pantalla
    E: Tablero
    S: Lo tira a la pantalla. Asi como a una bola 
    R: Ninguna
    """
    screen.clear()

    while(True):

        for i in range(0,len(tablero)):

            j = 0

            while j < len(tablero[0]):

                screen.addstr(tablero[i][j])
                j += 1

            screen.addstr("\n")
            i += 1
        screen.refresh()
        screen.clear()
        time.sleep(0.8)
        tablero = Tablero.vive_muere(tablero, dims[0],dims[1])
        imprimir_tablero(tablero)
iniciar()
