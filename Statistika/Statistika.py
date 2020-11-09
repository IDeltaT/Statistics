#----------------------------------------------
# Program by Krasnokutskiy.I.
# VKB-33
#
# Version   ---Date---    ----- Info -----
#   1.0     20.10.2020    Initial version
#
# Statistics 
# (Нахождение выборочного среднего, дисперсии, 
# среднего квадратического отклонения, 
# Построение Гистограммы и Полигона частот)
#----------------------------------------------

from collections import Counter
from math import sqrt, log10
import matplotlib.pyplot as plt

# File name: BitCoinCost.txt; Fish.txt; test.txt, data.txt

def read_file(file_name):
    '''
    Чтение и заполнение генеральной совокупности из файла.

    :param file_name: Имя файла (путь к файлу)
    :type  file_name: str
    :format: новое значение с новой строки

    :return: Возвращает список генеральной совокупности
    :rtype:  list

    Формат файла - каждое значение в новой строке.
    '''

    X_gen = []

    with open(file_name) as file:
        for line in file:
            X_gen.append(int(line.rstrip()))
    return X_gen
   

def print_sequence(sequence):
    '''
    Печать совокупности.

    :param sequence: совокупность
    :type  sequence: list
    '''

    for val in sequence:
        print(val, end = ', ')


def calculate_sample_mean(range_counter, sequence_len):
    '''
    Вычисление выборочного среднего значения 

    :param range_counter: Частотный словарь совокупности 
    :type  range_counter: dict

    :param sequence_len: Дина генеральной совокупности
    :type  sequence_len: int

    :return: Возвращает выборочное среднее значение
    :rtype:  float
    '''

    sample_mean = 0

    for val in range_counter:
        sample_mean += val * range_counter[val]
    sample_mean /= sequence_len
    
    return sample_mean


def calculate_dispersion(range_counter, sequence_len, sample_mean, type = 0):
    '''
    Вычисление выборочной или исправленной дисперсии 

    :param range_counter: Частотный словарь совокупности 
    :type  range_counter: dict

    :param sequence_len: Дина совокупности
    :type  sequence_len: int

    :param sample_mean: Выборочное среднее значение
    :type  sample_mean: float

    :param type: Тип дисперсии (default 0)
    :type type:  int
    #alignment = 0: - Выборочная
    #alignment = 1: - Исправленная 

    :return: Возвращает выборочную или исправленную дисперсию 
    :rtype:  float
    '''

    dispersion = 0

    for val in range_counter:
        dispersion += range_counter[val] * (val - sample_mean)**2
    dispersion /= sequence_len

    if(type):
        # Исправленная
        return dispersion * (sequence_len / (sequence_len - 1))
    else:
        # Выборочная
        return dispersion


def calculate_standard_deviation(dispersion):
    '''
    Вычисление среднего квадратического отклонения 

    :param dispersion: Выборочная или исправленная дисперсия 
    :type  dispersion: float

    :return: Возвращает среднее квадратическое отклонение 
    :rtype:  float
    '''

    standard_deviation = sqrt(dispersion)
    return standard_deviation


def polygon_print(range_counter_keys, range_counter_val, skip = 1):
    '''
    Печать Полигона.

    :param range_counter_keys: Значения совокупности
    :type  range_counter_keys: set

    :param range_counter_val: Частоты значений совокупности
    :type  range_counter_val: list

    :param skip: Пропуск элементов в выборке (default 1)
    :type  skip: int
    '''

    range_counter_keys_sorted = sorted(list(range_counter_keys))

    plt.plot(range_counter_keys_sorted, range_counter_val)

    if(skip > 1):
        plt.title('Выборка каждый ' + str(skip))
    else:
        plt.title('(Генеральная совокупность)')
    
    plt.show()


def optimal_partition(sequence_len):
    '''
    Вычисление оптимального разбиения по формуле Стерджеса

    :param sequence_len: Дина совокупности
    :type  sequence_len: int

    :return: Возвращает оптимальное разбиение по формуле Стерджеса
    :rtype:  int
    '''

    partition = 1 + 3.322 * log10(sequence_len)
    return int(partition)


