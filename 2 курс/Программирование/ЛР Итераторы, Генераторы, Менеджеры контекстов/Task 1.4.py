#Стецук Максим 2гр.1п.гр.
#Задание 1.4


def gen_country(dict, mass):
  for n in mass:
    line = 'Страна: ' + dict[n] + '; Город: ' + n
    yield line


list = [
  'Russia Saint-Petersburg Moscow Petrozavodsk',
  'Belarus Bobruisk Vitebsk Gomel', 'Armenia Yerevan Armavir Kotayk'
]

d = {}
for pos in list:
  country, *cities = pos.split()
  for city in cities:
    d[city] = country

mass = ('Saint-Petersburg', 'Bobruisk', 'Moscow', 'Vitebsk', 'Yerevan',
        'Petrozavodsk', 'Kotayk')

for some in gen_country(d, mass):
  print(some)
