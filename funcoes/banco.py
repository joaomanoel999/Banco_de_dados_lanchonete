import psycopg2

def criar_conexao():
    try:

        conn= psycopg2.connect(
            dbname="postgres",
            user="postgres",  
            password="postpost" , 
            host="localhost",
            port="5432"  
        )
      
        return conn
    except Exception as e:
        print(f"erro ao conetar com o banco de dados {e}")
        return None
