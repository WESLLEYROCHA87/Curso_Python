# https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=9

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre elas;

inf = input('Digite algo:  ')
print('É númerico: ', format(inf.isnumeric()))
print('É Letra: ', format(inf.isalpha()))
print('Somente maiúculo: ', format(inf.isupper()))
print('Somente minúsculo: ', format(inf.islower()))


