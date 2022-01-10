# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Entre com o valor em Metros: '))

c = valor * 100
m = valor * 1000

print('Centímetro(s): {}' .format(c))
print('Milímetro(s): {}' .format(m))
