# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-*-' *20 )
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-*-' *20)
n = int(input('Em que número eu pensei? '))
r = randint(0, 5)
print('Processando...')
sleep(2)
if n == r:
    print(f'Boa! Eu pensei no {n}. Acertou miseravi!')
else:
    print(f'Errou! Eu pensei no {r} e não no {n}. Ganhei!! CHUPA TROXA HAHAHA')