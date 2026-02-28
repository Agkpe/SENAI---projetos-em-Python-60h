import random


def soma1():
    print(10 + 10) # Se torna str, não utilizavel


def soma2():
    n1 = int(input('digite o valor 1'))
    n2 = int(input('digite o valor 2'))
    soma  = n1 + n2
    print(soma)


def soma3(n1, n2):
    print(n1 + n2)

# A MAIS PROFISSIONAL / MAIS UTILIZADA
# otimização -  é a melhor utilização de uma função
def soma4(n1, n2):
    return n1  + n2 # A única que é possível ser reutilizavel



n1 , n2  = 10,10
def soma5():
    print(n1 + n2)  # Não muito segura, solta no código - NÃO FAÇA


soma1()
soma2()
soma3(10,10)
soma = soma4()   
print(soma4(10,10))
soma5()




soma = soma4()  




