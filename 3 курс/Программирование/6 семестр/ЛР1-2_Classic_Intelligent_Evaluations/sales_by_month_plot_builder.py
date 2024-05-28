def sales_by_month():
  import matplotlib.pyplot as plt
  import numpy as np
  import pandas as pd
  
  data = pd.read_csv('MarketingSpend.csv', skiprows=1, names=['Date', 'Offline Spend', 'Online Spend'])
  data['Offline Spend'] = data['Offline Spend'].astype(float)
  data['Online Spend'] = data['Online Spend'].astype(float)
  data['Date'] = pd.to_datetime(data['Date'])
  data['Month'] = data['Date'].dt.to_period('M')
  data = data.drop(columns=['Date'])
  monthly_sales = data.groupby('Month').sum()
  
  sales_types = ['Online Spend', 'Offline Spend']
  sales_data = {type: monthly_sales[type].values for type in sales_types}
  
  months = monthly_sales.index.strftime('%B')

  width = 0.6
  fig, ax = plt.subplots()
  left = np.zeros(len(months))
  for sales_type, data_values in sales_data.items():
      p = ax.barh(months, data_values, width, label=sales_type, left=left)
      left += data_values
      ax.bar_label(p, label_type='center')
  for month, sales_sum in zip(months, monthly_sales.sum(axis=1)):
      ax.text(sales_sum, month,  round(sales_sum, 2) , ha='left', va='center')
  ax.set_title('Monthly Sales')
  ax.legend()
  ax.tick_params(axis='y', labelsize=8)
  plt.tight_layout() 
  
  plt.savefig(f'plots/sales_by_month.png')
