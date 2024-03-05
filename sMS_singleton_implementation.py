class Singleton(object):
    _instances = {}

    # safe the reference to the instance when it is called first time
    # if the instance is called again return the first reference
    def __new__(cls, *args, **kwargs) -> object:
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
