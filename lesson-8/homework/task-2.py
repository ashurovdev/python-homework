import uuid
import json
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def unique_number(self):
        return str(uuid.uuid4())

    def create_account(self, name, initial_deposit):
        account_number = self.unique_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Hurmatli {name}, sizning akkauntingiz yaratildi! Hisob raqamingiz: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Ism: {account.name}")
            print(f"Balans: {account.balance} so'm")
        else:
            print("Bunday hisob raqami topilmadi.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"{amount} so'm muvaffaqiyatli qo'shildi. Yangi balans: {account.balance} so'm")
            else:
                print("Iltimos, musbat miqdor kiriting.")
        else:
            print("Hisob topilmadi.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"{amount} so'm yechildi. Yangi balans: {account.balance} so'm")
            else:
                print("Noto'g'ri miqdor. Hisobda yetarli mablag' yo'q yoki noto'g'ri kiritildi.")
        else:
            print("Hisob topilmadi.")

    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, f)

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                for acc_num, acc_data in data.items():
                    self.accounts[acc_num] = Account.from_dict(acc_data)


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Dasturi ---")
        print("1. Hisob yaratish")
        print("2. Hisobni ko'rish")
        print("3. Pul qo'yish")
        print("4. Pul yechish")
        print("5. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-5): ")

        if tanlov == "1":
            name = input("Ismingizni kiriting: ")
            try:
                deposit = float(input("Boshlang'ich depozitni kiriting: "))
                bank.create_account(name, deposit)
            except ValueError:
                print("Faqat son kiriting")
        elif tanlov == "2":
            acc_num = input("Hisob raqamingizni kiriting: ")
            bank.view_account(acc_num)
        elif tanlov == "3":
            acc_num = input("Hisob raqamingizni kiriting: ")
            try:
                amount = float(input("Qo'yiladigan summani kiriting: "))
                bank.deposit(acc_num, amount)
            except ValueError:
                print("Faqat son kiriting")
        elif tanlov == "4":
            acc_num = input("Hisob raqamingizni kiriting: ")
            try:
                amount = float(input("Yechib olinadigan summani kiriting: "))
                bank.withdraw(acc_num, amount)
            except ValueError:
                print("Faqat son kiriting")
        elif tanlov == "5":
            print("Dasturdan chiqildi")
            break
        else:
            print("Noto'g'ri tanlov")

main()