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
print('==============================================================================')
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


# Desafio 061
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando  os 10 PRIMEIROS TERMOS  da progressão usando a estrutura WHILE.
print('==============================================================================')
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = ptermo
contador = 1
while contador <= 10:
    print('{}'.format(termo), end=' → ')
    termo += razao
    contador += 1
print('Fim!')


# Desafio 062
# Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar O termos.
print('==============================================================================')
print('=-=-=- GERADOR DE PA -=-=-=')
primeiro = int(input('Primerio termo: '))
razao = int(input('Razao: '))
ter = primeiro
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print('{} → '.format(ter), end='')
        ter += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quer ver mais quantas razoes?  '))
print('Progressao com {} termos mostrados.'.format(tot))


# Desafio 063
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma SEQUENCIA DE FIBONACCI.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
print('==============================================================================')
print('----- SEQUENCIA DE FIBINACCI -----')
fibo = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
contador = 0
if fibo <= 0:
    print('Por favor digite um numero impar!')
elif fibo == 1:
    print('Elemento fibonacci ,{}:'.format(fibo),end='')
    print(t1)
else:
    print('Sequencia fibonacci!')
    while contador < fibo:
        print(t1, end=' → ')
        total = t1 + t2
        t1 = t2
        t2 = total
        contador +=1
    print('Fim!')


# Desafio 064
# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados  e qual foi a soma entre eles (desconsiderando o flag).
print('==============================================================================')
tot = contador = digitados = 0
while contador != 999:
    numero = int(input('Digite um numero inteiro [se quiser parar digite 999]: '))
    contador = numero
    if contador != 999:
        tot += contador
        digitados += 1
print('Total de numero digitados {}, a soma entre os numeros digitados e {}'.format(digitados, tot))


# Desafio 065
# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução , mostre a média entre todos os valores e qual foi o maiore o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
print('==============================================================================')
soma = total = media = menor = maior = 0
resposta = str('S')
while resposta in 'Ss':
    n1 = int(input('Digite um numero: '))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    resposta = cont
    soma += n1
    total += 1
    if total == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma / total
print('Voce digitou {} numeros e a media foi {}'.format(total, media))
print('O menor valor digitado foi {} e o maior valor {}'.format(menor, maior))


# Desafio 066
# Crie um programa que leia varios numeros inteiros pelo teclado. o programa so vai parar quando o usuario digitar o valor 999, que e a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('==============================================================================')
print('='*20)
print(' DIGITANDO NUMEROS')
print('='*20)
quantidade = soma = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    quantidade += 1
    soma += n
print(f'Foram digitados {quantidade} numeros e a soma de todos foi {soma}.')


# Desafio 067
# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo.
print('==============================================================================')
from time import sleep
print('-----TABUADA-----')
while True:
    tabuada = int(input('Quer ver a tabuada de qual numero: '))
    if tabuada < 0:
        break
    print('~'*40)
    for c in range(0, 11):
        sleep(0.2)
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('~'*40)
print('Finalizando tabuada!')
sleep(1)
print('Fim')


# Desafio 068
# Faça um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
print('==============================================================================')
from random import randint
print('----- VAMOS JOGAR PAR OU IMPAR -----')
par = 'P'
impar = 'I'
contador = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0,10)
    resultado = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par [P] ou Impar [I]: ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {computador + jogador} ', end='' )
    print('deu PAR' if resultado % 2 == 0 else 'deu IMPAR')
    if resultado % 2 == 0:
        if escolha == par:
            contador += 1
            print('Voce ganhou!!!')
        else:
            print('Voce perdeu!!!')
            break
    if resultado % 2 == 1:
        if escolha == impar:
            contador += 1
            print('Voce ganhou!!!')
        else:
            print('Voce perdeu!!!')
            break
print(f'GAMER OVER! Voce venceu {contador} vezes.')


# Desafio 069
# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre:
# A) Quantos pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantos mulheres tem menos de 20 anos.
print('==============================================================================')
print('----- CADASTRO DE PESSOAS -----')
cont = masculino = feminino = 0
while True:
    idade = int(input('Idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F] ')).upper().strip()[0]
    continuar = ' '
    while continuar not in 'SN':
        print('~'*40)
        continuar = str(input('Quer continuar? [Sim / Nao] ')).upper().strip()[0]
    print('~'*40)
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        if idade < 20:
            feminino += 1
    if continuar not in 'S':
        break
print(f'Tem {cont} pessoas maiores de 18 anos.')
print(f'Foram cadastrado {masculino} homens.')
print(f'Tem {feminino} mulheres menor de 20 anos.')
print('~'*40)


# Desafio 070
# Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre:
# A) Qual e o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual e o nome do produto mais barato.
print('==============================================================================')
print('----- LOJA PONTO DC -----')
total = caro = barato = repeticao = 0
probarato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preco: R$'))
    print('='*50)
    total += valor
    repeticao += 1
    if valor >= 1000:
        caro += 1
    if repeticao == 1 or valor < barato:
        barato = valor 
        probarato = produto
    r = ' '    
    while r not in 'SN':
        r = str(input('Quer continuar a compra? [S/N]')).strip().upper()[0]
        print('='*50)
    if r == 'N':
        break
print('='*50)
print(f'Valor total da compra R${total:.2f}')
print(f'Tem {caro} produtos mais de R$1000') 
print(f'O produto mais barato e o {probarato} que custa R${barato:.2f}')
print('='*50) 


# Desafio 071
# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# OBS: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.
print('==============================================================================')
print('-'*40)
print('{:^40}'.format('BANCO DSC'))
print('-'*40)
print('Cedulas disponiveis! \nR$1, R$10, R$20, R$50')
valor = int(input('Qual o valor para saque? R$'))
total = valor
nota = 50
contnota = 0
while True:
    if total >= nota:
        total -= nota
        contnota += 1
    else:
        if contnota > 0:
            print(f'Total de {contnota} cedulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        contnota = 0
        if total == 0:
            break
print('-'*40)
print('Saque finalizado, Volte sempre!')
