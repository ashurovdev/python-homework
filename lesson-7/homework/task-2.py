import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
    
    def to_file_string(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}\n"
    
    @staticmethod
    def from_file_string(line):
        parts = line.strip().split(',')
        if len(parts) == 4:
            return Employee(parts[0], parts[1], parts[2], float(parts[3]))
        return None
    
class EmployeeManager():
    def __init__(self, filname = 'employees.txt'):
        self.filename = filname
        self.ensure_file()

    def ensure_file(self):
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()
    
    def load_emps(self):
        employees = []
        with open(self.filename, 'r') as file:
            for line in file:
                emp = Employee.from_file_string(line)
                if emp:
                    employees.append(emp)
        return employees
    
    def save_emps(self, employees):
        with open(self.filename, 'w') as file:
            for emp in employees:
                file.write(emp.to_file_string())
    
    def is_uniqe_id(self, employee_id):
        return all(emp.employee_id != employee_id for emp in self.load_emps())

    def add_emp(self):
        try:
            emp_id = input('ID sini kiriting: ')
            if not self.is_uniqe_id(emp_id):
                print('Bunday id mavjud')
                return
            emp_name = input('Ismini kiriting: ')
            emp_position = input('Mansabini kiriting: ')
            emp_salary = int(input('Oylik maoshini kiriting (son faqat): '))
            emp = Employee(employee_id=emp_id, name=emp_name, position=emp_position, salary=emp_salary)
            with open(self.filename, 'a') as file:
                file.write(emp.to_file_string())
            print('Hodim bazaga qo\'shildi')
        except ValueError:
            print('Kiritishda xatolik')

    def view_emps(self):
        employees = self.load_emps()
        if not employees:
            print('Baza bo\'sh')
            return
        
        choice = input('Filtrlash 1.ism 2.maosh 3.none: ').strip()
        if choice == '1':
            employees.sort(key=lambda e: e.name)
        elif choice == '2':
            employees.sort(key=lambda e: e.salary, reverse=True)
        
        print('Hodimlar')
        for emp in employees:
            print(emp)
    
    def search_emp(self):
        emp_id = input('Hodim ID sini kiriting: ').strip()
        for emp in self.load_emps():
            if emp.employee_id == emp_id:
                print('Hodim topildi\n', emp)
                return
        print('Hodim topilmadi')
    
    def update_emp(self):
        emp_id = input('Hodim ID sini kiriting: ').strip()
        employees = self.load_emps()
        for emp in employees:
            if emp.employee_id == emp_id:
                print(f"Hozirgisi: {emp}")
                emp.name = input("Ismini kiriting: ").strip()
                emp.position = input("Lavozimini kiriting: ").strip()
                try:
                    emp.salary = float(input("Oyligini kiriting: "))
                except ValueError:
                    print("Notogri kiritildi")
                    return
                self.save_emps(employees)
                print("Yangilanish muvaffaqiyatli o\'tdi")
                return
        print("Hodim topilmadi")
    
    def delete_emp(self):
        employee_id = input("Hodim ID sini kiriting: ").strip()
        employees = self.load_emps()
        new_employees = [emp for emp in employees if emp.employee_id != employee_id]
        if len(new_employees) == len(employees):
            print("Hodim topilmadi")
        else:
            self.save_emps(new_employees)
            print("Hodim o\'chirildi")

    def main(self):
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
                self.add_emp()
            elif choice==2:
                self.view_emps()
            elif choice==3:
                self.search_emp()
            elif choice==4:
                self.update_emp()
            elif choice==5:
                self.delete_emp()
            elif choice==6:
                print('Yakunlandi')
                break
            else:
                print('Xato kalit')

manager = EmployeeManager()
manager.main()

