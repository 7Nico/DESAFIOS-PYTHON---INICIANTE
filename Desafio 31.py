# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

from time import sleep
viagem = int(input('Diga a distância da sua viagem (em Km): '))
print (f'Vocês está prestes a iniciar uma viagem de {viagem}km!')
sleep(1)
if viagem <= 200:
    print(f'Sua viagem custou: R${viagem*0.50:.2f}')
else:
    print(f'Sua viagem custou: R${viagem*0.45:.2f}')