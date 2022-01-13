# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
'''import math #importa todas as funcionalidades
from math import trunc
num = float(input('Digite um número real: '))
print('O número {} digitado arredondado para cima fica: {} '.format(num, math.trunc(num)))'''

num = float(input('Digite um valor:  '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))


