class BankAccount:
    account_counter = 1000

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0
        self.account_number = BankAccount.account_counter

        # История операций
        self.history = []

        BankAccount.account_counter += 1

        self.history.append("Счет создан")

    # Пополнение
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        if amount > 50000:
            print("Максимальная сумма пополнения 50000")
            return

        self.balance += amount

        operation = f"Пополнение на {amount}"
        self.history.append(operation)

        print(f"{operation}. Баланс: {self.balance}")

    # Снятие
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        if amount > 50000:
            print("Максимальная сумма снятия 50000")
            return

        if amount > self.balance:
            print("Недостаточно средств")
            return

        self.balance -= amount

        operation = f"Снятие {amount}"
        self.history.append(operation)

        print(f"{operation}. Баланс: {self.balance}")

    # Показать баланс
    def show_balance(self):
        print(f"Баланс: {self.balance}")

    # Информация
    def show_info(self):
        print("\n===== ИНФОРМАЦИЯ О СЧЕТЕ =====")
        print(f"Владелец: {self.owner_name}")
        print(f"Номер счета: {self.account_number}")
        print(f"Баланс: {self.balance}")
        print("==============================")

    # История операций
    def show_history(self):
        print("\n===== ИСТОРИЯ ОПЕРАЦИЙ =====")

        if not self.history:
            print("История пуста")
            return

        for operation in self.history:
            print(operation)