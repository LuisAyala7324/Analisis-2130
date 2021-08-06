# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:00:04 2021

@author: felip
"""
import numpy

def biseccion(f,v_ini,v_fin,t):
    x1=v_ini
    x2=v_fin
    
    if(f(v_ini)*f(v_fin)>0):
        print('En esta seccion el metodo no funciona')
    while(abs(x1-x2)>t):
        x1=x2
        x2=(v_ini+v_fin)/2
        if(f(v_ini)*f(v_fin)<0):
            v_fin=x2
        if(f(v_ini)*f(v_fin)<0):
            v_ini=x2
        print(x2)
            
    return x2
    
f = lambda x: x*numpy.cos(x**2)+1
sol = biseccion(f,1,2,10**(-6))
print('La solucion es: ', sol)         
        