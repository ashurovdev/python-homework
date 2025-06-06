class Animal:
    def __init__(self, name, species):
        self.name = name      
        self.species = species  

    def speak(self):
        return f"{self.name} tovush chiqarmoqda"

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Sigir")

    def speak(self):
        return f"{self.name} 'Muu' deydi!"

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Tovuq")

    def speak(self):
        return f"{self.name} 'Qiyq-qiyq' deydi!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Mushuk")

    def speak(self):
        return f"{self.name} 'Miov' deydi!"
