# Desafio 036
# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o VALOR DA CASA, o SALARIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo será negado.
print('==============================================================================')
valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
quantosAnos = int(input('Quantos anos de financiamento? '))
prestacao = valorCasa / (quantosAnos * 12)
print('Valor da prestacao mensal R${:.2f}'.format(prestacao))
exceder = salario * 30 / 100
if prestacao <= exceder:
    print('Emprestimo aprovado, PARABENS!!!\n')
else:
    print('Emprestimo NEGADO!!! \nValor da prestacao excede 30% do seu salario\n')



# Desafio 037
# escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a BASE DE CONVERSÃO:
# 1 para BINÁRIO
# 2 para OCTAL
# 3 para HEXADECIMAL
print('==============================================================================')
n1 = int(input('Digite um numero inteiro: '))
print('Escolha qual base de conversao \n[1] - Binario \n[2] - Octal \n[3] - Hexadecimal')
conversao = int(input('Opcao escolhida: '))
binario = format(n1, "b")
octal = format(n1, "o")
hexa = format(n1, "x")
if conversao == 1:
    print('\nBase de conversao Binario: {}\n'.format(binario))  # outra opcao seria usar .format(bin(n1)[2:]), nao usaria as variaveis
elif conversao == 2:
    print('\nBase de conversao Octal: {}\n'.format(octal))
else:
    print('\nBase de conversao Hexadecimal: {}\n'.format(hexa))


# Desafio 038
# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# O PRIMEIRO VALOR é MAIOR
# O SEGUNDO VALOR é MAIOR
# NÃO EXISTE valor maior, os dois são IGUAIS
print('==============================================================================')
numero1 = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite o segundo numero inteiro: '))
if numero1 > numero2:
    print('O primeiro valor e maior: {}'.format(numero1))
elif numero2 > numero1:
    print('O segundo valor e maior: {}'.format(numero2))
else:
    print('O primeiro valor e o segundo sao iguais')


# Desafio 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele AINDA VAI SE ALISTAR ao serviço militar.
# - Se é a HORA DE SE ALISTAR.
# - Se já PASSOU DO TEMPO do alistamento.
# Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.
print('==============================================================================')
import datetime
anodenascimento = int(input('digite seu ano de nascimento: '))
date = datetime.date.today()
data = int(date.strftime('%Y'))  # Poderia usar so date.today().year para o ano atual
idade = data - anodenascimento
print('Sua idade em {} e {} anos'.format(data, idade))
if idade >= 16 and idade < 18:
    saldo = 18 - idade
    print('Se prepare para se alistar daqui {} anos'.format(saldo))
    ano = data + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade > 18 and idade < 30:
    saldo = idade - 18
    print('Deveria ter se alistado a {} anos'.format(saldo))
    ano = data - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade > 30:
    print('Ja deve ter servido ou dispensado')
else:
    print('Aproveita ainda ta longe de se alistar')


