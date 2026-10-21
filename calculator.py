def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")


def get_operation():
    while True:
        op = input("Введите операцию (+, -, *, /): ").strip()
        if op in ("+", "-", "*", "/"):
            return op
        print("Ошибка: неправильная математическая операция.")


def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            print("Ошибка: деление на ноль.")
            return None
        return a / b


def ask_continue():
    while True:
        answer = input("Хотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Ошибка: введите 'да' или 'нет'.")


def main():
    while True:
        a = get_number("Введите первое число: ")
        op = get_operation()
        b = get_number("Введите второе число: ")

        result = calculate(a, op, b)
        if result is not None:
            print(f"Результат: {result}")

        if not ask_continue():
            print("Работа программы завершена.")
            break


if __name__ == "__main__":
    main()