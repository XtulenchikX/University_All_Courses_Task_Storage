# Метод most_common([n])

from collections import Counter

count = Counter('What Amazing Text i wrote in the past! It was so nice, that i forgot them:)')
print(count.most_common(5))