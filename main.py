from Grafos.Grafo import *
from Personajes.Personaje import Personaje

__author__ = 'fredy'

# Toma un archivo con el laberinto en ASCII, imprime el inicio, el final y busca el mejor camino.
# Por ultimo escribe un archivo con formato solucion_archivo.txt en donde escribe el mejor camino encontrado.

def main():
    puntos_iniciales=[[9,1],[13,2],[13,4]]
    p = Personaje("Humano")
    p.setMountain(0)
    p.setEarth(1)
    p.setWater(2)
    p.setSand(3)
    p.setForest(4)
    p.setSwamp(5)
    p.setSnow(5)
    #p.setInicio([13,2])

    m = Personaje("Monkey")
    m.setMountain(0)
    m.setEarth(2)
    m.setWater(4)
    m.setSand(3)
    m.setForest(1)
    m.setSwamp(5)
    m.setSnow(0)

    o = Personaje("Octopus")
    o.setMountain(0)
    o.setEarth(2)
    o.setWater(1)
    o.setSand(0)
    o.setForest(3)
    o.setSwamp(2)
    o.setSnow(0)

    c = Personaje("Croc")
    c.setMountain(0)
    c.setEarth(3)
    c.setWater(2)
    c.setSand(4)
    c.setForest(5)
    c.setSwamp(1)
    c.setSnow(0)

    s = Personaje("Sasquatch")
    s.setMountain(15)
    s.setEarth(4)
    s.setWater(0)
    s.setSand(0)
    s.setForest(4)
    s.setSwamp(5)
    s.setSnow(3)

    w = Personaje("WereWolf")
    w.setMountain(0)
    w.setEarth(1)
    w.setWater(3)
    w.setSand(4)
    w.setForest(2)
    w.setSwamp(0)
    w.setSnow(3)

    list = []
    list.append(p)
    list.append(m)
    list.append(o)
    list.append(c)
    list.append(s)
    list.append(w)
    diccionario_costos={}
    name = "camino.txt"
    laberinto = leerArchivo(name)
    #K = key
    # P = Portal
    # T = Templo
    # S = Piedras Magicas
    #destinos={'K':[14,13],'T':[2,2],'S':[1,12],'F':[6,14]}
    destinos={'K':[6,9],'T':[5,1],'S':[0,10],'F':[6,10]}
    exit ={'P':[9,10]}
    #print "inicio %s " % buscarPosicion(p.getNombre()[0],laberinto)
    #print "final %s " % buscarPosicion(destinos['T'],laberinto)
    #algoritmo = Grafo(laberinto,p.getNombre()[0],destinos['T'],p)
    for i in list:
        dest = destinos.keys()
        for d in dest:
            laberinto = leerArchivo(name)
            algoritmo = Grafo(laberinto,puntos_iniciales[0],destinos[d],i)
            for g in algoritmo.costos:
                nom = ""+i.getNombre()[0]+"_"+str(d)
                diccionario_costos[nom]=g
            escribirSolucion(algoritmo.camino,laberinto,name,i,d)
            #el siguiente codigo es para imprimir de la K,T,P a exit
            laberinto = leerArchivo(name)
            algoritmo1 = Grafo(laberinto,destinos[d],exit['P'],i)
            for h in algoritmo1.costos:
                nom = ""+i.getNombre()[0]+"_"+str(d)+"_"+"P"
                diccionario_costos[nom]=h
            escribirSolucionSalida(algoritmo1.camino,laberinto,name,i,d,exit)
    finales=CostosTotales(diccionario_costos)
    #caminos=SeleccionarMision(finales,list)
    #GenerarUltimoCamino(caminos)

def SeleccionarMision(finales,list):
    Letras={}
    destinos={}
    l=finales.items()
    l.sort()
    l.sort(key=lambda x:x[1]) #Aqui ya estan ordenadas por menor costo.
    print l
    bandera= True
    while len(l)>0:
        a=l[0][0] #obtengo la primer mision de menor costo.
        if Letras.has_key(a[0]):
            print "Ya tiene llave"
        else:
            if destinos.has_key(a[2]):
                "Ya tiene ese desitno"
            else:
                Letras[a[0]]=l[0][0]
                destinos[a[2]]=a[2]
        l.remove((l[0][0],l[0][1]))
    print Letras
    return Letras
def GenerarUltimoCamino(caminos):

    #Funcion para generar mapa final.
    #Solo leera 3 caminos que hay que mezclar.
    #Las posibles combinaciones son:
    #Humano - Monkey  = B
    #Humano - Octopus = C
    #Monkey- Octopus. = D
    #Humano - Monkey - Octopus. = A
    nombre = " "+caminos['H']
    nombre2= " "+caminos['M']
    nombre3= " "+caminos['O']
    primer_camino = leerMisiones(nombre)
    segundo_camino = leerMisiones(nombre2)
    tercer_camino = leerMisiones(nombre3)

    diccionario={'A':'A','B':'B','C':'C'}
    person={'H_M_O':'A','H_O_M':'A','M_H_O':'A','M_O_H':'A','O_H_M':'A','O_M_H':'A', #todos juntos
            'H_M':'B','M_H':'B', #humano con mono
            'H_O':'C','O_H':'C', #humano con octopus
            'O_H':'D','O_M':'D'#octopus con mono
             }
    sname = "Soluciones\Mision_Completada.txt"
    solucion = open(sname,'w')
    for i in range(len(primer_camino)):
        linea = ""
        for j in range(len(primer_camino)):
            a=primer_camino[i][j]
            b=segundo_camino[i][j]
            c=tercer_camino[i][j]
            concatenacion=""
            if a=='H' or a=='M' or a=='O':
                if b=='H' or b=='M' or b=='O':
                    if  c=='H' or c=='M' or c=='O':
                        concatenacion =""+str(a)+"_"+str(b)+"_"+str(c)
                    else:
                        concatenacion =""+str(a)+"_"+str(b)
            elif b=='H' or b=='M' or b=='O':
                if c=='H' or c=='M' or c=='O':
                    concatenacion =""+str(b)+"_"+str(c)
            if person.has_key(concatenacion):
                linea = linea + person[concatenacion] + " "
            else:
                if a=='H' or a=='M' or a =='O':
                    linea = linea + a + " "
                elif b=='H' or b=='M' or b =='O':
                    linea = linea + b + " "
                elif c=='H' or c=='M' or c =='O':
                    linea = linea + c + " "
                else:
                    linea = linea + primer_camino[i][j] + " "
        solucion.write(linea+"\n")
    solucion.close()

    return


def CostosTotales(diccionario):
    #Humano al K y Salida.
    finales={}
    costos = diccionario.items()
    costos.sort()
    while len(costos)>0:
        suma=int(costos[0][1])+ int(costos[1][1])
        print "El costo de "+str(costos[1][0]) + " Es de :" + str(suma)
        finales[str(costos[1][0])]=suma
        costos.remove((costos[0][0],costos[0][1]))
        costos.remove((costos[0][0],costos[0][1]))
    return finales


main()