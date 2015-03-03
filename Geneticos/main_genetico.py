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
    p =10#Numero de individuos
    nobj=4 #numero de objetivos es el tamaño que tendrá nuestro cromosoma.
    poblacion=[]
    count =1
    while count<=p:
        cromosoma=[]
        c=1 #contador de referencia para el numero de de objetivos
        while c<=nobj:
            obj=[]
            punto=aleatorio_punto_inicio()
            personaje=personaje_aleatorio()
            while ComprobacionCosto(punto,personaje,c,costos)==True:
                print "Encontro Personaje con Costo -2"
                personaje=personaje_aleatorio()
                ComprobacionCosto(punto,personaje,c,costos)
            while BuscaRepetido(cromosoma,personaje)==True:
                #si devuelve True ya se encuentra ese Personaje Realizando esa misión por lo tanto generar otro personaje.
                print "Encontro Personaje repetido en cromosoma"
                print cromosoma
                personaje=personaje_aleatorio()
                ComprobacionCosto(punto,personaje,c,costos)
            obj.append(punto)
            obj.append(personaje)
            c=c+1
            cromosoma.append(obj)
        poblacion.append(cromosoma)
        count = count +1 # se ha generado un cromosoma correctamente
    print "Primera generacion Aleatoria:"
    for individuo in poblacion:
        print individuo

main()