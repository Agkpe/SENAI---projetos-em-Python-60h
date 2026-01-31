
print ( 'CALCULDORA' )
print ('...' * 10 )

#SOMA
print ('Soma de dois algarismos inteiros')
print('___' *10)
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print()
soma = n1 + n2
print ( n1, '+', n2, '=', soma )
print()
print()

#SUBTRAÇÃO
print(' Subtração de números decimais')
print('___' * 10)
n1 = float(input('Digite um número decimal: '))
n2 = float(input('Digite outro número decimal: '))
print()
subtracao = n1 - n2
print(f' {n1} - {n2} = {subtracao:.2f}')
print()
print()

#MULTIPLICAÇÃO
print(' Multiplicação de números reais')
print('___' * 10)
n1 = float(input('Digite um número real: '))         
n2 = float(input('Digite outro número real: '))
print()
mult = (n1) * (n2)
print (n1, '*', n2, '=', mult )
print()
print()

#DIVISÃO
print('Divisão de números inteiros')
print('___' * 10)
n1 = int(input('Digite o dividendo: '))
n2 = int(input('Digite o divisor: '))
print()
divisao = n1 / n2
print(n1, '/', n2, '=', divisao)
print(f' Restante{n1%n2}')
