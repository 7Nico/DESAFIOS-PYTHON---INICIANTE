# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
idade = ano - ano_nascimento

if idade < 9:
    categoria = 'MIRIM'
elif 14 > idade > 9:
    categoria = 'INFANTIL'
elif 19 > idade > 14:
    categoria = 'JÚNIOR'
elif 25 > idade > 19:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER'
print(f'O atleta nasceu no ano de {ano_nascimento}.')
print(f'Portanto, como ele tem {idade} anos, sua categoria é: {categoria}.')
