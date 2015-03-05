# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import random

def aleatorio_punto_inicio():
    return random.randint(1,3)


def personaje_aleatorio():
    return  random.randint(1,6)


def BuscaRepetido(lista, elemento):
    if len(lista) !=0:
        for x in lista:
            if x[1]==elemento:
                return True
    return False
#Funcion para leer tabla de costos y agregarlo a un diccionario
def LeerTablaCostos():
    dic={}
    archi=open('../Soluciones/costos.txt','r')
    linea="a"
    while linea!="":
        try:
            linea=archi.readline()
            lin= linea.split(',')
            print lin
            #print sin
            #raw_input("Espera")
            a= lin[0]
            c=lin[1]
            b=c[:-1]
            dic[a]=b
        except IndexError,e:
            pass #Este error se produce por caracter de salto de linea en el ultimo archivo
    archi.close()
    return dic #retorna en forma de diccionario todos los costos 'P3_M_K_P':'costo'

def ComprobacionCosto(punto,personaje,d,costos,lista):
    puntos ={1:'P1',2:'P2',3:'P3'}
    personajes ={1:'H',2:'M',3:'C',4:'O',5:'S',6:'W'}
    destinos ={1:'T',2:'K',3:'S',4:'F'}
    cadena=""+puntos[punto]+"_"+personajes[personaje]+"_"+destinos[d]+"_P"
    if costos.has_key(cadena):
        if costos[cadena] == "1000000":
            return True
        else:
            if len(lista) !=0:
                for x in lista:
                    if x[1]==personaje:
                        return True
                    #else:
                    #   return False
            return False
    else:
        return True

def CalculoFX(poblacion,costos):
    puntos ={'1':'P1','2':'P2','3':'P3'}
    personajes ={'1':'H','2':'M','3':'C','4':'O','5':'S','6':'W'}
    destinos ={'1':'T','2':'K','3':'S','4':'F'}
    for ind in poblacion: #para cada cromosoma del numero de la poblacion calcular su fx
        ob=1 # posicion en cromosoma tenemos 4 porque son 4 objetivos
        sum = 0
        for obj in ind:
            cadena=""+puntos[str(obj[0])]+"_"+personajes[str(obj[1])]+"_"+destinos[str(ob)]+"_P"
            valor = costos[cadena]
            print valor
            sum = sum + int(valor)
            ob = ob + 1
        ind.append(sum)
    return poblacion

def Penalizar(poblacion,costos):
    #las penalizaciones estarán dadas primero por repetirse y segunda por tener costos negativos
    puntos ={'1':'P1','2':'P2','3':'P3'}
    personajes ={'1':'H','2':'M','3':'C','4':'O','5':'S','6':'W'}
    destinos ={'1':'T','2':'K','3':'S','4':'F'}

    for ind in poblacion:
        listaPersonajes=[]
        count=1
        pena=0
        for ob in ind:
            try:
                cadena=""+puntos[str(ob[0])]+"_"+personajes[str(ob[1])]+"_"+destinos[str(count)]+"_P"
                cost=costos[cadena]
                if cost=="1000000":
                    print "Esta penalizando por costo infinito"
                    print cadena
                    pena=pena+10000
            except TypeError,e:
                pass #lo que pasa es que metimos f(X) y no corresponde el tamaño
            try:
                listaPersonajes.append(ob[1])
                count=count+1
            except TypeError,e:
                pena=0
                pass

        #print listaPersonajes
        num_rep=0
        for a in listaPersonajes:
            num_rep=num_rep+listaPersonajes.count(a)
        penaliz=0
        if num_rep !=4:
            print "Esta penalizando por repeticion"
            #comienza la penalizacion segun su numero de repeticiones.
            penaliz=num_rep * 100000
        #else:
         #   penaliz=0
            #print penaliz
        #Una vez terminada la penalizacion por repeticion de personaje en la mision global.
        #Se penalizara por tener un costo negativo :D
        #print ind
        totalpena= pena + penaliz + ind[4]
        #print totalpena
        ind.append(totalpena)
    return  poblacion


def SumatoriaFX(lista):
    suma=0
    for x in lista:
        suma=suma+abs(int(x[4]))
    return suma


def Probabilidad(sum,individuos):
    # for x in individuos:
    #     resta=float(sum)-float(x[4])
    #     p=(resta*100)/float(sum)
    #     x.append(int(p))
    for x in individuos:
         #resta=float(sum)-float(x[4])
         p=(float(x[5])/(float(sum)))*100
         x.append(int(p))
    return individuos

def Ruleta(lista):
    rul=[]
    for x in lista:
        x.reverse()
        rul.append(x)
    rul.sort()
    new=[]
    for y in rul:
        y.reverse()
        new.append(y)
    return new

def SeleccionParejas(opciones,p):
    count =0
    tabla_hijos=[]
    while count!=p:
        n=random.randrange(0,100)
        for x in opciones:
            if int(x[6]) <= n:
                tabla_hijos.append(x[:4])
                count=count+1
                break
            else:
                pass
    return opciones,tabla_hijos

def BEST(hijos,prueba):
    for h in hijos:
        if h[4]<prueba[4]:
            prueba[0]=h[0]
            prueba[1]=h[1]
            prueba[2]=h[2]
            prueba[3]=h[3]
            prueba[4]=h[4]
    return prueba