from banco import criar_conexao
from tratamento import cls


# Função para adicionar cliente com nome, telefone e endereço
def adicionar_cliente(nome_cliente, telefone, endereco):
    conn = criar_conexao()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO clientes (nome_cliente, telefone, endereco)
        VALUES (%s, %s, %s)
    """, (nome_cliente, telefone, endereco))
    conn.commit()
    print('cliente cadastrado com sucesso!')
    cls()
    cur.close()
    conn.close()


def listar_clientes():
    conn = criar_conexao() 
    cur = conn.cursor()
    
    cur.execute("""SELECT * FROM clientes
                ORDER BY id_cliente""")
    
    consulta = cur.fetchall()
  
    print('')
    for linha in consulta:
        
        print(linha)
    
    cur.close()
    conn.close()

def atualizar_clientes(coluna, novo_valor, id_cliente):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""UPDATE clientes SET {coluna} = '{novo_valor}' WHERE id_cliente =  {id_cliente}""")
    conn.commit()
    print('cliente atualizado com sucesso!')
    cls()
    cur.close()
    conn.close()
    
def lista_pedidos_cliente(nome_cliente):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""select nome_cliente , id_pedido 
                from pedido p 
                inner join clientes c on p.id_clientes = c.id_cliente
                 WHERE nome_cliente = '{nome_cliente}' """)
    consulta = cur.fetchall()

    for c in consulta:
        print(c)
    
    cur.close()
    conn.close()

def remover_cliente(id_cliente):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""DELETE FROM clientes WHERE id_cliente = {id_cliente} """)
    conn.commit()
    print('Cliente removido com sucesso !')
    cls()
    cur.close()
    conn.close()
