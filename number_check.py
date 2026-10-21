import math


def get_number():
    while True:
        try:
            return int(input("Введите число: "))
        except ValueError:
            print("Ошибка: введите целое число.")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def ask_continue():
    while True:
        answer = input("Проверить ещё одно число? (да/нет): ").strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Ошибка: введите 'да' или 'нет'.")


def main():
    while True:
        n = get_number()
        print(f"Ваше число: {n}")
        print(f"Положительное: {'да' if n > 0 else 'нет'}")
        print(f"Чётное: {'да' if n % 2 == 0 else 'нет'}")
        print(f"Делится на 3: {'да' if n % 3 == 0 else 'нет'}")
        print(f"Делится на 5: {'да' if n % 5 == 0 else 'нет'}")
        print(f"Простое: {'да' if is_prime(n) else 'нет'}")
        print(f"Количество цифр: {len(str(abs(n)))}")

        root = math.isqrt(abs(n))
        print(f"Полный квадрат: {'да' if root * root == abs(n) else 'нет'}")

        if not ask_continue():
            print("Работа программы завершена.")
            break


if __name__ == "__main__":
    main()