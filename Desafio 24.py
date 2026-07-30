# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite a sua cidade de nascimento: ')).strip()
cidas = cidade[:5].upper() == 'SANTO'
print(f'{cidas}')