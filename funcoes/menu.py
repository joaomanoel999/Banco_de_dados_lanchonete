

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    lista = ['sair','Cadastrar Funcionario','Cadastrar Clientes','Cadastrar Sanduiche','Adicionar Pedidos','Adicionar Venda','Listar Funcionario',
             'Listar Clientes','Listar Sanduiches','Listar Pedidos','Listar Venda','Atualizar  Clientes','Atualizar  Funcioario','Atualizar Sanduiche',
             'listar pedidos por cliente','Remover Cliente','Remover Funcionario','Remover Sanduiche']
    cabecalho('MENU PRINCIPAL')
    c = 0
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
