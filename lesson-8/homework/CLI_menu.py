from task_2 import Bank

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
            print("Dasturdan tugadi")
            break
        else:
            print("Notog'ri tanlov")

main()
