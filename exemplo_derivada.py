# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:38:11 2022

@author: mirelle
"""

import numpy as np
import sympy as smp

def eval_f(fx, x):
    return eval(fx)

x = smp.symbols('x')
f = '3*x**3 - 2*x**2'
dfdx = smp.diff(f, x)
print(dfdx)