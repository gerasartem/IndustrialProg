import pika
import psycopg2

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

db = psycopg2.connect("dbname=postgres user=postgres password=postgres host=task_db port=5432")
cursor = db.cursor()

cursor.execute("DROP TABLE messages")
cursor.execute("CREATE TABLE messages (message TEXT)")
db.commit()

def callback(ch, method, properties, body):
    cur = db.cursor()
    print('Receved message: {}'.format(body.decode()))
    cur.execute("INSERT INTO messages(message) VALUES ('{}')".format(body.decode()))
    db.commit()

channel.basic_consume(callback, queue='task_queue', no_ack=True)
channel.start_consuming()
