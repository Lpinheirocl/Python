from __future__ import print_function
from re import I


numero_secreto = 89
total_de_tentativas = 3
rodada = 1

for rodada in  range(1, total_de_tentativas + 1):
    print("Tentantivas {} de {} :".format(rodada, total_de_tentativas))
    chute_str    = input("Digite um numero de 1 a 100:")
    print("numero" ,  chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100 ):
        print("Você deve digitar um numero entre 1 a 100")
        continue

    acertou = chute == numero_secreto
    errouMaior = chute > numero_secreto
    errouMenor = chute < numero_secreto

    if (acertou):
        print("acerto")
        break
    else:
        if(errouMaior):
            print("errou numero informado e maior que o numero secreto")
        elif(errouMenor):
            print("errou numero informado e menor que o numero secreto")
    rodada = rodada +1

    print ("Fim do jogo")