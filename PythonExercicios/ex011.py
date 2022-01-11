# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m2.
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
print('Sua parede tem a dimenssão de {} x {} e sua área é de {} m2.' .format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {} l de tinta.' .format(tinta))
