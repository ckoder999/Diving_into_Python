class Pet():
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)

dog = Dog("Шарик", "Доберман")

print(dog.name)
print(dog.say())

import json

class ExportJson():
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
            })

class ExDog(Dog, ExportJson):
   def init(self, name, breed=None):
       #вызов метода по MRO
       super().__init__(name, breed)
       #то же самое, что
       #super(ExDog, self).__init__(name)

class WoolenDog(Dog, ExportJson):
    def __init__(self, name, breed=None):
        # явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = " Шерстяная собака породы {0}".format(breed)


dog = WoolenDog("Жучка", breed="Такса")
print(dog.breed)
print(dog.to_json())
print(dog.say())

#method resolution order
#порядок разрешения классов
print(ExDog.__mro__)
#список в mro называется линеаризацией класса

"""
#является ли потомком класса?
print(issubclass(Dog, Pet))
print(issubclass(Dog, object))
print(issubclass(Dog, int))

#является ли экземпляром класса?
print(isinstance(dog, object))
print(isinstance(dog, Dog))
print(isinstance(Dog, int))
"""

