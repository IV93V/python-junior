from block_1.common import (
    MyException
)

class Coffee:
    def ingr(self,value):
        if value.lower() == 'капучино':
            return 'Кофе: 20 грамм, Вода: 100мл, Молоко: 150мл'
        elif value.lower() == 'латте':
            return 'Кофе: 45 грамм, Сироп: 25мл, Молоко: 150мл'
        elif value.lower() == 'глясе':
            return 'Кофе: 20 грамм, Вода: 180мл, Мороженое: 150мл'
        else: 
            raise MyException
    pass

print(Coffee().ingr('Капучино'));
print(Coffee().ingr('Глясе'));
print(Coffee().ingr('Латте'));
print(Coffee().ingr('Эспрессо'));