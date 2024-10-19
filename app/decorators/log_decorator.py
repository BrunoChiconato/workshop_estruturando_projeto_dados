from loguru import logger # type: ignore
from functools import wraps

logger.remove()

logger.add('../app.log', colorize=True, format="{time:DD/MM/YYYY HH:mm:ss} {message} {level}", level="INFO")

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Executando a função {func.__name__}.')
        try:
            result = func(*args, **kwargs)
            logger.info(f'A função {func.__name__} finalizou com sucesso.')
            return result
        except Exception as e:
            logger.error(f'A função {func.__name__} falhou com a exceção: {e}')
            raise
    return wrapper