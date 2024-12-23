"""
conf -

Author: genzhengmiaobuhong@163.com
Date: 2024/12/23
"""
from enum import Enum


class Conf(Enum):
    username = 'guest'
    password = 'guest'
    host = 'localhost'
    port = 5672
    virtual_host = '/'
