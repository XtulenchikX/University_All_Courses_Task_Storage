# Пример 1. Рассмотрим шаблон в качестве else

print('Days: mon, tue, wed, thu, fri, sat, sun or 1, 2, 3, 4, 5, 6, 7')
day = str(input('введите день: '))
match day:
  case 'mon' | '1':
    print('Math classes')
  case 'tue' | '2':
    print('Language classes')
  case 'wed' | '3':
    print('PE classes')
  case 'thu' | '4':
    print('Prog classes')
  case 'fri' | '5':
    print('Web classes')
  case 'sat' | '6':
    print('Day of Extra sports')
  case 'sun' | '7':
    print('DayOff!')
  case _:
    print('Ошибка при вводе дня!')

# Пример 2. Воспользуемся подстановкой, чтобы определить количество элементов коллекции, сами значения нам не важны (стоит использовать при небольшом максимально количестве элементов, иначе получится слишком большая структура!)

Days_off = ('mon', 'tue')
print('Выходные дни: ', Days_off)
match Days_off:
  case (_,):
    print('1 day')
  case (_, _,):
    print('2 days')
  case (_, _, _,):
    print('3 days')