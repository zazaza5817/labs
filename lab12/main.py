def align_left(text):
    """
   Выравнивает текст по левому краю.
   :param text: Список строк текста.
   :return: Список строк текста, выровненных по левому краю.
   """
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")
    # Удаляем пробелы слева от каждой строки
    return [line.strip() for line in text]


def align_right(text):
    """
    Выравнивает текст по правому краю.
    :param text: Список строк текста.
    :return: Список строк текста, выровненных по правому краю.
    """
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")
    # Находим максимальную длину строки
    max_length = max(len(line.strip()) for line in text)
    # Выравниваем каждую строку по правому краю
    text = [line.strip().rjust(max_length) for line in text]
    return text



def align_center(text):
    """
    Выравнивает каждую строку в списке по центру и возвращает новый список.
    :param text: Список строк, которые нужно выровнять по центру.
    :return: Новый список строк, где каждая строка выровнена по центру.
    """
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")
    # Находим максимальную длину строки в списке
    max_length = max(len(line) for line in text)
    # Возвращаем новый список, где каждая строка выровнена по центру
    return [f"{line.strip():^{max_length}s}" for line in text]


def fill_center(text):
    """
    Выравнивает каждую строку в списке по центру и возвращает новый список.
    :param text: Список строк, которые нужно выровнять по центру.
    :return: Новый список строк, где каждая строка выровнена по центру.
    """
    for i in range(len(text)):
        while "  " in text[i]:
            text[i] = text[i].replace("  ", " ")
    # Находим максимальную длину строки в исходном тексте
    max_length = max(len(line) for line in text)
    # Создаем пустой список для хранения выровненных строк
    out_text = []
    # Проходимся по каждой строке в исходном тексте
    for i in range(len(text)):
        # Разбиваем строку на слова
        string = text[i].strip().split(" ")
        # Вычисляем количество пробелов, которые нужно добавить после каждого слова
        try:
            spaces_count = (max_length - len(text[i].replace(" ", ""))) // (len(string) - 1)
        except ZeroDivisionError:
            return text
        # Вычисляем остаток от деления количества пробелов на количество слов
        spaces_remainder = (max_length - len(text[i].replace(" ", ""))) % (len(string) - 1)
        # Создаем новую строку, добавляя к каждому слову необходимое количество пробелов
        new_string = ""
        for word in string:
            new_string += word + " " * spaces_count
            if spaces_remainder > 0:
                new_string += " "
                spaces_remainder -= 1
        # Удаляем лишние пробелы с обоих концов строки
        new_string.strip()
        # Добавляем новую строку в список выровненных строк
        out_text.append(new_string)
    # Возвращаем список выровненных строк
    return out_text


def replace_word(text, old_word, new_word):
    """
    Заменяет все вхождения старого слова на новое в тексте.
    :param text: Список строк, в котором будет произведена замена.
    :param old_word: Слово, которое нужно заменить.
    :param new_word: Слово, на которое нужно заменить старое.
    :return: Список строк с замененными словами.
    """
    # Создаем список со всеми возможными вариантами старого слова с пробелами слева и справа
    for char in [" ", ",", "."]:
        # Проходимся по каждой строке в тексте
        for i in range(len(text)):
            # Заменяем старое слово на новое
            text[i] = text[i].replace(f" {old_word}{char}", f" {new_word}{char}")
    # Возвращаем текст с замененными словами
    return text


def delete_word(text, word):
    """
   Удаляет указанное слово в каждой строке текста.
   :param text: Список строк текста.
   :param word: Слово, которое нужно удалить.
   :return: Список строк текста с удаленным словом.
   """
    # Перебираем каждую строку в тексте
    for i in range(len(text)):
        # Заменяем старое слово на пустую строку
        text[i] = text[i].replace(word, '')
    # Возвращаем измененный текст
    return text


def safe_input(type_func, prompt=""):
    """
    Бесконечный цикл для продолжения попыток ввода до тех пор, пока не будет введено корректное значение.
    :param type_func: Функция для преобразования ввода в определенный тип.
    :param prompt: Выводимое приглашение ввода пользователя.
    :return: Преобразованное значение ввода.
    """
    # Бесконечный цикл для продолжения попыток ввода до тех пор, пока не будет введено корректное значение
    while True:
        try:
            # Получаем ввод пользователя
            a = input(prompt)
            # Преобразуем ввод в указанный тип
            a = type_func(a)
            # Возвращаем преобразованное значение
            return a
        except ValueError:
            # Выводим сообщение об ошибке, если ввод не может быть преобразован в указанный тип
            print("Введено неподходящее значение")


def display_text(text):
    """
    Выводит все строки текста.
    :param text: Список строк текста, которые нужно вывести.
    """
    # Выводим каждую строку текста
    print("\n".join(text))


