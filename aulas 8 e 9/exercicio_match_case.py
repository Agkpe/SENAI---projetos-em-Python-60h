
print('NÚMERO É PAR OU ÍMPAR')
numero = int(input('Número: '))
match numero:
    case numero if numero % 2 == 0: 
        print('Número par')
    case _: 
        print('Número ímpar')
print()

# NUMERO POSITIVO, NEGATIVO OU ZERO
print('Seu número é positivo, negativo ou nulo?')
print()
numero = int(input('Digite um número inteiro: '))
match numero:
    case numero if numero > 0:
        print('Este número é positivo')
    case numero if numero == 0:
        print('Este número é nulo')
    case _:
        print('Este número é negativo')
print()

# VERIFICANDO STRING VAZIA OU NÃO 

nome = input('Qual seu nome: ')
match nome: 
    case '':
     print('Espaço vazio')
    case _: 
        print('Seu nome é', nome)
print()

# NÚMERO MENOR, MAIOR OU IGUAL 10
numero = int(input('Digite um número: '))
match numero:
    case numero if numero > 10:
        print('Este número é maior que 10')
    case numero if numero == 10:
        print('Este número é igual a 10')
    case _: 
        print('Este número é menor que 10')
print()

#CLASSIFICANDO IDADES
idade= int(input('Digite sua idade:'))
match idade:
    case idade if idade <= 12:
        print('Você é criança')
    case idade if idade <= 17:
        print('Você é adolescente')
    case idade if idade <=34:
        print('Você é jovem')
    case idade if idade <= 64:
        print('Você é adulto')
    case idade if idade >=65: 
        print('Você é idoso')
    

