import pika
import json

from main import Product, db

params = pika.URLParameters('amqps://hsfvjmxb:NnXl1xRXc4nx5YPeGhalfOkCm6S6O0Hx@possum.lmq.cloudamqp.com/hsfvjmxb')
connection = pika.BlockingConnection(params)
channel = connection.channel()

# declare the queue whose routing key will look for
channel.queue_declare(queue='main')

# declare what to do with the meossage
def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)


    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('product updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('product deleted')
  
   


# declare consume type and start consumming
channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print('Started consuming in main')
channel.start_consuming()

# close connection
channel.close()