#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample
aluno = sample([input('Digite o nome do primeiro aluno: '),
                input('Digite o nome do segundo aluno: '),
                input('Digite o nome do terceiro aluno: '),
                input('Digite nome do quarto aluno: ')], k=4)
print(f'A ordem de apresentação será:\n{aluno}')
