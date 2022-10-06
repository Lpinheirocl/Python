import forca
import adivinhacao

print("Escolha o Jogo")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o Jogo?"))

if(jogo == 1):
    print("Jogandi forca")
    forca.jogar_forca()
elif(jogo == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar_adivinhacao

