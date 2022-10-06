from __future__ import print_function
from re import I
import random

def jogar_adivinhacao():

    print("Adivinhe o numero")
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    rodada = 1
    pontos=100

    print("Qual o nivel da dificuldade?")
    print("(1)Facil (2)Medio (3)Difícil")

    nivel = int(input ("Define o nível: "))


    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

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
            print("Você acertou e faz {} pontos ".format(pontos))
            break
        else:
            if(errouMaior):
                print("errou numero informado e maior que o numero secreto")
            elif(errouMenor):
                print("errou numero informado e menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos -  pontos_perdidos


        print ("Fim do jogo")
        