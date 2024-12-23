# PyRabbitmqRpc
 ##### This package mainly provides a solution for developers to implement RPC functionality using RabbitMQ.

demo https://github.com/liu-xiaokai/PyRabbitmqRpc/tree/main/demo


``this is a simple example
``

``client.py``
``````
from PyRabbitmqRpc.client import RpcClient
import inspect
from demo.conf import Conf


class MyClient(RpcClient):

    def __init__(self, conf):
        RpcClient.__init__(self, conf)

    def get_sum(self, a=1, b=2, c=3):
        frame = inspect.currentframe()
        function_name = frame.f_code.co_name
        response = self.call(func_name=function_name, a=a, b=b, c=c)
        return response

if __name__ == '__main__':
    api_rpc = MyClient(Conf)
    print(api_rpc.get_sum())

``````
``manager.py``
``````
from PyRabbitmqRpc.manager import ManagerServer
from demo.conf import Conf


class Manager(object):

    def get_sum(self, a=1, b=2, c=3):
        return a + b + c


manager_server = ManagerServer(manager=Manager, conf=Conf)

``````

