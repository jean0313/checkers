
import pymysql
from checks.base import BaseCheck
from registry import check_registry

@check_registry.register('database_mysql')
class MySQLCheck(BaseCheck):
    def check(self):
        print(f'-> Check MySQL: {self.kwargs}')
        host = self.kwargs.get('host')
        port = self.kwargs.get('port')
        database = self.kwargs.get('database')
        user = self.kwargs.get('user')
        password = self.kwargs.get('password')

        connection = None
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            connection.close()
            return 0, 'MySQL Connection Check PASS'
        except pymysql.MySQLError as e:
            print(f'\tCheck MySQL connect FAIL: {e}')
            return 1, f'Check MySQL connect FAIL!'
        finally:
            if connection:
                connection.close()