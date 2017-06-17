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
    
    JOSHUA no se como conectar las cosas de las opciones, con lo de imprimir tablero sin que se haga un desmadre
    Esta todo sucio el codigo y es que quiero usar la misma funcion de imprimir para todas, pero no se hacerlo tipo loop
    ni que madres
    '''
    screen.nodelay(0)
    opcion, usuario, user = 0,0,0
    bv = curses.newwin(10, 50, 8, 20) #Dimensiones del cuadro de mensajes 
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
        k=k.decode(encoding='utf-8')
        screen.clear()
        dims = [24,80]
        tablero = Tablero.crear_tablero(dims[0],dims[1])
        tablero = Tablero.fijar_celulas(tablero,int(k),dims[0],dims[1])#Las fija de forma aleatoria
        mini = 2#Quiero que la misma funcion me sirva para configurado entonces mando estas cosas por parametro
        maxi = 3
        nace1 = 3
        nace2 = 6
        imprimir_tablero(tablero,dims,k,mini,maxi,nace1,nace2)

    elif opcion == 50:#Oscilador
        dims = [17,17]
        tablero  = Tablero.crear_tablero(dims[0],dims[1])
        tablero = Tablero.oscilador(tablero)
        imprimir_tablero(tablero,dims,0)

    elif opcion == 51:#Configurado. Vea el desmadre xD Muy largo codigo. pensaba en meter en una funcion. 
        #Como lo reduzco, se puede?
        bv.clear()
        bv.addstr(1,2,"Cantidad de columnas?")
        screen.refresh()
        bv.refresh()
        y = screen.getstr()
        y = y.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad de filas?")
        screen.refresh()
        bv.refresh()
        x = screen.getstr()
        x = x.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad de celulas iniciales?")
        screen.refresh()
        bv.refresh()
        cantidad = screen.getstr()
        cantidad = cantidad.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad de minima de celulas para vivir?")
        screen.refresh()
        bv.refresh()
        mini = screen.getstr()
        mini = mini.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad maxima de celulas de celulas para vivir?")
        screen.refresh()
        bv.refresh()
        maxi = screen.getstr()
        maxi.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad para nacer?")
        screen.refresh()
        bv.refresh()
        nace1 = screen.getstr()
        nace1 = nace1.decode(encoding = 'utf-8')
        bv.addstr(1,2,"Desea digitar otra cantidad? S/N")
        screen.refresh()
        bv.refresh()
        si_no = screen.getstr()
        if si_no == 83:
            bv.clear()
            bv.box()
            bv.addstr(1,2,"Cual es la otra cantidad?")
            nace2 = screen.getstr()
            nace2 = nace2.decode(encoding = 'utf-8')
            validar = validaciones(y,x,cantidad,mini,maxi,nace1,nace2)#Veo que haya digitado cosas aptas
        elif si_no == 78:#Este es el desmadre, no se como hacer 
            validar = validaciones(y,x,cantidad)

        tablero = Tablero.crear_tablero(y,x)
        tablero = Tablero.fijar_celulas(tablero, int(cantidad),y,x)
        (y,x) = screen.getstr()

    elif opcion == 52:
        curses.endwin()#Salga de ahi 
    
    else:
        bv.clear()
        bv.addstr(1,2,"Opcion invalida, intente de nuevo")
        time.sleep(2)
        screen.clear()
        iniciar()

def imprimir_tablero(tablero,dims,cantidad):
 
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

def validaciones(y,x,cantidad,vivir):

    if y.isnumeric() == False or x.isnumeric() == False:
        screen.clear()
        screen.addstr(12,40,"Buen intento, pero no.  Ingrese numeros. ENTEROS.")
        screen.refresh()
        time.sleep(2)
        iniciar()

    elif cantidad.isnumeric() == False or vivir.isnumeric() == False:
        screen.clear()
        screen.addstr(12,40,"Buen intento, pero no.  Ingrese numeros. ENTEROS.")
        screen.refresh()
        time.sleep(1)
        iniciar()

    elif y <= 0:

        screen.clear()
        screen.addstr(12,40,"Profe no meta numeros negativos ni 0 e.e")
        screen.refresh()
        time.sleep(2)
        iniciar()

    elif y > 24:
        screen.clear()
        screen.addstr(12,40,"Que no te salgas de la pantalla!")
        screen.refresh()
        time.sleep(2)
        iniciar()

    elif x <= 0:

        screen.clear()
        screen.addstr(12,40,"Profe no meta numeros negativos ni 0 e.e")
        screen.refresh()
        time.sleep(2)
        iniciar()

    elif x > 80:

        screen.clear()
        screen.addstr(12,40,"Que no te salgas de la pantalla!")
        time.sleep(2)
        screen.refresh()
        iniciar()

    elif cantidad < 0:

        screen.clear()
        screen.addstr(12,40,"Aqui no hay bug xD Ingrese una cantidad positiva")
        screen.refresh()
        time.sleep(2)
        iniciar()

    elif cantidad > x*y:

        screen.clear()
        screen.addstr(12,40,"Ingrese una cantidad decente que no se salga xD")
        screen.refresh()
        time.sleep(2)
        iniciar()
iniciar()
