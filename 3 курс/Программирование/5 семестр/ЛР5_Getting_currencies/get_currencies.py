def get_currencies(currencies_ids_lst: list) -> list:
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
    if (str(valute_id) in currencies_ids_lst):
        valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find(
            'Value').text
        valute_charcode = _v.find('CharCode').text
        valute[valute_charcode] = (valute_cur_name, valute_cur_val)
        result.append(valute)
  
  return result