
from checks.base import BaseCheck
from registry import check_registry

@check_registry.register('database_mysql')
class MySQLCheck(BaseCheck):
    def check(self):
        print('check mysql')
        return 0, "Connected"