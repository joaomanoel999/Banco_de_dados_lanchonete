from banco import criar_conexao
from tratamento import cls



def adicionar_funcionario(nome_funcionario, cpf, email, salario, data_nasc):
    conn = criar_conexao()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO funcionario (nome_funcionario, cpf, email, salario, data_nasc)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome_funcionario, cpf, email, salario, data_nasc))
    conn.commit()
    print('funcionario cadastrado com sucesso!')
    cls()
    cur.close()
    conn.close()


def listar_funcionario():
    conn = criar_conexao() 
    cur = conn.cursor()
    
   
    cur.execute("""SELECT * FROM funcionario
                ORDER BY id_funcionario""")
     
    consulta = cur.fetchall()
  
    print('')
    for linha in consulta:
        print(linha)
    
    cur.close()
    conn.close()

def atualizar_funcionario(coluna, novo_valor, id_funcionario):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""UPDATE funcionario SET {coluna} = '{novo_valor}' WHERE id_funcionario =  {id_funcionario}""")
    conn.commit()
    print('Funcionario atualizado com sucesso!')
    cls()
    cur.close()
    conn.close()

def remover_funcionario(id_funcionario):
    conn = criar_conexao()
    cur = conn.cursor()
    cls()
    cur.execute(f"""DELETE FROM funcionario WHERE id_funcionario = {id_funcionario} """)
    conn.commit()
    print('Funcionario removido com sucesso !')
    cls()
    cur.close()
    conn.close()