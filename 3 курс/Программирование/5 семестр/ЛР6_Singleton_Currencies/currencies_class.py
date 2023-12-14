def singleton(cls):
  instances = {}
  def getinstance():
      if cls not in instances:
          instances[cls] = cls()
      return instances[cls]
  return getinstance

@singleton
class Current_currencies:
  def __init__(self, all_cur = [], one_cur = {}):
    self.all_cur = all_cur
    self.one_cur = one_cur
    self.cur_save = []

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
      valute_cur_name, valute_val = _v.find('Name').text, _v.find(
          'Value').text
      valute_charcode = _v.find('CharCode').text
      valute_val_lst = valute_val.split(',')
      valute_cur_val = (valute_val_lst[0], valute_val_lst[1])
      valute[valute_charcode] = (valute_cur_name, valute_cur_val)
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
        valute_cur_name, valute_val = _v.find('Name').text, _v.find(
            'Value').text
        valute_charcode = _v.find('CharCode').text
        valute_val_lst = valute_val.split(',')
        valute_cur_val = (valute_val_lst[0], valute_val_lst[1])
        valute[valute_charcode] = (valute_cur_name, valute_cur_val)
    if valute == {}:
      self.one_cur = {ID : None}
    else:
      self.one_cur = valute
      self.cur_save.append(valute)

  def return_one_currenc(self):
    return self.one_cur

  def show_cur_save(self):
    return self.cur_save

  def clean_cur_save(self):
    self.cur_save.clear()
    return []