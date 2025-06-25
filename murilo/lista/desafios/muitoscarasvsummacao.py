qnde_de_humanos = 100
FORCA_DOS_RAPAZES = 1.0
FORCA_DO_GORILA = 5
MORDIDA_DO_GORILA = 10 


vida_dos_humanos = 10
vida_do_gorila = 500




hordas_dos_homens = 8


''' em 3 segundos
velocidade de ataque dos homens = 1
velocidade de ataque do gorila = 2
    em 9 segundos,mordida '''


tempo = 1
while(qnde_de_humanos > 0) and (vida_do_gorila >0):
    if tempo%3 == 0: 
        qnde_de_humanos -=1
        vida_do_gorila -= (hordas_dos_homens * FORCA_DOS_RAPAZES)
    
    if tempo %6 == 0:
        qnde_de_humanos -=1
    print(f'a quantidade de humanos e {qnde_de_humanos}')
    print(f'a vida do gorila e {vida_do_gorila:.0f}')
    print(f'ja se passaram {tempo} segundos\n')
    tempo = tempo +1
