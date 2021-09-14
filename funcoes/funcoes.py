
# funções pré-definidas que podemos utilizar

# print('olá')

 # recebe uma string para exibir no console e retorna uma string representando
 # o valor inserido pelo usuario
# nome = input('insira um nome: ')

# num = int('10')

# num2 = float('5.5')

#  Podemos imaginar alguns critérios para um número da sorte:

#  é positivo;
#  é negativo;
#  é par;
#  é ímpar;
#  é um múltiplo de 5;
#  é um número primo;
#  não é 17;
#  mais algum?

# número de sorte da Mari: é positivo E é ímpar E não é 17
num = 17
if num > 0 and num % 2 != 0 and num != 17:
  print(f'{num} é um número de sorte para a Mari')
else:
  print(f'{num} não é um número de sorte para a Mari')


# número de sorte da Miri: negativo e par
num = 30
if num < 0 and num % 2 == 0:
  print(f'{num} é um número da sorte para a Miri')
else:
  print(f'{num} não é um número de sorte para a Miri')

# número de sorte do Marcos: 



# COM FUNÇÕES É MAIS GOSTOSO

# definição de uma função

# entrada: um número a ser verificado
# saída: true caso o número seja positivo, false caso contrário
def ePositivo(num):
  if num > 0:
    return True
  else:
    return False

# entradas:  um número a ser verificado
# saída: true caso o número seja ímpar, false caso contrário
def eImpar(num):
  return (num % 2) != 0

# entradas:  um número a ser verificado
# saída: true caso o número seja diferente de 17, false caso contrário
def naoEDezessete(num):
  return num != 17

# def ePrimo(num):


# número de sorte da Mari: é positivo E é ímpar E não é 17
num = 35

# invocando/chamando/executando as funções
if ePositivo(num) and eImpar(num) and naoEDezessete(num):
  print(f'{num} é um número de sorte para a Mari')
else:
  print(f'{num} não é um número de sorte para a Mari')

# número de sorte da Miri: negativo e par
if not ePositivo(num) and not eImpar(num):
  print(f'{num} é um número de sorte para a Miri')
else:
  print(f'{num} não é um número de sorte para a Miri')

# Marcos, Lucas, Pedro, Luiz etc......


# entradas e saídas

# f(x) = ax + b = 0
# ex: 2x - 4 = 0
#     2x = 4
#      x = 4 / 2 = 2
# 
# fórmula: ax + b = 0
#           x = -b/a
# ex: 3x + 9
# a = 3
# b = 9
# x = -b/a = -9/3 = -3

# entrada: índices a e b de uma equação do primeiro grau
# saída: a raiz da equação para os índices dados
def primeiroGrau(a, b):
  return -b/a


result = primeiroGrau(5, -10)
print(f'raiz 5x - 10: {result}')

result = primeiroGrau(4, 26)
print(f'raiz 4x + 26: {result}')

result = primeiroGrau(-7, 17)
print(f'raiz -7x + 17: {result}')


print(f'raiz -8x - 10: {primeiroGrau(-8, -10)}')


# PRATICANDO

# 1. escreva a função quantoCarrega() em Python conforme descrita aqui:
# https://mumuki.io/br/exercises/4460-programacao-imperativa-funcoes-e-tipos-de-dados-aquecedores-de-agua

# 2. escreva a função quantoCusta() em Python conforme descrita aqui:
# https://mumuki.io/br/exercises/4469-programacao-imperativa-pratica-funcoes-e-tipos-de-dados-comprando-hardware

# 3. escreva a função meConvem() em Python conforme descrita aqui:
# https://mumuki.io/br/exercises/4470-programacao-imperativa-pratica-funcoes-e-tipos-de-dados-me-convem

