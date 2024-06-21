class BaseCheck:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def check(self):
        raise NotImplementedError("Check method must be implemented.")
