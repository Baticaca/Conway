import curses
import time
import Tablero

screen = curses.initscr()
screen.border(0)
screen.keypad(1)#True
#curses.noecho()#Que no salga en pantalla lo que el usuario digite
#curses.curs_set(1)

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
    screen.nodelay(1)
    opcion, usuario, user = 0,0,0
    y,x,cantidad,nace,mini,maxi = 0,0,0,0,0,0
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

    if opcion == 49: #Tengo la funcion de validaciones que solo devuelve True o False
        #Por si lo que ingresa el profe es chanchullo, ya que le encanta hacer eso

        bv.clear()
        bv.box()
        dims = [24,80]
        mini = 2
        maxi = 3
        nace = 3
        bv.addstr(1,2,"Cuantas celulas?")
        screen.refresh()
        bv.refresh()
        cantidad = screen.getstr(2,2)
        cantidad = cantidad.decode(encoding='utf-8')
        valido = validaciones(dims[0],dims[1],cantidad,2,3,3)

        if valido == False:
            bv.clear()
            bv.addstr(1,2,"Porque eres asi?")
            time.sleep(1.5)
            screen.clear()
            iniciar()

        tablero = Tablero.crear_tablero(dims[0],dims[1])
        tablero = Tablero.fijar_celulas(tablero,int(cantidad),dims[0],dims[1])#Las fija de forma aleatoria

    elif opcion == 50:#Oscilador

        dims = [17,17]
        tablero  = Tablero.crear_tablero(dims[0],dims[1])
        tablero = Tablero.oscilador(tablero)
        mini = 2 
        maxi = 3
        nace = 3

    elif opcion == 51:#Pide como que todas las especificaciones de juego

        bv.clear()
        bv.addstr(1,2,"Cantidad de columnas?")
        screen.refresh()
        bv.refresh()
        y = screen.getstr(2,2)
        y = y.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad de filas?")
        screen.refresh()
        bv.refresh()
        x = screen.getstr(2,2)
        x = x.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad de celulas iniciales?")
        screen.refresh()
        bv.refresh()
        cantidad = screen.getstr(2,2)
        cantidad = cantidad.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad de minima de celulas para vivir?")
        screen.refresh()
        bv.refresh()
        mini = screen.getstr(2,2)
        mini = mini.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad maxima de celulas de celulas para vivir?")
        screen.refresh()
        bv.refresh()
        maxi = screen.getstr(2,2)
        maxi.decode(encoding='utf-8')
        bv.clear()
        bv.box()
        bv.addstr(1,2,"Cantidad para nacer?")
        screen.refresh()
        bv.refresh()
        nace = screen.getstr(2,2)
        nace = nace.decode(encoding = 'utf-8')
        validar = validaciones(y,x,cantidad,mini,maxi,nace)

        if validar == False:
            bv.clear()
            bv.addstr(1,2,"Profe no haga trampa")
            time.sleep(2)
            screen.clear()
            iniciar()#Veo que haya digitado cosas aptas

        tablero = Tablero.crear_tablero(int(y),int(x))
        tablero = Tablero.fijar_celulas(tablero, int(cantidad),int(y),int(x))

    elif opcion == 52:
        curses.endwin()#Salga de ahi 
    
    else: #Metiste algo que nada que ver

        bv.clear()
        bv.addstr(1,2,"Opcion invalida, intente de nuevo")
        time.sleep(2)
        screen.clear()
        iniciar()

    while(True): #Aqui se imprime fila tras fila del tablero, y se actualiza con la llamada a vive_muere de manera infinita

        for i in range(0,len(tablero)):

            j = 0

            while j < len(tablero[0]):

                screen.addstr(tablero[i][j])
                j += 1

            screen.addstr("\n")
            i += 1

        screen.refresh()

        time.sleep(0.8)

        tablero = Tablero.vive_muere(tablero, dims[0],dims[1],int(mini),int(maxi),int(nace))

def validaciones(y,x,cantidad,mini,maxi,nace): #Validaciones para cada cosa

    '''
    E: dimensiones, cantidad de celulas, minimas para vivir, maximas, y con cuantas nace
    S: Se fija que el usuario haya metido algo valido
    R: Que sean numeros y dentro del rango establecido
    '''

    if str(y).isnumeric() == False or str(x).isnumeric() == False:
        return False

    elif str(cantidad).isnumeric() == False or str(nace).isnumeric() == False:
        return False

    elif str(mini).isnumeric() == False or str(maxi).isnumeric() == False:
        return False

    elif int(y) > 24 or int(x) > 80:
        return False

    elif int(cantidad) < 0  or int(nace) < 0 or int(x) < 0 or int(y) < 0 or int(mini) < 0 or int(maxi) < 0:
        return False

    elif int(cantidad) > int(x)*int(y):
        return False

    else:
        return True
iniciar()
