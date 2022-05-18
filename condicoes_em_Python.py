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
