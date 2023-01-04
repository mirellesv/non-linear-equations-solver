# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:55:10 2022

Trabalho 1 - Implementação de um sistema de resolução de equações
não lineares

Disciplina: Cálculo Numérico

Nome: Mirelle Silva Vieira

1. O programa recebe inicialmente uma equação e um intervalo para
plotar o gráfico.
2. O usuário pode ajustar o intervalo até que decida calcular a
raíz da equação
3. Quando o usuário confirmar o intervalo, o sistema calcula a raíz
utilizando os métodos estudados.
4. Os métodos Posição Falsa, Ponto Fixo e Secantes são utilizados.
"""

from Plotagem import *
from posicao_falsa import met_posicao_falsa
from secantes import met_secantes
from ponto_fixo import *
import numpy as np
import sympy as smp

print('---------------------------------------------')
print('SISTEMA DE RESOLUÇÃO DE EQUAÇÕES NÃO LINEARES')
print('---------------------------------------------')
    
f = input('Insira a equação desejada: ')
print('Determinando o intervalo [a, b] ...')
while True: # Laço de repetição que irá permitir que o usuário ajuste o
            # intervalo até decidir calcular a raíz da equação
    a = float(input('Insira o valor de a: '))
    b = float(input('Insira o valor de b: '))
    plot(f, a, b)
    print('Deseja alterar o intervalo? (S/N)')
    resp = input()
    if(resp.lower() == 'n'):
        break
    
    
tol = float(input('Insira a tolerância que limitará o erro: '))
n = int(input('Insira o número máximo de iterações: '))

while True:
    print('-------------------------------------------------------------')
    print('Selecione o método desejado para calcular a raíz da equação: ')
    print('[1] Posição Falsa')
    print('[2] Ponto Fixo')
    print('[3] Secantes')
    print('[4] Escolher outra equação')
    print('[5] Sair do programa')
    resp = int(input('Resposta: '))
    if(resp == 1):
        met_posicao_falsa(f, a, b, tol, n)
    elif(resp == 2):
        alpha = float(input('Insira o valor de α: '))
        g = 'x - ' + str(alpha) + '* (' + f + ')'
        x = smp.symbols('x')
        glx = str(smp.diff(g, x))
        plot_pf(f, g, glx, a, b)
        met_ponto_fixo(f, g, a, b, tol, n)
    elif(resp == 3):
        met_secantes(f, a, b, tol, n)
    elif(resp == 4):
        print('Ainda to pensando...')
    elif(resp == 5):
        print('Saindo...')
            
    print('Deseja continuar? (S/N)')
    resp = input()
    if (resp.lower() == 'n'):
        break    