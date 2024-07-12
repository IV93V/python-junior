"""
Что будет выведено после выполнения кода? Почему?
Ответ:
Будет выведено
3
3
1-я строка выведет 3 поскольку внутри функции printer переменной number присваивается значение 3
2-я строка выведет 3 поскольку внутри функции printer директива nonlocal переопределяет значение переменной в ближайшей зоне видимости (т.е. в enlocal)
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)
