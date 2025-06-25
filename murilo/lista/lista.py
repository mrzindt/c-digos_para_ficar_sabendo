lista = [5,10,15,20]

'''
.append adiciona
.pop remove
.insert substitui
'''
lista.append(25)

print (len(lista))
for numero in lista:
    print (numero)

for i in range (len(lista)):
    print (lista[i])
    
    
    
listadenomes = ['danilo','fransisvaldo','jose']
for i,valor in enumerate(listadenomes):
    print(f'o index {i},tem valor:{valor}')
