# mysql

import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    port = 3306,
    database = "python-practice"
)

print("Connected")
print(db)

print("=============================")

# # for running sql query
terminal = db.cursor()
# insert = "INSERT INTO Student (name, address, phone) VALUES ('John', 'Kathmandu', '9812345676')"
# terminal.execute(insert)
# db.commit()


# # Always use parameterized queries to avoid SQL injection and errors:
# terminal = db.cursor()

# insert = "INSERT INTO Student (name, address, phone) VALUES (%s, %s, %s)"
# values = ('dhiraj', 'tanahun', '98876543565')

# terminal.execute(insert, values)
# db.commit()
# print("data inserted")

# query = "SELECT * FROM Student"
# terminal.execute(query)

# result = terminal.fetchall()

# for row in result:
#     print(row)

query = "SELECT name, address FROM Student"
terminal.execute(query)

result = terminal.fetchall()

for row in result:
    print(row)

print("=============================")