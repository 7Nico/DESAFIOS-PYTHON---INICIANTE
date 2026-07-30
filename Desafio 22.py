# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome apenas com letras maiúsculas: {nome.upper()} \nSeu nome apenas com letras minúsculas: {nome.lower()}')
print(f'Seu nome tem ao todo: {len(nome) - nome.count(' ')} letras')
separa = nome.split()
sc = separa[0]
print(f'Seu primeiro nome é {sc} e tem ao todo: {len(sc)} letras')