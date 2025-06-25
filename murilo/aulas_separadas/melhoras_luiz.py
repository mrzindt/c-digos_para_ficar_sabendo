QTDE_AULAS = 24

nota = float(input("insira a sua nota: "))
presenca = int(input("insira sua quantidade de presenca: "))

percentual = int((presenca/QTDE_AULAS) * 100)

if nota >= 7 and percentual >= 70:
    print("voce esta aprovadado")
elif nota < 7 and percentual >=70:
    print ("voce reprovou por falta de nota")
elif percentual < 70 and nota >= 7:
    print("voce reprovou pois faltou dms")
else:
    print("ruan, tu n vem nem pra escola direito,ta achando q a vida e um morango?")