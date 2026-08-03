# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
count = 0
tot = 0
for n in range(1, 8):
    ano = int(input(f'Digite o ano em que a {n}º pessoa nasceu: '))
    total = ano_atual - ano
    if total >= 18:
        count += 1
    else:
        tot += 1
print(f'{count} pessoas já atingiram a maioridade e {tot} ainda não atingiram.')