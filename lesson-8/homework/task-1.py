class Animal:
    def __init__(self, name, spices):
        self.name = name
        self.spices = spices
    
    def make_sound(self):
        return f"{self.name} ovoz chiqarmoqda"

class Cow(Animal):
    def __init__(self, name, spices):
        super().__init__(name, spices)
    
    def make_sound(self):
        return super().make_sound()
    
class Dog(Animal):
    def __init__(self, name, spices):
        super().__init__(name, spices)
    
    def make_sound(self):
        return super().make_sound()

class Cat(Animal):
    def __init__(self, name, spices):
        super().__init__(name, spices)
    
    def make_sound(self):
        return super().make_sound()

class Farm:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def make_sound(self):
        for animal in self.animals:
            print(animal.make_sound())
        
farm = Farm()
farm.add_animal(Cow('Qizil burun', 'Sigir'))
farm.make_sound()