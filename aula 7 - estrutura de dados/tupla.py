#TUPLA SE PARECE COM LISTAS - 
# FORMAS DE REPRESENTA-LA
tupla = 1,2,3
tupla = [1,2,3]
t = tuple(range(1,11))
print (t)

#Tuplas são parcialmente imutáveis, formas de concatenação
t += (20, 30, 40)
print(t)

s = sum(t)
print(t, s)

len(t)
print(t)

max(t)
print(t)

print(dir(t))