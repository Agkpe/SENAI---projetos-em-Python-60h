print( 'SISTEMA DE NOTAS')
print('...' * 10)   # multiplicação pode ser mesclada com str

nome_aluno = input("Nome do Aluno: ")
n1_port = float(input('Nota de Português: '))
n2_mat = float(input('Nota de Matemática: '))
n3_ing = float(input('Nota de Inglês: '))

media = n1_port + n2_mat + n3_ing / 3

print('SITUAÇÃO DO ALUNO: ')
aprovado = media >= 7
reprovado = media < 5
recuperacao = media >= 5 and media < 7

print(nome_aluno, ' Aprovado?', aprovado)
print(nome_aluno, ' Reprovado?', reprovado)
print(nome_aluno, ' Recuperação?', recuperacao)


                
