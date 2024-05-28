def test_pandas_vals():
  import pandas as pd

  data = pd.read_csv('MarketingSpend.csv')

  print('Pandas mean values:', (data.loc[:, 'Offline Spend'].mean(), data.loc[:, 'Online Spend'].mean()))
  print('Pandas max values:', (data.loc[:, 'Offline Spend'].max(), data.loc[:, 'Online Spend'].max()))
  print('Pandas min values:', (data.loc[:, 'Offline Spend'].min(), data.loc[:, 'Online Spend'].min()))
  print('Pandas disp values:', (data.loc[:, 'Offline Spend'].var(), data.loc[:, 'Online Spend'].var()))
  print('Pandas sigma_sq values:', (data.loc[:, 'Offline Spend'].std(), data.loc[:, 'Online Spend'].std()))
