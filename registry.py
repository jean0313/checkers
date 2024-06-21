class CheckRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, check_type):
        def inner_wrapper(wrapped_class):
            self._registry[check_type] = wrapped_class
            return wrapped_class
        return inner_wrapper

    def get(self, check_type):
        return self._registry.get(check_type, None)

check_registry = CheckRegistry()