import sqlite3
import os

#criando pasta files
os.makedirs('files')

#Criando database
conn = sqlite3.connect("precoproduto.db")
cursor = conn.cursor()

#Criando tabela
cursor.execute("""CREATE TABLE preco
            (nomeproduto text, valorproduto text)
            """)
