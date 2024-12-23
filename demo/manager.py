from PyRabbitmqRpc.manager import ManagerServer
from demo.conf import Conf

class Manager(object):

    def get_sum(self, a=1, b=2, c=3):
        return a + b + c


if __name__ == '__main__':
    manager_server = ManagerServer(manager=Manager, conf=Conf)