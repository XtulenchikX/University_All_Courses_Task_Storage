import time

from currencies_class import Current_currencies
from new_print import new_print


# Демонстрация Singlton
obj = Current_currencies()
obj1 = Current_currencies()
obj2 = Current_currencies()

obj.get_one_currenc('R01815')
obj1.get_one_currenc('R01820')
obj2.get_one_currenc()
obj2.get_one_currenc('R00000')

new_print(obj.show_cur_save())
print('_______')
new_print(obj1.show_cur_save())
print('_______')
new_print(obj2.show_cur_save())
print('_______')

obj.clean_cur_save()
print(obj1.show_cur_save())
print('_______')

obj2.get_one_currenc()
new_print(obj.show_cur_save())

# Демонстрация времени между запросами на получение всех валют
print()
obj.get_currencies()
obj.get_currencies()
time.sleep(1)
obj.get_currencies()
time.sleep(0.5)
obj.get_currencies()