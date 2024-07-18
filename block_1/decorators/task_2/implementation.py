from block_1.common import (factorial,MyException)


def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper (arg):
        if (isinstance(arg, int)):
            if(arg >= 0):
                base_result = function(arg)
                return base_result
            else:
                raise MyException()
        else:
            raise MyException()
    return wrapper
    raise NotImplementedError


#def res_cache():
    """
    Обертка, которая будет кэшировать результат
    """
#    raise NotImplementedError
    
factorial_checked = check_value(factorial)    
a = (factorial_checked(5))
print (a)