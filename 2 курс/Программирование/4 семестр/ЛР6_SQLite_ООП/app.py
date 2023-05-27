import sqlite3
from another_func import write_log

def singleton(smth):
    instances = {}

    def get_instance(*args, **kwargs):
        if smth not in instances:
            instances[smth] = smth(*args, **kwargs)
        return instances[smth]

    return get_instance

@singleton
def connect(database_name):
  """
  This function is responsible for connecting to the database and returns NONE when connection failed.
  """
  con = None
  try:
    con = sqlite3.connect(database_name)
  except sqlite3.DatabaseError:
    print(f'Failed to connect to database named {database_name}')
  else:
    return (con)


def close(con):
  con.close()
  """
  This function is responsible for closing connection to the database
  """


def read_all(con, table):
  """
  A function designed to display all rows of a table.
  """
  if con != None:
    cur = con.cursor()
    query = f"SELECT * FROM {table}"
    write_log(query)
    try:
      res = cur.execute(query)
    except sqlite3.OperationalError:
      print(f'There is no table with name {table}')
    else:
      for row in res:
        print(row)


def insert(con, table, *values):
  """
  A function designed to enter data into a table.
  """
  if con != None:
    cur = con.cursor()
    inp = ' '
    for elem in values:
      inp = inp + f"('{elem.name}', {elem.height}, '{elem.created}'), "
    inp = inp[:-2]
    try:
      query = f"INSERT INTO {table} (name, height, created) VALUES {inp}"
      cur.execute(query)
      con.commit()
      write_log(query)
    except sqlite3.OperationalError:
      print(f"Error when edding data {elem} in table {table}")


def delete(con, table, *conditions):
  """
  A function designed to delete data from a table.
  """
  if con != None:
    cur = con.cursor()
    for cond in conditions:
      try:
        query = f"DELETE FROM {table} WHERE {cond}"
        cur.execute(query)
        con.commit()
        write_log(query)
      except sqlite3.OperationalError:
        print(f"Error when deleting data with condition {cond} from {table}")


def update(con, table, *params):
  """
  A function designed to change data in a table.
  """
  if con != None:
    cur = con.cursor()
    for param in params:
      try:
        query = f"UPDATE {table} SET {param[0]} WHERE {param[1]}"
        cur.execute(query)
        con.commit()
        write_log(query)
      except sqlite3.OperationalError:
        print(f"Update error {param[0]} with the condition {param[1]} in table {table} ")
