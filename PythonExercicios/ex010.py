# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar:
# Considere US$ 1,00 = R$ 3,27
carteira = float(input('Quanto tem em dinheiro: R$ '))
print('Pode comprar U$ {:.2f} em dólares.' .format(carteira / 3.27))
