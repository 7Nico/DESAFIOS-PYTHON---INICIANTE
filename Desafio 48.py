# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
count = 0
for n in range (3, 501, 3):
    if n % 2 == 1:
        soma = soma + n
        count = count + 1
print(f'A soma entre todos os {count} valores solicitados é igual a {soma}. ')