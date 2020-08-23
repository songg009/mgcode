import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('http://125.62.27.92:5672/cms_host'))
channel = connection.channel()
channel.queue.declare(queue="chongqing_youxian_jufang_assetInfo")
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("[x] Sent 'hello World!'")
