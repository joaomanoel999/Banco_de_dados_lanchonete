from banco import criar_conexao
from seguranca import checar_password, criotpgrafar
from usuarios import login
from getpass import getpass
from funcionario import adicionar_funcionario, listar_funcionario, atualizar_funcionario, remover_funcionario
from clientes import adicionar_cliente, listar_clientes, atualizar_clientes, lista_pedidos_cliente, remover_cliente
from sanduiche import adicionar_sanduiche, listar_sanduiche, atualizar_sanduiche, remover_sanduiche
from pedidos import adicionar_pedido, listar_pedidos,atualizar_pedido,remover_pedido
from venda import adicionar_venda, listar_venda,atualizar_venda, remover_venda
from tratamento import input_int


def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def gerenciamento_clientes(lista_cliente):
     lista_cliente = []
     lista_cliente = ['Cadastrar Clientes','Listar Clientes','Atualizar  Clientes','listar pedidos por cliente']
     cabecalho('Gerenciamento Clientes')
     c = 0
     for item in lista_cliente:
        print(f'{c+1} - {item}')
        c += 1
     linha()

     opc = input_int('digite a opção: ')

     if opc ==1:
                nome_cliente = input("Nome do Cliente: ")
                telefone = input("Telefone do Cliente: ")
                endereco = input("Endereço do Cliente: ")
                adicionar_cliente(nome_cliente, telefone, endereco)
     elif opc ==2:
                cabecalho('LISTA DE CLIENTES')
                listar_clientes()


     elif opc == 3:
                coluna = input('digite o nome da coluna: ')
                novo_valor = input('digite o novo valor do campo: ')
                id_cliente = input_int('Agora digite o numero do seu ID: ')
                atualizar_clientes(coluna,novo_valor,id_cliente)


     elif opc == 4:
                id_cliente = input('digite o ID do cliente para remover: ')
                remover_cliente(id_cliente)
           


def gerenciamento_funcionarios(lista_funcionario):
    lista_funcionario = []
    lista_funcionario = ['Cadastrar Funcionario','Listar Funcionarios','Atualizar  Funcioario','Remover Funcionario']
    cabecalho('Gerenciamento Funcionario')
    c = 0
    for item in lista_funcionario:
        print(f'{c+1} - {item}')
        c += 1
    linha() 

    opc = input_int('digite a opção: ')
    if opc == 1:
                nome_funcionario = input("Nome do Funcionário: ")
                cpf = input("CPF do Funcionário: ")
                email = input("Email do Funcionário: ")
                salario = int(input("Salário do Funcionário: "))
                data_nasc = input("Data de Nascimento (YYYY-MM-DD): ")
                adicionar_funcionario(nome_funcionario, cpf, email, salario, data_nasc)


    elif opc == 2:
         cabecalho('LISTA DE FUNCIONARIOS')
         listar_funcionario()


    elif opc ==3:
                coluna = input('digite o nome da coluna: ')
                novo_valor = input('digite o novo valor do campo: ')
                id_funcionario = input_int('Agora digite o numero do seu ID: ')
                atualizar_funcionario(coluna, novo_valor, id_funcionario)


    elif opc == 4:
                id_funcionario = input("digite o ID do funcionario: ")
                remover_funcionario(id_funcionario)
                


def gerenciamento_pedidos(lista_pedido):
     lista_pedido = []
     lista_pedido = ['Adicionar Pedidos','Listar Pedidos','Atualizar Pedido','Remover Pedido']
     cabecalho('Gerenciamento Pedidos')
     c = 0
     for item in lista_pedido:
        print(f'{c+1} - {item}')
        c += 1
     linha() 

     opc = input_int('digite a opção: ')  

     if opc== 1:
           id_funcionario = input_int('Digite o ID do Funcionario: ')
           id_cliente = input_int('digite o ID do Cliente:')
           id_sanduiche = input_int('digite o ID do sanduiche: ')
           adicionar_pedido(id_funcionario, id_cliente, id_sanduiche)


     elif opc== 2:
           cabecalho('LISTA DE PEDIDOS')
           listar_pedidos()


     elif opc == 3:
            coluna = input('digite o nome da coluna: ')
            novo_valor = input('digite o novo valor do campo: ')
            id_pedido = input_int('Agora digite o numero do seu ID: ')
            atualizar_funcionario(coluna, novo_valor, id_pedido)


     elif opc == 4:
                id_pedido = input("digite o ID do pedido: ")
                remover_funcionario(id_pedido)           



def gerenciamento_sanduiche(lista_sanduiche):
    lista_sanduiche= []

    lista_sanduiche = ['Cadastrar Sanduiche','Listar Sanduiche','Atualizar Sanduiche','Remover Sanduiche']
    cabecalho('Gerenciamento Sanduiche')
    c = 0
    for item in lista_sanduiche:
        print(f'{c+1} - {item}')
        c += 1
    linha()    

    opc = input_int('digite a opção: ')  

    if opc ==1:
            nome_sanduiche = input("Nome do Sanduíche: ")
            valor_sanduiche = float(input("Valor do Sanduíche: "))
            adicionar_sanduiche(nome_sanduiche, valor_sanduiche)


    elif opc== 2:
          cabecalho('LISTA DE SANDUICHES')
          listar_sanduiche()


    elif opc==3:
            coluna = input('digite o nome da coluna: ')
            novo_valor = input('digite o novo valor do campo: ')
            id_sanduiche = input_int('Agora digite o numero do seu ID: ')
            atualizar_sanduiche(coluna, novo_valor, id_sanduiche)


    elif opc==4:
            id_sanduiche = input("Digite o ID do sanduiche: ")
            remover_sanduiche(id_sanduiche) 
    

def gerenciamento_vendas(lista_venda):
    lista_venda = []
    forma_pagamento = ['Credito','Debito','Pix']

    lista_venda = ['Adicionar Pedido','Listar Vendas','Atualizar Venda','Remover Venda']

    cabecalho('Gerenciamento Sanduiche')
    c = 0
    for item in lista_venda:
        print(f'{c+1} - {item}')
        c += 1
    linha()   

    opc = input_int('digite a opção: ') 

    if opc == 1:
           id_venda = input_int('digite o ID do pedido: ')
           valor_venda = float(input('digite o valor da venda: '))
           c = 0
           for p in forma_pagamento:
                print(f'{c+1} - {p}') 
                c +=1
           forma_pagamento = input('digite a forma de pagamento: ')
           adicionar_venda(id_venda,valor_venda,forma_pagamento)


    elif opc == 2:
           listar_venda() 


    elif opc ==3:
            coluna = input('digite o nome da coluna: ')
            novo_valor = input('digite o novo valor do campo: ')
            id_venda = input_int('Agora digite o numero do seu ID: ')
            atualizar_sanduiche(coluna, novo_valor, id_venda)


    elif opc == 4:
            id_venda = input("Digite o ID da Venda: ")
            remover_venda(id_venda) 
           

def menu_up(lista_menu):
    cabecalho('MENU')
    lista_menu = ['Sair','Gerenciamento de Funcionarios','Gerenciamento de Clientes','Gerenciamento de Pedidos','Gerenciamento de Sanduiches','Gerenciamento de Vendas']
    c = 0
    for item in lista_menu:
        print(f'{c} - {item}')
        c += 1
    linha() 


def logar():
       cabecalho('LOGIN')
       email = input('digite seu email: ')
       senha = getpass("Digite sua senha: ")
       autenticado =  login(email, senha)
       return autenticado
