# Импорт необходимых модулей
import time
from random import randint


# Функция Gnome Sort
def gnome_sort(array):
    # Инициализация индекса и счетчика обменов
    index = 0
    swaps = 0
    # Запись времени начала сортировки
    start_time = time.time()
    # Основной цикл сортировки
    while index < len(array):
        # Если текущий элемент больше или равен предыдущему, переходим к следующему элементу
        if index == 0 or array[index] >= array[index - 1]:
            index += 1
        else:
            # Если текущий элемент меньше предыдущего, меняем их местами и переходим назад
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1
            swaps += 1
    # Запись времени окончания сортировки
    end_time = time.time()
    # Возвращаем отсортированный массив и время, затраченное на сортировку
    return array, end_time - start_time, swaps


# Основная функция программы
def main():
    # Попытка ввода массива чисел
    try:
        a = list(map(int, input("Введите массив чисел через пробел: ").split()))
    except ValueError:
        print("Вводимые значения должны быть целыми числами")
        return 0
    # Сортировка введенного массива
    sorted_a = gnome_sort(a)[0]
    # Вывод отсортированного массива
    print("Отсортированный массив: ")
    for number in sorted_a:
        print(f"{number:.5g} ", end="")
    print()
    # Попытка ввода трех чисел (кол-ва элементов в списках для сортировки)
    try:
        n1 = int(input("n1 = "))
        n2 = int(input("n2 = "))
        n3 = int(input("n3 = "))
    except ValueError:
        print("Необходимо вводить целые числа")
        return 0
    # Вывод шапки таблицы
    print("-" * 129)
    print(f"|{'':31s}|{n1:^31.7g}|{n2:^31.7g}|{n3:^31.7g}|")
    print(f"|{'':-^31s}|{'':-^31s}|{'':-^31s}|{'':-^31s}|")
    print(f"|{'':31s}|{'время':^15s}|{'перестановки':^15s}|{'время':^15s}|{'перестановки':^15s}|{'время':^15s}|"
          f"{'перестановки':^15s}|")
    print(f"|{'':-^31s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|")

    # Вывод первой строки таблицы
    ordered_list_n1 = list(range(n1))
    ordered_list_n2 = list(range(n2))
    ordered_list_n3 = list(range(n3))
    _, time_n1, swaps_n1 = gnome_sort(ordered_list_n1)
    _, time_n2, swaps_n2 = gnome_sort(ordered_list_n2)
    _, time_n3, swaps_n3 = gnome_sort(ordered_list_n3)
    print(f"|{'упорядоченный список':^31s}|{time_n1:^15.6g}|{swaps_n1:^15.6g}|{time_n2:^15.6g}|{swaps_n2:^15.6g}|"
          f"{time_n3:^15.6g}|{swaps_n3:^15.6g}|")
    print(f"|{'':-^31s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|")

    # Вывод второй строки таблицы
    random_list_n1 = [randint(1, n1 * 10) for _ in range(n1)]
    random_list_n2 = [randint(1, n2 * 10) for _ in range(n2)]
    random_list_n3 = [randint(1, n3 * 10) for _ in range(n3)]
    _, time_n1, swaps_n1 = gnome_sort(random_list_n1)
    _, time_n2, swaps_n2 = gnome_sort(random_list_n2)
    _, time_n3, swaps_n3 = gnome_sort(random_list_n3)
    print(f"|{'случайный список':^31s}|{time_n1:^15.6g}|{swaps_n1:^15.6g}|{time_n2:^15.6g}|{swaps_n2:^15.6g}|"
          f"{time_n3:^15.6g}|{swaps_n3:^15.6g}|")
    print(f"|{'':-^31s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|{'':-^15s}|")

    # Вывод третьей строки таблицы
    reversed_list_n1 = list(range(n1, 0, -1))
    reversed_list_n2 = list(range(n2, 0, -1))
    reversed_list_n3 = list(range(n3, 0, -1))
    _, time_n1, swaps_n1 = gnome_sort(reversed_list_n1)
    _, time_n2, swaps_n2 = gnome_sort(reversed_list_n2)
    _, time_n3, swaps_n3 = gnome_sort(reversed_list_n3)
    print(f"|{'упорядоченный в обр. порядке':^31s}|{time_n1:^15.6g}|{swaps_n1:^15.6g}|{time_n2:^15.6g}|"
          f"{swaps_n2:^15.6g}|{time_n3:^15.6g}|{swaps_n3:^15.6g}|")
    print("-" * 129)


if __name__ == "__main__":
    main()
