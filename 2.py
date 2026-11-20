# Контрольный пример (Фотография 2)
# Проверка на строке со спецсимволами и на пустой строке

for text in ("Заказ №15: 2 товара по 350 руб., скидка 10%!", ""):
    if not text.strip():
        print("Введена пустая строка. Чисел не найдено, сумма: 0")
        continue

    numbers = []
    current_digits = ""
    for ch in text + " ":
        if ch.isdigit():
            current_digits += ch
        elif current_digits:
            numbers.append(int(current_digits))
            current_digits = ""

    print("--- Результаты анализа строки ---")
    print(f"Исходная строка: {text}")
    print(f"Извлечённые числа: {numbers}")
    print(f"Количество найденных чисел: {len(numbers)}")
    print(f"Сумма всех чисел в строке: {sum(numbers)}\n")
