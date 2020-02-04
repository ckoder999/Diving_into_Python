import json

class Pet():
    def __init__(self, name=None):
        self.name = name
# __breed - приватный атрибут

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return "{0}: waw".format(self.name)

    def get_breed(self):
        return self.__breed

class ExportJson():
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": Dog.get_breed(self)
            })

class ExDog(Dog, ExportJson):
   def get_breed(self):
       return "порода {0} - {1}".format(self.name, self._Dog__breed) #обращение к приватному атрибуту суперкласса

doggo = ExDog("Beethoven", "Сollie")
print(doggo.get_breed())

print(doggo.__dict__)