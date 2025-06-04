import os

class Task:
    def __init__(self, id, sarlavha, tavsif, tugash_sanasi=None, holat="Kutilmoqda"):
        self.id = id
        self.sarlavha = sarlavha
        self.tavsif = tavsif
        self.tugash_sanasi = tugash_sanasi
        self.holat = holat

    def __str__(self):
        return f"{self.id}, {self.sarlavha}, {self.tavsif}, {self.tugash_sanasi}, {self.holat}"

    def to_file_string(self):
        return f"{self.id},{self.sarlavha},{self.tavsif},{self.tugash_sanasi},{self.holat}\n"

    @staticmethod
    def from_file_string(line):
        parts = line.strip().split(',')
        if len(parts) == 5:
            return Task(parts[0], parts[1], parts[2], parts[3], parts[4])
        return None

class TaskManager:
    def __init__(self, file_name='vazifalar.txt'):
        self.file_name = file_name
        self.ensure_file()

    def ensure_file(self):
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()

    def load_tasks(self):
        tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                task = Task.from_file_string(line)
                if task:
                    tasks.append(task)
        return tasks

    def save_tasks(self, tasks):
        with open(self.file_name, 'w') as file:
            for t in tasks:
                file.write(t.to_file_string())

    def add_task(self):
        id = input('ID: ')
        if any(t.id == id for t in self.load_tasks()):
            print('Bunday ID mavjud.')
            return
        sarlavha = input('Sarlavha: ')
        tavsif = input('Tavsif: ')
        tugash_sanasi = input('Tugash sanasi (YYYY-MM-DD): ')
        holat = input('Holat (Kutilmoqda/Jarayonda/Bajarildi): ')
        new_task = Task(id, sarlavha, tavsif, tugash_sanasi, holat)
        with open(self.file_name, 'a') as file:
            file.write(new_task.to_file_string())
        print('Vazifa qoshildi.')

    def view_tasks(self):
        tasks = self.load_tasks()
        if not tasks:
            print('Vazifalar mavjud emas.')
            return
        choice = input('Saralash: 1.sana 2.holat 3.yoq: ').strip()
        if choice == '1':
            tasks.sort(key=lambda t: t.tugash_sanasi or '')
        elif choice == '2':
            tasks.sort(key=lambda t: t.holat)
        print("\nVazifalar:")
        for t in tasks:
            print(t)

    def search_task(self):
        id = input('Vazifa ID sini kiriting: ').strip()
        for t in self.load_tasks():
            if t.id == id:
                print('Topildi:', t)
                return
        print('Topilmadi.')

    def update_task(self):
        id = input('Vazifa ID: ')
        tasks = self.load_tasks()
        for t in tasks:
            if t.id == id:
                print('Hozirgisi:', t)
                t.sarlavha = input('Yangi sarlavha: ') or t.sarlavha
                t.tavsif = input('Yangi tavsif: ') or t.tavsif
                t.tugash_sanasi = input('Yangi tugash sanasi: ') or t.tugash_sanasi
                t.holat = input('Yangi holat: ') or t.holat
                self.save_tasks(tasks)
                print('Yangilandi.')
                return
        print('Topilmadi.')

    def delete_task(self):
        id = input('Vazifa ID: ')
        tasks = self.load_tasks()
        updated = [t for t in tasks if t.id != id]
        if len(tasks) == len(updated):
            print('Topilmadi.')
        else:
            self.save_tasks(updated)
            print('Ochirildi.')

    def run(self):
        while True:
            print("\nTanlang:")
            print("1. Vazifa qoshish")
            print("2. Vazifalarni korish")
            print("3. Qidirish")
            print("4. Yangilash")
            print("5. Ochirish")
            print("6. Chiqish")
            choice = input("Amal: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.search_task()
            elif choice == '4':
                self.update_task()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                print('Tugatildi.')
                break
            else:
                print('Notogri tanlov.')

if __name__ == '__main__':
    manager = TaskManager()
    manager.run()
