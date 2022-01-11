# https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=24
# Utilizando Módulos
# Comando para a utilização de Módulos:
# 1. import -> bebidas -> Todos
# 2. from -> doce -> import -> produto específico
# 3. from -> doce -> import -> produto1, produto2

# Biblioteca padrao: math => significa Matemática - (Vai trazer biblioteca matemática)
# Exemplos ->
# math -> ceil =>  (faz o arredondamento para cima)
# math -> floor => (faz o arredondamento para baixo)
# math -> trunc => (vai eliminar da vírgula para frente, sem arredondamento algum )
# math -> pow => (Potência)
# math -> sqty => (calc raiz quadrada)
# math -> factorial => (calculo de fatorial)

#import math
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
