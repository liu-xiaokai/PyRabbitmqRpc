"""
manager -

Author: genzhengmiaobuhong@163.com
Date: 2024/12/23
"""
import pika
import json
from PyRabbitmqRpc import get_connection
from PyRabbitmqRpc.conf import Conf


class ManagerServer(object):

    def __init__(self, manager, conf=Conf):
        self.connection, self.channel = get_connection(conf)
        self.channel.queue_declare(queue='rpc_queue')
        self.channel.basic_consume('rpc_queue',
                                   on_message_callback=self.on_request)
        self.manager = manager()
        self.channel.start_consuming()

    def on_request(self, ch, method, props, body):
        body_dict = json.loads(body)
        func_name = body_dict.pop('func_name')

        if hasattr(self.manager, func_name):
            response = getattr(self.manager, func_name)(**body_dict)
        else:
            response = 'function not found'

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         # message需为字符串
                         body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
