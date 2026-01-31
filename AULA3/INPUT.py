# O INPUT naturalmente é um texto

nome = input('Digite seu nome: ')
sobrenome = input ('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))

print('Seu nome é', nome, sobrenome)
print('Idade:', idade)

#Transformando o INPUT em calculadora
ano = int(input("Quando você nasceu: "))
ano_atual = int(input("Em que ano estamos:"))

idade = ano_atual - ano
print ('Você têm', idade, 'anos')

#Calculadora FLOAT
numero = float(input('Digite um número: '))
numero_2 = float(input('Digite um numero:'))

soma = numero + numero_2

print (soma)
               
            
