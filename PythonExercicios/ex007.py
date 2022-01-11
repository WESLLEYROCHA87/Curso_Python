# https://www.youtube.com/watch?v=_QfISzy0IKs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=15
# Desenvolva um prograrma que leia as duas notas de um aluno e mostre sua média:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} é igual a: {:.1f}' .format(n1, n2, media))
