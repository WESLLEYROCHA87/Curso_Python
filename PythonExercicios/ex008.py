# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Entre com o valor em Metros: '))

cm = valor * 100
mm = valor * 1000

print('Centímetro(s): {}' .format(cm))
print('Milímetro(s): {}' .format(mm))
