# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:36:21 2022

@author: mirelle
"""
import numpy as np
import matplotlib.pyplot as pyplot

def eval_f(fx, x):
    return eval(fx)
    
def plot(fx, a, b):
    interval = np.linspace(a, b)
    pyplot.plot(interval, eval_f(fx, interval), label = "f(x)")
    pyplot.legend()
    pyplot.grid()
    pyplot.show()