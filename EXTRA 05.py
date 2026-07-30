# Escreva um programa que pergunte a distância de uma entrega em quilômetros (km) e calcule o preço da passagem/frete:
# Para viagens de até 200 km, cobre R$ 0,50 por km.
# Para viagens acima de 200 km, cobre R$ 0,45 por km.

while True:
    try:
        distancia = float(input('Digite a distância da sua viagem (em km): '))

        if distancia < 0:
            print ('A distância não pode ser negativa!')
            continue
        break
    except ValueError:
        print('O valor digitado não é válido, por favor digite novamente: ')

if distancia <= 200:
    valor = 0.50
else:
    valor = 0.45

distancia_total = distancia * valor

print(f'O valor a ser pago em sua viagem será de R${distancia_total:.2f} ')

