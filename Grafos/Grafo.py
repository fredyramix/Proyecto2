from Nodos.Nodo import Nodo

class Grafo:
    """
    laberinto : mapa
    pos_final : punto objetivo
    inicio : Nodo que contiene el punto inicial
    fin : Nodo que contiene el punto final
    abierta : lista con caminos abiertos
    cerrada : lista con caminos cerrados o inutiles
    """
    def __init__(self,laberinto,inicio,final,p):
        self.laberinto = laberinto  #Grafo ahora tiene un atributo con todos los nodos.
       #columnas, filas
        self.pos_final=final
        self.costos=[]
        self.inicio=Nodo(self.pos_final,inicio,None,p,laberinto)
        #self.pos_final = buscarPosicion(final,self.laberinto) #buscar posicion nos devuelve x & y de el nodo.
        #self.inicio = Nodo(self.pos_final,buscarPosicion(inicio,laberinto),None,p,laberinto)
        self.fin = Nodo(self.pos_final,self.pos_final,None,p,laberinto)
        self.abierta = []
        self.cerrada = []
        self.cerrada.append(self.inicio) #ponemos en cerrada porque no regresaremos a este nodo.
        self.abierta += self.vecinos(self.inicio,p,laberinto)
        while self.objetivo():
            self.buscar(p,laberinto)
        self.camino = self.camino()


    #Devuelve una lista con vecinos transitables
    def vecinos(self,nodo,p,laberinto):
        vecinos = []
        lista_movimientos={}
        no_permitidos={}
        lista_movimientos['0']=str(p.getMountain())
        lista_movimientos['1']=str(p.getEarth())
        lista_movimientos['2']=str(p.getWater())
        lista_movimientos['3']=str(p.getSand())
        lista_movimientos['4']=str(p.getForest())
        lista_movimientos['5']=str(p.getSwamp())
        lista_movimientos['6']=str(p.getSnow())
        for m,v in lista_movimientos.iteritems():
            if v=='0':
                no_permitidos[str(m)]=str(m)
        try:
            if no_permitidos.has_key(str(self.laberinto[nodo.posicion[0]+1][nodo.posicion[1]])):
                pass
            else:
                vecinos.append(Nodo(self.pos_final,[nodo.posicion[0]+1, nodo.posicion[1]],nodo,p,laberinto))
        except IndexError,e:
            pass
        try:
            if no_permitidos.has_key(str(self.laberinto[nodo.posicion[0]-1][nodo.posicion[1]])):
                pass
            else:
                vecinos.append( Nodo(self.pos_final,[nodo.posicion[0]-1, nodo.posicion[1]],nodo,p,laberinto))
        except IndexError,e:
            pass
        try:
            if no_permitidos.has_key(str(self.laberinto[nodo.posicion[0]][nodo.posicion[1]-1])):
                pass
            else:
                vecinos.append(Nodo(self.pos_final,[nodo.posicion[0], nodo.posicion[1]-1],nodo,p,laberinto))
        except IndexError,e:
            pass
        try:
            if no_permitidos.has_key(str(self.laberinto[nodo.posicion[0]][nodo.posicion[1]+1])):
                pass
            else:
                vecinos.append( Nodo(self.pos_final,[nodo.posicion[0], nodo.posicion[1]+1],nodo,p,laberinto))
        except IndexError, e:
            pass
        return vecinos

    #Pasa el vecino con menor costo (G+H) a la lista cerrada
    def f_menor(self):
        #try:
        actual = self.abierta[0]
        #except IndexError,e:
            #pass
         #   return False
        n = 0
        for i in range(1, len(self.abierta)):
            if self.abierta[i].f < actual.f:
                actual = self.abierta[i]
                n = i
        self.cerrada.append(self.abierta[n])
        del self.abierta[n]

    #comprueba la existencia de un nodo en una lista
    def exists(self,nodo,lista):
        for i in range(len(lista)):
            if nodo.posicion == lista[i].posicion:
                return True
        return False

    #Se evaluan los movimientos buscando que los nodos esten en lista cerrada o abierta
    #Si un nodo mejora el valor G del padre se comprueba en la lista abierta  y el padre se manda a la cerrada.
    #Despues el nodo que contenia un mejor valor se manda a la lista abierta
    def ruta(self):
        for i in range(len(self.nodos)):
            if self.exists(self.nodos[i], self.cerrada):
                continue
            elif not self.exists(self.nodos[i], self.abierta):
                self.abierta.append(self.nodos[i])
            else:
                if self.select.g+1 < self.nodos[i].g:
                    for j in range(len(self.abierta)):
                        if self.nodos[i].posicion == self.abierta[j].posicion:
                            del self.abierta[j]
                            self.abierta.append(self.nodos[i])
                            break

    # Analiza el elemento que recien se agrego a la lista cerrada es decir el nodo padre.
    def buscar(self,p,laberinto):
        self.f_menor()
        self.select = self.cerrada[-1]
        self.nodos = self.vecinos(self.select,p,laberinto)
        self.ruta()

    #Comprueba si el objetivo esta en la lista abierta para terminar de buscar.
    def objetivo(self):
        for i in range(len(self.abierta)):
            if self.fin.posicion == self.abierta[i].posicion:
                return False
        return True



    #Retorna una lista con las posiciones del mejor camino a seguir
    def camino(self):
        #print len(self.abierta)
        for i in range(len(self.abierta)):
            if self.fin.posicion == self.abierta[i].posicion:
                objetivo = self.abierta[i]
                #print objetivo.f
                self.costos.append(objetivo.f)

        camino = []
        while objetivo.padre != None:
            camino.append(objetivo.posicion)
            #print objetivo.f
            objetivo = objetivo.padre
        camino.reverse()

        return camino
#Escribe una ruta con caracteres en un archivo
def escribirSolucion(camino,laberinto,name,p,final,q):
    inicio=p.getNombre()[0]
    sname = "Soluciones\ "+q+"_"+str(inicio)+"_"+final+""
    solucion = open(sname,'w')
    for posicion in camino:
        laberinto[ posicion[0]][ posicion[1]] = inicio #Escribe la letra del Personaje
    for i in range(len(laberinto)):
        linea = ""
        for j in range(len(laberinto[0])):
            linea = linea + laberinto[i][j] + " "
        solucion.write(linea+"\n")
    solucion.close()

def escribirSolucionSalida(camino,laberinto,name,p,final,exit,q):
    e = exit.keys()
    Inicio=p.getNombre()[0]
    Final = final
    sname = "Soluciones\ "+q+"_"+str(Inicio)+"_"+final+"_P"
    solucion = open(sname,'w')
    for posicion in camino:
        laberinto[ posicion[0]][ posicion[1]] = Inicio
    for i in range(len(laberinto)):
        linea = ""
        for j in range(len(laberinto[0])):
            linea = linea + laberinto[i][j] + " "
        solucion.write(linea+"\n")
    solucion.close()


#Para leer un archivo y crear el laberinto
def leerArchivo(name):
    nombre="Caminos/"+name
    archivo = open(nombre,'r')
    laberinto = [linea.split() for linea in archivo.readlines()]
    archivo.close()
    return laberinto

def leerMisiones(name):
    nombre="Soluciones/"+name
    archivo = open(nombre,'r')
    laberinto = [linea.split() for linea in archivo.readlines()]
    archivo.close()
    return laberinto


def buscarPosicion(x,laberinto):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna] == x:
                return [fila,columna]
