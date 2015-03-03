# -*- encoding: utf-8 -*-
__author__ = 'fredy'
from funciones import *
import random
def main(): #recibira una tabla de costos. los puntos de incio y los personajes.
    #Primer paso crear una poblacion aleatoria de 60 individuos.
    #En el cromosoma no se deben repetir los personajes
    #Comprobar que el Personaje no tenga un costo -2.

    #Hacer una funcion para leer el archivo de costos y agregarlos a un diccionario:
    costos = LeerTablaCostos()
    #print costos
    p = 20#Numero de individuos
    nobj=4 #numero de objetivos es el tamaño que tendrá nuestro cromosoma.
    poblacion=[]
    count =1
    while count<=p:
        cromosoma=[]
        c=1
        while c<=nobj:
            obj=[]
            punto=aleatorio_punto_inicio()
            personaje=personaje_aleatorio()
            if ComprobacionCosto(punto,personaje,c,costos)==True:#donde c+1 es el objetivo
                while BuscaRepetido(cromosoma,personaje)==True:
                    #si devuelve True ya se encuentra ese Personaje Realizando esa misión por lo tanto generar otro personaje.
                    personaje=personaje_aleatorio()
                    BuscaRepetido(cromosoma,personaje)
                obj.append(punto)
                obj.append(personaje)
                c=c+1
            else:
                personaje1=personaje_aleatorio()
                ComprobacionCosto(punto,personaje1,c,costos)
            cromosoma.append(obj)
            cromosoma.append(obj)
        poblacion.append(cromosoma)
        print cromosoma
        count = count +1
    print "Primera generacion Aleatoria:"
    for individuo in poblacion:
        print individuo

main()