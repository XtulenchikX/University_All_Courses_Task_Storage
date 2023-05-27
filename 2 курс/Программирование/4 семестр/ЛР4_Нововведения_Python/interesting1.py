# Простой, но интересный пример использования match-case структуры при обработке массива

data = str(input('Введите информацию: '))

data_parts = data.split('-')
match data_parts:
  case day, mon, year, plan:
    print(f'На {day} день, {mon} месяца, {year} года, нужно {plan}')
  case _:
    print('Данные введены неверно!')