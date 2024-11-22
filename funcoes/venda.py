from banco import criar_conexao
from tratamento import cls




def adicionar_venda(id_pedido, valor_venda, forma_pagamento): #  FEITO
    conn = criar_conexao()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO venda (id_pedido, valor_venda, forma_pagamento)
        VALUES (%s, %s, %s)
    """, (id_pedido, valor_venda, forma_pagamento))
    conn.commit()
    print('venda cadastrado com sucesso!')
    cls()
    cur.close()
    conn.close()
    
def listar_venda(): #  FEITO
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("""select nome_cliente , v.valor_venda , v.forma_pagamento 
                    from venda v 
                    join pedido p on p.id_pedido  = v.id_pedido 
                    join clientes c on c.id_cliente = p.id_clientes""")
    
    consulta = cur.fetchall()

    print('')
    for linha in consulta:
        print(linha)
    
    cur.close()
    conn.close()


def atualizar_venda(coluna, novo_valor, id_venda):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""UPDATE venda SET {coluna} = '{novo_valor}' WHERE id_venda =  {id_venda}""")
    conn.commit()
    print('Venda atualizada com sucesso!')
    cls()
    cur.close()
    conn.close()


def remover_venda(id_venda):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""DELETE FROM venda WHERE id_venda = {id_venda} """)
    conn.commit()
    print('Venda removida com sucesso !')
    cls()
    cur.close()
    conn.close()