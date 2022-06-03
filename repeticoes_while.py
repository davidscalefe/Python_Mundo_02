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

# Desafio 059
# Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# seu programa deverá realizar a operação solicitada em cada caso.
print('==============================================================================')
from time import sleep
v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
r = 0
while r != 5:
    r = int(input('''Digite uma opcao:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair
    '''))
    if r == 1:
        s =  v1 + v2
        print('A soma entre {} e {} e igual a {}'.format(v1, v2, s)) 
    elif r == 2:
        s = v1 * v2
        print('A multiplicacao de {} com {} resulta em {}'.format(v1, v2, s))
    elif r == 3:
        if v1 > v2:
            print('O maior valor e {}'.format(v1)) 
        else:
            print('O maior valor e {}'.format(v2))
            print('='*25)  
    elif r == 4:
        
        v1 = int(input('Digite o 1° valor: '))
        v2 = int(input('Digite o 2° valor: '))
    elif r > 5:
        print('Valor invalido!')
    sleep(1)
    print('='*25) 
print('Finalizando...')
sleep(1) 
print('Fim')


# Desafio 060
# Faça um programa que leia um número qualquer e mostre o seu FATORIAL.
# Ex: 5! = 5x4x3x2x1 = 120
print('-=-=-= VAMOS QUALCULAR O FATORIAL -=-=-=')
numero = int(input('Digite um numero: '))
contador = numero
total = 1
print('calculando {}! ='.format(numero), end=' ')
while contador > 0:
    print(contador, end=' ')
    print('x' if contador > 1 else '=', end=' ')
    total *= contador
    contador -= 1
print(total)
