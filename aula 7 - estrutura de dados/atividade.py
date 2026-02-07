import os
os.system('cls')


ecommerce = {
'livro':25.15,
'tablet':3000.0,
'fone':500.0
}


carrinho = {
'produtos':[],
'valores':[]
}


produto1 = input('produto: ')
produto2 = input('produto: ')



carrinho['produtos'].append(produto1)
carrinho['produtos'].append(produto2)
carrinho['valores'].append(ecommerce[produto1])
carrinho['valores'].append(ecommerce[produto2])


soma =  sum(carrinho['valores'])

print('Total -  R$', soma)

print(carrinho)

pago ={
    'pagamento':[]
}
formas_pagamento = ['pix', 'cartão débito', 'cartão crédito', 'dinheiro']
print('Formas de pagamento:',formas_pagamento)
pagamento = input('Qual a forma de pagamento?:')
pago['pagamento'].append(pagamento)
print('Sua forma de pagamento escolhida foi:', pago)


