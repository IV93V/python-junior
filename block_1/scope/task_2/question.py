"""
Что будет выведено после выполнения кода? Почему?
Ответ:
Будет выведено 
Test message
None
1-я строка выводится потому что текст передается в функцию transmit_to_space. То есть при печати в функции data_transmitter переменная найдется на уровне enlocal
2-я строка не выведет ничего поскольку в функции transmit_to_space отсутствует return
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
