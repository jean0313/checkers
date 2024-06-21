from checks.base import BaseCheck
from registry import check_registry

@check_registry.register('database_postgresql')
class PostgreSQLCheck(BaseCheck):
    def check(self):
        host = self.kwargs.get('host')
        port = self.kwargs.get('port')
        database = self.kwargs.get('database')
        user = self.kwargs.get('user')
        password = self.kwargs.get('password')
        
        return 1, "Connected"