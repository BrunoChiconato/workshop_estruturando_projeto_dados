from loguru import logger # type: ignore
from functools import wraps

logger.remove()

logger.add('../app.log', colorize=True, format="{time:DD/MM/YYYY HH:mm:ss} {message} {level}", level="INFO")

def log_decorator(func):
    """
    Decorador para adicionar logs de execução a uma função.

    Este decorador registra automaticamente mensagens de log antes e depois
    da execução de uma função, além de capturar e registrar quaisquer 
    exceções que possam ocorrer durante a execução da função. As mensagens
    de log são gravadas em um arquivo especificado no formato configurado.

    Parameters:
    -----------
    func : callable
        A função que será decorada.

    Returns:
    --------
    callable
        A função decorada com o comportamento de logging.

    Raises:
    -------
    Exception
        Relança qualquer exceção que seja capturada durante a execução da função,
        permitindo que ela seja tratada em um nível superior.
    """
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