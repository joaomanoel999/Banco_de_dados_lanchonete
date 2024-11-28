from menu import  logar, gerenciamento_funcionarios,menu_up,gerenciamento_clientes,gerenciamento_pedidos,gerenciamento_sanduiche,gerenciamento_vendas
from tratamento import input_int, cls
import os
import time

lista_venda =[]
lista_cliente = []
lista_funcionario= []
lista_pedido = []
lista_sanduiche = []
lista_menu = []
escolha = int

while True:
       if escolha == 0:
              break
       
       autenticado = logar()
       if autenticado:
              print('Logado com sucesso!')
              cls()
              
              menu_up(lista_menu)

              while True:
                     escolha = input_int("digite uma opção: ")
                     

                     if escolha ==0:
                            print('saindo...')
                            break

                     elif escolha ==1:

                            print('Carregando...')
                            cls()
                            gerenciamento_funcionarios(lista_funcionario)
                            

                     elif escolha == 2:

                            print('Carregando...')
                            cls()
                            gerenciamento_clientes(lista_cliente)
                            

                     elif escolha ==3:

                            print('Carregando...')
                            cls()
                            gerenciamento_pedidos(lista_pedido)       
                            

                     elif escolha ==4:
                            
                            print('Carregando...')
                            cls()
                            gerenciamento_sanduiche(lista_sanduiche)
                            menu_up(lista_menu)

                     elif escolha == 5:
                            
                            print('Carregando...')
                            cls()
                            gerenciamento_vendas(lista_venda)
                            
                            
                     else:
                            print("Valor invalido, Tente novamente")
                            cls()
                            menu_up(lista_menu)
                            
       else:
              print('email ou senha invalidas!')
              print('Tente Novamente!')
              cls()
              