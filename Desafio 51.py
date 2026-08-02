# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite primeiro valor: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (10 - 1) * razão
for n in range(primeiro, décimo, razão):
    print(n, end= ' ➡ ')
print('ACABOU!')