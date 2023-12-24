# Неделин Никита ИУ7-16Б
# Подключение библиотек
import re
from random import randint

# Словарь функций
funcs = {
    "string": str,
    "int": int,
    "float": float
}
# Ширина столбца
column_width = 20


# Функция для извлечения заголовка из файла
def get_header(file):
    # Список доступных типов данных
    available_types = ["string", "int", "float"]
    # Чтение первой строки файла, которая содержит заголовок
    header_line = file.readline()
    # Создание списков для хранения имен столбцов и их типов
    column_names = []
    column_types = []
    # Разделение строки заголовка на отдельные столбцы
    for column in header_line.split("|"):
        # Поиск соответствия в строке столбца с шаблоном
        match = re.search('''"([^"]*)":([^|]*)''', column)
        # Если соответствие найдено
        if match:
            # Добавление имени столбца в список
            column_names.append(match.group(1))
            # Если тип столбца в списке доступных типов, добавление его в список
            if match.group(2).strip() in available_types:
                column_types.append(match.group(2).strip())
            # Если тип столбца не в списке доступных типов, возвращение None
            else:
                return None, None
        # Если соответствие не найдено, возвращение None
        else:
            return None, None
    # Возвращение списков имен столбцов и их типов
    return column_names, column_types


# Функция печатает заголовок таблицы
def print_table_header(column_names, column_types):
    # Создание строки для верхней границы таблицы
    string = "─" * column_width + "┬"
    # Печать верхней границы таблицы
    print("┌", string * len(column_names), end="", sep="")
    print("─" * column_width, "┐", sep="")
    # Печать вертикальной линии и начала первой строки таблицы
    print("│", end="")
    # Добавление "Номер записи" в начало списка имен столбцов
    column_names = ["Номер записи"] + column_names
    # Печать имен столбцов
    for column_name in column_names:
        print(f"{column_name.strip():{column_width}s}│", end="")
    # Печать новой строки
    print()
    # Печать вертикальной линии
    print("│", end="")
    # Добавление пробела в начало списка типов столбцов
    column_types = [" "] + column_types
    # Печать типов столбцов
    for column_type in column_types:
        print(f"{column_type.strip():{column_width}s}│", end="")
    # Печать новой строки
    print()
    # Создание строки для нижней границы таблицы
    string = "─" * column_width + "┼"
    # Печать нижней границы таблицы
    print("├", string * (len(column_names) - 1), "─" * column_width, "┤", sep="")


# Функция печати строки
def print_row(row, row_number, column_types):
    # Разделение строки на элементы по символу "|"
    row = row.split("|")
    # Проверка на равенство количества элементов в строке и количества типов столбцов
    if len(row) != len(column_types):
        return False
    # Цикл по элементам строки
    for i in range(len(column_types)):
        # Попытка применить функцию, соответствующую типу столбца, к элементу строки
        try:
            func = funcs[column_types[i]]
            func(row[i])
        # Если в процессе возникла ошибка, функция возвращает False
        except ValueError:
            return False
    # Добавление номера строки в начало строки и удаление пробелов в начале и конце каждого элемента строки
    row = [str(row_number)] + row
    row = [column.strip() for column in row]
    # Цикл печати строки, пока она не станет пустой
    while row != [""] * (len(column_types) + 1):
        print("│", end="")
        # Цикл по элементам строки
        for i in range(len(row)):
            # Если длина элемента строки больше ширины столбца, то выводим только часть строки,
            # соответствующую ширине столбца
            if len(row[i]) > column_width:
                text = row[i][:column_width]
                row[i] = row[i][column_width:]
            # Если длина элемента строки меньше или равна ширине столбца, то выводим весь элемент строки
            else:
                text = row[i]
                row[i] = ""
            # Вывод элемента строки, отформатированного под ширину столбца
            print(f"{text:{column_width}s}│", end="")
        print()
    return True


# Вывод футера таблицы
def print_footer(column_names):
    string = ("─" * column_width + "┴") * len(column_names)
    print("└", string, "─" * column_width, "┘", sep="")


