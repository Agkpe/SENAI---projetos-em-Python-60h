import os
os.system('cls')

# While infinito - tende a repetir o programa inúmeras vezes até a condição ser falsa

# Aplicando sistema em loop while
dados = {
'produtos' : []
}


perg =  input('Deseja comprar? sim ou não ')


while perg == 'sim':
    prod = input('nome do produto: ')
    dados['produtos'].append(prod)
    
    print(dados)
    perg =  input('Deseja continuar? sim ou não ')
else:
    print('Obrigado volte sempre! ')

#transformando o while em finito
c=0 
while c <=10:
    print (c)
    c = c+1 


#  While finito decrescente
c = 10
while c > 0 :
    print(c)
    c  =  c  - 1
    

