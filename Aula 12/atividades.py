import os
os.system('cls')

# # Exercícios com funções:
# # variáveis locais, globais e parâmetros
# # 1
# # CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
# def num_par_impar():
#     num1 = int(input('Digite um número: '))
#     num2 = int(input('Digite outro número: '))
#     if num1 % 2 ==0 and num2 % 2 ==0 :
#         print('Ambos os números são pares')
#     elif num1 %2 ==0 and num2 %2 != 0:
#         print(f" O número {num1} é par, enquanto o número {num2} é ímpar")
#     elif num1 %2 != 0 and num2 %2==0:
#         print(f" O número {num1} é ímpar, enquanto o número {num2} é par")
#     else: 
#         print('Ambos os números são ímpares')
# num_par_impar()
# print()
# # 2
# # CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
# def mult():
#     num1 = int(input('Digite um número: '))
#     num2 = int(input('Digite outro número: '))
#     num3 = int(input('Digite outro número: '))
#     multi = num1*num2*num3
#     print(f'A multiplicação de {num1} * {num2} * {num3} = {multi}')
# mult()
# print()
# # 3
# # CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
# def potencia(num1, expoente):
#     return num1 ** expoente

# print('10 **2 é =', potencia(10,2))



# # 4
# # CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.
# def idade ():
#     usuario=int(input('Qual sua idade? '))
#     if usuario <= 17:
#         print('Mensagem de idade Indisponível')
#     elif usuario == 18:
#         print('Seja bem-vindo a vida de maioridade. Os boletos te esperam!!')
#     else: 
#         print('Você já passou da época para te avisarmos')
# idade()
# # 5
# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
# def descoberta(ano_atual, ano_nasceu):
#     return   ano_atual - ano_nasceu
# print(f'Você possui {descoberta(2026, 2000)}')
# print()
# # 6
# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
# print('HISTÓRICO OFICIAL DA FIFA')
# def copa():
#     america = [1999,2001,2004,2007]
#     print('Entre esses anos de ocorrência da copa américa. Escolha um dos anos de ocorrência:', america)
#     ano = int(input('Qual ano escolhido? '))
#     while ano in america:
#         if ano == 1999 and 2007 and 2001:
#             print('BRASIL É HEXACAMPEÃO!')
#             break
#         else: 
#             print('Brasil não foi campeão')
#             break
#     else:
#         print('Ano inválido ')
# copa()
        
# 7
# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
# 1 - Função - cumprimentar o cliente
print('RESTAURANTE COMIDA DE VÓ')
def cliente ():
    print('Bom dia! Seja bem-vindo ao nosso cantinho.')

    ordem()
# 2 - Função - restaurante
def ordem():
    pedido = input('Gostaria de fazer um pedido? sim ou não:').lower()
    ordem_cliente = []
    while pedido =='sim':
        cardapio = ['salada', 'macarronada', 'sanduiche', 'sorvete']
        print('Aqui está o nosso cardápio de hoje: ', cardapio)
        ped_cliente = input('Qual seria o seu pedido? ').lower()
        if ped_cliente in cardapio: 
            ordem_cliente.append(ped_cliente)
            print('Item adicionado! Seu carrinho atual é: ', ordem_cliente)

        else:
            print('Desculpe! Não temos esse esse item')
    
        perg =(input('Gostaria de pedir mais alguma coisa? sim ou não')).lower()
        if ordem_cliente:
            print('Finalizando Pedido')
            forma_pagamento = ['cartão débito', 'cartão crédito', 'pix', 'dinheiro']
            print('Formas pagamento: ', forma_pagamento)
            pag = input('Qual a forma de pagamento escolhida? ').lower()
            if pag in forma_pagamento:
                print(f'Pedido:{ordem_cliente}. Forma de pagamento: {pag}')
                print('Obrigada pela compra. Volte sempre!')
            else: 
                print('Forma de pagamento inválida.')
    else: 
        print('Nenhum pedido realizado. Até a próxima')
        
    
cliente()
