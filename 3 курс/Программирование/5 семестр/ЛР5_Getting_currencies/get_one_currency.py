def get_one_currency(ID = 'R01235'):
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
    return {ID : None}
  else:
    return valute