#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('====== DESAFIO 04 ======')
a = input ('Digite algo')
print('É um número?', a.isnumeric())
print('Só tem espaço?', a.isspace())
print('Só tem letra maiúscula?',a.isupper())
print('Só tem letra minúscula?', a.islower())
print('É uma(s) letra(s)?', a.isalpha())
print('Está capitalizado? Com letras maiúsculas e minúsculas', a.istitle())