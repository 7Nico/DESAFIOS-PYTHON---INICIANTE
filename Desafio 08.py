#Escreva um programa que leia um valor em metros e o exiba convertido em várias unidades de medida de distância.

print('====== DESAFIO 08 ======')
n = float(input('Uma distância em metros:'))
print(f'A medida de {n} corresponde a: \n{n/1000}km \n{n/100}hm \n{n/10}dam')
print(f'{n}m \n{n*10:.0f}dm \n{n*100:.0f}cm \n{n*1000:.0f}mm')
