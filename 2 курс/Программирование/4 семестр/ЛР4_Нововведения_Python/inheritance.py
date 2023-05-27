# Пример наследования классов

from dataclasses import dataclass

@dataclass
class Person:
    fName: str
    sName: str

@dataclass
class Worker(Person):
    sallary: float

fN = str(input('Введите имя: '))
sN = str(input('Введите фамилию: '))
sal = str(input('Введите зарплату: '))

worker1 = Worker(fN, sN, sal)

print(worker1)