# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from funciones import *
from cruzamiento import Cruzar
from mutacion import Mutacion
import random
def main(): #recibira una tabla de costos. los puntos de incio y los personajes.
    #Primer paso crear una poblacion aleatoria de 60 individuos.
    #En el cromosoma no se deben repetir los personajes
    #Comprobar que el Personaje no tenga un costo -2.
    #Hacer una funcion para leer el archivo de costos y agregarlos a un diccionario:
    costos = LeerTablaCostos()
    #print costos
    p =10#Numero de individuos
    nobj=4 #numero de objetivos es el tamaño que tendrá nuestro cromosoma.
    poblacion=[]
    count =1
    best=[[1000,1000],[1000,1000],[1000,1000],[1000,1000],1000000000]
    while count<=p:
        cromosoma=[]
        c=1 #contador de referencia para el numero de de objetivos
        while c<=nobj:
            obj=[]
            punto=aleatorio_punto_inicio()
            personaje=personaje_aleatorio()
            while ComprobacionCosto(punto,personaje,c,costos,cromosoma)==True:
                print "Encontro Personaje con Costo infinito"
                personaje=personaje_aleatorio()
                punto=aleatorio_punto_inicio()
            obj.append(punto)
            obj.append(personaje)
            c=c+1
            #print "Cromosoma Creado"
            cromosoma.append(obj)
            print cromosoma
        poblacion.append(cromosoma)
        count = count +1 # se ha generado un cromosoma correctamente
    print "Primera generacion Aleatoria:"
    for individuo in poblacion:
        print individuo
    #Despues continua el ciclo hasta el numero de iteraciones que se considere.
    NG=2000 #numero de generaciones
    x=1
    while x != NG:
        print "Calculando FX"
        funcion_evaluada=CalculoFX(poblacion,costos)
        print "Cromosomas evaluados"
        for eva in funcion_evaluada:
            print eva
        print "Penalizando..."
        print "Cromosomas ya con la penalizacion"
        funcion_penalizada=Penalizar(funcion_evaluada,costos)
        for ind in funcion_penalizada:
            print ind
        #Calcular la probabilidad de ser elegidos en base a su penalizacion y si es maximo o  minimo.
        sumatoria=SumatoriaFX(funcion_penalizada)
        print sumatoria
        #asignar probabilidad de ser elegido.

        lista_con_probabilidad=Probabilidad(sumatoria,funcion_penalizada)

        for f in lista_con_probabilidad:
            print f
        print "termino el calculo de la probabilidad"
        opciones_disponibles=Ruleta(lista_con_probabilidad)
        for f in opciones_disponibles:
            print f
        print "Termino de invertir la probabilidad:"
        padres,hijos=SeleccionParejas(opciones_disponibles,p)
        print "Imprimiendo Hijos"
        for hij in hijos:
            print hij
        print "Procede evaluarlos y tomar el menor que sera nuestra mejor solucion"

        hijos_eval=CalculoFX(hijos,costos)

        for hijos_eval_cost in hijos_eval:
            print hijos_eval_cost

        print "Termino de evaluar hijos... procede a tomar el menor y guardarlo."

        best666=BEST(hijos_eval,best)
        print "Termino de escoger el menor."
        print "Sigue proceso de cruzamiento..."
        lista_ya_cruzada=Cruzar(hijos_eval)
        print "Ya se cruzaron:"
        for li in lista_ya_cruzada:
            print li
        print "Continua proceso de mutacion"
        mutados=Mutacion(lista_ya_cruzada,p)
        while mutados==False:
            mutados=Mutacion(lista_ya_cruzada,p)
        #raw_input("Encontro cromosoma valido")
        poblacion=mutados
        x=x+1
        print best
        #raw_input("Esperar....")
    puntos ={'1':'P1','2':'P2','3':'P3'}
    personajes ={'1':'HUMANO','2':'MONKEY','3':'CROC','4':'OCTOPUS','5':'SASQUATCH','6':'WEREWOLF'}
    personajes2 ={'1':'H','2':'M','3':'C','4':'O','5':'S','6':'W'}
    print "Acabo en numero de generacion= " + str(x)
    print("El resultado final es: \n")
    print("Asignando Misiones: \n")
    print"==========Mision de Templo:========="
    a= best[0]
    print "Punto de Partida: "+ puntos[str(a[0])]
    print "Personaje Seleccionado: "+personajes[str(a[1])]
    cadena=""+puntos[str(a[0])]+"_"+personajes2[str(a[1])]+"_T_P"
    print "Costo: "+ str(costos[cadena])
    print"==========Mision de Key:============"
    a= best[1]
    print "Punto de Partida: "+ puntos[str(a[0])]
    print "Personaje Seleccionado: "+personajes[str(a[1])]
    cadena=""+puntos[str(a[0])]+"_"+personajes2[str(a[1])]+"_K_P"
    print "Costo: "+ str(costos[cadena])
    print"==========Magic Stone:============"
    a= best[2]
    print "Punto de Partida: "+ puntos[str(a[0])]
    print "Personaje Seleccionado: "+personajes[str(a[1])]
    cadena=""+puntos[str(a[0])]+"_"+personajes2[str(a[1])]+"_S_P"
    print "Costo: "+ str(costos[cadena])
    print"==========Rescue a captive Friend:=============="
    a= best[3]
    print "Punto de Partida: "+ puntos[str(a[0])]
    print "Personaje Seleccionado: "+personajes[str(a[1])]
    cadena=""+puntos[str(a[0])]+"_"+personajes2[str(a[1])]+"_F_P"
    print "Costo: "+ str(costos[cadena])
    print"=========Total Cost:==============="
    print best[4]
    import winsound
    Freq = 2500 # Set Frequency To 2500 Hertz
    Dur = 100 # Set Duration To 1000 ms == 1 second
    winsound.Beep(Freq,Dur)
main()