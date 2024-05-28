from typing import List
from mathstats import MathStats

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
  from pandas_test import test_pandas_vals
  from sales_by_day_plot_builder import sales_by_day
  from sales_by_month_plot_builder import sales_by_month

  data = read_data(FILE)
  c = count_invoice(data[:5])
  print(f'Всего инвойсов (invoices): {c}')
  c = count_invoice(data[:11])
  print(f'Всего инвойсов (invoices): {c}')
  c = count_invoice(data)
  print(f'Всего инвойсов (invoices): {c}')
  print()

  c = count_different_values(data, 'InvoiceNo')
  print(f'Всего инвойсов выборка (InvoiceNo): {c}')
  c = count_different_values(data, 'InvoiceDate')
  print(f'Всего инвойсов выборка (InvoiceDate): {c}')
  c = count_different_values(data, 'StockCode')
  print(f'Всего инвойсов выборка (StockCode): {c}')
  print()

  c = get_total_quantity(data, 21421)
  print(f'Количество покупок по StockCode 21421: {c}')
  c = get_total_quantity(data, 22178)
  print(f'Количество покупок по StockCode 22178: {c}')
  print()

  data2 = MathStats(FILE2)
  # MathStats mean, max, min, disp, sigma_sq
  print('MathStats mean values: ', data2.mean)
  print('MathStats max values: ', data2.max)
  print('MathStats min values: ', data2.min)
  print('MathStats disp values: ', data2.disp)
  print('MathStats sigma_sq values: ', data2.sigma_sq)
  print()

  # pandas mean, max, min, disp, sigma_sq
  test_pandas_vals()
  print()

  # sales_by_month and sales_by_day graphics
  sales_by_month()
  sales_by_day()


def read_data(file: str) -> List[dict]:
  """
  The function reads data and returns values as a list from dictionaries
  """
  import csv
  data = []
  with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for _r in reader:
      row = _r
      data.append(row)
  return data


def count_invoice(data: List[dict]) -> int:
  """
  The function counts the number of unique Invoices
  """
  return len(set(_el['InvoiceNo'] for _el in data))


def count_different_values(data: List[dict], key: str) -> int:
  """
  The function returns the number of distinct values for the key column in the data list;
  key - InvoiceNo или InvoiceDate или StockCode
  """
  return len(set(_el[f'{key}'] for _el in data))


def get_total_quantity(data: List[dict], stock_code: int) -> int:
  """
  The function returns the total quantity of goods sold for a given stock_code
  """
  return sum(
      int(_el['Quantity']) for _el in data
      if _el['StockCode'] == str(stock_code))


if __name__ == "__main__":
  main()
