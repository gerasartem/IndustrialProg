import pika
import postgresql as psql

connection = pika.BlockingConnection(pika.ConnectionParametrs(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

db = psql.open('task_db')
db.execute('CREATE TABLE messages (message VARCHAR(256))')

def callback(ch, method, properties, body):
    db.execute('INSER INTO messages (message) VALUES ({})'.format(body))

channel.basic_consume(callback, queue='task_queue', no_ack=True)
channel.start_consuming()