def fill_intervals():



def print_bar_graph(sequence, partition = 20, skip = 1, auto_format_x = 0):
    '''
    Печать Гистограммы.

    :param sequence: совокупность
    :type  sequence: list

    :param partition: Кол-во столбиков разбиения (default 20)
    :type  partition: int

    :param skip: Пропуск элементов в выборке (default 1)
    :type  skip: int

    :param auto_format_x: Поворот значений оси x (default 0)
    :type  auto_format_x: int
    #auto_format_x = 0: - поворот на 90 градусов
    #auto_format_x = 1: - авто-поворот
    '''

    sequence_min = min(sequence)
    sequence_max = max(sequence)

    global_interval = sequence_max - sequence_min
    print("Общий интервал: ", global_interval)

    interval_len = int(global_interval / partition)
    print("Длина интервала: ", interval_len)

    intervals = []
    ticks = []

    # Добавление интервалов и заполнение делений по оси x
    sequence_min_copy = sequence_min
    #for i in range(partition + 3):
    for i in range(partition):
        intervals.append({(sequence_min_copy, sequence_min_copy + interval_len) : 0})
        ticks.append(sequence_min_copy)
        sequence_min_copy += interval_len

    # Заполнение интервалов попадающими в них значениями
    for i in sequence:
        for j in intervals:
            key = list(j.keys())
            left_board = key[0][0]
            right_board = key[0][1]
            if (left_board <= i < right_board):
                j[key[0]] += 1
                continue

    #################################################################################
    n = 1
    for i in intervals:
        print('n' + str(n), list(i.keys())[0], '=', list(i.values())[0])
        n += 1

    a = 92.3
    D = 237.29000000000002



    ##################################################################################

    heights = []

    # Заполнение высот
    for i in intervals:
        heights.append(list(i.values())[0] / interval_len)

    x = ticks
    y = heights

    fig, ax = plt.subplots()
    ax.bar(x, y, width = interval_len, edgecolor = 'black', align = 'edge')

    # Отмечаем все значения на оси x
    ax.set_xticks(x)

    fig.set_figwidth(8)    #  ширина Figure
    fig.set_figheight(6)   #  высота Figure

    # Поворот значений оси x
    if(auto_format_x):
        # Автоповорот
        fig.autofmt_xdate() 
    else:
        # Поворот на 90 градусов
        plt.xticks(rotation = 90) 

    if(skip > 1):
        plt.title('Выборка каждый ' + str(skip))
    else:
        plt.title('(Генеральная совокупность)')

    plt.show()


