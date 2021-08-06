# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 23:39:45 2021

@author: felip
"""

# Aqui se introduce la funcion
funcion = 'x^3-2*x^2+4*x/3−8/27'
val = 4
poli = funcion.replace('x',str(val))

suma = 0
rest = 0
mult = 0
div = 0
pot = 0
cont = 0

resul = int(poli[0])
for i in poli:
    if(i=='+'):
        resul+=int(poli[cont+1])
        suma+=1
        cont+=1
    elif(i=='-'):
        resul-=int(poli[cont+1])
        rest+=1
        cont+=1
    elif(i=='*'):
        resul=resul*int(poli[cont+1])
        mult+=1
        cont+=1
    elif(i=='/'):
        resul=resul/int(poli[cont+1])
        div+=1
        cont+=1
    elif(i=='^'):
        resul=pow(resul,int(poli[cont+1]))
        pot+=1
        cont+=1
    else:
        cont+=1
        pass

print ('La cantidad de sumas: ',suma,' restas: ',rest,' multiplicaciones: ',mult, 'divisiones: ',div,' potencias: ', pot)
print ('El resultado del polinomio es: ',resul)
