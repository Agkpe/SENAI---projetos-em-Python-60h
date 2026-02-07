import os
os.system('cls')

dicionario = {'key':'Value'}  # dict mais detalhada

# As estruturas de dados são dinâmicas e podem interagir entre si

usuario = {
    'nome' : 'Paulo', 
    'idade':25, 
    'endereço': 'rua 10', 
    'curso': ('python','js', 'go'),    # utilizando tuplas dentro do dicionário
    'documento':{132132132,1231231321,2123231231,123132132},   # Conjuntos dentro do dicionário
    'livros':{                                    #Dicionário dentro do dicionário
     'taleb':['antifragil','cisne negro'],  #Listas no dicionário 
     'harari':['homodeus']


    }
    }

print(usuario)

estoque = {
'eletronicos':{
'iphone':['17', '15','14'],
'tvs':['samsumg','lg' ],
},
'moveis':{
'mesas':['etna','x'],
'cadeiras':['etan','leroy']
}
}



d =  dict(a = 10, b = 20, c = 30)
print(d)





