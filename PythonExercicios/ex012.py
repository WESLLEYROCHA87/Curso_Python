# https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=20
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Informe o preço do produto: R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.' .format(preco,novo))
