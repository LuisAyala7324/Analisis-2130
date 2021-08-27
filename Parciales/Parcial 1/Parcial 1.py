# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:18:28 2021

@author: felip
"""

import math
from matplotlib import pyplot

def PuntoFijoCalcular(funcion,funcion2, referencia, tolerancia, iter):
    iteracionN = 1
    aux = 1
    condicion = True
    while condicion:
        x = funcion2(referencia)
        #print('Iteracion numero %d, el valor del punto fijo = %0.6f y  la funcion en este punto = %0.6f' % (iteracionN, x, funcion(x)))
        referencia = x

        iteracionN = iteracionN + 1
        
        if iteracionN > iter:
            aux=0
            print("\nSe alcanzo el maximo de iteraciones")
            break
        
        condicion = abs(funcion(x)) > tolerancia
        
    if aux==1:
        print('\nLa raiz para esta funcion es: %0.8f y la funcion en este punto = %0.8f' % (x, funcion(x)))
        print("Tolerancia: ",abs(funcion(x))," Iteraciones: ", iteracionN)
    else:
      print('El valor del punto fijo = %0.8f y  la funcion en este punto = %0.8f' % (x, funcion(x)))
      print("Tolerancia: ",abs(funcion(x))," Iteraciones: ", iteracionN)
      
TOL= 10**(-10)
n=10000
r=-1

#funcion
f1 = lambda x: x**3 + 2*x + math.sqrt(4+2)

#funcion de aproximación
g1 = lambda x: (-(x**3)-math.sqrt(4+2))/2

x = range(-2, 2)
pyplot.plot(x, [f1(i) for i in x])
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

respuesta = PuntoFijoCalcular(f1,g1,r,TOL,n)
 