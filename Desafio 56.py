# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

maior = 0
idade_total = 0
count = 0
nome_velho = 'Só há mulheres.'
for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p}° pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {p}° pessoa: '))
    sexo = int(input(f'Qual o sexo da {p}° pessoa? Digite 1 para masculino e 2 para feminino: '))
    if idade < 20 and sexo == 2:
        count += 1
    idade_total += idade
    if idade > maior and sexo == 1:
            maior = idade
            nome_velho = nome
média = idade_total / 4

print(f'A média de idade do grupo é de {média}\nO nome do homem mais velho é: {nome_velho}.\nE a quantidade de mulheres com menos de 20 anos é igual a: {count}. ')