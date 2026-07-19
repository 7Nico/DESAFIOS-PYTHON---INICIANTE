#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('====== DESAFIO 12 ======')
produto = float(input('Digite o preço do produto: R$'))
desconto = (produto/100)*5
ajuste = produto - desconto
print(f'O produto de R${produto} com um desconto de 5% está custando R${ajuste:.2f}.')