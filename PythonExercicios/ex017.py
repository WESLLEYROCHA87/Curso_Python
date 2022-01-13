# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa

# Modo Tradicinal:
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co * 2 + ca ** 2) ** (1/2)
print('A hipotenusa vau medir {}'.fomrat(hi))


# Modo com Biblioteca
'''from math import hypot
cOposto = float(input('Digite o comprimento do Cateto Oposto: '))
cAdjacente = float(input('Digite o comprimento do Cateto Adjacente: '))
cHipotenusa = hypot(cAdjacente, cOposto)
print('O comprimento da Hipotenusa é: {:.2f}'.format(cHipotenusa))'''
