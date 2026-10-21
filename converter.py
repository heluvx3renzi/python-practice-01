
def main():
    print("Выберите конвертер:")
    print("1. Градусы Цельсия -> Фаренгейты")
    print("2. Километры -> Мили")
    print("3. Килограммы -> Фунты")
    print("4. Метры -> Футы")

    choice = input("Ваш выбор: ")

    if choice not in ("1", "2", "3", "4"):
        print("Ошибка: неизвестный номер преобразования.")
        main()
        
    try:
        value = float(input("Введите исходное значение: "))

        if choice == "1":
            result = value * 9 / 5 + 32
            print(f"{value:g} C = {result:.1f} F")

        elif choice == "2":
            result = value * 0.621371
            print(f"{value:g} км = {result:.2f} миль")

        elif choice == "3":
            result = value * 2.20462
            print(f"{value:g} кг = {result:.2f} фунтов")

        elif choice == "4":
            result = value * 3.28084
            print(f"{value:g} м = {result:.2f} футов")

    except ValueError:
        print("Ошибка: необходимо ввести число.")
        main()

if __name__ == "__main__":
    main()
