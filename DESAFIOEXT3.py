# Crie um programa que peça ao usuário para digitar uma frase qualquer e um ano (ex: 2024).
# Mostre a frase toda em minúsculas, quantas vezes a letra "a" aparece nela e em qual posição ela aparece pela primeira vez (dica: ignore espaços nas pontas antes da análise).
# Analise o ano digitado usando condicionais (if/else) e informe se ele é um Ano Bissexto ou Não Bissexto.
# (Regra do ano bissexto: Um ano é bissexto se for divisível por 4 AND [não divisível por 100 OR divisível por 400]).

frase = str(input('Digite uma frase qualquer: ')).strip()
frase_min = frase.lower()
print(f'Sua frase em letras minúsculas: {frase_min}')

frase_a = frase_min.count('a')
print(f'A letra a aparece {frase_a} vezes na frase.')
ache_a = frase_min.find('a')
print(f'A letra a aparece pela primeira vez na posição: {(ache_a) + 1}')

ano = int(input('Digite um ano aleatório: '))
if ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')
