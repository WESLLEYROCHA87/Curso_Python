# https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=21
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Informe o valor so salario R$ '))
novoSalario = salario + (salario * 15/100)
print('O valor do salário {:.2f}, com um aumento de 15% passa a ser R$ {:.2f}'.format(salario, novoSalario))

