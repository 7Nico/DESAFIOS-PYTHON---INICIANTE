#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('====== DESAFIO 13 ======')
salário = float(input('Digite seu salário atual: R$'))
aumento = salário + (salário*15/100)
print(f'O seu salário antigo era de R${salário:.2f}, com o aumento ele passa a ser R${aumento:.2f}.')