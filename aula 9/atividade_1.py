# Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
n= 0
while n <=1000:
    print(n)
    n = n +1

# Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

pessoas = []

perguntas = 10
while perguntas > 0:
    perg = input('Digite um nome: ')  # Repete a pergunta
    pessoas.append(perg)  #Coloca a resposta do input na lista 'pessoas'
    perguntas = perguntas - 1 # Faz a contagem decrescente das perguntas
print(pessoas)  # Printa toda lista a cada looping