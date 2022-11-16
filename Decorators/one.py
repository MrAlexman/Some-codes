def new_decorator(main_func):
    def inside_func():
        print("I`ve printed!")
        main_func()
        print("I`ve also printed!")

    return inside_func


@new_decorator
def test():
    print("I`m the main func!")


test()
