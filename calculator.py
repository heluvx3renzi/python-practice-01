
def main():
    print("=== Консольный калькулятор ===")

    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию: ")
        b = float(input("Введите второе число: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("Ошибка: деление на ноль!")
                return
            result = a / b
        elif op == "^":
            result = a ** b
        elif op == "//":
            if b == 0:
                print("Ошибка: деление на ноль!")
                return
            result = a // b
            if b == 0:
                print("Ошибка: деление на ноль!")
                return
        elif op == "%":
            result = a % b
        else:
            print("Ошибка: неизвестная операция!")
            return

        print("Результат:", result)

    except ValueError:
        print("Ошибка: необходимо ввести число!")
        main()

if __name__ == "__main__":
    main()
