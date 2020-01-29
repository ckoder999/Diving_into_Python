# Статические методы

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150

human = Human('Bob', 25)

print(human.is_age_valid(25))

print(Human.is_age_valid(225))

### Вычисляемые свойства
"""
class Robot():
    def __init__(self, power):
        self.power = power

    def check_power(self, power):
        if power < 0:
            self.power = 0
        else:
            self.power = power

robot = Robot(20)
robot.power = -20
print(robot.power)
robot.check_power(-20)
print(robot.power)
"""

class Robot():
    def __init__(self, power):
        self._power = power #ставим приватный атрибут _power

    power = property() #объявляем объект property с тремя методами

    @power.getter #оборачиваем их декораторами
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        if power < 0:
            self._power = 0
        else:
            self._power = power

    @power.deleter
    def power(self):
        print("The robot is inactive!")
        del self._power


robot = Robot(120)
print(robot.power)

robot.power = -20
print(robot.power)

