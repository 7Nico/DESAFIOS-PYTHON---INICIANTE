#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('====== DESAFIO 11 ======')
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l*a
tinta = area/2
print(f'Sua parede tem uma dimensão de {l}x{a}, sua área total é de {area}.\nPara pinta-la é nescessário {tinta:.0f}L de tinta.')