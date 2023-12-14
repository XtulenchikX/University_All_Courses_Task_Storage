class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
      if cls not in cls._instances:
          cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
      return cls._instances[cls]

class Current_currencies_construct(metaclass=Singleton):
  def __init__(self, all_cur = [], one_cur = {}):
    self.all_cur = all_cur
    self.one_cur = one_cur
    self.cur_save = {}

  def get_currencies(self):
    pass

  def return_currencies(self):
    pass

  def get_one_currenc(self):
    pass

  def return_one_currenc(self):
    pass

  def show_cur_save(self):
    pass

  def clean_cur_save(self):
    pass


class Current_currencies(Current_currencies_construct):
  def get_currencies(self):
    import requests
    from xml.etree import ElementTree as ET

    cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    result = []

    root = ET.fromstring(cur_res_str.content)
    valutes = root.findall(
      "Valute"
    ) 
    for _v in valutes:
      valute_id = _v.get('ID')
      valute = {}
      valute_cur_name, valute_val = _v.find('Name').text, _v.find('Value').text
      valute_nominal = _v.find('Nominal').text
      valute_charcode = _v.find('CharCode').text
      valute_val_lst = valute_val.split(',')
      valute_cur_val = (valute_val_lst[0], valute_val_lst[1])
      valute[valute_charcode] = (valute_cur_name, valute_nominal, valute_cur_val)
      result.append(valute)

    self.all_cur = result

  def return_currencies(self):
    return self.all_cur

  def get_one_currenc(self, ID = 'R01235'):
    import requests
    from xml.etree import ElementTree as ET

    cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    result = {}

    root = ET.fromstring(cur_res_str.content)
    valutes = root.findall(
      "Valute"
    ) 
    valute = {}
    for _v in valutes:
      valute_id = _v.get('ID')
      if str(valute_id) == ID:
        valute_cur_name, valute_val = _v.find('Name').text, _v.find('Value').text
        valute_nominal = _v.find('Nominal').text
        valute_charcode = _v.find('CharCode').text
        valute_val_lst = valute_val.split(',')
        valute_cur_val = (valute_val_lst[0], valute_val_lst[1])
        valute[valute_charcode] = (valute_cur_name, valute_nominal, valute_cur_val)
    if valute == {}:
      self.one_cur = {ID : None}
    else:
      self.one_cur = valute
      self.cur_save[ID] = valute

  def return_one_currenc(self):
    return self.one_cur

  def show_cur_save(self):
    return self.cur_save

  def clean_cur_save(self):
    self.cur_save.clear()
    return []


class Deco_JSON(Current_currencies):
  def __init__(self, component: Current_currencies):
    self.component = component

  def show_cur_save(self):
    import json
    json_cur_save = json.dumps(
      self.component.cur_save,
      sort_keys=False,
      indent = 2,
      ensure_ascii=False,
      separators=(',', ': '))
    return json_cur_save

class Deco_CSV(Deco_JSON):
  def show_cur_save(self):
    import csv
    cur_dict = self.component.cur_save
    
    keys_list = cur_dict.keys()

    my_list = []
    
    for key in keys_list:
      part = cur_dict[key]
      eng = list(part.keys())[0]
      rus = part[eng][0]
      nominal = part[eng][1]
      cur = str(part[eng][2][0]) + '.' + str(part[eng][2][1])
      print(eng, '||||', rus, '||||', nominal, '||||', cur)
      my_list.append({'eng':eng, 'rus':rus, 'nominal':nominal, 'cur':cur})
      
    
    header = ['eng', 'rus', 'nominal', 'cur']

    with open('save.csv', 'w') as file:
      writer = csv.DictWriter(file, fieldnames=header)
      writer.writeheader()
      for row in my_list:
          writer.writerow(row)

    print('Look at save.csv')
    
    