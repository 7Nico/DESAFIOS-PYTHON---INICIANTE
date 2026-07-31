# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print('=*'*20)
print('PEDRA PAPEL E TESOURA GAME')
print('=*'*20)

print('[1] PEDRA \n[2] PAPEL\n[3] TESOURA')
jogador = int(input('Escolha uma opção: '))
print('JO')
sleep(0.5)
print('  KEN')
sleep(0.5)
print('   PO!!')
sleep(0.5)
pc = choice([1, 2, 3])
if jogador == 1 and pc == 2:
    print('AHA! GANHEI! Eu escolhi PAPEL e você escolheu PEDRA!')
elif jogador == 2 and pc == 3:
    print('AHA! GANHEI! Eu escolhi TESOURA e você escolheu PAPEL!')
elif jogador == 3 and pc == 1:
    print('AHA! GANHEI! Eu escolhi PEDRA e você escolheu TESOURA! ')
elif jogador == 1 and pc == 3:
    print('DROGA! VOCÊ GANHOU! Eu escolhi TESOURA e você PEDRA!')
elif jogador == 2 and pc == 1:
    print('DROGA! VOCÊ GANHOU! Eu escolhi PEDRA e você PAPEL!')
elif jogador == 3 and pc == 2:
    print('DROGA! VOCê GANHOU! Eu escolhi PAPEL e você TESOURA!')
else:
    print('EMPATE!!')