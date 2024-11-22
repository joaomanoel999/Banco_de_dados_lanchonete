import os
import time


def input_int(texto):
    lista = []
    while True:
        try:
            valor = int(input(texto))
            return valor
        except ValueError:
            print('Por favor digite um valor inteiro.')
            cls()
            
def cls():
    time.sleep(3)
    os.system('cls')