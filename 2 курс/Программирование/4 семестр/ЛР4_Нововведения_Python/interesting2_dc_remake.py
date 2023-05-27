from dataclasses import dataclass

@dataclass
class Students:
    FName: str
    SName: str
    mark: int

student1 = Students("Vasiliy", "Pupkin", 2)
student2 = Students("Ibragim", "Leshev", 4)
student3 = Students("Korney", "Ivanov", 3)

def what_result(data):
  """
  Данная функция проверяет объект, полученный на вход, по свойству mark и выдаёт различные сообщения в зависимости от значения mark.
  """
  match data:
    case Students(FName = str(FName), SName = str(SName), mark = 5|4 as mark):
      print(f'{FName} {SName} сдал и получил {mark}')
    case Students(FName = str(FName), SName = str(SName), mark = 3 as mark):
      print(f'{FName} {SName} получил {mark} и имеет право на аппеляцию')
    case Students(FName = str(FName), SName = str(SName), mark = 1|2 as mark):
      print(f'{FName} {SName} получил {mark} и не сдал')
    case _:
      print('Error with object')

print(what_result(student1))
print(what_result(student2))
print(what_result(student3))