def string_re_part(text, string_len):
    """
    Разбивает текст на строки заданной длины.
    :param text: Список строк, которые нужно объединить и разделить.
    :param string_len: Максимальная длина строки.
    :return: Список строк, где каждая строка имеет длину не более string_len.
    """
    # Создаем новый список строк, в который будем добавлять строки длиной не более string_len
    new_text = ['']
    # Проходим по каждому элементу в тексте
    for token in iterate_text(text, False):
        # Если добавление следующего токена приведет к превышению максимальной длины строки,
        # то добавляем новую строку в new_text
        if len(new_text[-1] + token) > string_len:
            new_text.append('')
        # Добавляем текущий токен и пробел к последней строке в new_text
        new_text[-1] += token + " "
    # Возвращаем новый список строк
    return new_text


def replace_arithmetic_operations(s):
    """
    Заменяет арифметические операции в строке.
    Функция принимает строку, содержащую числа и арифметические операции, и заменяет их на результаты этих операций.
    Операции могут быть сложными, то есть состоять из нескольких чисел и операций.
    :param s: Входная строка, содержащая числа и арифметические операции.
    :return: Список строк, где арифметические операции заменены на результаты этих операций.
    """
    s = "\n".join(s)
    # Создаем список чисел от 0 до 9 в виде строк
    numbers = list(map(str, range(10)))
    i = 0
    # Создаем пустой список для хранения позиций чисел в строке
    number_positions = []
    # Проходимся по строке
    while i < len(s):
        # Если текущий символ - это число
        if s[i] in numbers:
            # Запоминаем начальную позицию числа
            start_index = i
            # Продолжаем проход по строке, пока не встретим не число
            while i < len(s) and s[i] in numbers:
                i += 1
            else:
                # Запоминаем конечную позицию числа
                end_index = i - 1
                # Добавляем начальную и конечную позиции числа в список
                number_positions.append((start_index, end_index))
        i += 1

    # Создаем пустой список для хранения арифметических операций
    operations = []
    # Проходимся по списку позиций чисел
    for i in range(len(number_positions)):
        # Получаем текущую позицию
        position = number_positions[i]
        j = position[1] + 1
        # Пропускаем пробелы после числа
        while j < len(s) and s[j] == " ":
            j += 1
        # Если следующий символ не конец строки
        if j != len(s):
            # Если следующий символ '+'
            if s[j] == "+":
                # Запоминаем операцию как 1
                operation = 1
            # Если следующий символ '-'
            elif s[j] == "-":
                # Запоминаем операцию как -1
                operation = -1
            else:
                # Если следующий символ ни '+', ни '-', пропускаем эту операцию
                continue
            # Переходим к следующему символу
            j += 1
            # Пропускаем пробелы после операции
            while j < len(s) and s[j] == " ":
                j += 1

            # Если следующее число начинается сразу после операции
            if i + 1 < len(number_positions) and number_positions[i + 1][0] == j:
                # Запоминаем операцию и индекс следующего числа
                operations.append(((i, 1), (i + 1, operation)))

    # Создаем пустой список для хранения сложных операций
    complex_operations = []
    # Если есть операции
    if operations:
        # Добавляем первую операцию в список сложных операций
        complex_operations = [[operations[0][0], operations[0][1]]]
        i = 1
        # Проходимся по остальным операциям
        while i < len(operations):
            # Если текущая операция относится к последней сложной операции
            if operations[i][0][0] == complex_operations[-1][-1][0]:
                # Добавляем операцию в последнюю сложную операцию
                complex_operations[-1].append(operations[i][1])
            else:
                # Если текущая операция не относится к последней сложной операции, начинаем новую сложную операцию
                complex_operations.append([operations[i][0], operations[i][1]])
            i += 1

    # Создаем пустой список для хранения результатов
    results = []
    # Проходимся по сложным операциям
    for operation in complex_operations:
        # Инициализируем результат как 0
        result = 0
        # Проходимся по операциям в текущей сложной операции
        for action in operation:
            # Получаем позицию числа для текущей операции
            number = number_positions[action[0]]
            # Добавляем число к результату, умноженное на операцию
            result += int(s[number[0]:number[1] + 1]) * action[1]
        # Добавляем результат, начальную и конечную позиции в список результатов
        results.append((result, number_positions[operation[0][0]][0], number_positions[operation[-1][0]][1]))

    # Если есть результаты
    if results:
        # Инициализируем выходную строку с частью входной строки до первого результата
        out_s = s[:results[0][1]]
        # Проходимся по результатам
        for i in range(len(results)):
            # Добавляем результат в выходную строку
            result = results[i]
            out_s += str(result[0])
            # Если есть следующий результат после текущего
            if i + 1 < len(results):
                # Добавляем часть входной строки между текущим и следующим результатом в выходную строку
                out_s += s[results[i][2] + 1:results[i + 1][1]]
        # Добавляем часть входной строки после последнего результата в выходную строку
        out_s += s[results[-1][2] + 1:]
    else:
        # Если результатов нет, возвращаем входную строку без изменений
        out_s = s
    # Возвращаем выходную строку
    return out_s.split("\n")


