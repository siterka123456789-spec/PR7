from bank import Bank
import os

def clear():
    os.system("cls")

def wait_and_clear():
    input("\nНажмите Enter чтобы продолжить...")
    clear()

def menu():
    print("\n" + "=" * 50)
    print("           БАНКОВСКАЯ СИСТЕМА")
    print("=" * 50)

    print("1. Открыть новый счёт")
    print("2. Пополнить счёт")
    print("3. Снять средства")
    print("4. Перевести средства")
    print("5. Показать баланс")
    print("6. Показать информацию о счёте")
    print("7. Список всех счетов")
    print("8. Выход")
    
def main():
    bank = Bank()
    
    while 1:
        clear()
        menu()
        choice = int(input("\nВаш выбор: "))
        match choice:
            case 1:
                owner = input("\nВведите имя владельца: ")
                bank.create_account(owner)
                wait_and_clear()
            case 2:
                acc_num = int(input("Введите номер счета: "))
                amount = float(input("Введите сумму: "))
                account = bank.find_account(acc_num)
                if account:
                    account.deposit(amount)
                else:
                    print("Счет не найден")
                wait_and_clear()
            case 3:
                acc_num = int(input("Введите номер счета: "))
                amount = float(input("Введите сумму: "))
                account = bank.find_account(acc_num)
                if account:
                    account.withdraw(amount)
                else:
                    print("Счет не найден")
                wait_and_clear()
            case 4:
                from_acc = int(input("С какого счета: "))
                to_acc = int(input("На какой счет: "))
                amount = float(input("Введите сумму: "))

                sender = bank.find_account(from_acc)
                receiver = bank.find_account(to_acc)

                if sender and receiver:
                    sender.transfer(receiver, amount)
                else:
                    print("Один из счетов не найден")
                wait_and_clear()
            case 5:
                acc_num = int(input("Введите номер счета: "))
                account = bank.find_account(acc_num)
                if account:
                    account.show_balance()
                else:
                    print("Счет не найден")
                wait_and_clear()
            case 6:
                acc_num = int(input("Введите номер счета: "))
                account = bank.find_account(acc_num)
                if account:
                    account.show_info()
                else:
                    print("Счет не найден")
                wait_and_clear()
            case 7:
                bank.show_all_accounts()
                wait_and_clear()
            case 8:
                acc_num = int(input("Введите номер счета: "))

                account = bank.find_account(acc_num)

                if account:
                    account.show_history()
                else:
                    print("Счет не найден")
            case 9:
                print("Выход из программы...")
                break
            case _:
                print("Неверный выбор")

if __name__ == "__main__":
    main()