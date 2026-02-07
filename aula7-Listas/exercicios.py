import os
os.system('cls')

print('EXERCÍCIOS EM PYTHON - LISTAS')
print('___' *10 )

#1° exercicio - lista no método range()
lista = list(range(1,21,2))
print (lista)
print()

#2° exercício - Maneira clássica de criar lista manualmente
lista = [1,2,3,4,5,6,7,8,9,10]
x =lista.copy() # Copia a lista original sem alterações para que possa ser utilizada posteriormente

print(lista)
print()

#3° exercício - Imprimir o terceiro elemento 
print (lista[2])
print()

#4° exercício - Add num 9 a lista 
lista.append(9)
print(lista)
print()

#5° exercício - remover num 5
lista.remove(5)
print(lista)
print()

#6° exercício - Nova lista
carros = ['BYD', 'HB20', 'CIVIC']
print(f'{carros} {x}')

#Juntar ambas as listas
carros +=(x)
print(carros)