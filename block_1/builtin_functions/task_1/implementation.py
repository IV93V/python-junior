from block_1.common import (MyException)

class Value:
    def __init__(self,val):
        self.value = val
    
    def __add__(self, other):
        try:
            self.value + other
            return self.value + other
        except:
            raise MyException()
    def __sub__(self, other):
        try:
            self.value - other
            return self.value - other
        except:
            raise MyException()
    def __mul__(self, other):
        try:
            self.value * other
            return self.value * other
        except:
            raise MyException()
    def __truediv__(self, other):
        try:
            self.value / other
            return self.value / other
        except:
            raise MyException()

    pass
