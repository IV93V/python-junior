class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """
    vals = tuple()
    def __init__(self, *args):
        self.vals = args
        
        
    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        val_count = 0
        for i in range(len(self.vals)):
            if self.vals[i] == value:
                val_count += 1
        return val_count
        raise NotImplementedError

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        for i in range(len(self.vals)):
            if self.vals[i] == value:
                return i
        raise ValueError

    def __getitem__(self, item):
        return self.vals[item]

user_tuple = Tuple(1,2,3,3)
print(user_tuple[0])
print(user_tuple.count(3))
print(user_tuple.index(3))

