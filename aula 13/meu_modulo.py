# # meu_modulo.py

import random
# **1 - Crie um número aleatório de 5,10
def aleatorio(n1,n2):
   return random.randint(n1, n2)


# **2 - Crie 3 números aleatórios**
def ativ_2(lista):
    return random.choice(lista)


# **3 - Crie um número aleatório entre 10 a 30 utilize o range()**
def ativ_3(n1,n2):
    return random.randrange(n1,n2)

# **4 - Contagem regressiva simples**
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)
def ativ_4(num):
    for num in range(10,0,-1):
        print(num)
    print('Fogo!')
    

# **5 - Soma de números pares**

def ativ_5(n1):
    soma = 0

    for numero in range(2, n1 + 1):
        if numero % 2 == 0:
            soma += numero

    return soma





# **6 - Tabuada de multiplicação**

# ***Utilize print() na saída***

# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.

# (while ou for )
def ativ_6 (n):
    lista = [1,2,3,4,5,6,7,8,9,10]
    for i in lista:
        c=n*i
        print(n, 'x', i, '=', c)


# **7 -  Números ímpares reversos**

# Exiba uma contagem regressiva de números ímpares de 99 a 1.

# (for)
def ativ_7(num):
    for i in range(99 ,1, -2):
        print(i)

# ***Chamar todas elas para o arquivo main()***