# Desafio 040
# Crie um programa que leia duas notas de um aluino e calculesua média, mostrando uma mensagem no final, deacordo com a media atingida:
# - Media abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPEERAÇÃO
# - Média 7.0 ou sueperior: APROVADO
print('==============================================================================')
nota1 = float(input('Digite sua primeria nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print('\33[31mREPROVADO!!!\33[m \nSua media foi {:.1f}'.format(media))
elif media > 5.0 and media < 6.9:
    print('Voce esta em \33[33mRECUPERACAO!!!\33[m \nSua media foi {:.1f}'.format(media))
else:
    print('\33[1;34mAPROVADO PARABENS!!!\33[m \nSua media foi {:.1f}'.format(media))



# Desafio 041
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
print('==============================================================================')
from datetime import date
nascatleta = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
categoria = anoatual - nascatleta
if categoria <= 9:
    print('Voce tem {} anos sua categoria e MIRIM'.format(categoria))
elif categoria <= 14:
    print('Voce tem {} anos sua categoria e INFANTIL'.format(categoria))
elif categoria <= 19:
    print('Voce tem {} anos sua categoria e JUNIOR'.format(categoria))
elif categoria <= 25:
    print('Voce tem {} anos sua categoria e SENIOR'.format(categoria))
else:
    print('Voce tem {} anos sua categoria e a MASTER'.format(categoria))

# Desafio 042
# Refaça o DESAFIO 035 dos triângulos, acrecentando o recurso de mostrar que tipo de triangulo será formado:
# - EQUILÁTERO: todos os lados iguais 
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes
print('==============================================================================')
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Pode formar um triangulo \nTodos os lados sao iguais \nDo tipo \033[1;31mEQUILATERO\033[m')
    elif r1 != r2 !=r3 !=r1:
        print('Pode formar um triangulo \nTodos os lados sao diferentes! \nDo tipo \033[1;34mESCALENO\033[m')
    else:
        print('Pode formar um triangulo \nDois lados sao iguais! \nDo tipo \033[1;35mISOSCELES\033[m')
else:
    print('\033[4;31mNão pode formar um triangulo\033[m')


# Desafio 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso 
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
print('==============================================================================')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
status = peso / (altura * altura)
if status < 18.5:
    print('Voce esta \033[1;36mABAIXO DO PESO!\033[m \nSeu indice de massa corporal e {:.2f}'.format(status))
elif status >= 18.5 and status < 25:            # Poria nao usar o and e usar so um status ex: elif 18.5 <= status < 25
    print('Voce esta no \033[1;32mPESO IDEAL!\033[m \nSeu indice de massa corporal e {:.2f}'.format(status))
elif status >= 25 and status < 30:
    print('Voce esta com \033[1;33mSOBRREPESO!\033[m \nSeu indice de massa corporal e {:.2f}'.format(status))
elif status >= 30 and status < 40:
    print('Voce esta com \033[1;31mOBESIDADE!\033[m \nSeu indice de massa corporal e {:.2f}'.format(status))
else:
    print('Voce esta com \033[1;41;31mOBESIDADE MORBIDA!\033[m\nProcure ajuda urgente! \nSeu indice de massa corporal e {:.2f}'.format(status))

# Desafio 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# - À vista DINHEIRO/CHEQUE: 10% de desconto
# - À vista no CARTÃO: 5% de desconto
# - em até 2x no CARTÃO: preço normal
# - 3x OU MAIS no cartão: 20% de juros
print('==============================================================================')
produto = float(input('Qual o valor do produto? R$'))
opcao = int(input('\nEscolha a opcao de pagamento: \
                \n[1] A vista DINHEIRO/CHEQUE 10% de desconto \
                \n[2] A vista no CARTÃO: 5% de desconto \
                \n[3] Ate 2x no CARTAO preco normal \
                \n[4] 3x ou mais no CARTAO 20% de juros \n'))
if opcao == 1:
    print('O valor do produto com os 10% de desconto sera de R${:.2f} '.format(produto - (produto * 10 / 100)))
elif opcao == 2:
    print('O valor a ser pago com o desconto de 5% sera de R${:.2f}'.format(produto - (produto * 5 / 100)))
elif opcao == 3:
    print('Valor a ser  pago e de R${:.2f}'.format(produto))
else:
    parcela = int(input('Em quantas vezes: '))
    total = produto + (produto * 20 / 100)
    print('Valor  total do produto R${}'.format(total))
    print('O valor a pagar vai ser de {} vezes de R${:.2f}'.format(parcela, total / parcela))


# Desafio 045
# Crie um programa que faça o computador jogar JOKENPÔ com você.
print('==============================================================================')
from random import randint
from time import sleep
print('VAMOS JOGAR!!!')
jogador = int(input('''Escolha a opcao: 
[0] Pedra, 
[1] Papel, 
[2] Tesoura: 
Qual a sua opcao? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
if jogador == 0 and computador == 1:
    print('Voce Perdeu! \nComputador jogou {} \nVoce jogou {}'.format(itens[computador], itens[jogador]))
elif jogador == 1 and  computador == 2:
    print('Voce Perdeu! \nComputador jogou {} \nVoce jogou {}'.format(itens[computador], itens[jogador]))
elif jogador == 2 and computador == 0:
    print('Voce Perdeu! \nComputador jogou {} \nVoce jogou {}'.format(itens[computador], itens[jogador]))
elif jogador == 1 and computador == 0:
    print('Voce Ganhou! \nComputador jogou {} \nVoce jogou {}'.format(itens[computador], itens[jogador]))
elif jogador == 2 and  computador == 1:
    print('Voce Ganhou! \nComputador jogou {} \nVoce jogou {}'.format(itens[computador], itens[jogador]))
elif jogador == 0 and computador == 2:
    print('Voce Ganhou! \nComputador jogou {} \nVoce jogou {}'.format(itens[computador], itens[jogador]))
else:
    print('EMPATE! \nComputador jogou {} \nVoce jogou {}'.format(itens[computador], itens[jogador]))

