from base import Dependency


class DatabaseDependency(Dependency):
    def __init__(self, item):
        super().__init__(item)
        self.host = item.get('host')
        self.port = item.get('port')
        self.database = item.get('database')
        self.user = item.get('user')
        self.password = item.get('password')

    def check(self):
        raise NotImplementedError("Subclasses should implement this method!")
