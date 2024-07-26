class Multiplier:
    val = int
    def __init__(self,value):
        self.val = value
    
    def __add__(self,obj):
        if (isinstance(obj, Multiplier)):
            return Multiplier(self.val + obj.val)
        else:
            return Multiplier(self.val + obj)
        
    def __sub__(self,obj):    
        if (isinstance(obj, Multiplier)):
            return Multiplier(self.val - obj.val)
        else:
            return Multiplier(self.val - obj)
    
    def __mul__(self,obj):
        if (isinstance(obj, Multiplier)):
            return Multiplier(self.val * obj.val)
        else:
            return Multiplier(self.val * obj)
    
    def __truediv__(self,obj):
        if (isinstance(obj, Multiplier)):
            return Multiplier(self.val / obj.val)
        else:
            return Multiplier(self.val / obj)
        
    def get_value(self):
        return int(self.val)

class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self,value):
       self.val = value*100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self,value):
        self.val = value*1000


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self,value):
        self.val = value*1000000