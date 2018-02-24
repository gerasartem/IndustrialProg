import psycopg2

db = psycopg2.connect("dbname=postgres user=postgres password=postgres host=task_db port=5432")
cur = db.cursor()
cur.execute("""SELECT * from messages""")
rows = cur.fetchall()
for message in rows:
    print(message[0])


