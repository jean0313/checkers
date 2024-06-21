
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

        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            connection.close()
            print('MySQL connection OK')
            return 0, 'MySQL Connection OK'
        except pymysql.MySQLError as e:
            print(f'MySQL connect error{self.kwargs}, message:{e}')
            return 1, f'MySQL connect error!{self.kwargs}'