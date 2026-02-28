# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 

# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA
# E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES

import estatistica as et
def sistema():
    
    n = [10, 4, 8, 6, 8] 
    moda_alunos = et.moda(n)
    print('A moda das notas é', moda_alunos)

    media_alunos = et.media(n)
    print('A média das notas é', media_alunos)

    desvio_alunos = et.desvio(n)
    print ('O desvio de notas é', round(desvio_alunos))
    tam_nota()

def tam_nota():
    n = [10, 4, 8, 6, 8] 
    maior = max(n)
    menor = min(n)
    print('A maior nota foi', maior)
    print('A menor nota foi', menor)

sistema()


