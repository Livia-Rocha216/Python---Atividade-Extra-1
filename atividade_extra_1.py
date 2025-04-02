import random
import time
aleatorio = random.uniform(1, 100)
numero = input("Escolha um número de 1 a 100.")
while int(numero) != int(aleatorio):
    input("Escolha um número de 1 a 100.")
    if int(numero) != int(aleatorio):
        if int(numero) > int(aleatorio):
            print("Incorreto! O número digitado é maior que o número escolhido; tente novamente.")
        else: int(numero) < int(aleatorio)
        print("Incorreto! O número digitado é menor que o número escolhido; tente novamente.")
    else: int(numero) == int(aleatorio)
    print("Correto! Número de tentativas: ")