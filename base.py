class Dependency:
    def __init__(self, item):
        self.type = item.get('type')

    def check(self) -> int:
        raise NotImplementedError("Subclasses should implement this method!")
