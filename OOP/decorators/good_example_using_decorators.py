"""
Com os decorators as funções param de repetir código
e passam cada uma a ter apenas uma atribuição: pegar a Query
e retornar os valores específico dela vindos do banco de dados
"""


import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='leo',
    password='leo123',
    database='ecommerce',
    port='3306' # default=3306
)

# Montando um decorator
def query(func):
    def run(conn, *args, **kwargs):
        cursor = conn.cursor()
        result = False
        try:
            result = func(cursor, *args, **kwargs)
        except mysql.connector.Error as err:
            print(f'Connection failed: {err}')
        finally:
            cursor.close()
        return result
    
    return run


@query
def find_all(cursor):
    cursor.execute("SELECT * FROM usuario")
    rows = cursor.fetchall()
    return (rows if rows != None else 'Empty table.')

@query
def find_one_by_id(cursor, id):
    cursor.execute("SELECT * FROM usuario WHERE id = %s", (id,))
    row = cursor.fetchone()
    return (row if row != None else 'Invalid ID.')

@query
def find_one_by_name(cursor, nome):
    cursor.execute("SELECT * FROM usuario WHERE nome = %s", (nome,))
    row = cursor.fetchone()
    return (row if row !=None else "There's no user with this name")


print(find_all(conn))
print(find_one_by_id(conn, 1))
print(find_one_by_name(conn, 'leonardo'))
