from block_1.common import (
    MyException
)

class ClassFather:
    _name = 'Father'  
    registered_list = []
    
    @classmethod
    def register(cls):
        if issubclass(cls,ClassFather) and cls != ClassFather:
            ClassFather().registered_list.append(cls)
        else:
            raise MyException()
    
    @classmethod
    def get_name(cls):
        if (cls in ClassFather().registered_list):
            return cls._name
        else:
            raise MyException()
    
    #pass


class User1(ClassFather):
    _name = 'Child1'


class User2(ClassFather):
    _name = 'Child2'