def delete_sentence(text):
    """
    Выводит и удаляет из заданного текста предложение, в котором содержится минимальное число слов
    :param: Входной текст состоящий из списка строк.
    :return: Текст без предложения с наименьшим количеством строк.
    """
    sentences = [""]
    for line in text:
        for char in line:
            sentences[-1] += char
            if char == ".":
                sentences.append("")
        sentences[-1] += " /"
    sentences = [str(sentence).strip() for sentence in sentences]
    sentences.pop(-1)
    if not sentences:
        print("В тексте нет предложений")
        return text
    shortest_sentence = str(min(sentences, key=lambda x: len(x.split())))
    if "/" in shortest_sentence and sentences.index(shortest_sentence) > 0:
        sentences[sentences.index(shortest_sentence)-1] += " /"
    sentences.remove(shortest_sentence)
    print("============Самое короткое предложение:")
    print(shortest_sentence.replace("/", ""))
    print("============")
    text = [""]
    for sentence in sentences:
        for char in sentence:
            if char == "/":
                text.append("")
            else:
                text[-1] += char
        text[-1] += " "
    return text



def iterate_text(text, needs_newline):
    """
    Функция для итерации по тексту и выдачи каждого слова (токен) по отдельности.
    :param: Список строк текста.
    :yield token: Слово из текста.
    """
    # Проходимся по каждой строке в тексте
    for string in text:
        # Добавляем символ новой строки в конец строки, если необходимо
        if needs_newline:
            string += "\n"
        # Разбиваем строку на слова
        string = string.split(" ")
        # Проходимся по каждому слову в списке слов
        for token in string:
            # Выдаем слово
            yield token


def main():
    # Создаем список строк
    text = [
        "— Потрудитесь мне сказать что-нибудь о Крестовом походе Людовика Святого, — сказал он,",
        "покачиваясь на стуле и задумчиво глядя себе под ноги. — Сначала вы мне скажете о причинах,",
        "побудивших короля французского взять крест, — сказал он, поднимая брови и указывая пальцем на",
        "чернильницу, — потом объясните мне. общие характеристические черты этого похода, — прибавил он,",
        "делая всей кистью движение такое, как будто хотел поймать что-нибудь, — и, наконец, влияние",
        "этого похода на европейские государства вообще, — сказал он, ударяя тетрадями по левой стороне",
        "стола, — и на французское королевство в особенности, — заключил он, ударяя по правой стороне",
        "стола и склоняя голову направо."
    ]
    # Создаем копию исходного текста
    text_copy = text.copy()

    # Отображаем исходный текст
    display_text(text)

    # Определяем длину строки
    string_len = 90

    # Начинаем бесконечный цикл
    while True:
        # Выводим меню
        print("1. Выровнять текст по левому краю.\n"
              "2. Выровнять текст по правому краю.\n"
              "3. Заполнить текстом по ширине.\n"
              "4. Удалить слово\n"
              "5. Заменить все вхождения заданного слова на другое: \n"
              "6. Заменить все арифметические операции сложения и вычитания на их результат\n"
              "7. Удалить самое короткое по количеству слов предложение\n"
              "8. Заменить текст на исходный\n"
              "9. Переразбить текст на строки\n"
              "10. Выровнять текст по центру")

        # Получаем ввод пользователя
        n = safe_input(int, "Выберите элемент меню: ")

        # Выполняем действия в зависимости от ввода пользователя
        if 0 < n < 11:
            if n == 1:
                text = align_left(text)
            elif n == 2:
                text = align_right(text)
            elif n == 3:
                text = fill_center(text)
            elif n == 4:
                for_remove = input("Введите слово для удаления: ")
                text = delete_word(text, for_remove)
            elif n == 5:
                old_string = input("Введите слово которое необходимо заменить: ")
                new_string = input("Введите слово на которое необходимо заменить: ")
                text = replace_word(text, old_string, new_string)
            elif n == 6:
                text = replace_arithmetic_operations(text)
            elif n == 7:
                text = delete_sentence(text)
            elif n == 8:
                text = text_copy.copy()
            elif n == 9:
                text = string_re_part(text, string_len)
            elif n == 10:
                text = align_center(text)
            # Отображаем измененный текст
            display_text(text)
        else:
            print("Элемента с таким номером нет в меню")


if __name__ == "__main__":
    main()
