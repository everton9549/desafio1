import tagui as t
import os
from datetime import date
import sqlite3

t.init()

#pegando o dia para o print
h = date.today()
data = h.strftime("%d_%m_%Y")

#Abrindo url e pegando valores na pagina
t.url('https://www.mercadolivre.com.br/smart-tv-philco-ptv55q20snbl-dled-4k-55/p/MLB15591953?source=search#searchVariation=MLB15591953&position=3&type=product&tracking_id=7e70dc55-73cc-4d3b-a4a9-c47b7e99812f')
valor = t.read('price-tag-fraction')
n = str(t.read('ui-pdp-title'))
nome = n[0:14]

#Tirando print da pagina
t.snap('page', 'results.jpg')

#Movendo print para pasta files e mudando nome
titulo = nome + "_" + data
os.rename('results.jpg', 'files/' + titulo + '.jpg')

#Criando database
conn = sqlite3.connect("precoproduto.db")
cursor = conn.cursor()

#Criando tabela
cursor.execute("""CREATE TABLE preco
            (nomeproduto text, valorproduto text)
            """)

#inserindo valores da pagina na tabela
cursor.execute("INSERT INTO preco VALUES(?,?)", (nome, valor))
#conn.commit()
sql = "SELECT * FROM preco"
cursor.execute(sql)
conn.commit()

#Clicando na loja, tirando print e movendo para pasta files
t.click('ui-pdp-action-modal ui-pdp-seller__link-trigger')
t.snap('page', 'results1.jpg')
os.rename('results1.jpg', 'files/print_de_teste.jpg')