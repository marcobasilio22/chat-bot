import mysql.connector

config = {
    'user': 'root',
    'password': 'M@rco1234',
    'host': 'localhost',
    'database': 'chatbotalb',
    'raise_on_warnings': True
}

def connection():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(f"Erro de MySQL: {err}")
        return None
    finally:
        cursor.close()
        conn.close()
