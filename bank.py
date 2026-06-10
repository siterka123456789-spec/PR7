from bankAccount import BankAccount


class Bank:
    def __init__(self):
        # Хранилище всех счетов
        self.accounts = []

    # Создание счета
    def create_account(self, owner_name):
        account = BankAccount(owner_name)

        self.accounts.append(account)

        print(
            f"Счет создан. Номер счета: "
            f"{account.account_number}"
        )

    # Поиск счета
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        return None

    # Перевод между счетами
    def transfer_between_accounts(
        self,
        sender_number,
        receiver_number,
        amount
    ):
        sender = self.find_account(sender_number)
        receiver = self.find_account(receiver_number)

        if not sender or not receiver:
            print("Один из счетов не найден")
            return

        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        if amount > 20000:
            print("Максимальный перевод 20000")
            return

        if amount > sender.balance:
            print("Недостаточно средств")
            return

        sender.balance -= amount
        receiver.balance += amount

        sender.history.append(
            f"Перевод {amount} на счет "
            f"{receiver.account_number}"
        )

        receiver.history.append(
            f"Получено {amount} от счета "
            f"{sender.account_number}"
        )

        print("Перевод выполнен")

    # Показать все счета
    def show_all_accounts(self):
        if not self.accounts:
            print("Счетов нет")
            return

        print("\n===== ВСЕ СЧЕТА =====")

        for account in self.accounts:
            print(
                f"{account.account_number} | "
                f"{account.owner_name} | "
                f"{account.balance}"
            )