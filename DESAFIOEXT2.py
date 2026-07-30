# "Calculadora de Tinta e Hipotenusa"Uma empresa de pintura precisa de um programa para calcular custos em obras.
# Faça um programa que leia a largura e a altura de uma parede retangular (em metros) e faça o seguinte:
# Calcule e mostre a área da parede e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
# Suponha que essa parede seja cortada na diagonal para um design especial.
# Calcule o comprimento da diagonal (hipotenusa) dessa parede a partir da largura e altura informadas, utilizando a função apropriada do módulo math. Mostre o resultado com 2 casas decimais.

from math import hypot

largura = float(input('Digite a largura da parede (em m): '))
altura = float (input('Digite a altura da parede (em m): '))
area = largura * altura
tinta = area / 2
print(f'Sabendo que a área da parede é de {area:.2f} metros quadrados, o total de tinta necessário para pintá-la será de {tinta:.0f}L.')

hipot = hypot(largura, altura)
print(f'A diagonal dessa parede (hipotenusa) será igual a {hipot:.2f}')