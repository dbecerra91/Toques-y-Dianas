from random import randint
import os
from time import sleep
l, tit = '-'*20, 'Regras do jogo'
# Número random para ser adivinhado

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

# Funções a serem utilizadas

def particao(num):
    z, y, x, w = num // 1 % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10
    N = [w, x, y, z]
    return N

def verificacao(num):
    log1, log2 = True, True
    N = particao(num)
    t = 1
    while log1 or log2:
        if t == 3:
            print('\nVocê está de sacanagem comigo, né?')
            sleep(1)
        elif t == 4:
            print('\nMais um chute errado e acaba o jogo!')
            sleep(1)
        elif t == 5:
            print('\nQue pena, o número era {}'.format(1000 * a + 100 * b + 10 * c + d))
            exit()
        if num < 1000 or num > 9999:
            num = int(input('Digite um numero de 4 cifras: '))
            N = particao(num)
            t = t + 1
        elif N[0] == N[1] or N[0] == N[2] or N[0] == N[3] or N[1] == N[2] or N[1] == N[3] or N[2] == N[3]:
            num = int(input('Digite sem repetir os dígitos: '))
            N = particao(num)
            t = t + 1
        log1 = num < 1000 or num > 9999
        log2 = N[0] == N[1] or N[0] == N[2] or N[0] == N[3] or N[1] == N[2] or N[1] == N[3] or N[2] == N[3]
    return num

os.system('clear')
# Regras do jogo
print(l,'\n',tit)
print(l,'\n')
print('A ideia do jogo é adivinhar um número que é gerado pelo sistema de')
print('forma aleatória, esse número é de 4 digitos e elas não se repetem.')
print('Para adivinhar o número você deve utilizar um máximo de 7 chutes')
print('certos, isto é, cada chute deve ser um número de 4 digitos distintas,')
print('em cada chute você terá informação em forma de toques e dianas, que')
print('vai ajudar você a adivinhar o número.\n')
print('Cada toque indica que no seu chute tem um dígito certo na posição')
print('errada.\n')
print('Cada diana indica que no seu chute tem um dígito certo na posição')
print('certa.\n')
input('Enter para continuar... ')
os.system('clear')
for cont in range(1, 8):
    if cont < 7:
        chute = int(input('Digite o {}o chute: '.format(cont)))
    else:
        chute = int(input('Digite o último chute: '))
    chute = verificacao(chute)
    N = particao(chute)
    diana = 0
    toque = 0
    for i in range(4):
        if ran[i] == N[i]:
            diana = diana + 1
        for j in range(4):
            if ran[i] == N[j]:
                toque = toque +1
    toque = toque - diana
    if ran == N:
        print('\nParabéns, você acertou o número.')
        exit()
    elif toque == 1 and diana == 1:
        print('\n{} toque; e\n{} diana\n'.format(toque,diana))
    elif toque == 1:
        print('\n{} toque; e\n{} dianas\n'.format(toque,diana))
    elif diana == 1:
        print('\n{} toques; e\n{} diana\n'.format(toque,diana))
    else:
        print('\n{} toques; e\n{} dianas\n'.format(toque,diana))
print('O número era {}'.format(1000 * a + 100 * b + 10 * c + d))
