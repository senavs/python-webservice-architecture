class Singleton:
    def __new__(cls, *args, **kwargs):
        if not (instance := getattr(cls, "__instance", None)):
            instance = super().__new__(cls)
            setattr(cls, "__instance", instance)
        return instance
