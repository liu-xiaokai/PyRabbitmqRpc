"""
client -

Author: genzhengmiaobuhong@163.com
Date: 2024/12/23
"""
from abc import ABC, abstractmethod
import pika
import uuid
import json
import inspect
from PyRabbitmqRpc import get_connection
from PyRabbitmqRpc.conf import Conf


class AbstractClient(ABC):

    @abstractmethod
    def call(self, func_name=None, **kwargs):
        pass

    @abstractmethod
    def cast(self, func_name=None, **kwargs):
        pass


class RpcClient(AbstractClient):
    def __init__(self, conf=Conf):
        self.connection, self.channel = get_connection(conf)
        result = self.channel.queue_declare('', exclusive=True)
        self._queue = result.method.queue
        self.channel.basic_consume(queue=self._queue,
                                   on_message_callback=self.on_response,
                                   auto_ack=True)
        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, func_name=None, **kwargs):
        body = {**kwargs, 'func_name': func_name}
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self._queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   # message需为字符串
                                   body=json.dumps(body))

        while self.response is None:
            self.connection.process_data_events()

        return self.response

    def cast(self, func_name=None, **kwargs):
        body = {**kwargs, 'func_name': func_name}
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self._queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   # message需为字符串
                                   body=json.dumps(body))