# Функция для отображения содержимого базы данных из файла
def display_db(filepath):
    try:
        # Открываем файл для чтения
        file = open(filepath, "r")
    except OSError:
        # Если файл не существует или недостаточно прав для его чтения, выводим сообщение об ошибке и возвращаем False
        print("Заданного файла не существует или недостаточно прав для его чтения")
        return False
    # Получаем заголовки столбцов и их типы
    column_names, column_types = get_header(file)
    # Если заголовки или типы столбцов не определены, выводим сообщение об ошибке и возвращаем False
    if not column_types or not column_names:
        print("Неправильный заголовок базы данных")
        return False
    # Выводим заголовок таблицы
    print_table_header(column_names, column_types)
    # Читаем первую строку файла
    row = file.readline()
    # Инициализируем номер строки
    row_number = 1
    # Читаем строки файла до конца
    while row:
        # Если строка не может быть отпечатана, выводим сообщение об ошибке и возвращаем False
        if not print_row(row, row_number, column_types):
            print_footer(column_names)
            print(f"ошибка чтения базы данных на строчке {row_number}")
            return False
        # Увеличиваем номер строки
        row_number += 1
        # Читаем следующую строку файла
        row = file.readline()
    # Выводим подвал таблицы
    print_footer(column_names)
    # Закрываем файл
    file.close()
    # Возвращаем True, если все строки файла были успешно прочитаны
    return True


# Функция инициализации базы данных
def init_db(filepath):
    # Заголовок базы данных
    default_header = '"field1":string|"field2":float|"field3":int'
    # Количество строк, которые будут записаны в файл
    default_rows_count = 5
    # Алфавит, который будет использоваться для генерации строк
    alph = "abcdefghijklmnopqrstuvwxyz1234567890"
    try:
        # Открываем файл для записи
        file = open(filepath, "w")
    except PermissionError:
        # Если у нас нет прав на запись в файл, выводим сообщение об ошибке и возвращаем False
        print("Нет прав на запись в файл")
        return False
    except OSError:
        # Если выбранная директория не существует или у нас недостаточно прав на создание/перезапись файлов в ней,
        # выводим сообщение об ошибке и возвращаем False
        print("Выбранная директория не существует либо недостаточно прав на создание/перезапись файлов в ней")
        return False
    # Записываем заголовок в файл
    file.write(default_header + "\n")
    # Генерируем строки и записываем их в файл
    for _ in range(default_rows_count):
        string = ""
        for _ in range(10):
            string += alph[randint(0, len(alph) - 1)]
        string += "|"
        string += str(randint(10, 500) / randint(20, 60))
        string += "|"
        string += str(randint(10, 1000000000))
        string += "\n"
        file.write(string)


# Функция для вставки данных в базу данных
def insert_db(filepath):
    try:
        # Открываем файл для чтения
        file = open(filepath, "r")
    except OSError:
        # Если файл не существует или нет прав на чтение, выводим сообщение об ошибке и возвращаем False
        print("Заданного файла не существует или недостаточно прав для его чтения")
        return False
    # Получаем имена и типы столбцов из файла
    column_names, column_types = get_header(file)
    # Закрываем файл после чтения
    file.close()
    # Если имена или типы столбцов не определены, выводим сообщение об ошибке и возвращаем False
    if not column_types or not column_names:
        print("ERROR bad db header")
        return False
    try:
        # Открываем файл для записи
        file = open(filepath, "a")
    except PermissionError:
        # Если нет прав на запись, выводим сообщение об ошибке и возвращаем False
        print("Недостаточно прав для записи")
        return False
    # Инициализируем строку для записи
    string = ""
    # Цикл по каждому столбцу
    for i in range(len(column_types)):
        # Получаем значение для столбца от пользователя
        s = input(f"Введите {column_names[i]}({column_types[i]}): ")
        # Если введен символ "|", выводим сообщение об ошибке и возвращаем False
        if "|" in s:
            print("Введен структурный символ базы данных")
            return False
        # Пытаемся применить функцию для проверки типа данных
        try:
            func = funcs[column_types[i]]
            func(s)
        except ValueError:
            # Если тип данных неверен, выводим сообщение об ошибке, закрываем файл и возвращаем False
            print("Невозможное значение для этого типа данных")
            file.close()
            return False
        # Добавляем значение в строку для записи
        string += f"{s.strip()}|"
    # Удаляем последний символ "|" и добавляем символ новой строки
    string = string[:-1] + "\n"
    # Записываем строку в файл
    file.write(string)
    # Закрываем файл после записи
    file.close()


