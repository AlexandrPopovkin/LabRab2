array_snails_x = []
array_snails_y = []

min_time=100000000000001
def adding():
    x_snail = input('Введите x улитки: \n')
    y_snail = input('Введите y улитки: \n')
    array_snails_x.append(int(x_snail))
    array_snails_y.append(int(y_snail))


def mergeSort(array_snails_x, array_snails_y):
    if len(array_snails_x) == 1 and len(array_snails_y) == 1:
        return array_snails_x, array_snails_y
    middle_x = (len(array_snails_x) - 1) // 2
    middle_y = (len(array_snails_y) - 1) // 2

    list_first_part_x = (array_snails_x[:middle_x + 1])
    list_first_part_y = (array_snails_y[:middle_y + 1])

    mergeSort(list_first_part_x, list_first_part_y)
    list_second_part_x = (array_snails_x[middle_x + 1:])
    list_second_part_y = (array_snails_y[middle_y + 1:])
    mergeSort(list_second_part_x, list_second_part_y)
    print(list_first_part_x, list_second_part_x,list_first_part_y, list_second_part_y )
    time = merge(list_first_part_x, list_second_part_x, list_first_part_y, list_second_part_y)

    return time


def merge(lst1x, lst2x, lst1y, lst2y):
    global min_time
    lstx = []
    lsty = []
    ix = 0
    jx = 0
    iy = 0
    jy = 0
    while ((ix <= len(lst1x) - 1) and (jx <= len(lst2x) - 1) and (iy <= len(lst1y) - 1) and (jy <= len(lst2y) - 1)):
        if (lst1x[ix] != lst2x[jx]) and (lst1y[iy] != lst2y[jy]):
            if ((lst1x[ix] - lst2x[jx]) ** 2 + (lst1y[iy] - lst2y[jy]) ** 2) < min_time:
                lstx.append(lst1x[ix])
                lsty.append(lst1y[iy])
                min_time = ((((lst1x[ix] - lst2x[jx]) ** 2 + (lst1y[iy] - lst2y[jy]) ** 2)) ** 0.5)

                ix += 1
                iy += 1

            else:
                lstx.append(lst2x[jx])
                lsty.append(lst2y[jy])

                jx += 1
                jy += 1

        else:
            if ((abs(lst1x[ix] - lst2x[jx])) + (abs(lst1y[iy] - lst2y[jy]))) < min_time:
                lstx.append(lst1x[ix])
                lsty.append(lst1y[iy])
                min_time = ((abs(lst1x[ix] - lst2x[jx])) + (abs(lst1y[iy] - lst2y[jy])))
                ix += 1
                iy += 1
            else:
                lstx.append(lst2x[jx])
                lsty.append(lst2y[jy])

                jx += 1
                jy += 1

    if ((ix > len(lst1x) - 1) and (iy > len(lst1y) - 1)):
        while ((jx <= len(lst2x) - 1) and (jy <= len(lst2y) - 1)):
            lstx.append(lst2x[jx])
            lsty.append(lst2y[jy])
            jx += 1
            jy += 1
    else:
        while ((ix <= len(lst1x) - 1) and (iy <= len(lst1y) - 1)):
            lstx.append(lst1x[ix])
            lsty.append(lst1y[iy])
            ix += 1
            iy += 1
    print (min_time)
    return lstx, lsty
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
                x = array_snails_x[0]
                y = array_snails_y[0]
                array_snails_x.pop(0)
                array_snails_y.pop(0)

                array_snails_x.sort()
                array_snails_y.sort()
                mergeSort(array_snails_x, array_snails_y)

                array_snails_x.insert(0, x)
                array_snails_y.insert(0, y)
                mergeSort(array_snails_x, array_snails_y)

                print('Первая пара образуется через ', round(min_time / 2, 3), ' секунд(ы)')
                return 0
        elif ind == 3:
            if c == 0:
                print('Улиток здесь еще нет')
            else:
                for i in range(c):
                    print('Улитка', i+1, ' ', array_snails_x[i], ' : ' , array_snails_y[i])


        elif ind == 4:
            array_snails_x.clear()
            array_snails_y.clear()
            c = 0

        else:
            print('Выберите значение из меню\n')


main()
