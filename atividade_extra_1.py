import random
import time
aleatorio = random.uniform(1, 100)
numero = input("Escolha um número de 1 a 100.")
while numero != aleatorio:
    input("Escolha um número de 1 a 100.")
    if numero != aleatorio:
        if numero > aleatorio:
            print("Incorreto! O número digitado é maior que o número escolhido; tente novamente.")
        else: numero < aleatorio
        print("Incorreto! O número digitado é menor que o número escolhido; tente novamente.")
    else: numero == aleatorio
    print("Correto! Número de tentativas: ")