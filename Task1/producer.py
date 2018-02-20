import pika

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()
channel.queue_declare(queue='task_queue')

print('Write your message. To exit type "exit".')
while True:
    message = input()

    if message == 'exit':
        print('Recived an exit command.')
        break

    channel.basic_publish(exchange='',
        routing_key='task_queue',
        body=message)

channel.close()

