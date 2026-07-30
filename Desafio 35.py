# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('='*40)
print('\033[1;30;43mANALISADOR DE TRIÂNGULOS\033[m')
print('='*40)

while True:
    try:
        a = float(input('Primeiro segmento: '))
        b = float (input('Segundo segmento: '))
        c = float (input('Terceiro Segmento: '))

        if a <= 0 or b <= 0 or c <= 0:
            print('Esse valor não é permitido.')
            continue
        break
    except ValueError:
        print('Valor inválido.')
if a + b > c and b + c > a and a + c > b:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
