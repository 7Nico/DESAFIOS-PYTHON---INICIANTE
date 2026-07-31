# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

genero = str(input('Seu gênero é masculino ou feminino?: ')).strip().lower()

if genero == 'feminino' :
    print('Como você é mulher, não precisa se alistar!')

elif genero == 'masculino':
    atual = date.today().year
    ano = int(input('Digite o ano de seu nascimento: '))
    idade = atual - ano
    ano_alistamento = (atual - idade) + 18

    if idade > 18 and genero == 'masculino':
        saldo = idade - 18
        print(f'Como você tem {idade} anos, o seu alistamento foi em {ano_alistamento}. Há {saldo} ano(s) atrás.')
    elif idade < 18 and genero == 'masculino':
        saldo = 18 - idade
        print(f'Como você tem {idade} anos, o seu alistamento será em {ano_alistamento}. faltam {saldo} ano(s).')
    elif idade == 18 and genero == 'masculino':
        print(f'Como você tem {idade} anos, o seu alistamento é esse ano de {ano_alistamento}. Se aliste já!')
