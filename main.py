#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
# Если максимальный элемент в таблице больше минимального в 10 раз, то все нули заменить единицами, а
# отрицательные числа заменить на их значения по модулю



import random  # импортируем модуль random для генерации случайных чисел


# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
def random_array(n, m):
    array = []  # инициализируем массив
    # Цикл for. Оператор range выдает диапазон чисел, в данном случае
    # от 0 до n-1
    for i in range(0, n):
        sub_array = []  # инициализируем подмассив
        # Если передать range один аргумент, то нижняя граница 0, в данном
        # случае диапазон чисел будет от 0 до m-1
        for j in range(m):
            # Генерируем слуйчаное число от 0 до 19 и добавляем его в подмассив
            number = random.randrange(-5, 51, 1)
            sub_array.append(number)
        # Добавляем полученный подмассив в основной массив
        array.append(sub_array)
    return array  # возвращаем массив из случайных чисел


def print_array(array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("%d\t" % j, end='')  # выводим каждое значение и табуляцию

        print()  # переход на новую строку

def main():
    array = random_array(6, 7)  # заполняем массив случайными числами
    print_array(array)  # выводим массив на экран
    # Бесконечный цикл while, который закончится только при помощи break
    while True:
        print  # переход на новую строку
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        # Получаем ввод команды от пользователя
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # если команда 1, то заполняем массив заново
            array = random_array(6, 7)
            print_array(array)
            min_digit = array[0][0]
            max_digit = array[0][0]
            for i in array:
                for j in i:
                    if min_digit > j:
                        min_digit = j
                    if max_digit < j:
                        max_digit = j
            print(min_digit, max_digit)
            # После этого условия цикл начнется с начала
        elif key == '2':  # если команда 2, то проверяем условие
            print()  # переход на новую строку
            min_digit = array[0][0]
            max_digit = array[0][0]
            for i in array:
                for j in i:
                    if min_digit > j:
                        min_digit = j
                    if max_digit < j:
                        max_digit = j
            if max_digit/(min_digit - min_digit*2) != 10:
                print("Максимальный элемент в таблице меньше минимального в 10 раз. Задание не будет выполнено.")
            else:
                try:
                    for i in range(len(array)):
                        for j in range(len(array[i])):
                            if array[i][j] == 0:
                                array[i][j] = 1
                            if array[i][j] < 0:
                                array[i][j] = abs(array[i][j])
                except ValueError:
                    break
                print("Отрицательные числа заменены на их значения по модулю")
                print("Все 0 были заменены на 1.")
                print_array(array)
                break  # выход из цикла



        elif key =='3':
            exit()

if __name__ == '__main__':
    main()

