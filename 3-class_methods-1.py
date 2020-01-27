"""class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.event_date = event_date

    def __str__(self):
        return f"Event {self.description} at {self.event_date}"


from datetime import date

event_description = "Рассказать, что такое #classmethod"
event_date = date.today()

event = Event(event_description, event_date)
print(event)
"""

from datetime import date

class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.event_date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.event_date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        event_date = extract_date(user_input)
        return cls(description, date)


def extract_description(user_string):
    return "Чемпионат мира по футболу"


def extract_date(user_date):
    return date(2018, 6, 14)


event = Event.from_string("Добавить в мой календарь Чемпионат мира по футболу на 14 июня 2018 года")
print(event)
