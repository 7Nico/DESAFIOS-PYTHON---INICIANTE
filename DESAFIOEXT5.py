# Faça um programa que leia a idade de 6 pessoas e, no final, mostre:
# A maior idade e quantas pessoas têm essa idade;

maior = 0
count = 0
for i in range(1, 7):
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    if i == 1:
        maior = idade
        count += 1
    else:
        if idade > maior:
            count = 0
            maior = idade
            count += 1
        elif idade == maior:
            count += 1
print(f'A maior idade é {maior} e {count} pessoa(s) tem essa idade.')