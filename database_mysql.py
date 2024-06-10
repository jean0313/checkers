from database import DatabaseDependency
import mysql.connector

class MySQLDependency(DatabaseDependency):
    def check(self) -> int:
        try:
            connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                print(f"MySQL connection successful to {self.database}@{self.host}:{self.port}")
                connection.close()
        except Exception as e:
            print(f"MySQL check failed for {self.database}@{self.host}:{self.port} - {e}")
