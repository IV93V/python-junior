class FileRows():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        lines = len(self.file.readlines())
        print('Кол-во строк - ', lines)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        
with FileRows('log.txt','r') as f:
    print('Тест')