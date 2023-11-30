def justify_left(text):
    return [line.strip().lstrip() for line in text]


def justify_right(text):
    max_length = max(len(line) for line in text)
    return [line.strip().rjust(max_length) for line in text]


def justify_width(text):
    max_length = max(len(line) for line in text)
    return [f"{line.strip():^{max_length}s}" for line in text]


def main():
    while True:
        text = [
            "— Потрудитесь мне сказать что-нибудь о Крестовом походе Людовика Святого, — сказал он,",
            "покачиваясь на стуле и задумчиво глядя себе под ноги. — Сначала вы мне скажете о причинах,",
            "побудивших короля французского взять крест, — сказал он, поднимая брови и указывая пальцем на",
            "чернильницу, — потом объясните мне общие характеристические черты этого похода, — прибавил он,",
            "делая всей кистью движение такое, как будто хотел поймать что-нибудь, — и, наконец, влияние",
            "этого похода на европейские государства вообще, — сказал он, ударяя тетрадями по левой стороне",
            "стола, — и на французское королевство в особенности, — заключил он, ударяя по правой стороне",
            "стола и склоняя голову направо."
        ]
        print("1. Выровнять текст по левому краю.\n"
              "2. Выровнять текст по правому краю.\n"
              "3. Выровнять текст по ширине.\n")
        n = int(input("Введите число "))
        if n == 1:
            text = justify_left(text)
        elif n == 2:
            text = justify_right(text)
        elif n == 3:
            text = justify_width(text)
        print("\n".join(text))
        print("\n\n")
        print("123")


if __name__ == "__main__":
    main()
