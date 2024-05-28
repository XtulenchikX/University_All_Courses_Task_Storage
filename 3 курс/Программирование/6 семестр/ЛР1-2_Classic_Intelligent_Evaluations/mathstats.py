class MathStats():

  def __init__(self, file):
    import csv

    self._file = file
    self._data = []
    self._mean = None
    self._max = float('-Inf')
    self._min = float('Inf')
    with open(self._file, newline='') as csvfile:
      reader = csv.DictReader(csvfile)

      for _r in reader:
        row = {
            'Date': _r[''],
            'Offline': float(_r['Offline Spend']),
            'Online': float(_r['Online Spend']),
        }
        self._data.append(row)

  @property
  def data(self):
    """
    Function gets data from csv file
    """
    return self._data

  @property
  def mean(self):
    """
    Function find mean value for each type of spend
    """
    sums = {'offline': 0, 'online': 0}
    for _l in self._data:
      sums['offline'] += _l['Offline']
      sums['online'] += _l['Online']

    self._mean = (sums['offline'] / len(self._data),
                  sums['online'] / len(self._data))

    return self._mean

  @property
  def max(self):
    """
    Function find max value for each type of spend
    """
    max_for_two = {'offline': 0, 'online': 0}
    for _l in self._data:
      if _l['Offline'] > max_for_two['offline']:
        max_for_two['offline'] = _l['Offline']
      if _l['Online'] > max_for_two['online']:
        max_for_two['online'] = _l['Online']
    self._max = (max_for_two['offline'], max_for_two['online'])
    return self._max

  @property
  def min(self):
    """
    Function find min value for each type of spend
    """
    min_for_two = {'offline': -1, 'online': -1}
    for _l in self._data:
      if (_l['Offline'] < min_for_two['offline']) or (min_for_two['offline'] < 0):
        min_for_two['offline'] = _l['Offline']
      if (_l['Online'] < min_for_two['online']) or (min_for_two['online'] < 0):
        min_for_two['online'] = _l['Online']
    self._min = (min_for_two['offline'], min_for_two['online'])
    return self._min

  @property
  def disp(self):
    """
    Function find dispersion value for each type of spend
    """
    disps = {'offline': 0, 'online': 0}
    means = self.mean
    for _l in self._data:
        disps['offline'] += (_l['Offline'] - means[0])**2
        disps['online'] += (_l['Online'] - means[1])**2
    self._disp = (disps['offline'] / len(self._data), disps['online'] / len(self._data))
    return self._disp

  @property
  def sigma_sq(self):
    """
    Function find standard deviation value for each type of spend
    """
    from math import sqrt
    disps = self.disp
    self._sigma_sq = (sqrt(disps[0]), sqrt(disps[1]))
    return self._sigma_sq
