def get_name():
    while True:
        name = input("Введите название товара: ").strip()
        if name:
            return name
        print("Ошибка: название не должно быть пустым.")


def get_positive(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Ошибка: значение должно быть положительным.")
        except ValueError:
            print("Ошибка: введите число.")


def ask_continue():
    while True:
        answer = input("Добавить ещё один товар? (да/нет): ").strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Ошибка: введите 'да' или 'нет'.")


def main():
    total = 0.0
    while True:
        name = get_name()
        price = get_positive("Введите цену: ")
        quantity = get_positive("Введите количество: ")

        cost = price * quantity
        total += cost
        print(f"Товар: {name}, стоимость: {cost:.2f}")

        if not ask_continue():
            break

    discount = total * 0.05 if total > 5000 else 0
    final = total - discount

    print(f"Общая стоимость: {total:.2f}")
    print(f"Скидка: {discount:.2f}")
    print(f"Итого к оплате: {final:.2f}")


if __name__ == "__main__":
    main()