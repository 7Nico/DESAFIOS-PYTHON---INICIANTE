# Escreva um programa em Python que:
# Leia uma frase qualquer digitada pelo usuário.
# Monte uma nova string contendo apenas as vogais da frase original, mas na ordem inversa (da última letra para a primeira).
# Ignore espaços, acentos e diferenças entre maiúsculas e minúsculas (pode converter tudo para maiúsculas, por exemplo).
# No final, exiba a frase original sem espaços e a nova frase com as vogais invertidas.

frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
vogais = 'AEIOU
print(separado)