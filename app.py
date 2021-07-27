DB_HOST = "localhost"
DB_NAME = "newdatabase"
DB_USER = "nedememanka"
DB_PASS = ""


import psycopg2


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


cur = conn.cursor()


# cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")




# cur.execute("INSERT INTO student (name) VALUES(%s)", ("Victoria Secret",))


cur.execute("SELECT * FROM student;")

print(cur.fetchall())
conn.commit()

cur.close()


conn.close()


