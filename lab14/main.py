import struct
import string
import random
import os

column_width = 30


def remove_line(db_path, db_format, line_index):
    line_size = struct.calcsize(db_format)
    try:
        with open(db_path, "r+b") as f:
            f.seek(line_size * line_index)
            while True:
                line = f.read(line_size)
                if not line:
                    break
                f.seek(-line_size * 2, os.SEEK_CUR)
                f.write(line)
                f.seek(line_size, os.SEEK_CUR)
            f.truncate(os.path.getsize(db_path) - line_size)
    except PermissionError:
        print("Нет прав на запись в файл")
        return False
    except OSError:
        print("Выбранный файл не существует либо недостаточно прав на создание/перезапись файлов в директории")
        return False


def construct_line(db_format):
    string1 = input("Введите field1(str): ")
    if len(string1) > 30:
        print("Введена слишком большая строка, она будет обрезана")
        string1 = string1[:30]
    string2 = input("Введите field2(str): ")
    if len(string2) > 30:
        print("Введена слишком большая строка, она будет обрезана")
        string2 = string2[:30]
    try:
        int1 = int(input("Введите field3(int): "))
    except ValueError:
        print("Необходимо вводить целые числа")
        return False
    structured_line = struct.pack(db_format, string1.encode(), string2.encode(), int1)
    return structured_line


def add_line(db_path, db_format, line_index):
    line_size = struct.calcsize(db_format)
    new_line = construct_line(db_format)
    if not new_line:
        print("Ошибка ввода новой строки")
        return False
    lines_count = get_lines_count(db_path, db_format)
    if not lines_count:
        return False
    try:
        with open(db_path, 'r+b') as f:
            f.seek(-line_size, os.SEEK_END)
            while lines_count > line_index - 1:
                prev_chunk = f.read(line_size)
                f.write(prev_chunk)
                if line_index == 1:
                    if lines_count - line_index != 0:
                        f.seek(-line_size * 3, os.SEEK_CUR)
                    else:
                        f.seek(0)
                else:
                    f.seek(-line_size * 3, os.SEEK_CUR)
                lines_count -= 1
            if lines_count == 0:
                f.seek(0)
            elif line_index != 1:
                f.seek(line_size, os.SEEK_CUR)
            f.write(new_line)
    except PermissionError:
        print("Нет прав на запись в файл")
        return False
    except OSError:
        print("Выбранный файл не существует либо недостаточно прав на создание/перезапись файлов в директории")
        return False


def get_lines_count(db_path, db_format):
    line_size = struct.calcsize(db_format)
    try:
        with open(db_path, 'rb') as f:
            try:
                f.seek(0, os.SEEK_END)
                size = f.tell()
            except OSError:
                f.seek(0)
                size = f.tell()
    except OSError:
        print("Выбранный файл не существует либо недостаточно прав на создание/перезапись файлов в директории")
        return False
    return size // line_size


def init_db(db_path, db_format):
    try:
        with open(db_path, 'w+b') as f:
            for i in range(5):
                f.write(gen_random_string(db_format))
    except PermissionError:
        print("Нет прав на запись в файл")
        return False
    except OSError:
        print("Выбранный файл не существует либо недостаточно прав на создание/перезапись файлов в директории")
        return False


def gen_random_string(db_format):
    letters = string.ascii_lowercase
    rand_string_1 = ''.join(random.choice(letters) for _ in range(random.randint(2, 10)))
    rand_string_2 = ''.join(random.choice(letters) for _ in range(random.randint(2, 10)))
    rand_int = random.randint(1, 1000000)
    structured_line = struct.pack(db_format, rand_string_1.encode(), rand_string_2.encode(), rand_int)
    return structured_line


def print_lines(db_path, db_format):
    print_table_header(["field1", "field2", "field3"], ["str", "str", "int"])
    line_size = struct.calcsize(db_format)
    try:
        with open(db_path, "rb") as f:
            line = f.read(line_size)
            line_number = 1
            while line:
                line = struct.unpack(db_format, line)
                decoded_line = [line[0].replace(b"\x00", b"").decode(),
                                line[1].replace(b"\x00", b"").decode(), line[2]]
                print_row(decoded_line, line_number)
                line = f.read(line_size)
                line_number += 1
            print_footer()
    except PermissionError:
        print_footer()
        print("Нет прав на запись в файл")
        return False
    except OSError:
        print_footer()
        print("Выбранный файл не существует либо недостаточно прав на создание/перезапись файлов в директории")
        return False


def print_footer():
    el_string = ("─" * column_width + "┴") * 3
    print("└", el_string, "─" * column_width, "┘", sep="")


