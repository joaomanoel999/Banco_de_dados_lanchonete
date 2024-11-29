from banco import criar_conexao
from seguranca import checar_password, criotpgrafar
from usuarios import login
from getpass import getpass
from funcionario import adicionar_funcionario, listar_funcionario, atualizar_funcionario, remover_funcionario
from clientes import adicionar_cliente,buscar_cliente, listar_clientes, atualizar_clientes, lista_pedidos_cliente, remover_cliente
from sanduiche import adicionar_sanduiche, listar_sanduiche, atualizar_sanduiche, remover_sanduiche
from pedidos import adicionar_pedido, listar_pedidos,atualizar_pedido,remover_pedido
from venda import adicionar_venda, listar_venda,atualizar_venda, remover_venda
from tratamento import input_int, cls


def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())



              

def gerenciamento_clientes(lista_cliente):
     
     lista_menu = []
     lista_cliente = []
     lista_cliente = ['Menu Principal','Cadastrar Clientes','Listar Clientes','Buscar Cliente','Atualizar  Clientes','Remover Cliente']
     cabecalho('Gerenciamento Clientes')
     c = 0
     for item in lista_cliente:
        print(f'{c} - {item}')
        c += 1
     linha()

     opc = input_int('digite a opção: ')

     if opc == 0:
                    print('carregando...')
                    cls()
                    menu_up(lista_menu)

     elif opc ==1:
                    print('carregando...')
                    cls()
                    nome_cliente = input("Nome do Cliente: ")
                    telefone = input("Telefone do Cliente: ")
                    endereco = input("Endereço do Cliente: ")
                    adicionar_cliente(nome_cliente, telefone, endereco)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Clientes')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_clientes(lista_cliente)
                     
     elif opc ==2:
                    print('carregando...')
                    cls()
                    cabecalho('LISTA DE CLIENTES')
                    listar_clientes()

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Clientes')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_clientes(lista_cliente)
     elif opc == 3:
                    print('carregando...')
                    cls()
                    nome = input('digite as iniciais do nome desejado: ')
                    buscar_cliente(nome)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Clientes')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_clientes(lista_cliente)


     elif opc == 4:
                    print('carregando...')
                    cls()
                    coluna = input('digite o nome da coluna: ')
                    novo_valor = input('digite o novo valor do campo: ')
                    id_cliente = input_int('Agora digite o numero do seu ID: ')
                    atualizar_clientes(coluna,novo_valor,id_cliente)
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Clientes')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_clientes(lista_cliente)



     elif opc == 5:
                    print('carregando...')
                    cls()
                    id_cliente = input('digite o ID do cliente para remover: ')
                    remover_cliente(id_cliente)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Clientes')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_clientes(lista_cliente)



     else:
             print('Opção invalida! Tente novamente')
             cls()
             gerenciamento_clientes(lista_cliente)
           


