from banco import criar_conexao
from tratamento import cls
from menu import cabecalho

def adicionar_pedido(id_funcionario, id_cliente, id_sanduiche):
    conn = criar_conexao()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO clientes (id_funcionario, id_cliente, id_sanduiche 
        VALUES (%s, %s, %s)
    """, (id_funcionario, id_cliente, id_sanduiche))
    conn.commit()
    print('pedido cadastrado com sucesso!')
    cls()
    cur.close()
    conn.close()

def listar_pedidos():
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("""SELECT nome_cliente , id_pedido , s.nome_sanduiche 
                from pedido p 
                join clientes c on id_cliente = p.id_clientes 
                join sanduiche s on s.id_sanduiche = p.id_sanduiche """)
    
    consulta = cur.fetchall()

    cabecalho('  LISTA DE Pedidos  ')
    print('')
    for linha in consulta:
        print(linha)
    
    cur.close()
    conn.close()