# Метод subtract([iterable-or-mapping])

from collections import Counter

count1 = Counter(x=7, y=5, z=3)
count2 = Counter(x=3, y=2, z=1)

count1.subtract(count2)

print('x: ', count1['x'])
print('y: ', count1['y'])
print('z: ', count1['z'])