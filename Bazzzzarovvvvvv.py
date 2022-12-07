if __name__ == "__main__":
    a = []
    flag = 1
    N = int(input("Введите количество столбцов"))
    M = int(input("Введите количество строк"))
    print("Заполните массив построчно")
    for i in range(N):
        temp = []
        for j in range(M):
            temp.append(float(input("Введите число")))
        a.append(temp)
    for k, v in enumerate(a[0]):
        for j in range(1, M):
            if a[j][k] > v:
                flag = 0
    if flag == 0:
        print("Не верно")
    else:
        print("Верно")

