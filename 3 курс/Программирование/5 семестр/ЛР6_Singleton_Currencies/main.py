import time

from currencies_class import Current_currencies
from new_print import new_print


# Демонстрация Singleton
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

# Демонстрация ограничения количества запросов в секунду
print('\n_______')
print("Проверка на ограничение количества запросов в секунду:\n")
obj.get_currencies()
obj1.get_currencies()
time.sleep(1)
obj1.get_currencies()
time.sleep(0.5)
obj.get_currencies()
