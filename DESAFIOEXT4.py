# Escreva um programa em Python que calcule e mostre a soma de todos os números ímpares que sejam múltiplos de 5 e que estejam no intervalo de 1 a 300 (inclusive).

soma = 0
count = 0
for n in range(5, 301, 5):
    if n % 2 == 1:
        soma = soma + n
        count = count + 1
print(f'A soma entre os {count} valores solicitados é igual a {soma}.')