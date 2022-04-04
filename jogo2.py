from operator import truediv
from random import randint
import os
from signal import pause
from time import sleep

# Funções a serem utilizadas

def particao(num):
    comp = len(str(num))
    N = ['']*comp
    for i in range(comp):
        N[i] = (num // 10**(comp - 1 - i)) % 10
    return N

def simnao(sn):
    sn = sn.upper()
    while (sn in ['S', 'N', 'SIM', 'NAO', 'NÃO']) == False :
        sn = input('Opção inválida. Tente novamente: [s/n] ')
        sn = sn.upper()
    return sn

def GerarNumRand(compri):
    N = ['']*compri
    N[0] = randint(1, 9)
    num = N[0] * 10**(compri - 1)
    i = 1
    while i < compri :
        N[i] = N[0]
        log = True
        while log:
            log = False
            for j in range(i):
                log = log or (N[j] == N[i])
            if log :
                N[i] = randint(0,9)
        num = num + N[i]*10**(compri - 1 - i)
        i = i + 1
    print('\033[01;31m{}\033[m'.format(num))
    return N

def verificacao(num, compri):
    log1, log2 = True, True
    num = esnumero(num)
    N = particao(num)
    t = 1
    while log1 or log2:
        if t == 2:
            print('\nNo próximo chute errado, será assignado um número aleatório')
            sleep(2)
        elif t == 3:
            N = GerarNumRand(compri)
            num = 0
            for i in range(len(N)):
                num = num + N[i] * 10**(len(N) - i - 1)
            sleep(2)
        
        if (len(N) == compri) == False:
            num = input('Digite um numero de {} cifras: '.format(compri))
            num = esnumero(num)
            N = particao(num)
            t = t + 1
        else :
            log2 = False
            for i in range(len(N)):
                for j in range(i) :
                    log2 = log2 or N[i] == N[j]
            if log2:
                num = input('Digite sem repetir os dígitos: ')
                num = esnumero(num)
                N = particao(num)
                t = t + 1
        log1 = (len(N) == compri) == False
        log2 = False
        for i in range(len(N)):
            for j in range(i):
                log2 = log2 or N[i] == N[j]
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

def comparar(Num1,Num2):
    comp = len(Num1)
    diana = 0
    toque = 0
    for i in range(comp):
        if Num1[i] == Num2[i]:
            diana = diana + 1
        for j in range(comp):
            if Num1[i] == Num2[j]:
                toque = toque + 1
    return [toque - diana, diana]


jogarnovamente = True
while jogarnovamente:
    os.system('clear')

    numjogadores = input('Quantas pessoas vão jogar: ')
    numjogadores = esnumero(numjogadores)
    while numjogadores < 1 :
        numjogadores = input('Digite um número maior que 0: ')
        numjogadores = esnumero(numjogadores)
    print('')
    for i in range(numjogadores): 
        jogadori = input('Digite o nome do {}o jogador: '.format(i + 1))
        if i == 0 :
            Jogador = [jogadori]
        else :
            Jogador = Jogador + [jogadori]
    print('')

    comprimNum = input('Digite a quantidade de dígitos que deve(m) ter o(s) número(s): ')
    comprimNum = numcerto(comprimNum, 1, 10)

    for i in range(numjogadores) :
        os.system('clear')
        numi = input('Digite o número de {}: '.format(Jogador[i]))
        numi = verificacao(numi, comprimNum)
        Numi = particao(numi)
        if i == 0 :
            Num = [Numi]
        else :
            Num = Num + [Numi]

    log = False
    ToquDian = ['']*numjogadores   
    while log == False:
        os.system('clear')
        rand = GerarNumRand(comprimNum)
        sleep(2)
        for i in range(numjogadores):
            ToquDian[i] = comparar(rand, Num[i])
        for i in range(numjogadores):
            print('\n{:10} {}T {}D'.format(Jogador[i], ToquDian[i][0], ToquDian[i][1]))
        sn = input('\nTentar adivinhar? [s/n]')
        sn = simnao(sn)
        if sn in ['S', 'SIM']:
            chute = input('Digite a tentativa: ')
            chute = verificacao(chute,comprimNum)
            Chute = particao(chute)
            adivinhados = 0
            for i in range(numjogadores):
                if Chute == Num[i]:
                    adivinhados = adivinhados + 1
                    print('\nO número de {} foi adivinhado'.format(Jogador[i]))
                    ContiTent = input('Continuar outro número? [s/n]')
                    ContiTent = simnao(ContiTent)
                    log = ContiTent in ['N', 'NAO', 'NÃO']
            if adivinhados == 0:
                input('Nenhum número acertado. Enter para o próximo número.')

    sn = input('Deseja jogar novamente? [s/n]')
    sn = simnao(sn)
    if sn in ['N', 'NAO', 'NÃO']:
        jogarnovamente = False
