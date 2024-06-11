from base import Dependency
import ssl
from datetime import datetime



def check_ssl_cert_file_expiry(cert_file_path: str) -> bool:
    x509 = ssl._ssl._test_decode_cert(cert_file_path)
    expiry_date_str = x509['notAfter']
    expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
    current_date = datetime.utcnow()
    return current_date > expiry_date
    
class CertDependency(Dependency):
    def __init__(self, item):
        super().__init__(item)
        self.path = item.get('path')

    def check(self) -> int:
        print(f"check cert")
        try:
            if check_ssl_cert_file_expiry(self.path):
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Cert check failed for {self.path} - {e}")
            return 2
