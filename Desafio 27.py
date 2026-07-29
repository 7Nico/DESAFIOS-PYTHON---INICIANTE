# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: '))
ns = nome.split()
print(f'Seu primeiro nome é {ns[0]}.')
print(f'Seu último nome é {ns[-1]}.')