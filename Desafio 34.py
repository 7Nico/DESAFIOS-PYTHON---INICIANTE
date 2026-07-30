#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

while True:
    try:
        salario = float(input('Digite o seu salário: R$'))

        if salario <0:
            print('Digite novamente! O salário não pode ser negativo!!')
            continue
        break
    except ValueError:
        print('Valor inválido! Digite apenas números!')
if salario <= 1250:
    s1 = ((salario/100) * 15) + salario
    print(f'O seu novo salário será de: R${s1:.2f}')
if salario > 1250:
    s2 = ((salario/100) * 10) + salario
    print(f'O seu novo salário será de: R${s2:.2f}')

