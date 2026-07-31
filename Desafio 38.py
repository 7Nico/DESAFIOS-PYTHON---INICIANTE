# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))

if primeiro > segundo:
    print(f'O PRIMEIRO valor é maior.')
elif segundo > primeiro:
    print(f'O SEGUNDO valor é maior.')
else:
    print(f'Não existe valor maior, os dois valores são IGUAIS.')