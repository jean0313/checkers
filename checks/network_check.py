import socket
from checks.base import BaseCheck
from registry import check_registry

@check_registry.register('network')
class NetworkCheck(BaseCheck):
    def check(self):
        host = self.kwargs.get('host')
        port = self.kwargs.get('port')
        print(f'-> Check network: {host}:{port}')
        try:
            with socket.create_connection((host, port), timeout=5) as sock:
                return 0, "Connected"
        except (socket.timeout, ConnectionRefusedError, socket.gaierror, OSError):
            print(f'Not Connected for {host}:{port}')
            return 1, "Not Connected"