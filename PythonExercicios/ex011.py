# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m2.

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura

totalTinta = area * area

print('Total tinta: {}', format(totalTinta))






