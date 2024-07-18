import time 

def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(arg):
        start_time = time.perf_counter_ns() 
        base_result = function(arg)
        end_time = time.perf_counter_ns()
        print((end_time - start_time)/1000)
        return base_result

    return wrapper    
    
    #raise NotImplementedError



@time_execution
def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

#decor = time_execution(factorial)
print(factorial(200))

