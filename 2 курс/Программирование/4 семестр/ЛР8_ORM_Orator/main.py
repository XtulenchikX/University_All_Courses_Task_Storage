from orator import DatabaseManager
from user_class_consrtruct import Users_construct


config = {
  'default': 'sqlite',
  'sqlite': {
    'driver': 'sqlite',
    'database': 'ormdb.db'
  },
}

db = DatabaseManager(config)

from orator import Model

Model.set_connection_resolver(db)


class User(Model):
  __table__ = 'user'
  __timestamps__ = False
  __fillable__ = ['name', 'height', 'created_date']

  # Создание пользователей

  def create_user(*users):
    for u in users:
      new_user = User.create(name=u.name, height=u.height, created_date=u.created)
      new_user.save()

  # Выборка по всем, id, name

  def select_all():
    print("-" * 45)
    print("{:<5} {:<10} {:<8} {:<20}".format("ID", "Name", "Height", "Created date"))
    print("-" * 45)
    users = User.all()
    for user in users:
      print("{:<5} {:<10} {:<8} {:<20}".format(user.id, user.name, user.height, user.created_date))
      # print(f"#{user.id}  {user.name}  {user.height}  {user.created_date}")
    print('-' * 45, '\n')

  def select_by_id(*id_s):
    print('-' * 25)
    print(f'Выборка по id = {id_s}:')
    for id in id_s:
      user_get = User.find(id)
      print(user_get.name, user_get.height, user_get.created_date)
    print('\n')

  def select_by_name(option, name):
    print('-' * 25)
    print(f'Имя {option} {name}:')
    users = User.where('name', option, name).get()
    for user in users:
      print(f"#{user.id}  {user.name}  {user.height}  {user.created_date}")
    print('\n')

  def select_by_height(option, height):
    print('-' * 25)
    print(f'Рост {option} {height}:')
    users = User.where('height', option, height).get()
    for user in users:
      print(f"#{user.id}  {user.name}  {user.height}  {user.created_date}")
    print('\n')

  # Обновление по id, имени

  def update_by_id(user_id, name=None, height=None):
    user_upd = User.find(user_id)
    if name != None:
      user_upd.name = name
    if height != None:
      user_upd.height = height
    user_upd.save()

  def update_by_name(option, name, name_new=None, height=None):
    user_upd = User.where('name', option, name).get()
    for u in user_upd:
      if name_new != None:
        u.name = name_new
      if height != None:
        u.height = height
      u.save()

  # Удаление по id, имени, росту

  def delete_by_id(*user_id):
    for id in user_id:
      User.find(id).delete()

  def delete_by_names(*names):
    for name in names:
      users_f_del = User.where('name', name).get()
      for u in users_f_del:
        u.delete()

if __name__ == '__main__':
  # user1 = Users_construct('Maks', 1.93, '2023-06-01 15:31:29')
  # user2 = Users_construct('Vlad', 1.91, '2023-06-01 16:27:15')
  # User.create_user(user1, user2)
  
  # User.select_all()
  # User.select_by_id(1, 4, 7, 11, 16)
  # User.select_by_name('<>','Mike')
  # User.select_by_height('>', 1.8)
  
  # User.update_by_id(4, None, 1)
  # User.update_by_name('=','Mike', None, 1.6)
  
  # User.delete_by_id(3, 6, 7, 8, 9, 10, 11, 12)
  User.delete_by_names('Maks', 'Vlad')

  
  ### Проверял корректность работы проверки вводимых значений при создании объекта класса "Users_construct"
  # userTest = Users_construct('Vlad', 1.91, '2023-06-01 16:27:15')
  # userTest.name = '1Vlad'
  # User.create_user(userTest)
  
  User.select_all()
