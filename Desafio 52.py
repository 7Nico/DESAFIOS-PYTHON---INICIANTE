#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print(f'\033[32m{n}', end= ' ')
        tot += 1
    else:
        print(f'\33[31m{n}', end=' ')
print(f'\nO número {num} foi divisível {tot} vezes! ')
if tot == 2:
    print('ELE É PRIMO!')
else:
    print('ELE NÃO É PRIMO!')
