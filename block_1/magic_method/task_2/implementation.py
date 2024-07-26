class MathClock:
    
    def __init__(self):
        self.t = int
        self.h = 0
        self.m = 0
        
    def __add__(self,value):
        self.t = self.h*60 + self.m
        self.m = (self.t+value)%60
        self.h = (self.t+value)//60
        
    def __sub__(self,value):
        self.t = self.h*60 + self.m
        self.m = (self.t-value)%60
        self.h = (self.t-value)//60
        
    def __mul__(self,value):
        self.m = self.m
        self.h = (self.h+value)%24
    
    def __truediv__(self,value):
        self.m = self.m
        self.h = (self.h-value)%24
    def get_time(self):
        return "{:02d}:{:02d}".format(self.h, self.m)


time_obj = MathClock()
time_obj * 9
print(time_obj.get_time())         