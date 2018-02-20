import postgresql as psql

db = psql.open('pq://postgres:postgres@localhost:5432')
for message in db.execute('SELECT * FROM messages'):
    print(message[0])


