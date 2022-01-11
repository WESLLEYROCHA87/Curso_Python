# https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=23
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

DiasAlugado = float(input('Quantos dias alugados: '))
dia = DiasAlugado * 60
print('O total a pagar pelo(s) {} dia(s) alugado é de: R$ {:.2f}'.format(DiasAlugado, dia))

KmRodado = float(input('Informe os Km rodados '))
km = KmRodado * 0.15
print ('O total a pagar pelo(s) Km rodados {} é de R$ {:.2f}'.format(KmRodado, km))

pagar = dia + km
print('O valor total a ser pago é de R$ {:.2f}'.format(pagar))



