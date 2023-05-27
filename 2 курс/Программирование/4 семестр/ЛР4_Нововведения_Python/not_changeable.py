# НЕ изменяемая структура

from dataclasses import dataclass

@dataclass(frozen = True)
class Person:
    fName: str
    sName: str
    Year: int = 2023

fN = str(input('Введите имя: '))
sN = str(input('Введите фамилию: '))
user1 = Person(fN, sN)

print(user1)

fN = str(input('Введите имя на которое заменить: '))
user1.fName = fN

print(user1)