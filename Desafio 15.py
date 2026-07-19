#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

print('====== DESAFIO 15 ======')
d = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km ele percorreu?'))
dpreço = d*60
kmpreço = km*0.15
print(f'O valor total a se pagar pelo carro alugado é de R${dpreço + kmpreço:.2f}!')