def gerenciamento_funcionarios(lista_funcionario):
    lista_menu = []
    lista_funcionario = []
    lista_funcionario = ['Menu Principal','Cadastrar Funcionario','Listar Funcionarios','Atualizar  Funcioario','Remover Funcionario']
    cabecalho('Gerenciamento Funcionario')
    c = 0
    for item in lista_funcionario:
        print(f'{c} - {item}')
        c += 1
    linha() 

    opc = input_int('digite a opção: ')

    if opc == 0:
                    print('carregando...')
                    cls()
                    menu_up(lista_menu)


    elif opc == 1:
                    print('carregando...')
                    cls()
                    nome_funcionario = input("Nome do Funcionário: ")
                    cpf = input("CPF do Funcionário: ")
                    email = input("Email do Funcionário: ")
                    salario = int(input("Salário do Funcionário: "))
                    data_nasc = input("Data de Nascimento (YYYY-MM-DD): ")
                    adicionar_funcionario(nome_funcionario, cpf, email, salario, data_nasc)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Funcionarios')

                    escolha = input_int('digite a opção: ')
                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_funcionarios(lista_funcionario)


    elif opc == 2:
                    print('carregando...')
                    cls()
                    cabecalho('LISTA DE FUNCIONARIOS')
                    listar_funcionario()
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Funcionarios')

                    escolha = input_int('digite a opção: ')
                    if escolha == 1:
                                print('carregando...')
                                cls()
                                menu_up(lista_menu)
                    elif escolha ==2:
                                print('carregando...')
                                cls()
                                gerenciamento_funcionarios(lista_funcionario)         


    elif opc ==3:
                    print('carregando...')
                    cls()
                    coluna = input('digite o nome da coluna: ')
                    novo_valor = input('digite o novo valor do campo: ')
                    id_funcionario = input_int('Agora digite o numero do seu ID: ')
                    atualizar_funcionario(coluna, novo_valor, id_funcionario)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Funcionarios')

                    escolha = input_int('digite a opção: ')
                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_funcionarios(lista_funcionario)


    elif opc == 4:
                    print('carregando...')
                    cls()
                    id_funcionario = input("digite o ID do funcionario: ")
                    remover_funcionario(id_funcionario)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Funcionarios')

                    escolha = input_int('digite a opção: ')
                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_funcionarios(lista_funcionario)

    else:
                    print('Opção invalida! Tente novamente')
                    cls()
                    gerenciamento_funcionarios(lista_funcionario)



def gerenciamento_pedidos(lista_pedido):
     lista_menu = []
     lista_pedido = []
     lista_pedido = ['Menu Principal','Adicionar Pedidos','Listar Pedidos','Atualizar Pedido','Remover Pedido']
     cabecalho('Gerenciamento Pedidos')
     c = 0
     for item in lista_pedido:
        print(f'{c} - {item}')
        c += 1
     linha() 

     opc = input_int('digite a opção: ')  

     if opc == 0:
                    print('carregando...')
                    cls()
                    menu_up(lista_menu)

     elif opc == 1:
                    print('carregando...')
                    cls()
                    id_funcionario = input_int('Digite o ID do Funcionario: ')
                    id_cliente = input_int('digite o ID do Cliente:')
                    id_sanduiche = input_int('digite o ID do sanduiche: ')
                    adicionar_pedido(id_funcionario, id_cliente, id_sanduiche)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Pedidos')

                    escolha = input_int('digite a opção: ')
                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_pedidos(lista_pedido)


     elif opc== 2:
                    print('carregando...')
                    cls()
                    cabecalho('LISTA DE PEDIDOS')
                    listar_pedidos()
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Pedidos')

                    escolha = input_int('digite a opção: ')
                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_pedidos(lista_pedido)


     elif opc == 3:
                    print('carregando...')
                    cls()
                    coluna = input('digite o nome da coluna: ')
                    novo_valor = input('digite o novo valor do campo: ')
                    id_pedido = input_int('Agora digite o numero do seu ID: ')
                    atualizar_pedido(coluna, novo_valor, id_pedido)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Pedidos')

                    escolha = input_int('digite a opção: ')
                    if escolha == 1:
                        print('carregando...')
                        cls()
                        menu_up(lista_menu)
                    elif escolha ==2:
                        print('carregando...')
                        cls()
                        gerenciamento_pedidos(lista_pedido)

       

     elif opc == 4:
                    print('carregando...')
                    cls()
                    id_pedido = input("digite o ID do pedido: ")
                    remover_pedido(id_pedido)  

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Pedidos')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_pedidos(lista_pedido)  

     else:
                    print('Opção invalida! Tente novamente')
                    cls()
                    gerenciamento_pedidos(lista_pedido)       



