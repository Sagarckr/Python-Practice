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
terminal = db.cursor(buffered=True)

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

# Fetch all students
query = "SELECT name, address FROM Student"
terminal.execute(query)

result = terminal.fetchall()

for row in result:
    print(row)

print("=============================")

# Fetch one student
query = "SELECT * FROM Student WHERE name = %s"
value = ("dhiraj",)

terminal.execute(query, value)

result = terminal.fetchone()
print(result)

print("=============================")

# Update student
query = "UPDATE Student SET address = %s, phone = %s WHERE name = %s"
values = ("sindupalchowk", "9800000000", "dhiraj")

terminal.execute(query, values)
db.commit()

print("Record updated successfully")

print(f"{terminal.rowcount} record(s) updated")
print("=============================")

# Delete student
query = "DELETE FROM Student WHERE name = %s"
value = ("dhiraj",)

terminal.execute(query, value)
db.commit()

print("Record deleted successfully")
print(f"{terminal.rowcount} record(s) deleted")

print("=============================")

terminal.close()
db.close()