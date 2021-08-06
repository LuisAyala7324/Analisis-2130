# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 22:00:26 2021

@author: felip
"""

#2,1 Aproximacion

import math

# Teniendo en cuenta la serie de taylor para e^x = 1 + 1/1!*x + 1/2!*x^2 + 1/3!*x^3 ...
def Taylor(x,rep):
    resul = 0
    for cont in range (rep):
        resul += x**cont/(math.factorial(cont))
    return resul

# Resolviendo para e^0,3 con 10 cifras significativas y repitiendo la serie de taylor 4 veces

ans = Taylor(0.3, 100)
round(ans,10)
print ('La solucion es: ',ans)

"""
Dependiendo del numero de repeticiones de la serie va a ser mas o menos exacto el valor obtenido, de aqui viene el 
error de truncamiento
"""