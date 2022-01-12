# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
cOposto = float(input('Digite o comprimento do Cateto Oposto: '))
cAdjacente = float(input('Digite o comprimento do Cateto Adjacente: '))
cHipotenusa = hypot(cAdjacente, cOposto)
print('O comprimento da Hipotenusa é: {}'.format(cHipotenusa))
