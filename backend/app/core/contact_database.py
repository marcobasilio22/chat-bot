from app.core.database import get_connection

def resgister_contact(name, number):
    conn = get_connection()
    if conn is None:
        print("Erro ao conectar com o banco de dados.")
        return False
    try:
        validation = """
        SELECT name FROM contacts;
        """
        if name in validation == False:
            cursor = conn.cursor()
            query = """
            INSERT INTO contacts (name, number, creation_date)
            VALUES (%s, %s, NOW())
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


