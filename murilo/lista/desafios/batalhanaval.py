import random
tiros = 6
OCEANO = ['🌊'] * 10
print(OCEANO)
navios = []
acertos = 0
while len(navios) <4:
    posicao = random.randint(0,9)
    if posicao not in navios:
        navios.append(posicao)

print(navios)

while acertos <4 and tiros >0:
    print("tiros disponiveis :", tiros)
    posicao_alvo = int(input('informe uma posicao entre 0 e 9: '))
    if posicao_alvo <0 or posicao_alvo > 9:
        print ('posicao invalida')
        continue 
    if OCEANO[posicao_alvo] == '❌':
        tiros = tiros - 1
        print('essa posicao ja foi atingida ')
        continue
    if posicao_alvo in navios:
        print('acertou o navio! 💥')
        OCEANO[posicao_alvo] = '🚢'
        acertos = acertos +1
        tiros = tiros -1
        navios.remove(posicao_alvo)
        print(OCEANO)
    else:
        OCEANO[posicao_alvo] = '❌'
        tiros = tiros -1
        print ('tiro na agua! ')
        print(OCEANO)
if tiros ==0:
    print('acabou a bala')
if acertos == 4:
    print ('voce venceu! EU SEI OQ VC FEZ...')
