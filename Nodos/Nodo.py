from Personajes.Personaje import Personaje


class Nodo:
    """
    pos_final : punto objetivo
    posicion : localizacion x,y del nodo
    padre : Nodo padre
    h : valor Heuristico, costo desde el nodo actual hasta el objetivo
    g : valor g, costo desde el nodo inicial hasta el nodo actual
    """
    def __init__(self, pos_final, posicion=[0, 0], padre=None, p=Personaje("pedro"), laberinto=[]):
        self.posicion = posicion
        self.padre = padre
        self.h = manhattan(self.posicion, pos_final)
        if self.padre == None:
            self.g = 0
        else:
            #raw_input("espera")
            if str(laberinto[posicion[0]][posicion[1]]) == str(0):
                self.g = self.padre.g + p.Mountain()
            if str(laberinto[posicion[0]][posicion[1]]) == str(1):
                self.g = self.padre.g + p.getEarth()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(4):
                self.g = self.padre.g + p.getForest()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(3):
                self.g = self.padre.g + p.getSand()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(2):
                self.g = self.padre.g + p.getWater()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(5):
                self.g = self.padre.g + p.getSwamp()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(6):
                self.g = self.padre.g + p.getSnow()
            else:
                self.g = self.padre.g + 1000
        self.f = self.g + self.h

# Calcula la distancia manhattan<
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])