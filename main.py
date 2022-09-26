from __future__ import print_function
from re import I


numero_secreto = 89
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentantivas {} de {} :".format(rodada, total_de_tentativas))
    chute_str    = input("Digite um numero: ")
    print("numero" ,  chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    errouMaior = chute > numero_secreto
    errouMenor = chute < numero_secreto

    if (acertou):
        print("acerto")
    else:
        if(errouMaior):
            print("errou numero informado e maior que o numero secreto")
        elif(errouMenor):
            print("errou numero informado e menor que o numero secreto")
    rodada = rodada +1

    print ("Fim do jogo")