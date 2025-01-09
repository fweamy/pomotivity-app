import sqlite3

connection = sqlite3.connect("new.db")

crsr = connection.cursor()
sql_command = """SELECT name FROM sqlite_master WHERE type='table';"""
crsr.execute(sql_command)
print(crsr.fetchall())

connection.commit()

connection.close()