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
            return 1, f"Cert Check FAIL: Certificate file {cert_path} not found"
        
        try:
            cert = ssl._ssl._test_decode_cert(cert_path)
            expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            now = datetime.utcnow()
            expired = now > expiry_date
            if not expired:
                return 0, "Cert Check PASS"
            return 1, f"Cert Check FAIL: cert expires on {expiry_date}"
        except Exception as e:
            print("\tCert Check FAIL")
            return 1, f"Cert Check FAIL: {e}"
