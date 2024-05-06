import sqlite3

con = sqlite3.connect("system.db")

cur = con.cursor()

cur.execute("CREATE TABLE contato(nome, endereco, telefone)")

