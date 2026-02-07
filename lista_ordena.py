
lista = [1,2,3,4,5,6]


# ordenar a lista /  revertendo a ardem
lista.reverse()

print(lista)
print()
#Ordena a lista
lista.sort()
print(lista)
print()
# Ordena a lista, invertendo seus valores
lista.sort(reverse=True)
print(lista)
print()

# sum  -  somar todos os dados
print(sum(lista))

# copy -  copiar
x  = lista.copy()
print(x)

# index -  verifica a posição do indice
indice =  lista.index(5)
print(indice)
print()

# clear -  limpa
lista.clear()
print(lista)
