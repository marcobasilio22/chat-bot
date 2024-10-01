from app.core.database import get_connection

def show_contacts():
    conn = get_connection()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        
        query = """
            SELECT id, name, number, creation_date FROM contacts
        """
        
        cursor.execute(query,)
        contacts = cursor.fetchall()

        result = [{"id": contact[0], "name": contact[1], "number": contact[2], "creation_date": contact[3]} for contact in contacts]

        return result

    except Exception as e:
        print(f"Erro ao trazer contatos: {e}")
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
        
def rename_contact_to_number(number: str, new_name: str):
    conn = get_connection()
    if conn is None:
        return {"error": "Could not establish a database connection."}

    try:
        cursor = conn.cursor()
        
        query = """
            UPDATE contacts
            SET name = %s
            WHERE number = %s;
        """
        cursor.execute(query, (new_name, number)) 
        conn.commit()

        return {"message": f"Contato renomeado para {new_name}"}

    except Exception as e:
        print(f"Erro ao renomear contato: {e}")
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()

def get_customer_id_by_number(number: str):
    conn = get_connection()
    if conn is None:
        return {"error": "Could not establish a database connection."}

    try:
        cursor = conn.cursor()
        
        query = """
            SELECT id FROM contacts
            WHERE number = %s;
        """
        cursor.execute(query, (number,))
        result = cursor.fetchone()

        if result:
            return result[0]  
        else:
            return {"error": "Contato não encontrado."}

    except Exception as e:
        print(f"Erro ao buscar customer_id: {e}")
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()


def delete_messages_by_number(number: str):
    customer_id_response = get_customer_id_by_number(number)

    if isinstance(customer_id_response, dict) and "error" in customer_id_response:
        return customer_id_response 
    
    customer_id = customer_id_response  

    conn = get_connection()
    if conn is None:
        return {"error": "Could not establish a database connection."}

    try:
        cursor = conn.cursor()
        
        query = """
            DELETE FROM conversations
            WHERE customer_id = %s;
        """
        cursor.execute(query, (customer_id,))
        conn.commit()

        return {"message": f"Todas as mensagens do contato {number} foram apagadas."}

    except Exception as e:
        print(f"Erro ao apagar mensagens: {e}")
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()

def delete_contact_and_messages(number: str):
    customer_id_response = get_customer_id_by_number(number)

    if isinstance(customer_id_response, dict) and "error" in customer_id_response:
        return customer_id_response 

    customer_id = customer_id_response  

    conn = get_connection()
    if conn is None:
        return {"error": "Could not establish a database connection."}

    try:
        cursor = conn.cursor()

        delete_messages_query = """
            DELETE FROM conversations
            WHERE customer_id = %s;
        """
        cursor.execute(delete_messages_query, (customer_id,))

        delete_contact_query = """
            DELETE FROM contacts
            WHERE number = %s;
        """
        cursor.execute(delete_contact_query, (number,))

        conn.commit()

        return {"message": f"Contato {number} e todas as mensagens foram apagadas."}

    except Exception as e:
        print(f"Erro ao apagar contato e mensagens: {e}")
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()

