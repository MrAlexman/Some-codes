# В этом задании создайте класс банковского счёта, который имеет два атрибута:
#
# owner - владелец
# balance - баланс
# и два метода:
#
# deposit - внести средства
# withdraw - снять средства
# Дополнительное условие - сумма снятия не должна превышать доступный баланс.
#
# Создайте экземпляр класса, сделайте несколько внесений и снятий средств,
# а также проверьте, что баланс счёта не может уходить в минус при снятии средств.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print("Внесение выполнено")
            return 1
        else:
            print("Некорректный ввод")
            return 0

    def withdraw(self, money):
        if self.balance >= money > 0:
            self.balance -= money
            print("Снятие выполнено")
            return 1
        else:
            if money <= 0:
                print("Некорректный ввод")
                return 0
            else:
                print("Недостаточно средств!")
                return 0

    def __str__(self):
        return (f"Владелец счёта: {self.owner}\n"
                f"Баланс счёта: ${self.balance}")


acct1 = Account('Влад', 100)
print(acct1)
acct1.deposit(50)
print(acct1)
acct1.withdraw(75)
print(acct1)
acct1.withdraw(500)
print(acct1)