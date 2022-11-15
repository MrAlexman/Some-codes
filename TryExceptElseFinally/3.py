# Напишите функцию, которая спрашивает пользователя ввести число, и затем выводит это число в квадрате.
# Используйте цикл while и блоки try, except и else для обработки некорректно введённых данных.

def ask():
    while True:
        try:
            a = float(input("Введите число: "))

        except TypeError:
            print("Вы ввели не число!")
            continue
        else:
            print("Спасибо за число!")
            return round(a ** 2, 4)
        finally:
            print("Функция завершена!")


if __name__ == "__main__":
    print(ask())