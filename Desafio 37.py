# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

while True:
    try:
        numero = int(input('Digite um núemero inteiro: '))
        print('Digite 1 para binário, 2 para octal e 3 para hexadecimal')
        base = int(input('Qual será a base de conversão? '))
        if base > 3 or base < 1:
                print('Valor inválido. Digite novamente.')
                continue
        break
    except ValueError:
            print('Valor inválido. Digite novamente.')
if base == 1:
    binario = bin(numero) [2:]
    print(f'O número {numero} na base binária é igual a: {binario}')
elif base == 2:
    octa = oct(numero) [2:]
    print(f'O número {numero} na base octal é igual a: {octa}')
else:
    hexa = hex(numero) [2:]
    print(f'O número {numero} na base hexadecimal é igual a: {hexa}')





