array_snails = []

import math

def time(a, b):
    return (math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))/2)
def search(a, p, q, m):
    if len(a) == 2:
        dist = time(a[0], a[1])
        if dist < m:
            p, q = a[0], a[1]
            m = dist
    else:
        for x in range(0, len(a) - 1):
            for y in range(x + 1, len(a)):
                if m > time(a[x], a[y]):
                    m = time(a[x], a[y])
                    p, q = a[x], a[y]
    return p, q, m

def pair(a, p, q, m):
    l = len(a)
    if l <= (3): return (search(a, p, q, m))
    midl = l // 2
    midx = a[midl][0]
    Left_half = a[:midl]
    Right_half = a[midl:]

    p, q, m = pair(Left_half, p, q, m)
    p, q, m = pair(Right_half, p, q, m)
    p, q, m = dist(a, midx, p, q, m)

    return (p, q, m)


def dist(a, xc, p, q, m):
    strip = []
    right, left = xc + int(m), xc - int(m)
    for x in a:
        if x[0] > right:
            break
        elif left <= x[0] <= right:
            strip.append(x)
    strip.sort(key=lambda x: x[1])
    for x in range(0, len(strip)):
        for y in range(x + 1, min((x + 7), len(strip))):
            dist = time(strip[x], strip[y])
            if dist < m:
                p, q = strip[x], strip[y]
                m = dist
    return (p, q, m)

def adding():
    x_snail = int(input('Введите x улитки: \n'))
    y_snail = int(input('Введите y улитки: \n'))
    if (x_snail > 100000000000) or (y_snail > 100000000000):

        print('Введено значение больше максимума')
    else:
        array_snails.append([int(x_snail),int(y_snail)])

def menu():
    print('\nВыберите пункт из меню:\n'
          '--------------------------------\n'
          '1.Добавить улитку в массив\n'
          '2.Посчитать через какое время пара улиток встретится\n'
          '3.Посмотреть координаты улиток в массиве\n'
          '4.Убрать всех улиток\n'
          '0.Завершить работу программы\n'
          '--------------------------------\n')


def main():
    ind = -1
    c = 0
    while ind:
        menu()
        try:
            ind = int(input('Выбор: '))
        except:
            print('Введено некорректное значение')
        if ind == 0:
            return 0

        elif ind == 1:
            adding()
            c += 1
        elif ind == 2:
            if c == 0:
                print('Никогда, улиток нет на участке земли, вы можете добавить их при помощи пункта 1')
            elif c == 1:
                print('Никогда, у вас всего 1 улитка, вы можете добавить их при помощи пункта 1')
            else:
                array_snails.sort()

                arr1, arr2 = array_snails[0], array_snails[1]
                min_time = time(array_snails[0], array_snails[1])
                pt1, pt2, distance = pair(array_snails, arr1, arr2, min_time)


                print('Первая пара образуется через ', round(distance, 3), ' секунд(ы)')
                return 0
        elif ind == 3:
            if c == 0:
                print('Улиток здесь еще нет')
            else:
                for i in range(c):
                    print('Улитка', i+1, ' ', array_snails[i])


        elif ind == 4:
            array_snails.clear()
            c = 0

        else:
            print('Выберите значение из меню\n')

main()
