from db.configs.connection import get_connection
from datetime import datetime
import sys


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

def store_conversation(customer_id, message, type_message, date_message=None):
    conn = get_connection()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()

        if date_message is None:
            date_message = datetime.now()

        if not isinstance(customer_id, int):
            raise ValueError("customer_id deve ser um inteiro")
        
        query = """
        INSERT INTO conversations (customer_id, message, type_message, date_message)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (customer_id, message, type_message, date_message))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao armazenar conversa: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def last_message():
    conn = get_connection()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        
        query = """
            SELECT c.customer_id, c.message, c.date_message
            FROM conversations c
            INNER JOIN (
                SELECT customer_id, MAX(date_message) as last_message_date
                FROM conversations
                GROUP BY customer_id
            ) as latest ON c.customer_id = latest.customer_id AND c.date_message = latest.last_message_date;
        """
        
        cursor.execute(query,)
        messages = cursor.fetchall()

        result = [{"customer_id": message[0], "message": message[1], "date": message[2]} for message in messages]

        return result

    except Exception as e:
        print(f"Erro ao trazer a ultima mensagem: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
        