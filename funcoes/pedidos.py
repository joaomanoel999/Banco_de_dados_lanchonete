from banco import criar_conexao
from tratamento import cls


def adicionar_pedido(id_funcionario, id_cliente, id_sanduiche):
    conn = criar_conexao()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO pedido (id_funcionario, id_clientes, id_sanduiche)
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

  
    print('')
    for linha in consulta:
        print(linha)
    
    cur.close()
    conn.close()

def atualizar_pedido(coluna, novo_valor, id_pedido):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""UPDATE pedido SET {coluna} = '{novo_valor}' WHERE id_pedido =  {id_pedido}""")
    conn.commit()
    print('Pedido atualizado com sucesso!')
    cls()
    cur.close()
    conn.close()

def remover_pedido(id_pedido):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""DELETE FROM pedido WHERE id_pedido = {id_pedido} """)
    conn.commit()
    print('Pedido removido com sucesso !')
    cls()
    cur.close()
    conn.close()