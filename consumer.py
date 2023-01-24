import pika


params = pika.URLParameters('amqps://hsfvjmxb:NnXl1xRXc4nx5YPeGhalfOkCm6S6O0Hx@possum.lmq.cloudamqp.com/hsfvjmxb')
connection = pika.BlockingConnection(params)
channel = connection.channel()

# declare the queue whose routing key will look for
channel.queue_declare(queue='main')

# declare what to do with the meossage
def callback(ch, method, properties, body):
    print('Received in main')
    print(body)
    pass


# declare consume type and start consumming
channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print('Started consuming in main')
channel.start_consuming()

# close connection
channel.close()