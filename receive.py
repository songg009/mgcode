import pika

#创建链接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='http://125.62.27.92:5672/cms_host'))

#建立通道
channel = connection.channel()

#回调函数
def callback(ch,method,properties,body):
    print("[x] Received {}".format(body))

#绑定消息
'''
告诉RabbitMQ这个回调函数（callback）将会从名为"hello"的队列中接收消息
auto_ack=True：如果设置为真，将使用自动确认模式。
'''
channel.basic_consume(on_message_callback=callback,
                      queue='chongqing_youxian_jufang_assetInfo',
                      auto_ack=True
                      )

print('[*] Waiting for messages. To exit press CTRL+C')

#我们运行一个用来等待消息数据并且在需要的时候运行回调函数的无限循环
channel.start_consuming()
