# Обработайте исключение, которое вызывает код ниже, с помощью блоков try и except.
# Затем используйте блок finally, чтобы сказать, что всё сделано.
x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("Деление на ноль!")
finally:
    print("Выполнение завершено!")
