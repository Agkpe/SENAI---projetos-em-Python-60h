import os
os.system('cls')



# # Exercício 1:
# # Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
def calcular():
    try:
        n1 = int(input('Insira um número: '))
    except:
        print('Este número não pertence a classe dos Z - Inteiros')

calcular()
print()


# # Exercício 2:
# # Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
while True:
    try: 
        n1 = int(input('Insira um dividendo: '))
        n2 = int(input('Insira um dividor: '))
        print('A divisão de', n1, 'e', n2, '=', (n1 /n2))
        break
    except ZeroDivisionError as erro:
        print('Erro: ', erro)
print()

# # Exercício 3:
# # Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
l = [1,2,3,4,5]
list = [6,7,8,9,0]
try: 
    print(l[7])
except IndexError:
    print('Índice inferido incorreto') 
print()

# EXERCICIO QUE EU CRIEI COM BASE NO 3 - LOOP COMO ESCOLHA DE INDICE NA LISTA
list = [6,7,8,9,0]
print('list',list)
indice= int(input('Digite um Indice para acessar a lista: '))

while True:
    try:
       if list[indice]:
           print(f"O índice escolhido é igual a {indice} e o valor retirado da lista é {list[indice]}")
           break
    except IndexError: 
        print('Indice não está na lista')    
        break
  
    
