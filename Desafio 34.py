#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: '))
if salario <= 1250:
    s1 = ((salario/100) * 15) + salario
    print(f'O seu novo salário será de: R${s1:.2f}')
else:
    s2 = ((salario/100) * 10) + salario
    print(f'O seu novo salário será de: R${s2:.2f}')

