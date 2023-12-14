# from get_currencies import get_currencies
from get_one_currency import get_one_currency
from currencies_class import Current_currencies

# res = get_currencies(['R01035', 'R01335', 'R01700J'])
# if res:
#     print(get_currencies(['R01035', 'R01335', 'R01700J']))


obj = Current_currencies()
obj.get_currencies()
print(obj.return_currencies())
print()
# print(obj.all_cur)

obj.get_one_currenc('R012701111')
print(obj.one_cur)
print('-------')

obj.get_one_currenc('R01270')
print(obj.one_cur)
print()

obj1 = Current_currencies()
obj1.get_one_currenc()
print(obj1.return_one_currenc())
print('-------')

print(obj.show_cur_save())
print(obj.clean_cur_save())
print(obj1.show_cur_save())

print('------')

obj2 = Current_currencies()
print(obj2.return_currencies())
print(obj2.return_one_currenc())

# print('------')
# print('------')

# print(get_one_currency())
# print(get_one_currency('R01815'))
# print(get_one_currency('R19999999'))
