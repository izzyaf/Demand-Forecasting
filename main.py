import psycopg2

# connect to postgresql
connection = psycopg2.connect(database="frepple", user="minhphl", password="qweasd")

# open a cursor to perform db operations
cursor = connection.cursor()

# query
query = "SELECT DATE(DUE), SUM(QUANTITY) FROM DEMAND GROUP BY DUE ORDER BY DUE ASC"
cursor.execute(query)
print(cursor.fetchall())

# close connection
cursor.close()
connection.close()
