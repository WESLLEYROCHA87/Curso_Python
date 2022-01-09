# https://www.youtube.com/watch?v=Vw6gLypRKmY&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=12

# Curso Python #07 - Operadores Aritméticos
print('=='*70)

print('Soma: ', format(5 + 2))
print('Subtraçaõ: ', format(5 - 2))
print('Multiplicação: ', format(5 * 2))
print('Divisão: ', format(5 / 2))
print('Exponenciação: ', format(5 ** 2))
print('Divisão inteira: ', format(5 // 2))
print('Resto: ', format(5 % 2))

print('=='*40)

# Ordem de Procedência:
# 1- Parenteses;
# 2- Exponenciação;
# 3- Multiplicação -> Divisão -> Divisão inteira -> Resto da Divisão;
# 4- Soma -> Subtração;

# Outra forma de fazer exponeciação:

print('Exponeciação através da função interna POW: ', pow(4, 3))

print('=='*40)

# Formatação
print('=='*40)
nome = input ('Informe seu nome: ')
# centralizado dentro de 20 espaços
print('Prazer em te conhecer {:^20}!'.format(nome))

# Formatando casas decimais:
n1 = 5
n2 = 5.25
total = n1 * n2
print('A Multiplicação e: {:.3f}' .format(total))

# Quebra de Linha -> \n
# Não quebrar -> digitar no final da linha: ,end=''
