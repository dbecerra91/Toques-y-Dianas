from random import randint
import os
from time import sleep
l, tit = '-'*20, 'Regras do jogo'

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
print('''A ideia do jogo é adivinhar um número que é gerado pelo sistema
de forma aleatória, esse número é de 4 digitos e elas não se repetem.
Para adivinhar o número você deve utilizar um máximo de 7 chutes
certos, isto é, cada chute deve ser um número de 4 digitos distintas,
em cada chute você terá informação em forma de toques e dianas, que
vai ajudar você a adivinhar o número.\n
Cada toque indica que no seu chute tem um dígito certo na posição
errada.\n
Cada diana indica que no seu chute tem um dígito certo na posição
certa.\n''')
input('Enter para continuar... ')
os.system('clear')

n = int(input('''Opções para jogar

1. Deseja adivinhar um número aleatório gerado pela máquina?
2. Deseja digitar um numero para outra pessoa adivinhar

Digite sua opção: '''))
while (n in [1, 2]) == False :
    if n < 1 or n > 2 :
        n = int(input('Digite um número entre 1 e 2: '))

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
    os.system('clear')
else :
    ran = int(input('Digite um número para outra pessoa adivinhar: '))
    ran = verificacao(ran)
    ran = particao(ran)
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
