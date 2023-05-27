# DataClass с значением по умолчанию

from dataclasses import dataclass

@dataclass
class Person:
    fName: str
    sName: str
    Year: int = 2023

fN = str(input('Введите имя: '))
sN = str(input('Введите фамилию: '))
user1 = Person(fN, sN)

print(user1)