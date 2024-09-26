from app.core.database import get_connection

def insert_data(name, number):
    conn = get_connection()
    if conn is None:
        print("Erro ao conectar com o banco de dados.")
        return False
    try:
        cursor = conn.cursor()

        query = """
            INSERT INTO contacts(name, number)
            VALUES (%s, %s)
            """
        cursor.execute(query, (name, number))
        conn.commit()
        return True    
    
    except Exception as e:
        print(f"Erro ao gravar cliente: {e}")
        return False
    finally:
        if 'cursor' in locals(): 
            cursor.close()
        conn.close()

