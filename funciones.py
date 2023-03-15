#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:50:57 2023

@author: alejandro
"""

from math import e, factorial, comb


def binomial(N:int, x:int, p:float) -> float:
    
    N = int(N)
    x = int(x)
    p = float(p)
    
            
    if (p < 0) or (p > 1):
        raise ValueError('El valor de p debe estar entre 0 y 1')
    
    if (N < 0) or (x < 0):
        raise ValueError('Se debe cumplir: 0 <= N, 0 <= x')
    
    if N < x:
        raise ValueError('Se debe cumplir: x <= N')
    
    
    resultado = comb(N, x) * p ** x * (1 - p) ** (N - x)
    return resultado
#%%
binomial(-10, 0, 0.2)



