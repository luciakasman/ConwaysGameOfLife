"""
Conway's Game of Life
---------------------

https://es.wikipedia.org/wiki/Juego_de_la_vida

El "tablero de juego" es una malla formada por cuadrados ("células") que se
extiende por el infinito en todas las direcciones. Cada célula tiene 8 células
vecinas, que son las que están próximas a ella, incluidas las diagonales. Las
células tienen dos estados: están "vivas" o "muertas" (o "encendidas" y
"apagadas"). El estado de la malla evoluciona a lo largo de unidades de tiempo
discretas (se podría decir que por turnos). El estado de todas las células se
tiene en cuenta para calcular el estado de las mismas al turno siguiente.
Todas las células se actualizan simultáneamente.

Las transiciones dependen del número de células vecinas vivas:

* Una célula muerta con exactamente 3 células vecinas vivas "nace" (al turno
  siguiente estará viva).
* Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso
  muere o permanece muerta (por "soledad" o "superpoblación").
"""

def main():
    """
    Función principal del programa. Crea el estado inicial de Game of LIfe
    y muestra la simulación paso a paso mientras que el usuario presione
    Enter.
    """
    life = life_crear([
        '..........',
        '..........',
        '..........',
        '.....#....',
        '......#...',
        '....###...',
        '..........',
        '..........',
    ])
    while True:
        for linea in life_mostrar(life):
            print(linea)
        print()
        input("Presione Enter para continuar, CTRL+C para terminar")
        print()
        life = life_siguiente(life)

#-----------------------------------------------------------------------------

def life_crear(mapa):
    """
    Crea el estado inicial de Game of life a partir de una disposición
    representada con los caracteres '.' y '#'.

    `mapa` debe ser una lista de cadenas, donde cada cadena representa una
    fila del tablero, y cada caracter puede ser '.' (vacío) o '#' (célula).
    Todas las filas deben tener la misma cantidad de caracteres.

    Devuelve el estado del juego, que es una lista de listas donde cada
    sublista representa una fila, y cada elemento de la fila es False (vacío)
    o True (célula).
    """
    
    return [[elemento=="#" for elemento in fil] for fil in mapa]

#-----------------------------------------------------------------------------

def life_mostrar(life):
    """
    Crea una representación del estado del juego para mostrar en pantalla.

    Recibe el estado del juego (inicialmente creado con life_crear()) y
    devuelve una lista de cadenas con la representación del tablero para
    mostrar en la pantalla. Cada una de las cadenas representa una fila
    y cada caracter debe ser '.' (vacío) o '#' (célula).
    """
    return ["".join(["#" if elemento else "." for elemento in fil]) for fil in life]

#-----------------------------------------------------------------------------

def cant_adyacentes(life, f, c):
    """
    Calcula la cantidad de células adyacentes a la celda en la fila `f` y la
    columna `c`.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa.
    """

    return sum([1 if ( i % len(life), j % len(life[0])) != (f, c) and life[i % len(life)][j % len(life[0])] else 0 for j in range(c - 1, c + 2) for i in range(f - 1, f + 2)])


#-----------------------------------------------------------------------------

def celda_siguiente(life, f, c):
    """
    Calcula el estado siguiente de la celda ubicada en la fila `f` y la
    columna `c`.

    Devuelve True si en la celda (f, c) habrá una célula en la siguiente
    iteración, o False si la celda quedará vacía.
    """
    celda = life[f][c]
    
    n = cant_adyacentes(life, f, c)
    
    return (celda and (n==2 or n==3)) or (not celda and n==3)

#-----------------------------------------------------------------------------

def life_siguiente(life):
    """
    Calcula el siguiente estado del juego.

    Recibe el estado actual del juego (lista de listas de False/True) y
    devuelve un _nuevo_ estado que representa la siguiente iteración según las
    reglas del juego.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa.
    """
    siguiente = []
    for f in range(len(life)):
        fila = []
        for c in range(len(life[0])):
            fila.append(celda_siguiente(life, f, c))
        siguiente.append(fila)
    return siguiente

#-----------------------------------------------------------------------------

main()
