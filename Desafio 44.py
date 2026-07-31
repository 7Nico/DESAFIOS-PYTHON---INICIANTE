# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('='*44)
print('LOJAS OLIVEIRAS DAS FARIAS')
print('='*44)

produto = float(input('Digite o valor do produto: R$'))
print('1 - À vista no dinheiro ou pix (10% de desconto) 3 - Em até 2x no cartão \n2 - À vista no cartão (5% de desconto) 4 - 3x ou mais no cartão (20% de juros) ')
pagamento = int(input('Digite a opção para pagamento: '))

if pagamento == 4:
    parcelas = int(input('Quantas parcelas serão? '))
    valor4 = produto + (produto * 20 / 100)
    valor_total = valor4 / parcelas
    print(f'O produto fica no valor de {parcelas}x de R${valor_total:.2f} com juros')
elif pagamento == 1:
    valor = produto - (produto * 10 / 100)
    print(f'O produto fica no valor de R${valor:.2f}')
elif pagamento == 2:
    valor =  produto - (produto * 5 / 100)
    print(f'O produto fica no valor de R${valor:.2f}')
elif pagamento == 3:
    valor3 = (produto / 2)
    print(f'O produto fica no valor de 2x de R${valor3:.2f} sem juros.')
    print(f'O produto fica no valor de R${valor:.2f}')
else:
    print('Valor inválido.')