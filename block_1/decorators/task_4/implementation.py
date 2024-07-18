from block_1.common import (
    specific_func,
    MyException,
)
import time

def decorator_maker(times,delay):
    def decorator(function):
        def wrapper():
            nonlocal times
            while times > 0:
                try:
                    base_result=function()
                    return base_result
                except Exception:
                    times -= 1
                    if (times > 0):
                        time.sleep(delay)
                    else:
                        raise MyException(Exception)
                        
            return base_result
        return wrapper
    return decorator
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    raise NotImplementedError

