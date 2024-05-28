def sales_by_day():
  import matplotlib.pyplot as plt
  import pandas as pd

  data = pd.read_csv('Retail.csv')
  data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
  daily_sales = data.groupby(
      data['InvoiceDate'].dt.dayofyear)['Quantity'].sum()

  plt.figure(figsize=(10, 6))
  plt.scatter(daily_sales.index, daily_sales.values, color='green', alpha=0.7)
  plt.xlabel('Day of Year')
  plt.ylabel('Quantity Sold')
  plt.title('Daily Sales')
  plt.xticks(range(1, 365, 15))
  plt.grid(True)
  plt.tight_layout()

  plt.savefig(f'plots/sales_by_day.png')
