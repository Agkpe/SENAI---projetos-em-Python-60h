### Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.
num = 7
print(num **2)

### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.
nome = 'Ágatha'
sobrenome = 'Barros'
sobrenome_2 = 'Kempe'

print (nome, sobrenome, sobrenome_2)
print()

### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

final = n1+n2 
print(f'O resultado de {n1} + {n2} = {final} ')
print()
      # Outra interpretação
nasc =input('Que dia você nasceu? ')
hora = input('Que horas você nasceu? ')
print (f'Você nasceu no dia {nasc} às {hora} horas')
print()
### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
linguagem = 'Python'
numero = '3.14'
print(f'{linguagem} {numero}')
print()
### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.
print('Continue o ditado popular: ')
print('Quem não tem cão...')
answer = input('Digite aqui: ')
ditado = "Quem não tem cão "

print(f'Sua resposta para o ditado{ditado}, foi {answer}. ')
print(f'Ficando assim: {ditado} {answer}')


# tipos de CONCATENAÇÕES
nome, sobrenome = 'Ágatha', 'Kempe'
print(nome + ' ' +sobrenome)
print('{} {}'.format(nome, sobrenome))
print('%s %s'%(nome, sobrenome))
print(f'{nome} {sobrenome}')