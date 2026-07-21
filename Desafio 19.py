# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

al = choice([input('Digite o nome do primeiro aluno: '),
             input('Digite o nome do segundo aluno: '),
             input('Digite o o nome do tereceiro aluno: '),
             input('Digite o nome do quarto aluno: ')])
print(F'O aluno sorteado foi o {al}')