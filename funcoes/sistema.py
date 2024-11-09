from funcionario import adicionar_funcionario, listar_funcionario, atualizar_funcionario, remover_funcionario
from clientes import adicionar_cliente, listar_clientes, atualizar_clientes, lista_pedidos_cliente, remover_cliente
from sanduiche import adicionar_sanduiche, listar_sanduiche, atualizar_sanduiche, remover_sanduiche
from pedidos import adicionar_pedido, listar_pedidos
from venda import adicionar_venda, listar_venda
from menu import menu
from tratamento import input_int, cls

lista = []

menu(lista)

while True:
        escolha = input_int("digite uma opção: ")

       
        if escolha == 1:
                nome_funcionario = input("Nome do Funcionário: ")
                cpf = input("CPF do Funcionário: ")
                email = input("Email do Funcionário: ")
                salario = int(input("Salário do Funcionário: "))
                data_nasc = input("Data de Nascimento (YYYY-MM-DD): ")
                adicionar_funcionario(nome_funcionario, cpf, email, salario, data_nasc)
                
            
        elif escolha == 2:
                nome_cliente = input("Nome do Cliente: ")
                telefone = input("Telefone do Cliente: ")
                endereco = input("Endereço do Cliente: ")
                adicionar_cliente(nome_cliente, telefone, endereco)
                
            
        elif escolha == 3:
                nome_sanduiche = input("Nome do Sanduíche: ")
                valor_sanduiche = float(input("Valor do Sanduíche: "))
                adicionar_sanduiche(nome_sanduiche, valor_sanduiche)

        elif escolha == 4:
               adicionar_pedido # Feito , precisa de ajuste


        elif escolha == 5:
               adicionar_venda # Feito precisa de ajuste
                

        elif escolha == 6:
               listar_funcionario()
               break
              

        elif escolha == 7:
               listar_clientes()
               break


        elif escolha == 8:
               listar_sanduiche()
               break
        

        elif escolha == 9:
               listar_pedidos()   # Falta teste
               break
        

        elif escolha == 10:
               listar_venda()
               break
        

        elif escolha == 11:
               coluna = input('digite o nome da coluna: ')
               novo_valor = input('digite o novo valor do campo: ')
               id_cliente = input_int('Agora digite o numero do seu ID: ')
               
               atualizar_clientes(coluna, novo_valor, id_cliente)
               break
        
        
        elif escolha == 12:
               coluna = input('digite o nome da coluna: ')
               novo_valor = input('digite o novo valor do campo: ')
               id_funcionario = input_int('Agora digite o numero do seu ID: ')
               atualizar_funcionario(coluna, novo_valor, id_funcionario)

               break
        
        
        elif escolha == 13:
               coluna = input('digite o nome da coluna: ')
               novo_valor = input('digite o novo valor do campo: ')
               id_sanduiche = input_int('Agora digite o numero do seu ID: ')
               atualizar_sanduiche(coluna, novo_valor, id_sanduiche)
               break
        elif escolha == 14:
              nome_cliente = input('digite o nome do cliente que deseja procurar: ')
              lista_pedidos_cliente(nome_cliente)
        

        elif escolha == 0:
               print('saindo...')
               break
        

        elif escolha == 15:
               id_cliente = input('digite o ID do cliente para remover: ')
               remover_cliente(id_cliente)
               break


        elif escolha == 16:
              id_funcionario = input("digite o ID do funcionario: ")
              remover_funcionario(id_funcionario)
              break

       
        elif escolha == 17:
              id_sanduiche = input("Digite o ID do sanduiche: ")
              remover_sanduiche(id_sanduiche)
              break

 
        else:
             print("Valor invalido, Tente novamente")
             cls()
        menu(lista)
