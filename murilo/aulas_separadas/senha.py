LOGIN="pedrin123"
SENHA="pedrin456"


TENTATIVA=0
while TENTATIVA<5:
    QUAL_A_SENHA= input("ïnforme sua senha")
    QUAL_SEU_LOGIN= input("informe seu login")

    if QUAL_SEU_LOGIN==LOGIN and QUAL_A_SENHA==SENHA:
        print("voce emtrou na sua conta")
        break
    else:
        print("senha ou login incorreto")     
        TENTATIVA=TENTATIVA+1