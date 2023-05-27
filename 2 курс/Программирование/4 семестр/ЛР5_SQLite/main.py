import app

database = 'database.sqlite'

if __name__ == '__main__':

  con = app.connect(database)

  user1 = {'name':'Petr', 'height':1.6, 'created':'2023-03-04 12:15:20' }
  user2 = {'name':'Ivan', 'height':1.7, 'created':'2023-05-04 13:20:41' }
  user3 = {'name':'Maks', 'height':1.9, 'created':'2023-10-04 19:18:54' }
  app.insert(con, 'user', user1, user2, user3)

  # cond1 = 'name LIKE "%n"'
  # cond2 = 'height > 1.7'
  # app.delete(con, 'user', cond1, cond2)

  # cond = 'id <> 0'
  # app.delete(con, 'user', cond)

  # param1 = ['height = height + 0.05', 'name = "Petr"']
  # param2 = ['height = height + 0.1', 'name = "Ivan"']
  # app.update(con, 'user', param1, param2)

  app.read_all(con, 'user')
