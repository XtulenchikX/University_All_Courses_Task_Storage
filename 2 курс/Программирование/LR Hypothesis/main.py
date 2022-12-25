from n_min import n_min


def main():
  list = []
  op = 1
  while op != "":
    op = input("Введите число: ")
    if op == "":
      break
    else:
      try:
        op = int(op)
      except ValueError:
        print('Ошибка: Допустим ввод только целых чисел!\n')
        quit()
      list.append(op)
  print('Массив: ', list)
  n = int(input('Введите количество чисел в произведении: '))
  result = n_min(list, n)
  print('Минимальное произведение', n, 'элементов массива =', result)


if __name__ == '__main__':
  main()
