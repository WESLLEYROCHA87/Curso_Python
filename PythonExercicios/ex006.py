#https://www.youtube.com/watch?v=mqcNw_dhl8I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=14
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número qualquer: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O Dobro é: {}, \no Triplo é: {} e a \nRaiz Quadrada é: {:.2f}'. format(d, t, r))



