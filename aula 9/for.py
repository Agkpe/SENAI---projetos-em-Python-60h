import os
os.system('cls')
import time

#FOR --> finito
#ITERAR PERCORRENDO E REPETINDO
for i in range(10):
    print(i)  # Número de 0 a 9
    time.sleep(0.5) # Demonstra o resultado em 0.5s

for i in range (1,6): 
    print(i)  #Números de 1 a 5


for l in range(0,10,2): # Números de 0 a 9 de 2 em 2 
    print(l)

# Aplicando um break em meio ao loop
for i in range(10):   
    if i == 5:
        break

#Estruturação de dados com loop
dados = {
'produtos' : []
}


for produto in range(5):
    prod =  input('Digite o nome de um produto: ')
    dados['produtos'].append(prod)
print(dados)


for dado in dados.values():
    print(dado)

# Contagem decrescentes de números até o de 1 em 1 
for x in range(10,0,-1):
    print(x)