def print_row(row, row_number):
    row = [str(row_number)] + row
    row = [str(column) for column in row]
    while row != [""] * (3 + 1):
        print("│", end="")
        for i in range(len(row)):
            if len(row[i]) > column_width:
                text = row[i][:column_width]
                row[i] = row[i][column_width:]
            else:
                text = row[i]
                row[i] = ""
            print(f"{text:{column_width}s}│", end="")
        print()
    return True


def print_table_header(column_names, column_types):
    header_string = "─" * column_width + "┬"
    print("┌", header_string * len(column_names), end="", sep="")
    print("─" * column_width, "┐", sep="")
    print("│", end="")
    column_names = ["Номер записи"] + column_names
    for column_name in column_names:
        print(f"{column_name.strip():{column_width}s}│", end="")
    print()
    print("│", end="")
    column_types = [" "] + column_types
    for column_type in column_types:
        print(f"{column_type.strip():{column_width}s}│", end="")
    print()
    header_string = "─" * column_width + "┼"
    print("├", header_string * (len(column_names) - 1), "─" * column_width, "┤", sep="")


def search_by_column(db_path, db_format, filter_string):
    print_table_header(["field1", "field2", "field3"], ["str", "str", "int"])
    line_size = struct.calcsize(db_format)
    try:
        with open(db_path, "rb") as f:
            line = f.read(line_size)
            line_number = 1
            while line:
                line = struct.unpack(db_format, line)
                decoded_line = [line[0].replace(b"\x00", b"").decode(),
                                line[1].replace(b"\x00", b"").decode(), line[2]]
                if decoded_line[0] == filter_string:
                    print_row(decoded_line, line_number)
                line = f.read(line_size)
                line_number += 1
            print_footer()
    except PermissionError:
        print_footer()
        print("Нет прав на запись в файл")
        return False
    except OSError:
        print_footer()
        print("Выбранный файл не существует либо недостаточно прав на создание/перезапись файлов в директории")
        return False


def search_by_two_columns(db_path, db_format, filter_string, filter_int):
    print_table_header(["field1", "field2", "field3"], ["str", "str", "int"])
    line_size = struct.calcsize(db_format)
    try:
        with open(db_path, "rb") as f:
            line = f.read(line_size)
            line_number = 1
            while line:
                line = struct.unpack(db_format, line)
                decoded_line = [line[0].replace(b"\x00", b"").decode(),
                                line[1].replace(b"\x00", b"").decode(), line[2]]
                if decoded_line[0] == filter_string and decoded_line[2] == filter_int:
                    print_row(decoded_line, line_number)
                line = f.read(line_size)
                line_number += 1
            print_footer()
    except PermissionError:
        print_footer()
        print("Нет прав на запись в файл")
        return False
    except OSError:
        print_footer()
        print("Выбранный файл не существует либо недостаточно прав на создание/перезапись файлов в директории")
        return False


def main():
    db_path = ""
    db_format = "30s 30s i"
    while True:
        print("1. Выбрать файл",
              "2. Инициализировать базу данных в файле",
              "3. Вывести содержимое базы данных",
              "4. Добавить запись в базу данных",
              "5. Удалить произвольную запись",
              "6. ---",
              "7. ---", sep="\n")
        while True:
            try:
                option = int(input("Выберите пункт меню: "))
                # Проверка выбора пользователя
                if option > 7 or option < 1:
                    print("Нет такого пункта меню")
                else:
                    break
            except ValueError:
                print("Необходимо вводить целые числа")
        # Выбор действия в зависимости от выбора пользователя
        if option == 1:
            db_path = input("Введите путь до файла базы данных: ")
            if db_path[-4:] != ".bin":
                print("Введен некорректный путь для базы данных, он не будет сохранен")
        elif option == 2:
            init_db(db_path, db_format)
        elif option == 3:
            print_lines(db_path, db_format)
        elif option == 4:
            try:
                number = int(input("Введите номер места на которое вы хотите вставить строку: "))
                if number < 1:
                    print("Необходимо вводить номера строк (>0)")
                    continue
                add_line(db_path, db_format, number)
            except ValueError:
                print("Необходимо вводить целые числа")
        elif option == 5:
            try:
                number = int(input("Введите строки, которую необходимо удалить: "))
                if number < 1:
                    print("Необходимо вводить номера строк (>0)")
                    continue
                remove_line(db_path, db_format, number)
            except ValueError:
                print("Необходимо вводить целые числа")
        elif option == 6:
            filter_string = input("Введите строчку для поиска по field1: ")
            search_by_column(db_path, db_format, filter_string)
        elif option == 7:
            try:
                filter_string = input("Введите строчку для поиска по field1: ")
                filter_int = int(input("Введите целое число для поиска по field3: "))
                search_by_two_columns(db_path, db_format, filter_string, filter_int)
            except ValueError:
                print("Для поиска по field3 необходимо вводить целые числа")


if __name__ == "__main__":
    main()
