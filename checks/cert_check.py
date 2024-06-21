import ssl
import os
from datetime import datetime
from checks.base import BaseCheck
from registry import check_registry

@check_registry.register('cert')
class CertCheck(BaseCheck):
    def check(self):
        cert_path = self.kwargs.get('path')
        print(f'-> Check cert: {cert_path}')
        if not os.path.isfile(cert_path):
            return f"Certificate file {cert_path} does not exist."
        
        try:
            cert = ssl._ssl._test_decode_cert(cert_path)
            expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            now = datetime.utcnow()
            expired = now > expiry_date
            return 0, f"Expires on {expiry_date} (Expired: {expired})"
        except Exception as e:
            return 1, f"Failed to check certificate expiry: {e}"
