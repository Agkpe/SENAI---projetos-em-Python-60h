# 'Condicionais'que avaliam os dados de uma váriavel  - não muito utilizado
# Mais objetivo
senha = input('Digite sua senha: ')


match senha:
    case 123:
        print('Acesso aprovado')
    case _: 
        print('Acesso Reprovado')