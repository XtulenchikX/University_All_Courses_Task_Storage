# Подсчёт наиболее часто встречающихся слов в тексте с помощью метода класса Count()

from collections import Counter

with open('text.txt') as inp:
    mass_word = inp.read().split()

count = Counter(mass_word).most_common(10)
print(count)
