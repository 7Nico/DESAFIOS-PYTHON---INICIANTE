# Faça um programa que leia a nota de 8 alunos (notas de 0 a 10, podem ter casas decimais) e, no final, mostre:
# A menor nota da turma;
# Quantos alunos tiraram essa menor nota;
# A posição (número do aluno) da primeira vez que essa menor nota apareceu (ex: se foi o 3º aluno digitado, deve mostrar "3").

menor = 0
count = 0
posição = 0
for n in range(1, 9):
    nota = float(input(f'Digite a nota do {n}° aluno: '))
    if n == 1:
        menor = nota
        count += 1
        posição = 1
    else:
        if nota < menor:
            posição = 0
            count = 0
            menor = nota
            count += 1
            posição = n
        elif nota == menor:
            count += 1
print(f'A menor nota da turma foi {menor}, exatamente {count} aluno(s) tirou essa nota \nA posição exata que essa nota apareceu foi na {posição}° posição')
