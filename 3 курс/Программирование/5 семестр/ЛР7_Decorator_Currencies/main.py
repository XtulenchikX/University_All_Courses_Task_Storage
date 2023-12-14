from currencies_class import Current_currencies, Deco_CSV, Deco_JSON

obj = Current_currencies()
obj1 = Current_currencies()
obj2 = Current_currencies()

obj.get_one_currenc('R01815')
obj1.get_one_currenc('R01820')
obj2.get_one_currenc()
obj2.get_one_currenc('R01010')
obj.get_one_currenc('R01565')
obj1.get_one_currenc('R01280')
obj.get_one_currenc('R01717')

print(obj.show_cur_save())
print('_______')
print(obj1.show_cur_save())
print('_______')
print(obj2.show_cur_save())
print('_______')

obj3 = Deco_JSON(obj)
print(obj3.show_cur_save())

obj4 = Deco_CSV(obj)
obj4.show_cur_save()

obj.clean_cur_save()
print(obj1.cur_save)
print('_______')

obj2.get_one_currenc()
print(obj.cur_save)

