# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import randint
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digiite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
sorteio = randint(nome1, nome2, nome3, nome4)






