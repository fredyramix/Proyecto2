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
    linea=archi.readline()
    while linea!="":
        linea=archi.readline()
        #sin = linea.split(' ')
        #print sin
        #raw_input("Espera")
        a= linea[2:10]
        b=linea[13:15]
        dic[a]=b
    archi.close()
    return dic

def ComprobacionCosto(punto,personaje,d,costos):
    puntos ={1:'P1',2:'P2',3:'P3'}
    personajes ={1:'H',2:'M',3:'C',4:'O',5:'S',6:'W'}
    destinos ={1:'T',2:'K',3:'S',4:'F'}
    cadena=""+puntos[punto]+"_"+personajes[personaje]+"_"+destinos[d]+"_P"
    if costos.has_key(cadena):
        valor = costos[cadena]
        return True
    else: return False

