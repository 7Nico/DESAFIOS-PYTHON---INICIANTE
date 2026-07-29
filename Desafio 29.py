# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

vel = int(input('Qual é a velocidade atual do seu carro (em km/h)? '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Tudo certo Senhor! Está abaixo do limite!')
    print('Tenha um excelente dia!! :)')
else:
    print(f'VAGABUNDO!!! VAI TOMAR MULTA!! MULTINHA DE R${multa:.2f}!!')
    sleep(2)
    print('Tenha um excelente dia meu amigo! :))')