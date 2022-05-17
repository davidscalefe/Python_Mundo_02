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