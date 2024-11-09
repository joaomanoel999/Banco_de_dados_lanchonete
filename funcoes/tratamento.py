import os
import time
from menu import menu

def input_int(texto):
    lista = []
    while True:
        try:
            valor = int(input(texto))
            return valor
        except ValueError:
            print('Por favor digite um valor inteiro.')
            cls()
            menu(lista)
def cls():
    time.sleep(3)
    os.system('cls')