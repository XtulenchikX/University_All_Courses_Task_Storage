import pytest
from get_one_currency import get_one_currency

def test_goc_1():
  assert get_one_currency('R00000') == {'R00000': None}, "Случай с неверно введенным ID"
  
def test_goc_2():
  currency_inform = get_one_currency()
  eng_key = (list(currency_inform.keys()))[0]
  rus_key = currency_inform[eng_key][0]
  assert eng_key == 'USD'
  assert rus_key == 'Доллар США', "Проверка на получение информации о курсе доллара, при вызове без указания ID"

def test_goc_3():
  currency_inform = get_one_currency('R01270')
  eng_key = (list(currency_inform.keys()))[0]
  rus_key = currency_inform[eng_key][0]
  assert eng_key == 'INR'
  assert rus_key == 'Индийских рупий', "Проверка на получение информации о курсе валюты, при вызове с указанием корректного ID"