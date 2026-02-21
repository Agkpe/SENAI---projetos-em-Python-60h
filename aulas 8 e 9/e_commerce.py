import os
os.system ('cls')
# cadastro no e-commerce
dados = { 
    'login': [],
    'senha': [],
        'produtos':{
                '1':['Computador Dell - R$', 5000],
                '2':['Fone Apple - R$', 2000],
                '3':['Mouse Lenovo - R$', 250],
                '4':['Monitor Lenovo - R$', 3500],
  }
}
print ('CADASTRE-SE:')
cad_login = input('Cadastre seu login: ')
cad_senha = input('Cadastre a sua senha: ')
print()

dados['login'].append(cad_login)
dados['senha'].append(cad_senha)

# acessar o e-commerce
print('ACESSE O SITE')
sso_login = input('Digite seu login de acesso: ')
sso_senha = input('Digite a sua senha:')
print()

if sso_login == dados['login'][0] and sso_senha == dados['senha'][0]:
#Outra condição para caso haja mais dados: if sso_login in dados['login'] and sso_senha in dados['senha']:
    print ('Seja Bem-Vindo ao E-commerce X')
    print()
    # verificar a lista de produtos
    print('PRODUTOS: ')
    produto = input(f'''

    {dados['produtos']} 
    Dentre os produtos 1 - 2 - 3 - 4 ->
    Escolha um dos produtos: 
''')

# comprar um produto
    carrinho = []
    valores = []
    carrinho.append (dados['produtos'][produto][0])
    valores.append (dados['produtos'][produto][1])
    print(carrinho[0], valores [0])

# paga o produto
    soma = sum(valores)
    print('Valor a pagar - R$', soma)
    pag = input('Digite a forma de pagamento:')
    print( 'Forma de pagamento: ', pag)
    print('Obrigada, volte sempre!')







else: 
    print('Digitação de login ou senha incorretos')
    print('Faça novamente')
  