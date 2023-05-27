# Простой пример для выборки дня недели

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