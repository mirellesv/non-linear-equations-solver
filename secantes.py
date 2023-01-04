# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:16:12 2022

@author: mirelle
"""

from Plotagem import eval_f

# Método das Secantes
# Recebe a função f, o intervalo [a, b], a tolerância e o número máximo de iterações

def met_secantes(f, a, b, tol, n):
    xant = a
    x = b
    
    for k in range(n):
        fx = eval_f(f, x)
        fxant = eval_f(f, xant)
        error = abs((x - xant)/max(x, 1)) # Calculando o erro relativo
        # Mostra os resultados da iteração atual
        print('Iteração {k:3d}: a = {a:+.6f}'.format(k = k, a = a) + 
              ' b = {b:+.6f}, f(x) = {fx:+.6f}'.format(b = b, fx = fx) +
              ' f(xant) = {fxant:+.6f}'.format(fxant = fxant) +
              ' error = {e:+.6f}'.format(e = error))
        if(fx == 0) or (error < tol): # Testando o critério de parada
            print('Raíz aproximada encontrada: {r:+.6f}'.format(r = x))
            break # O laço de repetição parará se o critério for respeitado
        xprox = x - fx * (x - xant)/(fx - fxant) # Calculando xprox
        xant = x # Atualizando xant
        x = xprox # Atualizando x
        
        