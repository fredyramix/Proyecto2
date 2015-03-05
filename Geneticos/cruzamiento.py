__author__ = 'fredy'
def Cruzar(hijos):
    cruzados=[]
    for i in hijos:
        i.pop() # quito el valor del resultado que ya no nos servira
    while len(hijos) != 0:
        try:
            mitad1=hijos[0][0:2] #obtenemos la mitad del cromosoma
            mitad2=hijos[0][2:4]
            mitad3=hijos[1][0:2] #obtenemos la mitad del cromosoma
            mitad4=hijos[1][2:4]
            cromo1= mitad1 + mitad4
            cromo2 = mitad3 + mitad2
            cruzados.append(cromo1)
            cruzados.append(cromo2)
            del hijos[0]
            del hijos[0]
            pass
        except IndexError, e: #Este error es porque
            pass
            break

    return cruzados