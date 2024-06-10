from base import Dependency
import socket


class NetworkDependency(Dependency):
    def __init__(self, item):
        super().__init__(item)
        self.host = item.get('host')
        self.port = item.get('port')

    def check(self) -> int:
        try:
            with socket.create_connection((self.host, self.port), timeout=5):
                print(f"Network check passed for {self.host}:{self.port}")
                return 0
        except Exception as e:
            print(f"Network check failed for {self.host}:{self.port} - {e}")
            return 1
