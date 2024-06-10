from database import DatabaseDependency
import psycopg2

class PostgreSQLDependency(DatabaseDependency):
    def check(self) -> int:
        try:
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.database,
                user=self.user,
                password=self.password
            )
            print(f"PostgreSQL connection successful to {self.database}@{self.host}:{self.port}")
            connection.close()
        except Exception as e:
            print(f"PostgreSQL check failed for {self.database}@{self.host}:{self.port} - {e}")
