# Метод elements()

from collections import Counter

count = Counter(x=7, y=5, z=3)

for elem in count.elements():
  print(elem)