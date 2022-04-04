from random import randint
import os
from time import sleep

# Funções a serem utilizadas

def particao(num):
    z, y, x, w = num // 1 % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10
    N = [w, x, y, z]
    return N

def verificacao(num):
    log1, log2 = True, True
    num = esnumero(num)
    N = particao(num)
    t = 1
    while log1 or log2:
        if t == 2:
            print('\nNo próximo chute errado, será assignado um número aleatório')
            sleep(2)
        elif t == 3:
            x = randint(1,9)
            y = x
            while y == x:
                y = randint(0,9)
            z = y
            while z == x or z == y:
                z = randint(0,9)
            w = z
            while w == z or w == y or w == x:
                w = randint(0,9)
            num = 1000 * x + 100 * y + 10 * z + w
            N = particao(num)
            print('''
Foi assignado o seguinte número de forma aleatória:

{}
'''.format(num))
            sleep(2)
        if num < 1000 or num > 9999:
            num = input('Digite um numero de 4 cifras: ')
            num = esnumero(num)
            N = particao(num)
            t = t + 1
        elif N[0] == N[1] or N[0] == N[2] or N[0] == N[3] or N[1] == N[2] or N[1] == N[3] or N[2] == N[3]:
            num = input('Digite sem repetir os dígitos: ')
            num = esnumero(num)
            N = particao(num)
            t = t + 1
        log1 = num < 1000 or num > 9999
        log2 = N[0] == N[1] or N[0] == N[2] or N[0] == N[3] or N[1] == N[2] or N[1] == N[3] or N[2] == N[3]
    return num

def esnumero(variavel) :
    vf = variavel.isdigit()
    while vf == False :
        variavel = input('Digite um número: ')
        vf = variavel.isdigit()
    variavel = int(variavel)
    return variavel

def numcerto(n, min: int, max: int) :
    n = esnumero(n)
    while (n in range(min,max+1)) == False:
        n = input('Opção inválida, digite um número entre {} e {}: '.format(min, max))
        n = esnumero(n)
    return n

jogarnovamente = True
while jogarnovamente:
    os.system('clear')
    n = input('''Opções para jogar

    1. Deseja adivinhar um número aleatório gerado pela máquina?
    2. Deseja digitar um número para outra pessoa adivinhar

Digite sua opção: ''')

    n = numcerto(n, 1, 2)

    chutesmaximos = input('\nDigite a quantidade máxima de chutes: ')
    chutesmaximos = esnumero(chutesmaximos)
    while chutesmaximos < 1 :
        chutesmaximos = input('Digite um número possitivo: ')
        chutesmaximos = esnumero(chutesmaximos)

    if n == 1 :
        a = randint(1,9)
        b = a
        while b == a:
            b = randint(0,9)
        c = b
        while c == a or c == b:
            c = randint(0,9)
        d = c
        while d == c or d == b or d == a:
            d = randint(0,9)
        ran = [a, b, c, d]
        print('Um número aleatório foi gerado.')
        sleep(2)
    else :
        ran = input('\nDigite um número para outra pessoa adivinhar: ')
        ran = verificacao(ran)
        ran = particao(ran)
    os.system('clear')
    cont = 0
    while cont in range(0, chutesmaximos):
        if cont + 1 < chutesmaximos:
            chute = input('Digite o {}o chute: '.format(cont + 1))
        else:
            chute = input('Digite o último chute: ')
        chute = verificacao(chute)
        cont = cont + 1
        N = particao(chute)
        diana = 0
        toque = 0
        for i in range(4):
            if ran[i] == N[i]:
                diana = diana + 1
            for j in range(4):
                if ran[i] == N[j]:
                    toque = toque + 1
        toque = toque - diana
        if ran == N:
            print('\nParabéns, você acertou o número.')
            cont = chutesmaximos + 1
        elif toque == 1 and diana == 1:
            print('\n{} toque; e\n{} diana\n'.format(toque,diana))
        elif toque == 1:
            print('\n{} toque; e\n{} dianas\n'.format(toque,diana))
        elif diana == 1:
            print('\n{} toques; e\n{} diana\n'.format(toque,diana))
        else:
            print('\n{} toques; e\n{} dianas\n'.format(toque,diana))
    simnao = input('''O número era {}

Deseja jogar novamente? [s/n]'''.format(1000 * ran[0] + 100 * ran[1] + 10 * ran[2] + ran[3]))
    simnao = simnao.upper()
    while (simnao in ['S', 'N', 'SIM', 'NAO', 'NÃO']) == False :
        simnao = input('Opção inválida. Tente novamente: [s/n] ')
        simnao = simnao.upper()
    if simnao in ['N', 'NAO', 'NÃO']:
        jogarnovamente = False
