
# estruturas de fluxo de controle 
#mais fluida


# palavra_reservada condição = v or f


nome  = input('digite seu nome: ')


# utilização do pass
if nome == 'Fernanda':
    pass


# condicional  simples


# falso
if nome  == 'Kaio':
    print('Seja bem vindo', nome)


# verdadeiro
if nome != 'Kaio':
    print('Não pode acessar ... ')


# condicional composta


if nome == 'kaio':
    print('seja bem vindo', nome)
else:
    print('Não pode acessar ... ')    


# condicional composta if elif else



if nome == 'Kaio':
    print('Seja bem vindo ', nome)
elif nome == 'Lucas':
    print('Não pode acessar')
elif nome == 'Fenanda':
    print('Olá', nome)    
else:
    print('faça o cadastro')




# só posso inciar condicionais com if
# elif quantos eu quiser 
# else só tem um (dentro de um fluxo de condição)
# if só tem um (dentro de um fluxo de condição)




# cadastro no e-commerce
dados = { 
    'login:': [],
    'senha:': []
}
print ('CADASTRE-SE:')
cad_login = input('Cadastre seu login: ')
cad_senha = input('Cadastre a sua senha: ')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)

# acessar o e-commerce
print('ACESSE O SITE')
sso_login = input('Digite seu login de acesso: ')
sso_senha = input('Digite a sua senha:')

if sso_login == dados['login'][0] and sso_senha == dados['senha'][0]:
    print ('Seja Bem-Vindo ao E-commerce Z')
else: 
    print('Digitação de login ou senha incorretos')
    print('Faça novamente')
# verificar a lista de produtos
# comprar um produto
# paga o produto                                                                                                                                                                    