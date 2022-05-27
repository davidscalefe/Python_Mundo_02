# Desafio 046
# faça um programa que mostre na tela uma contagem regressiva parao estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles.
print('==============================================================================')
from time import sleep
for c in range (10, -1, -1):
    sleep(1)
    print (c)
print(' ;`;`;`;` \033[1;32mBUM!\033[m ;`;`;`;`')
print('         ;`;`;`;`\033[1;33mBUM!\033[m;`;`;`;`')
print('                 ;`;`;`;`\033[1;31mPOOOW!\033[m;`;`;`;`')


# Desafio 047
# Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.
print('==============================================================================')
for p in range(2, 51, 2):
    print(p, end=' ')
print('FIM!')


# Desafio 048
# Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.
print('==============================================================================')
soma = 0
quantidade = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        quantidade += 1
print('Quantidade de numeros imparares multiplos de 3 sao: {}'.format(quantidade))
print('A soma de todos os numeros impares multiplos de 3 de 1 a 500 e: {}'.format(soma))


# Desafio 049
# Refaça p DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um LAÇO FOR.
print('==============================================================================')
from time import sleep
print('------TABUADA------')
tabuada= int(input('Digite um numero: '))
for contador in range(1, 11):
    sleep(0.5)
    print('{} x {} = {}'.format(tabuada, contador, tabuada*contador))
print('FIM!')


# Desafio 050
# desenvolva um programa que leia SEIS NUMEROS INTEIROS e mostre a soma apenas daqueles que foram PARES. Se o valor digitado for IMPAR, desconsidere-o.
print('==============================================================================')
print('---DIGITE SEIS NUMEROS INTEIRO!---')
soma1 = 0
for x in range(1, 7):
    n1 = int(input('Digite o {} numero: '.format(x)))
    if n1 % 2 == 0:
        soma1 += n1
if soma1 == 0:
    print('Nao digitou nenhum numero PAR')
else:
    print('A soma dos numeros PARES digitado: {}'.format(soma1))


# Desafio 051
# Desenvolva um programa que leia o PRIIMEIRO TERMO e a RAZÃO de uma PA. No final =, mostre os 10 primeiros termos dessa progressao.
print('==============================================================================')
print('PRIMEIROS TERMOS DE UM PA')
a1 = int(input('Digite o Primeiro termo: '))
r = int(input('Razao: '))
for n in range(0,10):
    n = a1 + r * (n + 1)
    print('{}'.format(n), end=' → ')
print('FIM!')
