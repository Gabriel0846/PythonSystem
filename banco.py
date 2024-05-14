import sqlite3

con = sqlite3.connect("system.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS contato(nome TEXT, endereco TEXT, telefone TEXT)")

con.commit()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

table_names = cur.fetchone()

print(table_names)

cur.close()
con.close()