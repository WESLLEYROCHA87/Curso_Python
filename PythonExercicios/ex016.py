# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import ceil
num = float(input('Digite um número real: '))
num = ceil(num)
print('O número digitado arredondado para cima fica: {} '.format(num, ceil(num)))