def full_analysis_gen(sequence, type = 0, partition = 20, skip = 1, polygon = 1, bar_graph = 1):
    '''
    Полный анализ совокупности

    :param sequence: совокупность
    :type  sequence: list

    :param type: Выбор между Ген. совокупностью и выборкой (default 0)
    :type  type: int
    #type = 0: - Генеральная совокупность
    #type = 1: - Выборка

    :param partition: Кол-во столбиков разбиения (default 20)
    :type  partition: int

    :param skip: Пропуск элементов в выборке (default 1)
    :type  skip: int

    :param polygon: Построение полигона (default 1)
    :type  polygon: int
    #polygon = 0: - Построить полигон
    #polygon = 1: - Не строить полигон

    :param bar_graph: Построение гистограммы (default 1)
    :type  bar_graph: int
    #bar_graph = 0: - Построить гистограмму
    #bar_graph = 1: - Не строить гистограмму
    '''

    sequence_len = len(sequence)

    if not(type):
        print('Генеральная совокупность (Xген): ')
    else:
        print('Выборка каждый ' + str(skip) + ': ')

    print_sequence(sequence)

    print('\n\n')

    # Сортировка изначальной совокупности
    sequence_sorted = sorted(sequence)
    print('Вариационный ряд: ')
    print_sequence(sequence_sorted)

    print('\n\n')

    # Счетчик элементов в совокупности
    range_counter = Counter(sequence_sorted)

    range_counter_val = list(range_counter.values()) # Значения 
    range_counter_keys = set(range_counter.elements()) # Ключи 

    # Расчет выборочного среднего значения
    sequence_average_value = calculate_sample_mean(range_counter, sequence_len)
    if not(type):
        print('Среднее значение генеральной совокупности: ', sequence_average_value)
    else:
        print('Среднее значение выборки: ', sequence_average_value)

    # Расчет дисперсии
    dispersion = calculate_dispersion(range_counter, sequence_len, sequence_average_value, 0)
    if not(type):
        print('Дисперсия генеральной совокупности: ', dispersion)
    else:
        print('Дисперсия выборочная: ', dispersion)
        dispersion_fix = calculate_dispersion(range_counter, sequence_len, sequence_average_value, 1)
        print('Дисперсия исправленная: ', dispersion_fix)

    # Расчет среднего квадратического отклонения
    deviation = calculate_standard_deviation(dispersion)
    if not(type):
        print('Среднее квадратическое отклонение генеральной совокупности: ', deviation)
    else:
        print('Выборочное среднее квадратическое отклонение: ', deviation)
        deviation_fix = calculate_standard_deviation(dispersion_fix)
        print('Исправленное среднее квадратическое отклонение: ', deviation_fix)

    # Вывод полигона
    if(polygon):
        polygon_print(range_counter_keys, range_counter_val, skip)

    # Вывод гистограммы
    if(bar_graph):
        print_bar_graph(sequence_sorted, partition, skip)


def sample(main_sequence, start = 0, stop = 1, step = 1):
    '''
    Выборка из совокупности начиная с номера start, заканчивая номером stop,
    с шагом step.

    :param main_sequence: совокупность 
    :type  main_sequence: list

    :param start: Начало среза (default 0)
    :type  start: int

    :param stop: Конец среза (default 1)
    :type  stop: int

    :param step: Шаг среза (default 1)
    :type  step: int

    :return: Возвращает выборку из заданной совокупности
    :rtype:  list
    '''

    new_sequence = main_sequence[start - 1 : stop : step]
    return new_sequence


def main():
    '''
    Главная функция.
    Пример работы программы.
    '''

    # Чтение и печать генеральной совокупности
    X_gen = read_file('Fish.txt')

    '''
    # Анализ генеральной совокупности
    full_analysis_gen(X_gen, type = 0, partition = 20, skip = 1, polygon = 1, bar_graph = 1)
    print('Всего элементов: ', len(X_gen))

    print('\n\n')
    print('------------------------------------------------------------------------------------------------------------------')
    print('\n\n')

    # Анализ выборки через 2 (Построение гистограммы)
    sequence_2 = sample(X_gen, 1, len(X_gen), 2)
    full_analysis_gen(sequence_2, type = 1, partition = 20, skip = 2, polygon = 0, bar_graph = 1)
    print('Всего элементов: ', len(sequence_2))

    print('\n\n')
    print('------------------------------------------------------------------------------------------------------------------')
    print('\n\n')

    # Анализ выборки через 5 (Построение полигона)
    sequence_5 = sample(X_gen, 1, len(X_gen), 5)
    full_analysis_gen(sequence_5, type = 1, partition = 20, skip = 5, polygon = 1, bar_graph = 0)
    print('Всего элементов: ', len(sequence_5))

    print('\n\n')
    print('------------------------------------------------------------------------------------------------------------------')
    print('\n\n')

    # Анализ выборки через 3 (классная часть)
    sequence_k = sample(X_gen, 2, len(X_gen), 3)
    full_analysis_gen(sequence_k, type = 1, partition = 20, skip = 3, polygon = 0, bar_graph = 0)
    print('Всего элементов: ', len(sequence_k))
    '''

    # Проверка критеря Пирсона 
    full_analysis_gen(X_gen, type = 1, partition = 25, skip = 1, polygon = 0, bar_graph = 1)
    print('Всего элементов: ', len(X_gen))



if __name__ == "__main__":
    '''
    Выполнение программы.
    '''
    main()
