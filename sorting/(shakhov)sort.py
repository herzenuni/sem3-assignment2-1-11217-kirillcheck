# Практическое задание NOD
# Реализуйте два алгоритма сортировки: методом пузырька и быструю сортировку, протестируйте их работу с использованием пакета hypothesis
# Шахов Кирилл
# ИВТ

def sort(x):
  list = []
  for i in x:
      i = str(i)
      s = 0
      for j in i:
          s += int(j)**2
      if 0 == s % 17:
          list.append(i)
  return list

def main():
    print(' Result: ', sort(range(10,100)))

if __name__ == '__main__':
    main()
