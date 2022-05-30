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


# Desafio 052
# Faça um programa que leia um NUMERO INTEIRO e diga se ele e ou nao um NUMERO PRIMO.
print('==============================================================================')
ni = int(input('Digite um numero interio: '))
t = 0
for c in range(1, ni + 1):
    if ni % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'. format(ni, t))
if t == 2:
    print('Numero PRIMO!')
else:
    print('Nao e PRIMO!')


# Desafio 053
# Crie um programa que leia um FRASE qualquer e diga se ela e um PALINDROMO, desconsiderando os espaços.
# Ex: APOS A SOPA - A SACADA DA CASA - A TORRE DA DERROTA - O LOBO AMA O BOLO - ANOTARAM A DATA DA MARATONA
print('==============================================================================')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverter = ''
for letra in range(len(juntar) -1, -1, -1):
    inverter += juntar[letra]
print('A frase {} invertida fica {}'.format(juntar, inverter))
if inverter == juntar:
    print('A frase e PALINDROMO!')
else:
    print('A frase nao e um PALINDROMO!')


# Desafio 054
# Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
print('==============================================================================')
import datetime
data = datetime.date.today().year
quantidade1 = 0
quantidade2 = 0

for pessoas in range(1, 8):
    anonascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    maior = data - anonascimento
    if maior >= 21:
        quantidade1 += 1
    else:
        quantidade2 += 1
print('{} pessoas sao de maior'.format(quantidade1))
print('{} pessoas sao de menor'.format(quantidade2))


# Desafio 055
# Faça um programa que leia o peso de cinco  pessoas. No final, mostre qual foi o maior e o menor peso lidos.
print('==============================================================================')
pesomaior = 0
pesomenor = 0
for pes in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(pes)))
    if pes == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('\nO Maior peso e {}'.format(pesomaior))
print('O Menor peso e {}'.format(pesomenor))


# Desafio 056
# Desenvolva um programa que leia o NOME, IDADE, e SEXO de 4 PESSOAS. No final do programa , mostre:
# A media de idade do grupo,
# Qual e o nome do homem mais velho.
# Quantas mulheres tem MENOS DE 20 anos.
print('==============================================================================')
somaridade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for z in range(1, 5):
    print('---------- {}ª PESSOA ----------'.format(z))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
    somaridade += idade
    if z == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaidade = somaridade / 4
print('O homem mais velho e o {} com {} anos'.format(nomevelho, maioridadehomem))
print('A media de idade do grupo e {} anos'.format(mediaidade))
print('Tem {} mulheres menor de 20 anos\n'.format(mulher20))
