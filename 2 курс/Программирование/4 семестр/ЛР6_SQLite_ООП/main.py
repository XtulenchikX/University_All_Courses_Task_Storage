import app
from user import Users

database = 'database.sqlite'

if __name__ == '__main__':

  con = app.connect(database)

  # user1 = Users('Petr', 1.6, '2023-03-04 12:15:20')
  # user2 = Users('Ivan', 1.7, '2023-05-04 13:20:41')
  # user3 = Users('Maks', 1.9, '2023-10-04 19:18:54')
  # user4 = Users('Mark', 1.8, '2023-10-04 19:24:54')
  # user5 = Users('Vlad', 1.85, '2023-10-04 19:14:54')
  # app.insert(con, 'user', user1, user2, user3, user4, user5)

  user = Users('TestUser', 1.9, '2023-03-04 12:15:20')
  user.name = 'NiceName'
  user.heigt = 1.76
  user.created = '2023-05-04 12:15:20'
  app.insert(con, 'user', user)

  # cond1 = 'height > 1.8'
  # cond2 = 'height < 1.7'
  # app.delete(con, 'user', cond1, cond2)

  # cond = 'id <> 0'
  # app.delete(con, 'user', cond)

  # param1 = ['height = height + 0.05', 'name = "Petr"']
  # param2 = ['height = height + 0.1', 'name = "Ivan"']
  # app.update(con, 'user', param1, param2)

  app.read_all(con, 'user')
