# Desafio 057
# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça  a digitação novamente até ter um valor correto.
print('==============================================================================')
sexo = str(input('Informe seu sexo [M/F]: '))
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Registrado com sucesso!')

# Desafio 058
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
print('==============================================================================')
from random import randint
computador = randint(0, 10)
print('----- Vamos brincar de adivinha! -----')
acerto = False
tentativas = 0
while not acerto:
    jogador = int(input('Digite um numero de 0 a 10: '))
    tentativas += 1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
print('ACERTOU!!! \n{} Tentativas. Parabens!'.format(tentativas))
