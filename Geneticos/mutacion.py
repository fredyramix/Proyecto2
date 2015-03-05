# -*- encoding: utf-8 -*-
__author__ = 'fredy'
import random

def Mutacion(cromozomas_cruzados,p):
    n = random.randrange(1,p-1) #para escoger que cromosoma.
    #convertir esa mutacion
    print n
    m=Convertir_a_Binario(cromozomas_cruzados[n])
    print m
    nuevo_mutado=[]
    while len(m)!=0:
        lisss=[]
        a=m[0:2]
        b=m[2:5]
        num=""
        num=num+a[0]
        num=num+a[1]
        person=""
        person=person+b[0]
        person=person+b[1]
        person=person+b[2]
        nu=int(num,2)
        pe=int(person,2)
        lisss.append(nu)
        lisss.append(pe)
        nuevo_mutado.append(lisss)
        del m[0:5]
    print nuevo_mutado
    while VerificarMutacion(nuevo_mutado)==False:
        #no cromosomas validos
        #raw_input("Encontro cromosoma invalido")
        return False
        break
    cromozomas_cruzados[n]=nuevo_mutado
    for x in cromozomas_cruzados:
        print x
    return cromozomas_cruzados


def Convertir_a_Binario(X):
    print X
    numbinarizado=""
    for i in X:
        a=bin(i[0]) #punto #convertirlo a 2 bits  1  1
        b=bin(i[1])#personaje  ... convertirlo a 3 bits  1 1 1
        c= a[2:]
        d= b[2:]
        if len(c)==1:
            var='0'
            var=var+c
            c=var
        if len(d)==1:
            var='00'
            var=var+d
            d=var
        if len(d)==2:
            var='0'
            var=var+d
            d=var
        numbinarizado=numbinarizado+c+d
    alistada=[]
    for h in numbinarizado:
        alistada.append(h)
    n = random.randrange(1,20)
    if alistada[n]=='0':
        alistada[n]='1'
    else:
        alistada[n]='0'
    return alistada

def VerificarMutacion(nuevo_mutado):
    bandera=True
    for i in nuevo_mutado:
        if i[0] > 0 and i[1] >0 and i[1]<7 :
            print i
            bandera=True
        else:
            print i
            bandera=False
            break

    return bandera