"""
Muito código repetido e funções com mais de uma responsabilidade,
ferindo os princípios de Single Responsibility do SOLID e o DRY.
"""

import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='leo',
    password='leo123',
    database='ecommerce',
    port='3306' # default=3306
)


def find_all():
    query = "SELECT * FROM usuario"
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        print(rows if rows !=None else 'Tabela vazia.')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def find_one_by_id(user_id):
    query = "SELECT * FROM usuario WHERE id = %s"
    try:
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        cursor.close()
        print(row if row != None else print('ID inexistente.'))
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


def find_one_by_name(name):
    query = "SELECT * FROM usuario WHERE nome= %s"
    try:
        cursor = conn.cursor()
        cursor.execute(query, (name,))
        row = cursor.fetchone()
        cursor.close()
        print(row if row != None else print('Usuário não existe no banco de dados.'))
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")


find_all()
find_one_by_id(1)
find_one_by_name('leonardo')
