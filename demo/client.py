
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

