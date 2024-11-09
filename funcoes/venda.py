from banco import criar_conexao
from tratamento import cls
from menu import cabecalho



def adicionar_venda(id_pedido, valor_venda, forma_pagamento):
    conn = criar_conexao()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO clientes (id_pedido, valor_venda, forma_pagamento
        VALUES (%s, %s, %s)
    """, (id_pedido, valor_venda, forma_pagamento))
    conn.commit()
    print('venda cadastrado com sucesso!')
    cls()
    cur.close()
    conn.close()
    
def listar_venda(): 
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("""select nome_cliente , v.valor_venda , v.forma_pagamento 
                    from venda v 
                    join pedido p on p.id_pedido  = v.id_pedido 
                    join clientes c on c.id_cliente = p.id_clientes""")
    
    consulta = cur.fetchall()

    cabecalho('  LISTA DE Vendas  ')
    print('')
    for linha in consulta:
        print(linha)
    
    cur.close()
    conn.close()
    