def main():
    print("=== КАЛЬКУЛЯТОР ПОКУПОК ===")

    cart = []
    total = 0

    while True:
        name = input("\nНазвание товара: ").strip()

        if not name:
            print("Название не может быть пустым!")
            continue

        try:
            price = float(input("Цена товара: "))
            quantity = int(input("Количество: "))
        except ValueError:
            print("Ошибка ввода!")
            continue

        if price <= 0 or quantity <= 0:
            print("Цена и количество должны быть больше нуля!")
            continue

        cost = price * quantity
        cart.append((name, price, quantity, cost))
        total += cost

        print(f"Стоимость: {cost:.2f} руб.")

        if input("Добавить еще товар? (да/нет): ").lower() != "да":
            break

    if total < 5000:
        percent = 0
    elif total < 10000:
        percent = 5
    elif total < 15000:
        percent = 10
    else:
        percent = 15

    discount = total * percent / 100

    print("\n========== ЧЕК ==========")

    for name, price, quantity, cost in cart:
        print(f"{name}: {price:.2f} x {quantity} = {cost:.2f} руб.")

    print("-------------------------")
    print(f"Сумма: {total:.2f} руб.")
    print(f"Скидка: {percent}%")
    print(f"Экономия: {discount:.2f} руб.")
    print(f"К оплате: {total - discount:.2f} руб.")
    print("=========================")


if __name__ == "__main__":
    main()
