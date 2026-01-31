# Só pode começar ou com letras ou com _
# = (recebe - atribuição)
# Constante - é uma váriavel que eu não quero que mude, no caso de Python não existe

numero = 10  #Exemplo de váriavel
nome = "Ágatha"
sobrenome = "Kempe"
 
print(numero)
print(nome)

#concatenar (,) -> juntar
print (nome, sobrenome, ' Seja bem vinda!') # concatenado 

# 'Seja bem vindo' é um exemplo de dado literal - está diretamente na memória, não depende de váriavel

nome = 'Robson'
idade = 26
estado = 'MG'
curso = 'Python60'

print(f'Seu nome é: {nome}, você possui {idade} anos, você mora em {estado}, e está cursando {curso}')
      


# Conversão de dados 
nome = 'Carla'
idade = 25
cidade  =  'Guarulhos'
estado = 'SP'
curso = 'Python60'
casada_ = True 


# funções casting -  str | float |  int |  bool
# altera o tipo de dado

dado = bool(nome)
print(dado)


dado_3 =  float(idade)
print(dado_3)


dado_4 = int(casada_)
print(dado_4)


print(100 +  200)
print(10 - 100)
print(10 * 100)
print(10 / 100)


print('nome:', nome)
print('idade:', idade)
print('cidade:', cidade)
print('estado:', estado)
print('curso:', curso)
