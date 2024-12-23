"""
__init__ -

Author: genzhengmiaobuhong@163.com
Date: 2024/12/23
"""
import pika

def get_connection(conf):
    credentials = pika.PlainCredentials(conf.username.value, conf.password.value)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=conf.host.value,
                                                                   port=conf.port.value,
                                                                   virtual_host=conf.virtual_host.value,
                                                                   credentials=credentials))

    channel = connection.channel()

    return connection, channel
