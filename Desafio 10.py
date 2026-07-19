#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#Considere: U$1.00 = R$5.11

print('====== DESAFIO 10 ======')
din = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = din/5.11
print(f'Com R${din:.2f} você pode comprar U${dol:.2f}.')

