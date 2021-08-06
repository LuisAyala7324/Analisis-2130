# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:34:06 2021

@author: felip
"""

# 1. Algoritmo

from math import sqrt

#Donde n es el numero a evaluar, E la tolerancia y x el valor inicial
def algoritmo(n,E,x):
    y = (1/2)*(x+(n/x))
    while(abs(x-y)>E):
        x = y
        y = (1/2)*(x+(n/x))
        print (y)
    return y

# Resultado con nivel de tolerancia de 10^-8

resul1 = algoritmo(7, 10**-8, 2)
print ('El resultado con nivel de tolerancia de 10^-8 es: ', resul1)   

# Resultado con nivel de tolerancia de 10^-16

resul2 = algoritmo(7, 10**-16, 2)
print ('El resultado con nivel de tolerancia de 10^-16 es: ', resul2)   

#Validacion

resulv = sqrt(7)
print ('El resultado con sqrt es: ', resulv) 
