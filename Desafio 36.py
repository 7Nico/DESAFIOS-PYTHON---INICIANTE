# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$'))
salario = float (input('Digite o seu salário: R$'))
ano = int (input('Digite em quantos anos você irá pagar: '))

meses = ano * 12
casa_meses = casa/meses
salario_porc = (salario/100 * 30)

print(f'Para pagar uma casa de R${casa:.2f} em {ano} anos a prestação será de R${casa_meses:.2f} ')
if salario_porc >= casa_meses:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')

