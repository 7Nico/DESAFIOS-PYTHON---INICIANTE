# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

altura = float(input('Digite a sua altura (Em m): '))
peso = float(input('Digite o seu peso (Em kg): '))
IMC = peso / (altura**2)

print(f'Seu peso é {peso:.1f} kg e sua altura é {altura:.2f} m. Portanto seu IMC será {IMC:.1f}.')
if IMC < 18.25:
    print('Você está ABAIXO DO PESO!')
elif IMC >= 18.25 and IMC < 25:
    print('Você está no PESO IDEAL!')
elif IMC >= 25 and IMC < 30:
    print('Você está em SOBREPESO!')
elif IMC >= 30 and IMC < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')

