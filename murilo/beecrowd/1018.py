valor = int(input())
cedulas =[100,50,20,10,5,2,1]
for nota in cedulas:
    totaldenotas = valor// nota
    print(f'{totaldenotas} nota(s) de R$ {nota},00')
    valor = valor%nota
    