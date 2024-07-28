def fib(n):
    s1=1
    yield s1
    
    s2=1
    yield s2
    
    for i in (range(2,n)):
        r = s1+s2
        yield r
        s1 = s2
        s2 = r