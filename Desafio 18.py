#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, cos, sin, tan

g = float(input('Digite um ângulo: '))
r = radians(g)
print(f'O ângulo de {g} tem o SENO de {sin(r):.2f}\nO ângulo de {g} tem o COSSENO de {cos(r):.2f}\nO ângulo de {g} tem a TANGENTE de {tan(r):.2f}')