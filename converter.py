CONVERTERS = {
    1: ("Цельсий -> Фаренгейт",   lambda v: v * 9 / 5 + 32, "°F"),
    2: ("Километры -> Мили",       lambda v: v * 0.621371, "миль"),
    3: ("Килограммы -> Фунты",     lambda v: v * 2.20462, "фунтов"),
    4: ("Метры -> Футы",           lambda v: v * 3.28084, "футов"),
    5: ("Литры -> Галлоны",        lambda v: v * 0.264172, "галлонов"),
    6: ("Мегабайты -> Гигабайты",  lambda v: v / 1024, "ГБ"),
}


def get_choice():
    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if choice in CONVERTERS:
                return choice
            print("Ошибка: выберите пункт из списка.")
        except ValueError:
            print("Ошибка: введите число.")


def get_value():
    while True:
        try:
            return float(input("Введите значение: "))
        except ValueError:
            print("Ошибка: введите корректное число.")


def ask_continue():
    while True:
        answer = input("Выполнить ещё одно преобразование? (да/нет): ").strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Ошибка: введите 'да' или 'нет'.")


def main():
    while True:
        print("Выберите конвертер:")
        for num, (name, _, _) in CONVERTERS.items():
            print(f"{num}. {name}")

        choice = get_choice()
        value = get_value()
        _, func, unit = CONVERTERS[choice]
        result = func(value)
        print(f"{value} -> {result:.2f} {unit}")

        if not ask_continue():
            print("Работа программы завершена.")
            break


if __name__ == "__main__":
    main()