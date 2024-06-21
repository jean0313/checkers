
from checks.base import BaseCheck
from registry import check_registry

@check_registry.register('echo')
class EchoCheck(BaseCheck):
    def check(self):
        print('-> Check echo')
        return 0, "ok"