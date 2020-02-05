import json

class Pet():
    def __init__(self, name=None):
        self.name = name


class PetExport:
    def export(self, dog):
        raise NotImplementedError


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

class ExportJson(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed
        })

class ExportXML(PetExport):
    def export(self, dog):
        return """<?xml version "1.0" encoding "utf-8"?>
<dog>
    <name>{0}</name>
    <breed>{1}</breed>
</dog>
""".format(dog.name, dog.breed)

class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):  #композиция: передаем дополнительный объект для экспорта данных
                                                          # в инициализаторе этого класса
        super().__init__(name, breed)
        self._exporter = exporter or ExportJson()         #сохраним этот объект в self и зададим экспортер по умолчанию
        if not isinstance(self._exporter, PetExport):
            raise ValueError("Bad exporter", exporter)

    def export(self):  #метод экспорт, чтобы класс мог экспортировать данные
        return self._exporter.export(self)

dog = ExDog("Шарик", "дворняга", exporter = ExportXML())
print(dog.export())

doggo = ExDog("Барбос", "мопс")
print(doggo.export())

#если нужно добавить еще форматов для экспорта, нам не понадобится менять класс ExDog,
# а просто добавим новый класс-экспортер в иерархию классов экспорта