from banco import criar_conexao
from tratamento import cls


# Função para adicionar sanduíche com nome e valor
def adicionar_sanduiche(nome_sanduiche, valor_sanduiche):
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO sanduiche (nome_sanduiche, valor_sanduiche)
        VALUES (%s, %s)
    """, (nome_sanduiche, valor_sanduiche))
    conn.commit()
    print('sanduiche cadastrado com sucesso!')
    cls()

    cur.close()
    conn.close()

def listar_sanduiche():
    conn = criar_conexao() 
    cur = conn.cursor()
    
    cur.execute("""SELECT * FROM sanduiche
                ORDER BY id_sanduiche""")
    
    consulta = cur.fetchall()

  
    print('')
    for linha in consulta:
        print(linha)
    
    cur.close()
    conn.close()

def atualizar_sanduiche(coluna, novo_valor, id_sanduiche):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""UPDATE sanduiche SET {coluna} = '{novo_valor}' WHERE id_sanduiche =  {id_sanduiche}""")
    conn.commit()
    print('sanduiche atualizado com sucesso!')
    cls()
    cur.close()
    conn.close()

def remover_sanduiche(id_sanduiche):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""DELETE FROM sanduiche WHERE id_sanduiche = {id_sanduiche} """)
    conn.commit()
    print('Sanduiche removido com sucesso !')
    cls()
    cur.close()
    conn.close()