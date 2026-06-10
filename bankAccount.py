class BankAccount:
    account_counter = 1000
    
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0
        self.account_number = BankAccount.account_counter
        
        BankAccount.account_counter += 1
        
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        if amount > 50000:
            print("Максимальная сумма пополнения 50.000")
            return
        
        self.balance += amount
        print(f"Пополнение на {amount}. Баланс: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        if amount > 50000:
            print("Максимальная сумма снятия: 50000")
            return

        if amount > self.balance:
            print("Недостаточно средств")
            return

        self.balance -= amount
        print(f"Снятие {amount}. Баланс: {self.balance}")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Сумма должна быть больше 0")
            return
        if amount > 20000:
            print("Максимальная сумма снятия 20.000")
            return
        if amount > self.balance:
            print("Недостаточно средств")
            return
        self.balance -= amount
        other_account.balance += amount
            
        print(
            f"Перевод {amount} со счета "
            f"{self.account_number} на счет "
            f"{other_account.account_number}"
        )

    def show_balance(self):
        print(f"Текущий баланс: {self.balance}")
            
    def show_info(self):
        print("\n===== ИНФОРМАЦИЯ О СЧЕТЕ =====")
        print(f"Владелец: {self.owner_name}")
        print(f"Номер счета: {self.account_number}")
        print(f"Баланс: {self.balance}")
        print("==============================")