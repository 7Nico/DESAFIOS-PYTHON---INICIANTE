#Ex gerado por IA: Um grupo de 5 amigos foi a uma lanchonete e, na hora de pagar a conta, decidiram fazer um sorteio para ver quem vai pagar tudo sozinho.
#O seu desafio:
#Escreva um programa em Python que:
#Leia o nome dos 5 amigos.
#Sorteie aleatoriamente um deles.
#Exiba na tela uma mensagem informando o nome do amigo sorteado para pagar a conta.

from random import choice
a = choice([input('Digite o primeiro amigo: '),
            input('Digite o segundo amigo: '),
            input('Digite o terceiro amigo: '),
            input('Digite o quarto amigo: '),
            input('Digite o quinto amigo: ')])
print(f'O amigo trouxa a ser sorteado é o {a} hahahah se fudeu otário' )