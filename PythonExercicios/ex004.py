# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre elas;

inf = input('Digite algo:  ')
print('É númerico: ', format(inf.isnumeric()))
print('É Letra: ', format(inf.isalpha()))
print('Somente maiúculo: ', format(inf.isupper()))
print('Somente minúsculo: ', format(inf.islower()))


