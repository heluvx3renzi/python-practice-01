
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    try:
        number = int(input("Введите целое число: "))

        print(f"Ваше число: {number}")

        if number > 0:
            print("Положительное: да")
        else:
            print("Положительное: нет")

        if number % 2 == 0:
            print("Четное: да")
        else:
            print("Четное: нет")

        if number % 3 == 0:
            print("Делится на 3: да")
        else:
            print("Делится на 3: нет")

        if number % 5 == 0:
            print("Делится на 5: да")
        else:
            print("Делится на 5: нет")

        if is_prime(number):
            print("Простое: да")
        else:
            print("Простое: нет")

        digits = len(str(abs(number)))
        print(f"Количество цифр: {digits}")

    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
        main()

if __name__ == "__main__":
    main()
