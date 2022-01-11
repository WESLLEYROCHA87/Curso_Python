# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

precoInicial = float(input('Informe o preço inicial: '))
desconto = 0.05
precoFinal = precoInicial * desconto - precoInicial

print('Preço com desconto é de: {}' .format(precoFinal))

