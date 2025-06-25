CONTA = 0.0
PRECO_POR_BOLA = 30.0

print('ola,bem vindo a sorveteria')

POTE = input ("voce quer um pote de plastico ou biscoito?")
if POTE.lower() == ('biscoito') :
    CONTA += 5.0
QUANTIDADE_DE_BOLAS = int (input("quantas bolas voce quer?"))
PRECO_BASE = (PRECO_POR_BOLA * QUANTIDADE_DE_BOLAS)
total_bolas = CONTA + PRECO_BASE
print('\n', 'qual acompanhamento voce quer?', '\n' ,'Temos', '\n', '1 leite em po(gourmet)', '\n' ,'2 granulado(do imalaia)', '\n' ,'3 bolinhas de chocolate(cacau show)', '\n' ,'0 caso nao queira acompanhamento')
PRECO_DO_ACOMPANHAMENTO = 0
ACOMPANHAMENTO = int(input())

if ACOMPANHAMENTO != 0:
    for i in range(3):
        if ACOMPANHAMENTO == 1:
            PRECO_DO_ACOMPANHAMENTO += 5.0
        elif ACOMPANHAMENTO == 2:
            PRECO_DO_ACOMPANHAMENTO += 35.0
        elif ACOMPANHAMENTO == 3:
            PRECO_DO_ACOMPANHAMENTO += 10.0
        else:
            PRECO_DO_ACOMPANHAMENTO += 0.0

        if i == 2:
            break
        
        ACOMPANHAMENTO = int(input('escolha seu proximo acompanhamento'))

# contra_barra = "\"
CONTA = PRECO_DO_ACOMPANHAMENTO + total_bolas
VALOR_DA_COBERTURA = 0
print('\n', 'qual cobertura voce quer temos:','\n', '1 leite condensado', '\n','2 cobertura de fruta', '\n', '3 cobertura de chocolate ')
QUER_COBERTURA = int(input('deseja cobertura ? (1 - para sim 0 - para nao)'))

if QUER_COBERTURA == 1:
    while QUER_COBERTURA !=0:
        print(' 1 leite condensado', '\n','2 cobertura de fruta', '\n', '3 cobertura de chocolate ','\n', ' 0 para finalizar o pedido')
        QUER_COBERTURA = int(input())
        if QUER_COBERTURA == 1:
            VALOR_DA_COBERTURA +=10.0
        elif QUER_COBERTURA == 2:
            VALOR_DA_COBERTURA +=7.0
        elif QUER_COBERTURA == 3:
            VALOR_DA_COBERTURA +=10.0

else:
    print("VALOR TOTAL: R$ ",CONTA)

total = CONTA + VALOR_DA_COBERTURA
print (f'SUA CONTA FOI {CONTA + VALOR_DA_COBERTURA}')

def calcularTroco(n):
    cedulas =[100,50,20,10,5,2,1]
    for nota in cedulas:
        totaldenotas = n// nota
        print(f'{totaldenotas} nota(s) de R$ {nota},00')
        n = n%nota

calcularTroco(total)
