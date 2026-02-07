import os
os.system('cls')

# EXERCÍCIOS 1: 


# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
print('NÚMERO POSITIVO, NEGATIVO OU NEUTRO')
print('***' * 10)
num = int(input('Digite um número: '))
if num < 0:
 print('Esse número é Negativo')
elif num == 0 :
 print('Esse número é Nulo')
else :
 print('Esse número é positivo')
print()

# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
print('Você pode votar?')
print('***' * 10)
idade = int(input('Digite sua idade: '))
titulo_eleitor = input('Possui titulo de eleitor? sim ou não: ')
if idade >= 17 and titulo_eleitor == 'sim':
 print('Você pode votar')
elif idade >= 17 and titulo_eleitor == 'não':
 print('Você deveria ter o título de eleitor')
else:
 print("Você não pode votar ainda")
print()

# 3*
# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
print('ESTE NÚMERO É PAR OU ÍMPAR!')
print('***' * 10)
num = int(input('Digite um número: '))
if num % 2 == 0:
 print('O número', num, 'é par!')
else:
 print('O número', num, 'é ímpar!')
print()

# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
print('QUE TIPO DE TRIÂNGULO É O SEU?')
print('***' * 10)
escaleno = input('Seu triângulo possui catetos? sim ou não: ')
if escaleno == 'sim': 
    print('Seu triângulo é Escaleno!')
else: 
    print('Ou seu triângulo é equilátero ou é isósceles')

    triangulo = input('Seu triângulo possui base e lados iguais?: sim ou não')
    if triangulo == 'sim': 
        print('Seu triângulo é Equilátero!' )
    else:
        print('Seu triângulo é Isósceles!')
print()



# 5*
# Determine se um número é múltiplo de 5 e 7.
print('SEU NÚMERO É MÚLTIPLO DE 5 E 7?')
print('***' * 10)
num = int(input('Digite um número: '))
if num % 35 ==0:
    print('Seu número é múltiplo de 5 e 7')
else:
    print('Seu número não é múltiplo de 5 e 7')
print()

# 6*
# Verifique se um número é positivo e maior que 10
print('SEU NÚMERO É POSITIVO E MAIOR QUE 10')
print('***' * 10)
num = int(input('Digite um número: '))
if num > 10:
    print('Seu número é positivo e maior que 10!')
print()

# 7*
# Verifique se um número é divisível por 3 ou 5.
print('O NÚMERO É DIVISÍVEL POR 3 OU 5?')
print('***' * 10)
num = int(input('Digite um número:'))
if num % 3 or num % 5 == 0:
    print('Seu número', num, 'é divisível por 3 ou 5!')
else: 
    print('Seu número', num, 'não é divisível por 3 ou 5!')

