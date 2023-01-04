# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:51:52 2022

@author: mirelle
"""

from Plotagem import eval_f

# Método da Posição Falsa
# Recebe a função f, o intervalo [a, b], a tolerância e o número de iterações

def met_posicao_falsa(f, a, b, tol, n):
    xant = float("nan") # Não existe um x anterior no início
    fa = eval_f(f, a)
    fb = eval_f(f, b)
    for k in range(n):
        x = (a*fb - b*fa)/(fb - fa) # Calculando x
        fx = eval_f(f, x)
        sinal = fa * fx # O sinal é fa * fx. Ele determinará o novo intervalo
        error = abs((x - xant)/max(x, 1)) # Calculando o erro relativo
        xant = x # xant é atualizado para que possa ser utilizado na próxima iteração
        # Mostrando os resultados da iteração atual
        
        print('Iteração {k:3d}: a = {a:+.6f}, '.format(k = k, a = a) + 
              'b = {b:+.6f}, error = {error:+.6f}, '.format(b = b, error = error) +
              'x = {x:+.6f}, f(x) = {fx:+.6f}, '.format(x = x, fx = fx) +
              'sinal = {sinal:+.6f}'.format(sinal = sinal))
        
        if(fx == 0) or (error < tol): # Testando o critério de parada
            print('Raíz aproximada encontrada: {r:+.6f}'.format(r = x))
            break # Saímos do laço de repetição se o critério for respeitado
        
        if(sinal > 0): # A raíz está entre x e b?
            a = x
            fa = fx
        else: # A raíz está entre a e x?
            b = x
            fb = fx
        