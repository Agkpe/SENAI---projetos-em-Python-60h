import os
os.system('cls')

print('PEDRA, PAPEL E TESOURA')
print('***' * 10)

import random # Biblioteca de aletoriedade

lista_maquina = ['🪨', '🧻', '✂️']
chute_maquina = random.choice(lista_maquina) #Programa escolhe um dos 'textos' para escolher 

 #print(chute_maquina)
#🪨🧻✂️  -- Emojis retirados do comando ('win' +'.')

minha_lista = ['', '🪨','🧻', '✂️' ]
 #print(minha_lista[2])

# Aplicação de condicionais
print('Escolha seu Icone')
print('1-🪨  | 2-🧻   | 3-✂️')
icone_escolhido = int(input('Escolha pelo indice: '))
print()

if chute_maquina == minha_lista[icone_escolhido]:
    print('EMPATE!')
    print()
    print('Escolha máquina: ', chute_maquina)
    print('Meu chute: ', minha_lista[icone_escolhido])

if chute_maquina == '🪨' and minha_lista[icone_escolhido] == '✂️' :
    print('Vitória da máquina!')
    print()
    print('Escolha máquina: ', chute_maquina)
    print('Meu chute: ', minha_lista[icone_escolhido])

if chute_maquina == '🧻' and minha_lista[icone_escolhido] == '🪨' :
    print('Vitória da máquina!')
    print()
    print('Escolha máquina', chute_maquina)
    print('Meu chute:', minha_lista[icone_escolhido])

if chute_maquina == '✂️' and minha_lista[icone_escolhido] == '🧻' :
    print('Vitória da máquina!')
    print()
    print('Escolha máquina', chute_maquina)
    print('Meu chute:', minha_lista [icone_escolhido])

if chute_maquina == '✂️' and minha_lista[icone_escolhido] == '🪨' :
    print('VOCÊ GANHOU!')
    print()
    print('Escolha máquina', chute_maquina)
    print('Meu chute:', minha_lista [icone_escolhido])

if chute_maquina == '🪨' and minha_lista[icone_escolhido] == '🧻' :
    print('VOCÊ GANHOU!')
    print()
    print('Escolha máquina', chute_maquina)
    print('Meu chute:', minha_lista [icone_escolhido])

if chute_maquina == '🧻' and minha_lista[icone_escolhido] == '✂️' :
    print('VOCÊ GANHOU!')
    print()
    print('Escolha máquina', chute_maquina)
    print('Meu chute:', minha_lista [icone_escolhido])