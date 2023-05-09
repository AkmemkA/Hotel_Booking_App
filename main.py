import datetime

class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
    def get_name(self):
        return self.name.title()
    def age(self, current_year):
        result = current_year - self.birthyear
        return result

akhmed = User('akhmed', 1993)
print(akhmed.age(2023))
print(akhmed.get_name())