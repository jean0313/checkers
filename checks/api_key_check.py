import socket

import requests
from checks.base import BaseCheck
from registry import check_registry

@check_registry.register('api_key')
class APIKeyCheck(BaseCheck):
    def check(self):
        print(f'-> Check API key: {self.kwargs}')
        url = self.kwargs.get('url')
        key = self.kwargs.get('key')
        method = self.kwargs.get('method')
        headers = {"Authorization": f"Bearer {key}"}
        try:
            with requests.request(method, url, headers=headers) as response:
                if response.status_code == 200:
                    response.close()
                    return 0, "API key is OK"
        except Exception as e:
            print(f'\tAPI check FAIL: {e}')
            return 1, "API check FAIL"