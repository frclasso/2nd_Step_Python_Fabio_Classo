import postgres

conn = postgres.make_Connection('dbname=mydb, user=fabio')

cur = conn.cursor()

cur.execute("CREATE TABLE person (id serial PRIMARY KEY, name text, age integer);")

cur.execute("INSERT INTO person (name, age) VALUES (%s, %s) ", ("O'Reilly", 60))

conn.commit()

cur.execute("SELECT * FROM person;")
cur.fetchall()

cur.close()
conn.close()