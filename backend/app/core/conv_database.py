from app.core.database import get_connection
from datetime import datetime
import sys
print(sys.path)

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

def location_contacts(number):
    conn = get_connection()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        
        query = "SELECT id FROM contacts WHERE number = %s"
        cursor.execute(query, (str(number),)) 
        
        results = cursor.fetchall()
        
        return results 
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
