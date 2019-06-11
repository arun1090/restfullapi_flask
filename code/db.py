import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_query = "CREATE TABLE IF NOT EXISTS item (name text , price int)"
cursor.execute(create_query)
print('Db created ')

item =('pen', 10.00)
query = "INSERT INTO item values(?, ?)"
cursor.execute(query, item)
print('db inserted')
connection.commit()
connection.close()


