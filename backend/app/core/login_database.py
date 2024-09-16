from app.core.database import get_connection

def fetch_all_conversations():
    conn = get_connection()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM conversations")
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Erro ao buscar conversas: {e}")
        return None
    finally:
        cursor.close()
        conn.close()