# Обработайте исключение, которое вызывает код ниже, с помощью блоков try и except.
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Ошибка типов!")