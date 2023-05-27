# Сравнение объектов класса

from dataclasses import dataclass

@dataclass(order = True)
class Person:
    age: int
    fName: str
    sName: str

p1 = Person(18, 'Rafael', 'Raf')
print(p1)
p2 = Person(17, 'Leanardo', 'Leo')
print(p2)

if p1 > p2:
  print('p1 старше p2' )
else:
  print('p2 старше p1')
