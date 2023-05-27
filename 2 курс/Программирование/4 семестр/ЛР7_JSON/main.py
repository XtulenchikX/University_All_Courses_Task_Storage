import json


def load_json(file_name):
  """
    Reading and loading json
    
    :param file_name: name of JSON
    :return: data of JSON
  """
  try:
    f = open(f'{file_name}')
  except FileNotFoundError:
    print('File not found')

  except PermissionError:
    print('No rights to read the file')

  else:
    res = []
    try:
      data = json.load(f)
    except json.JSONDecodeError as e:
      print(f'Error reading JSON: {e}')
    else:
      for el in data:
        keys = ['name', 'gender', 'email', 'phone', 'address', 'friends']
        for key in keys:
          if key not in el:
            raise ValueError(
              print(f'Error reading, missing field: {key}')
            )
            
        res.append((el['name'], el['gender'], el['email'], el['address'],
                    el['friends']))
    if res == []:
      raise ValueError(
        print('No data available')
      ) 
      return
    f.close()
    return res


def print_json(data):
  """
    Output data from json to the screen with pprint

    :param data: loaded JSON data
    :return: None
  """
  if data == None:
    return
  import pprint
  pprint.pprint(data)


def add_users_data():
  """
    Adding user data from the keyboard

    :return: dictionary with user-entered data
    """
  name = input("Enter name: ")
  gender = input("Enter gender: ")
  email = input("Enter email: ")
  phone = input("Enter phone: ")
  address = input("Enter address: ")
  friends = input("Enter friends by separating them with commas: ").split(',')
  return {
    'name': name,
    'gender': gender,
    'email': email,
    'phone': phone,
    'address': address,
    'friends': friends
  }


def save_json(f, data):
  """
    Saving the received data to a json file

    :param f: file descriptor
    :param data: data to save
    :return: None
    """
  try:
    serialized_data = json.dumps(data)
    f.writelines([
      serialized_data,
    ])
  except Exception:
    print('Error writing to JSON')

def insertion(file_name):
  """
  Combines functions add_users_data и save_json, when called it asks the user about the need to execute, if 'y' executes functions add_users_data и save_json.

  :param file_name: file name where to save
  :return: None
  """
  answer = str(input('Do you want to input user Data y/n?'))
  if answer == 'y':
    user_data = add_users_data()
    try:
      with open(file_name, 'w') as f:
        save_json(f, user_data)
    except PermissionError:
      print('No rights to write the file')
  else:
    print('Okay!')
    

if __name__ == '__main__':
  file_name1 = 'data.json'
  file_name2 = 'clients_data.json'

  insertion(file_name2)
  
  data = load_json(file_name1)
  
  print_json(data)
