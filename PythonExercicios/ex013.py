# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salarioInicial = float(input('Qual o salário: '))
acrescimo = 0.15
salarioFinal = salarioInicial * acrescimo + salarioInicial

print('Seu novo salário é: {}'.format(salarioFinal))