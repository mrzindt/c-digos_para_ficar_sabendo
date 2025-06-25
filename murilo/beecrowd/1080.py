maiorvalor = 0
posiçao = 0
for i in range (0, 100, 2):
    valor = int(input())
    if valor>maiorvalor:
        maiorvalor = valor
        posicao = i        
print(maiorvalor)
print(posicao)