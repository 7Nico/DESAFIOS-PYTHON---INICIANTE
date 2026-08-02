# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
count = 0
for n in range (1, 7):
    n = int(input(f'Digite o {n}º número: '))
    if n % 2 == 0:
        soma += n
        count = count + 1
print(f'A soma entre os {count} valores PARES é igual a {soma}.')
