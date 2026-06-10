from bankAccount import BankAccount

class Bank:
    def __init__(self):
        self.accounts = []
        
    def create_account(self, owner_name):
        account = BankAccount(owner_name)
        self.accounts.append(account)
        
        print(
            f"Счет создан! "
            f"Номер счета: {account.account_number}"
        )
    
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def show_all_accounts(self):
        if not self.accounts:
            print("Список счетов пуст")
            return
        print("\n===== СПИСОК СЧЕТОВ =====")

        for account in self.accounts:
            print(
                f"Счет: {account.account_number} | "
                f"Владелец: {account.owner_name} | "
                f"Баланс: {account.balance}"
            )

        print("=========================")