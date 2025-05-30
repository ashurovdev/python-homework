import os

filename = 'lesson-6/homework/employees.txt'

def add_emp():
    with open(filename, 'a') as file:
        emp_id = input('ID sini kiriting: ')
        emp_name = input('Ismini kiriting: ')
        emp_position = input('Mansabini kiriting: ')
        emp_salary = int(input('Oylik maoshini kiriting (son faqat): '))
        file.write(f'{emp_id}, {emp_name}, {emp_position}, {emp_salary}\n')
        print('Hodim bazaga qo\'shildi')

def view_emps():
    if not os.path.exists(filename):
        print('Baza mavjud emas')
        return
    with open(filename, 'r') as file:
        records = file.readlines()
        if not records:
            print('Baza bo\'sh')
            return
        print('\nHodimlar: ')
        for record in records:
            print(record.strip())
        print()

def search_emp():
    emp_id = input('ID sini kiriting: ')
    found = False
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(emp_id+','):
                print(f'Hodim: {line.strip()}')
                found = True
                break
    if not found:
        print('Bunday hodim mavjud emas')
    
def update_emp():
    emp_id = input('Id sini kiriting: ')
    updated = False
    if not os.path.exists(filename):
        print('Baza topilmadi')
        return
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if line.startswith(emp_id+','):
                print(f'Hozirgi holatdagi ma\'lumot: \n{line.strip()}')
                emp_id = input('ID sini kiriting: ')
                emp_name = input('Ismini kiriting: ')
                emp_position = input('Mansabini kiriting: ')
                emp_salary = int(input('Oylik maoshini kiriting (son faqat): '))
                file.write(f'{emp_id}, {emp_name}, {emp_position}, {emp_salary}\n')
                updated = True
                print('Yangilandi')
                return
            else:
                file.write(line)
                return
        if not updated:
            print('Bunday hodim mavjud emas')
            return
        

def del_emp():
    emp_id = input('Id sini kiriting: ')
    deleted = False
    if not os.path.exists(filename):
        print('Baza topilmadi')
        return
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if line.startswith(emp_id+','):
                deleted = True
                print('Hodim o\'chirildi')
                continue
            file.write(line)
    if not deleted:
        print('Hodim topilmadi')
        return

def main():
    while True:
        print('\nAmallardan birini tanlang: ')
        print('1. Hodim qo\'shish')
        print('2. Barcha hodimlarni ko\'rish')
        print('3. Hodimni qidirish ')
        print('4. Hodim ma\'lumotlarini yangilash')
        print('5. Hodimni o\'chirish')
        print('6. Chiqish')
        choice = int(input('Amalni kiriting (1-6): '))

        if choice==1:
            add_emp()
        elif choice==2:
            view_emps()
        elif choice==3:
            search_emp()
        elif choice==4:
            update_emp()
        elif choice==5:
            del_emp()
        elif choice==6:
            print('Yakunlandi')
            break
        else:
            print('Xato kalit')

main()