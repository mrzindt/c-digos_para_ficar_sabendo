'''lista = 'casa suja,chão sujo'
lista = lista.replace(' ', '') 


numerais = 'ca2a su8987a, chão 2ujo'
numerais = numerais.replace('2','')
numerais_corretos = ''
print(numerais)
for letra in numerais:
    if not letra.isdigit()==True:
        numerais_corretos+= letra
print (numerais_corretos)'''

nome = input('nome?')

for i in range (1,len(nome)+1,2):
    print (nome[0:i])