def gerenciamento_sanduiche(lista_sanduiche):
    
    lista_sanduiche= []
    lista_menu = []

    lista_sanduiche = ['Menu Principal','Cadastrar Sanduiche','Listar Sanduiche','Atualizar Sanduiche','Remover Sanduiche']
    cabecalho('Gerenciamento Sanduiche')
    c = 0
    for item in lista_sanduiche:
        print(f'{c} - {item}')
        c += 1
    linha()    

    opc = input_int('digite a opção: ')  

    if opc == 0:
                    print('carregando...')
                    cls()
                    menu_up(lista_menu)

    elif opc == 1:
                    print('carregando...')
                    cls()
                    nome_sanduiche = input("Nome do Sanduíche: ")
                    valor_sanduiche = float(input("Valor do Sanduíche: "))
                    adicionar_sanduiche(nome_sanduiche, valor_sanduiche)
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Sanduiches')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_sanduiche(lista_sanduiche)


    elif opc== 2:
                    print('carregando...')
                    cls()
                    cabecalho('LISTA DE SANDUICHES')
                    listar_sanduiche()

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Sanduiches')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_sanduiche(lista_sanduiche)


    elif opc==3:
                    print('carregando...')
                    cls()
                    coluna = input('digite o nome da coluna: ')
                    novo_valor = input('digite o novo valor do campo: ')
                    id_sanduiche = input_int('Agora digite o numero do seu ID: ')
                    atualizar_sanduiche(coluna, novo_valor, id_sanduiche)

                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Sanduiches')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_sanduiche(lista_sanduiche)


    elif opc==4:
                    print('carregando...')
                    cls()
                    id_sanduiche = input("Digite o ID do sanduiche: ")
                    remover_sanduiche(id_sanduiche)
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Sanduiches')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_sanduiche(lista_sanduiche)
        
    else:
            print('Opção invalida! Tente novamente')
            cls()
            gerenciamento_sanduiche(lista_sanduiche)
    

def gerenciamento_vendas(lista_venda):
    lista_menu = []
    lista_venda = []
    forma_pagamento = ['Credito','Debito','Pix']

    lista_venda = ['Menu Principal','Adicionar Venda','Listar Vendas','Atualizar Venda','Remover Venda']

    cabecalho('Gerenciamento de Vendas')
    c = 0
    for item in lista_venda:
        print(f'{c} - {item}')
        c += 1
    linha()   

    opc = input_int('digite a opção: ') 

    if opc == 0:
                    print('carregando...')
                    cls()
                    menu_up(lista_menu)

    elif opc == 1:
                    print('carregando...')
                    cls()
                    id_venda = input_int('digite o ID do pedido: ')
                    valor_venda = float(input('digite o valor da venda: '))
                    c = 0
                    for p in forma_pagamento:
                            print(f'{c+1} - {p}') 
                            c +=1
                    forma_pagamento = input('digite o nome da forma de pagamento: ')
                    adicionar_venda(id_venda,valor_venda,forma_pagamento)
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Vendas')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_vendas(lista_venda)


    elif opc == 2:  
                    print('carregando...')
                    cls()
                    cabecalho('LISTA DE VENDAS')
                    listar_venda()
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Vendas')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_vendas(lista_venda) 


    elif opc ==3:
                    print('carregando...')
                    cls()
                    coluna = input('digite o nome da coluna: ')
                    novo_valor = input('digite o novo valor do campo: ')
                    id_venda = input_int('Agora digite o numero do seu ID: ')
                    atualizar_venda(coluna, novo_valor, id_venda)
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Vendas')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_vendas(lista_venda)


    elif opc == 4:
                    print('carregando...')
                    cls()
                    id_venda = input("Digite o ID da Venda: ")
                    remover_venda(id_venda) 
                    print('')
                    print('')
                    print('1- Ir para Menu Principal')
                    print('2- Ir para Gerenciamento de Vendas')

                    escolha = input_int('digite a opção: ')

                    if escolha == 1:
                            print('carregando...')
                            cls()
                            menu_up(lista_menu)
                    elif escolha ==2:
                            print('carregando...')
                            cls()
                            gerenciamento_vendas(lista_venda)

    else:
            print('Opção invalida! Tente novamente')
            cls()
            gerenciamento_vendas(lista_venda) 
           

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
