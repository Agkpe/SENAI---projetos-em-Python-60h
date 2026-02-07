import os
os.system('cls')

import random
aleatorio = random.randint(1,10)
chute = int(input('Chute um número de 1 a 10: '))

if aleatorio == chute:
    print('Acertou em cheio!')
    print('O número é', aleatorio)

else: 
    print('Errou feio!')
    print('O número é', aleatorio)