def search_by_column(filepath, filter_string="test"):
    try:
        # Открываем файл на чтение
        file = open(filepath, "r")
    except OSError:
        # Если файл не существует или нет прав на чтение, выводим сообщение об ошибке и возвращаем False
        print("Заданного файла не существует или недостаточно прав для его чтения")
        return False
    # Получаем заголовки столбцов и их типы
    column_names, column_types = get_header(file)
    # Если заголовки столбцов или их типы отсутствуют, выводим сообщение об ошибке и возвращаем False
    if not column_types or not column_names:
        print("ERROR bad db header")
        return False
    # Выводим заголовки таблицы
    print_table_header(column_names, column_types)
    # Читаем первую строку файла
    row = file.readline()
    row_number = 1
    # Читаем строки файла до конца
    while row:
        # Разделяем строку на части по символу "|"
        data = row.split("|")
        # Если количество частей не равно 3, выводим сообщение об ошибке и возвращаем False
        if len(data) != 3:
            print_footer(column_names)
            print(f"ошибка чтения базы данных на строчке {row_number}")
            return False
        # Проверяем, соответствует ли первый столбец строки фильтрующей строке
        column = data[0]
        if column != filter_string:
            row_number += 1
            row = file.readline()
            continue
        # Если строка не может быть выведена, выводим сообщение об ошибке и возвращаем False
        if not print_row(row, row_number, column_types):
            print_footer(column_names)
            print(f"ошибка чтения базы данных на строчке {row_number}")
            return False
        row_number += 1
        row = file.readline()
    # Выводим нижний колонтитул таблицы
    print_footer(column_names)
    # Закрываем файл
    file.close()
    # Возвращаем True, если все строки были успешно обработаны
    return True


def search_by_two_columns(filepath, filter_string="test", filter_int=12):
    # Попытка открыть файл
    try:
        file = open(filepath, "r")
    except OSError:
        # Если файл не существует или недостаточно прав для чтения, выводим сообщение об ошибке и возвращаем False
        print("Заданного файла не существует или недостаточно прав для его чтения")
        return False
    # Получаем заголовки столбцов и их типы
    column_names, column_types = get_header(file)
    # Если заголовки столбцов или их типы отсутствуют, выводим сообщение об ошибке и возвращаем False
    if not column_types or not column_names:
        print("ERROR bad db header")
        return False
    # Выводим заголовок таблицы
    print_table_header(column_names, column_types)
    # Читаем первую строку файла
    row = file.readline()
    row_number = 1
    # Пока строка не пустая, продолжаем чтение и обработку строк
    while row:
        # Разделяем строку на данные
        data = row.split("|")
        # Если количество данных не равно трем, выводим сообщение об ошибке и возвращаем False
        if len(data) != 3:
            print_footer(column_names)
            print(f"ошибка чтения базы данных на строчке {row_number}")
            return False
        # Пытаемся преобразовать третью колонку в целое число
        try:
            int(data[2])
        except ValueError:
            # Если преобразование не удалось, выводим сообщение об ошибке и возвращаем False
            print_footer(column_names)
            print(f"ошибка чтения базы данных на строчке {row_number}")
            return False
        # Если данные не соответствуют фильтру, пропускаем строку и переходим к следующей
        if data[0] != filter_string or int(data[2]) != filter_int:
            row_number += 1
            row = file.readline()
            continue
        # Если данные соответствуют фильтру, выводим строку
        if not print_row(row, row_number, column_types):
            print_footer(column_names)
            print(f"ошибка чтения базы данных на строчке {row_number}")
            return False
        row_number += 1
        row = file.readline()
    # Выводим подвал таблицы
    print_footer(column_names)
    # Закрываем файл
    file.close()
    # Возвращаем True, если поиск прошел успешно
    return True


# Главная функция программы
def main():
    # Путь к файлу базы данных
    db_path = ""
    # Бесконечный цикл, показывающий меню и обрабатывающий выбор пользователя
    while True:
        # Вывод меню
        print("1. Выбрать файл",
              "2. Инициализировать базу данных в файле",
              "3. Вывести содержимое базы данных",
              "4. Добавить запись в конец базы данных",
              "5. Поиск по одному полю",
              "6. Поиск по двум полям", sep="\n")
        # Бесконечный цикл, показывающий меню и обрабатывающий выбор пользователя
        while True:
            try:
                # Получение выбора пользователя
                option = int(input("Выберите пункт меню: "))
                # Проверка выбора пользователя
                if option > 6 or option < 1:
                    print("Нет такого пункта меню")
                else:
                    break
            except ValueError:
                print("Необходимо вводить целые числа")
        # Выбор действия в зависимости от выбора пользователя
        if option == 1:
            db_path = input("Введите путь до файла базы данных: ")
            if db_path[-4:] != ".txt":
                db_path = ""
                print("Введен некорректный путь для базы данных, он не будет сохранен")
        elif option == 2:
            init_db(db_path)
        elif option == 3:
            display_db(db_path)
        elif option == 4:
            insert_db(db_path)
        elif option == 5:
            filter_string = input("Введите строчку для поиска по field1: ")
            search_by_column(db_path, filter_string)
        elif option == 6:
            try:
                filter_string = input("Введите строчку для поиска по field1: ")
                filter_int = int(input("Введите целое число для поиска по field3: "))
                search_by_two_columns(db_path, filter_string, filter_int)
            except ValueError:
                print("Для поиска по field3 необходимо вводить целые числа")


if __name__ == "__main__":
    main()
