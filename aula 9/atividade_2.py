import os
os.system('cls')


print('ACESSO DE PROFESSORES')
print('___' * 10)
# - Acesso a conta com condicionais
dic = {
    'login': [],
    'senha': []
}

print('Fazendo seu cadastro')
cad_login = input('Digite seu e-mail profissional para login: ')
cad_senha = input('Registre uma senha para acesso: ')
print()
dic['login'].append(cad_login)
dic['senha'].append(cad_senha)
print()


# - 3 chances de acessar o sistema
print('Acessando o sistema')

for chances in range(3):
    l = input('Digite seu login: ')
    s = input('Digite sua senha: ')

    if l == dic['login'][0] and s == dic['senha'][0]:
            print(" Acesso concedido!")
            perg = input('Gostaria de calcular a média? Sim ou não: ')
            while perg == 'sim':
                print('Calculando a média dos alunos')
                print()
                aluno = input('Digite o nome do aluno: ')
                notas = []
                n1 =  float(input('Nota português: '))
                n2 =  float(input('Nota matemática: '))
                n3 =  float(input('Nota inglês: '))
                notas.extend([n1,n2,n3])
                media  =  sum(notas)/len(notas)
                print ('média do aluno(a):', aluno)
                print(media)
                cadastrar = input('deseja cadastrar um novo aluno? ')
                if cadastrar == 'não':
                    print('Até logo!')
                    break
            else:
                print('Até logo!')
    else: 
        print('Tente novamente')
print('Conta bloqueada!')



# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***

# - Ao finalizar o código, insira na borda do script, no última linha:

# input(’Digite enter para sair’)