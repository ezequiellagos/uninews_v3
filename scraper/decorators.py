import logging

def logging_decorator(func=None, *, level=logging.DEBUG, name=None, message=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(name)
            logger.setLevel(level)
            logger.debug(message)
            return func(*args, **kwargs)
        return wrapper

    def __init__(self):
        pass
        # logging.debug('Lanzado')
        # logging.debug('Deteniendo')

