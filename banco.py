import sqlite3

con = sqlite3.connect("system.bd")

cur = con.cursor()

cur.execute("CREATE TABLE contato(nome, endereco, telefone)")

