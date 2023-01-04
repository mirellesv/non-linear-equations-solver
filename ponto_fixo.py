# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:26:39 2022

@author: mirelle
"""

import numpy as np
import matplotlib.pyplot as pyplot

def eval_f(fx, x):
    return eval(fx)

def plot_pf(fx, gx, glx, a, b):
    interval = np.linspace(a, b)
    pyplot.plot(interval, eval_f(fx, interval), label = "f(x)")
    pyplot.plot(interval, eval_f(gx, interval), label = "g(x)")
    pyplot.plot(interval, eval_f(glx, interval), label = "g'(x)")
    pyplot.legend()
    pyplot.grid()
    pyplot.show()
    
def met_ponto_fixo(f, g, a, b, tol, n):
    xant = float("nan")
    x = (a + b) / 2
    for k in range(n):
        xant = x
        x = eval_f(g, x)
        error = abs((x - xant) / max(x, 1))
        print("Iteração {k:3d}: x = {x:+.6f}, ".format(k = k, x = xant) +
              "g(x) = {gx:+.6f}, error = {error:+.6f}".format(gx = x, error = error))
        if(x == xant) or (error < tol):
            print('Raíz paroximada encontrada {raiz:+.6f}'.format(raiz = x))
            break