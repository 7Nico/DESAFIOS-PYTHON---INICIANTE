#Radar Eletrônico e Analisador de Nome
#Escreva um programa que leia o nome completo de um condutor e a velocidade registrada do seu carro (em km/h).
#O programa deve exibir o primeiro nome do condutor em letras maiúsculas.
#A velocidade máxima permitida na via é de 80 km/h.
#Se o motorista ultrapassar 80 km/h, exiba uma mensagem avisando que ele foi multado e mostre o valor da multa. A multa custa R$ 7,00 por cada km acima do limite.
#Se o motorista estiver dentro do limite, exiba uma mensagem de "Boa viagem!".

nome = str(input('Olá Condutor! Por gentileza, digite o seu nome: ')).upper()
nome_s = nome.split()
primeiro_n = nome_s[0]
print(f'Olá {primeiro_n}!')

velocidade = float(input('Digite a sua velocidade máxima registrada (em km/h): '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Atenção {primeiro_n}! Você foi multado em R${multa}')
else:
    print('Boa Viagem!')